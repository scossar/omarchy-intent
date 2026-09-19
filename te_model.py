# using a pre-trained text encoder

import json

import numpy as np

# sentence_transformers has to be imported before tensorflow
from sentence_transformers import SentenceTransformer
import tensorflow as tf

tf.keras.utils.set_random_seed(42)


def load_jsonl(path):
    with open(path, encoding="utf-8") as f:
        examples = [json.loads(line) for line in f if line.strip()]

    queries = [example["query"] for example in examples]
    labels = np.array(
        [example["label"] for example in examples],
        dtype=np.int32,
    )
    return queries, labels


# train_queries, train_labels = load_jsonl("data/datasets/train.jsonl")
train_queries, train_labels = load_jsonl("data/datasets-v2/train-v2.jsonl")
validation_queries, validation_labels = load_jsonl(
    "data/datasets-v2/validation-v2.jsonl"
)
test_queries, test_labels = load_jsonl("data/datasets-v2/test-v2.jsonl")

encoder = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2",
    device="cpu",
)


def encode_queries(queries):
    return encoder.encode(
        queries,
        batch_size=64,
        show_progress_bar=True,
        convert_to_numpy=True,
        normalize_embeddings=True,
    ).astype(np.float32)


train_vectors = encode_queries(train_queries)
validation_vectors = encode_queries(validation_queries)
test_vectors = encode_queries(test_queries)

print(train_vectors.shape)


def make_dataset(vectors, labels, training=False):
    ds = tf.data.Dataset.from_tensor_slices((vectors, labels))

    if training:
        ds = ds.shuffle(
            buffer_size=len(labels),
            seed=42,
            reshuffle_each_iteration=True,
        )

    return ds.batch(32).prefetch(tf.data.AUTOTUNE)


train_ds = make_dataset(train_vectors, train_labels, training=True)
validation_ds = make_dataset(validation_vectors, validation_labels)
test_ds = make_dataset(test_vectors, test_labels)

classifier = tf.keras.Sequential(
    [
        tf.keras.Input(shape=(train_vectors.shape[1],)),
        tf.keras.layers.Dense(
            223,
            activation="softmax",
            kernel_regularizer=tf.keras.regularizers.L2(1e-6),
        ),
    ]
)

classifier.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(),
    # metrics=["accuracy"],
    metrics=[
        tf.keras.metrics.SparseCategoricalAccuracy(name="accuracy"),
        tf.keras.metrics.SparseTopKCategoricalAccuracy(
            k=3,
            name="top_3_accuracy",
        ),
    ],
)

classifier.fit(
    train_ds,
    validation_data=validation_ds,
    epochs=500,
    callbacks=[
        tf.keras.callbacks.EarlyStopping(
            monitor="val_loss",
            min_delta=0.001,
            patience=10,
            restore_best_weights=True,
        )
    ],
)


probabilities = classifier.predict(validation_ds, verbose=0)
predicted_labels = probabilities.argmax(axis=1)

incorrect_indices = np.flatnonzero(predicted_labels != validation_labels)

print(f"{len(incorrect_indices)} incorrect predictions out of {len(validation_labels)}")

with open("validation_errors.jsonl", "w", encoding="utf-8") as f:
    for i in incorrect_indices:
        record = {
            "query": validation_queries[i],
            "true_label": int(validation_labels[i]),
            "predicted_label": int(predicted_labels[i]),
            "confidence": float(probabilities[i, predicted_labels[i]]),
        }
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

# run once you've finished selecting setting susing validation
# classifier.evaluate(test_ds)
#
# classifier.save("pretrained_query_classifier.keras")
# encoder.save("query_encoder")

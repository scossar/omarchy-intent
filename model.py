## model.py

import json
from pathlib import Path

import tensorflow as tf

DATASET_DIR = Path("data/datasets")
source_path = DATASET_DIR / "train.jsonl"
validation_path = DATASET_DIR / "validation.jsonl"

queries = []
labels = []

with source_path.open("r", encoding="utf-8") as f:
    for line in f:
        row = json.loads(line.strip())
        queries.append(row["query"])
        labels.append(row["label"])

train_ds = tf.data.Dataset.from_tensor_slices((queries, labels))
train_ds = (
    train_ds.shuffle(
        buffer_size=len(queries),
        seed=42,
        reshuffle_each_iteration=True,
    )
    .batch(32)
    .prefetch(tf.data.AUTOTUNE)
)

validation_queries = []
validation_labels = []
with validation_path.open("r", encoding="utf-8") as f:
    for line in f:
        row = json.loads(line.strip())
        validation_queries.append(row["query"])
        validation_labels.append(row["label"])

validation_ds = tf.data.Dataset.from_tensor_slices(
    (validation_queries, validation_labels)
)
validation_ds = validation_ds.batch(32).prefetch(tf.data.AUTOTUNE)


vectorizer = tf.keras.layers.TextVectorization(
    max_tokens=10_000,
    standardize="lower",
    split="whitespace",
    output_mode="int",
)

train_text = train_ds.map(lambda query, label: query)
vectorizer.adapt(train_text)

open_keybindings = vectorizer(tf.constant(["Open open_keybindings"])).numpy()

model = tf.keras.Sequential(
    [
        tf.keras.Input(shape=(), dtype=tf.string),
        vectorizer,
        tf.keras.layers.Embedding(
            input_dim=len(vectorizer.get_vocabulary()),
            output_dim=64,
            mask_zero=True,
        ),
        tf.keras.layers.GlobalAveragePooling1D(),
        tf.keras.layers.Dense(223, activation="softmax"),
    ]
)

model.compile(
    optimizer="adam",
    loss=tf.keras.losses.SparseCategoricalCrossentropy(),
    metrics=["accuracy"],
)

model.fit(
    train_ds,
    validation_data=validation_ds,
    epochs=30,
    callbacks=[
        tf.keras.callbacks.EarlyStopping(
            monitor="val_loss",
            patience=3,
            restore_best_weights=True,
        )
    ],
)

model.save("query_classifier.keras")

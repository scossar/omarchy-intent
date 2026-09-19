import json
from pathlib import Path

import tensorflow as tf

DATASET_DIR = Path("data/datasets")
label_map_path = DATASET_DIR / "label-map.json"
label_dict = {}

with label_map_path.open("r") as f:
    label_dict = json.load(f)

model = tf.keras.models.load_model("query_classifier.keras")

queries = tf.constant(["make the background blue"])
probabilities = model(queries, training=False)

predicted_label = tf.argmax(probabilities[0]).numpy()
score = tf.reduce_max(probabilities[0]).numpy()

print(f"Predicted label: {label_dict[str(predicted_label)]}")
print(f"Score: {score:.3f}")

top = tf.math.top_k(probabilities[0], k=5)

for label, score in zip(top.indices.numpy(), top.values.numpy()):
    print(f"{label_dict[str(label)]}, Score: {score}")

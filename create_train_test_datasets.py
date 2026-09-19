# create shuffled test and validation splits from test.jsonl
import json
import random
from collections import defaultdict
from pathlib import Path

dataset_dir = Path("data/datasets")
test_source_path = dataset_dir / "test-source.jsonl"

rng = random.Random(42)
by_label = defaultdict(list)

with test_source_path.open(encoding="utf-8") as f:
    for line in f:
        example = json.loads(line)
        by_label[example["label"]].append(example)

assert set(by_label) == set(range(223))
assert all(len(examples) == 10 for examples in by_label.values())

splits = {"test": [], "validation": []}

for label in sorted(by_label):
    examples = by_label[label]
    rng.shuffle(examples)

    splits["test"].extend(examples[:5])
    splits["validation"].extend(examples[5:])

for name, examples in splits.items():
    rng.shuffle(examples)
    output_path = dataset_dir / f"{name}.jsonl"

    with output_path.open("x", encoding="utf-8") as f:
        for example in examples:
            f.write(json.dumps(example, ensure_ascii=False) + "\n")

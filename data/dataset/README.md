# Omarchy Shortcut Classifier Training Data

This directory contains a synthetic training set for predicting an Omarchy keybinding row from a user intention.

## Files

- `train.jsonl` — 11,150 training records, with 50 records for each of 223 numeric labels.
- `label-map.json` — numeric label to command and display label.
- `row-metadata.json` — label-map data plus intentions, rationale, and original source-row position.
- `dataset-manifest.json` — source, exclusions, relabeling, generation rules, and artifact inventory.
- `validation-report.json` — final structural and rule-based validation results.
- `reviews/` — semantic-review findings used to correct generated records.
- `chunks/` and `corrected/` — intermediate generation artifacts; use `train.jsonl` for training.

## Record schema

```json
{"query":"Make this window stop floating","label":11}
```

Labels are zero-based, contiguous, and correspond to `label-map.json`. No evaluation split is included.

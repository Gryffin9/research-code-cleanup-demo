# Research Code Cleanup Demo

A synthetic before/after demo for turning messy research code into a readable, reproducible workflow.

This repository uses dummy data only. It does not include private research data, private product data, or confidential implementation details from any private project.

## Repository structure

- `messy_version/`: a deliberately compact, hard-to-maintain script.
- `clean_version/`: a small reusable analysis package with a deterministic runner.
- `data/`: synthetic measurements.
- `docs/before_after.md`: what changed and why.
- `docs/reproducibility_checklist.md`: checklist for research-code cleanup sprints.
- `tests/`: standard-library tests for the cleaned workflow.

## Run the messy version

```bash
python3 messy_version/messy_analysis.py
```

## Run the clean version

```bash
PYTHONPATH=clean_version python3 clean_version/run_analysis.py
```

## Validate

```bash
PYTHONPATH=clean_version python3 -m unittest discover -s tests
```

## What this demonstrates

- Separating I/O from analysis logic
- Replacing hidden assumptions with named functions
- Adding deterministic synthetic data
- Adding tests around the cleaned analysis
- Writing documentation that makes the workflow reproducible

# Research Code Cleanup Demo

A synthetic messy-to-clean research-code workflow showing how an unclear notebook/script can be converted into a reproducible, documented analysis.

## Problem

Research code often starts as a quick notebook or script built during exploration. That is normal, but it can become hard to debug, rerun, explain, or hand to another person when assumptions are hidden and analysis steps are mixed together.

This repo shows a small synthetic example of that cleanup process.

## Before/after workflow

- `messy_version/`: a compact script with hard-coded assumptions and mixed I/O, analysis, and output.
- `clean_version/`: a small, structured workflow with named functions, typed records, and a deterministic runner.
- `docs/before_after.md`: a short explanation of what changed and why.

## What gets improved

- cleaner structure
- clearer functions
- synthetic data separated from code
- better tables and command-line output
- documentation for the workflow
- reproducibility checks
- tests for the cleaned analysis

## Repository structure

- `data/`: synthetic CSV data only
- `messy_version/`: intentionally rough starting point
- `clean_version/`: cleaned analysis package and runner
- `docs/`: before/after notes and reproducibility checklist
- `tests/`: unit tests for the cleaned workflow

## Reproducibility checklist

The demo checklist lives in `docs/reproducibility_checklist.md`. It covers data separation, named assumptions, deterministic commands, tests, generated outputs, and review for confidential material before public sharing.

## How to run

Run the messy version:

```bash
python3 messy_version/messy_analysis.py
```

Run the clean version:

```bash
PYTHONPATH=clean_version python3 clean_version/run_analysis.py
```

Run tests:

```bash
PYTHONPATH=clean_version python3 -m unittest discover -s tests
```

## What this demonstrates

This is public proof for research-code cleanup and debugging sprints: taking unclear exploratory code and turning it into a small, readable, documented, reproducible workflow.

All data is synthetic. No private client data, private research data, or confidential project internals are included.

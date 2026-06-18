# Before And After

This demo uses synthetic measurements to show the shape of a research-code cleanup sprint.

## Before

The messy script:

- Reads directly from a hard-coded path.
- Mixes I/O, filtering, calculation, and printing in one file.
- Has unnamed assumptions, such as using only the final timepoint.
- Has no testable functions.
- Produces output that is hard to reproduce or extend.

## After

The clean version:

- Defines a typed `Measurement` record.
- Separates CSV reading from analysis.
- Names the key analysis choice: `final_timepoint_mean_by_group`.
- Uses deterministic synthetic data.
- Adds unit tests around the cleaned behavior.
- Keeps command-line output small and inspectable.

## Why it matters

Research-code cleanup is usually not about making code fancy. It is about making the workflow readable enough to debug, rerun, explain, and trust.

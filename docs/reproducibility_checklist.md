# Reproducibility Checklist

Use this checklist for small research-code cleanup and debugging sprints.

- State the research question or analysis goal in plain language.
- Keep raw or synthetic input data separate from generated outputs.
- Replace hidden assumptions with named functions or documented constants.
- Separate I/O, transformation, analysis, and reporting where practical.
- Add a deterministic command that reruns the core workflow.
- Add at least one test for a representative calculation.
- Record dependency and Python version expectations.
- Document what the script produces and where outputs go.
- Use synthetic or approved public data for portfolio demos.
- Review for confidential data, private paths, credentials, and unpublished findings before sharing.

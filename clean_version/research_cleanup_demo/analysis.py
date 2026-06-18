"""Analysis functions for the synthetic research-code cleanup demo."""

from __future__ import annotations

from collections import defaultdict

from .io import Measurement


def final_timepoint_mean_by_group(measurements: list[Measurement]) -> dict[str, float]:
    """Compute mean corrected signal at the final observed timepoint for each group."""
    if not measurements:
        raise ValueError("measurements must not be empty")

    final_time = max(measurement.time_s for measurement in measurements)
    grouped_values: dict[str, list[float]] = defaultdict(list)

    for measurement in measurements:
        if measurement.time_s == final_time:
            grouped_values[measurement.group].append(measurement.corrected_signal)

    return {
        group: sum(values) / len(values)
        for group, values in sorted(grouped_values.items())
    }

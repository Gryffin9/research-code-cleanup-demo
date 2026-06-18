"""Input helpers for the synthetic research-code cleanup demo."""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Measurement:
    sample_id: str
    group: str
    time_s: float
    signal: float
    baseline: float

    @property
    def corrected_signal(self) -> float:
        return self.signal - self.baseline


def read_measurements(path: Path) -> list[Measurement]:
    """Read synthetic measurement rows from a CSV file."""
    measurements: list[Measurement] = []
    with path.open(newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            measurements.append(
                Measurement(
                    sample_id=row["sample_id"],
                    group=row["group"],
                    time_s=float(row["time_s"]),
                    signal=float(row["signal"]),
                    baseline=float(row["baseline"]),
                )
            )
    return measurements

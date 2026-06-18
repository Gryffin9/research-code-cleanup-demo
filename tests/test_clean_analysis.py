from __future__ import annotations

import unittest
from pathlib import Path

from research_cleanup_demo import final_timepoint_mean_by_group, read_measurements


class CleanAnalysisTests(unittest.TestCase):
    def test_final_timepoint_mean_by_group_is_reproducible(self) -> None:
        measurements = read_measurements(Path("data/synthetic_measurements.csv"))
        summary = final_timepoint_mean_by_group(measurements)
        self.assertAlmostEqual(summary["control"], 1.08)
        self.assertAlmostEqual(summary["treatment"], 1.385)

    def test_empty_measurements_raise_clear_error(self) -> None:
        with self.assertRaisesRegex(ValueError, "measurements must not be empty"):
            final_timepoint_mean_by_group([])


if __name__ == "__main__":
    unittest.main()

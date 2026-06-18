"""Clean research-code demo package using synthetic data."""

from .analysis import final_timepoint_mean_by_group
from .io import Measurement, read_measurements

__all__ = ["Measurement", "final_timepoint_mean_by_group", "read_measurements"]

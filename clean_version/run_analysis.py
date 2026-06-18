from __future__ import annotations

from pathlib import Path

from research_cleanup_demo import final_timepoint_mean_by_group, read_measurements


def main() -> None:
    data_path = Path("data/synthetic_measurements.csv")
    measurements = read_measurements(data_path)
    summary = final_timepoint_mean_by_group(measurements)

    print("Mean corrected signal at final timepoint")
    for group, value in summary.items():
        print(f"{group}: {value:.3f}")


if __name__ == "__main__":
    main()

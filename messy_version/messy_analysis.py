from __future__ import annotations

import csv


rows = []
with open("data/synthetic_measurements.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        rows.append(row)

out = {}
for row in rows:
    group = row["group"]
    corrected = float(row["signal"]) - float(row["baseline"])
    if group not in out:
        out[group] = []
    if float(row["time_s"]) == 2.0:
        out[group].append(corrected)

for group in out:
    vals = out[group]
    print(group, sum(vals) / len(vals))

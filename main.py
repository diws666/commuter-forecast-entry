#!/usr/bin/env python3
"""Writes the commuter forecast entry to /output/entry.txt."""

import os

FORECAST = "Tomorrow in New Borington: light drizzle, heavy traffic, and a 100% chance your bus leaves exactly one minute early."  # 116 characters

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(FORECAST)

print("wrote", len(FORECAST.encode("utf-8")), "bytes")

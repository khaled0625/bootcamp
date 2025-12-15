from __future__ import annotations

from csv import DictReader
from pathlib import Path

def read_csv_rows(path: str | Path) -> list[dict[str, str]]:
    try:
        with open(path, "r", newline="") as file:
            reader = DictReader(file)
            for line in reader:
                print(line)
            reader = DictReader(file)
            return [dict(line) for line in reader]
    except FileNotFoundError:
        print(f"{path} does not exist")


if __name__ == "__main__":
    reader = read_csv_rows("/home/khaled/Agents/ADK/bootcamp/csv-profiler/src/data/sample.csv")


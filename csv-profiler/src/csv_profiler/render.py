from __future__ import annotations

import datetime
import json
from pathlib import Path
from datetime import datetime

def write_json(report: dict, path: str| Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2, ensure_ascii=False) +"\n")

def write_markdown(report: dict, path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    cols = report.get("columns")
    missing = report.get("missing", {})
    cols_stats = report.get("cols_stats", {})
    lines = []
    lines.append("# CSV profiling Report\n")
    lines.append(f"- number of Rows: **{report.get("rows", 0)}**")
    lines.append(f"- number of columns: **{len(report.get("columns", 0))}**")
    lines.append(f"- Columns: **{report.get('columns', 0)}**")
    lines.append(f"- Missing Rows: **{missing}**")
    lines.append(f"- Missing Columns: **{missing}**")
    lines.append("| Column | Stats |")
    lines.append("|--------|-------|")
    for col, stats in cols_stats.items():
        lines.append(f"| {col} | {stats} |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")

def new_write_markdown(report: dict, path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    rows = report["summary"]["rows"]
    lines: list[str] = []
    lines.extend(md_header(f"{path}"))

    lines.append("## Summary")
    lines.append(f"- Rows: {rows:,}")
    lines.append(f"- Columns: {report['summary']['columns']:,}")
    lines.append("")

    lines.append("## Columns (table)")
    lines.extend(md_table_header())

    for name, col in report["columns"].items():
        typ = col["type"]
        stats = col["stats"]

        missing = stats.get("missing", 0)

        if typ == "number":
            details = (
                f"count={stats['count']}, "
                f"unique={stats['unique']}, "
                f"min={stats['min_value']}, "
                f"max={stats['max_value']}, "
                f"avg={stats['avg']:.2f}"
            )
        else:
            details = (
                f"unique={stats['unique']}, "
                f"top={', '.join(t['value'] for t in stats['top'])}"
            )

        lines.append(
            f"| {name} | {typ} | {missing} | {details} |"
        )


    path.write_text("\n".join(lines), encoding="utf-8")

def md_header(source: str) -> list[str]:
    ts = datetime.now().isoformat(timespec="seconds")
    return [
        "# CSV profiling Report",
        "",
        f" - source: {source}",
        f"- generated at: {ts}",
    ]


def md_table_header() -> list[str]:
    return [
        "| column | type | Missing| stats |",
        "|---|---|---:|---|",
    ]


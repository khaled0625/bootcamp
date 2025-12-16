from __future__ import annotations
import json
from pathlib import Path

def write_json(report: dict, path: str| Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2, ensure_ascii=False) +"\n")

def write_markdown(report: dict, path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    cols = report.get("columns")
    missing = report.get("missing", {})
    lines = []
    lines.append("# CSV profiling Report\n")
    lines.append(f"- number of Rows: **{report.get("rows", 0)}**")
    lines.append(f"- number of columns: **{len(report.get("columns", 0))}**")
    lines.append(f"- Columns: **{report.get('columns', 0)}**")
    lines.append(f"- Missing Rows: **{missing}**")
    lines.append(f"- Missing Columns: **{missing}**")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


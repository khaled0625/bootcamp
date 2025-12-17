from rich import columns

empty_list= ['na', "n/a", "null", "none", "nan", "",None]

def get_columns(rows: list[dict[str, str]]) -> list[str]:
    if not rows:
        return []
    return list(rows[0].keys())

def new_basic_profile(rows: list[dict[str, str]]) -> dict:
    cols = get_columns(rows)
    report  = {
        "summary": {
            "rows": len(rows),
            "columns": len(cols),
            "columns_names": cols,
        },
        "columns" : {}
    }
    for col in cols:
        values = column_values(rows, col)
        typ = infer_type(values)
        if typ == "text":
            stats = text_stats(values, top_k = 5)
        else :
            stats = numeric_stats(values)
        report["columns"][col] = {
            "type": typ,
            "stats": stats,
        }
    return report

def basic_profile(rows: list[dict[str, str]]) -> dict:
    if not rows:
        return {"rows": 0 , "columns": {}, "notes": ["empty dataset"]}
    columns = list(rows[0].keys())
    missing = {c: 0 for c in columns}
    non_empty = {c: 0 for c in columns}

    for row in rows:
        for c in columns:
            v = (row.get(c) or "").strip()
            if v == "":
                missing[c] += 1
            else:
                non_empty[c] += 1
    cols_stats = {}
    for c in columns:
        cvalues = column_values(rows, c)
        if infer_type(cvalues) == "number":
            print("Getting numerical stats")
            cols_stats[c] = numeric_stats(cvalues)
        else:
            cols_stats[c] = text_stats(cvalues)
            cols_stats[c] = text_stats(cvalues, top_k = 5)
            # cols_stats[c] = column_values(rows, c)
        # cols_stats[c] = numeric_stats(cols_stats[c])


    return {
        "rows": len(rows),
        "n_cols": len(columns),
        "columns": columns,
        "missing": missing,
        "non_empty": non_empty,
        "cols_stats": cols_stats,
    }


def is_missing(value: str | None)-> bool:
    if value is None:
        return True
    return value.strip().casefold() in empty_list

def try_float(value: str) -> float | None:
    try:
        return float(value)
    except ValueError:
        return None

def infer_type(values: list[str]) -> str | None:
    usable = [v for v in values if not is_missing(v)]
    if not usable:
        return "text"
    for v in usable:
        if try_float(v) is None:
            return "text"
    return "number"

def column_values(rows: list[dict[str, str]], col: str) -> list[str]:
    return [row.get(col, "") for row in rows]

def numeric_stats(values: list[str]) -> dict:
    usable = [v for v in values if not is_missing(v)]
    missing = len(values) - len(usable)
    nums: list[float] = []
    for v in usable:
        x = try_float(v)
        if x is None:
            raise ValueError(f"Non-numeric value: {v!r}")
        nums.append(x)

    count = len(nums)
    unique = len(set(nums))
    max_value = max(nums)
    min_value = min(nums)
    avg = sum(nums) / count
    return {

        "count": count,
        "unique": unique,
        "missing": missing,
        "nums": nums,
        "max_value": max_value,
        "min_value": min_value,
        "avg": avg,
    }

def by_count(pair):
    return pair[1]

def text_stats(values, top_k :int = 5) :
    usable = [v for v in values if not is_missing(v)]
    missing = len(values) - len(usable)

    counts = {}
    for v in usable:
        counts[v] = counts.get(v, 0) + 1

    top_items = sorted(counts.items(), key= by_count, reverse = True)[:top_k]
    top = [{"value": v, "count": c} for v, c in top_items]

    return {
        "counts": len(counts),
        "missing": missing,
        "unique": len(set(counts.keys())),
        "top": top,

    }







if __name__ == "__main__":
    x = [{'name': 'Aisha', 'age': '23', 'city': 'Riyadh', 'salary': '12000'}, {'name': 'Fahad', 'age': '', 'city': 'Jeddah', 'salary': '9000'}, {'name': 'Noor', 'age': '29', 'city': '', 'salary': ''}, {'name': 'salem', 'age': '31', 'city': 'Dammam', 'salary': '15000'}]
    print(new_basic_profile(x))






empty_list= ['na', "n/a", "null", "none", "nan", "",None]

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

    return {
        "rows": len(rows),
        "n_cols": len(columns),
        "columns": columns,
        "missing": missing,
        "non_empty": non_empty,
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
    usable = [v for v in values if not is_missing]
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
    return {
        "count": count,
        "unique": unique,
        "missing": missing,
        "nums": nums,
        "unique_nums": len(unique),
        "unique_count": len(unique),
    }








# if __name__ == "__main__":
#     x = [{'name': 'Aisha', 'age': '23', 'city': 'Riyadh', 'salary': '12000'}, {'name': 'Fahad', 'age': '', 'city': 'Jeddah', 'salary': '9000'}, {'name': 'Noor', 'age': '29', 'city': '', 'salary': ''}, {'name': 'salem', 'age': '31', 'city': 'Dammam', 'salary': '15000'}]
#     print(basic_profile(x))





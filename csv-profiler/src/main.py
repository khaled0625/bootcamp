from csv_profiler.io import read_csv_rows
from csv_profiler.profile import basic_profile, try_float, infer_type, is_missing, column_values
from csv_profiler.render import write_json, write_markdown


def main() -> None:
    rows = read_csv_rows("data/sample.csv")
    report = basic_profile(rows)
    write_json(report, "output/report.json")

    write_markdown(report, "output/report.md")
    print("write output/report.json and output/report.md")


if __name__ == "__main__":
    main()
from csv_profiler.io import read_csv_rows
from csv_profiler.profile import new_basic_profile
from csv_profiler.render import write_json, new_write_markdown


def main() -> None:
    rows = read_csv_rows("data/sample.csv")
    report = new_basic_profile(rows)
    write_json(report, "output/report.json")

    new_write_markdown(report, "output/report.md")
    print("write output/report.json and output/report.md")


if __name__ == "__main__":
    main()



def main(): -> None:
    rows = read_csv_rows("data/sample.csv")
    report = basic_profile(rows)
    write_json(report, "data/report.json")
    write_markdown(report, "data/report.md")
    print("write output/report.json and output/report.md")

if __name__ == "__main__":

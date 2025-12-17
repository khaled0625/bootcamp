import typer
from pathlib import Path
import typer

from .io import read_csv_rows
from .profile import basic_profile, new_basic_profile
from .render import write_json, write_markdown, new_write_markdown



app = typer.Typer()


@app.command()
def hello(name: str):
    print(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")

@app.command(help = "profile csv file ")
def profile(
        input_path: Path = typer.Argument(..., help="input csv file path"),
        out_dir: Path = typer.Option(Path("output"), "--out-dir", help="output folder"),
        report_name: Path = typer.Option("report", "--report-name", help="base report name for output"),
):
    typer.echo(f"input: {input_path}")
    typer.echo(f"out : {out_dir}")
    typer.echo(f"name : {report_name}")


    rows = read_csv_rows(input_path)
    report = new_basic_profile(rows)
    write_json(report, f"{out_dir}/report.json")

    new_write_markdown(report, f"{out_dir}/report.md")
    print("write output/report.json and output/report.md")
if __name__ == "__main__":
    app()

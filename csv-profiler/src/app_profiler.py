import requests
import streamlit as st
import csv
from io import StringIO
import pandas as pd
import json
from pathlib import Path
from csv_profiler.profile import new_basic_profile
from csv_profiler.render import to_markdown

def read_markdown_file(file_path):
    """Reads the content of a markdown file."""
    try:
        return Path(file_path).read_text()
    except FileNotFoundError:
        return f"Error: The file '{file_path}' was not found."

def save_json(report: dict, filename: str):
    """Saves the JSON report to the specified file path."""
    output_path = Path("output_from_streamlet")
    output_path.mkdir(parents=True, exist_ok=True)
    with open(output_path / filename, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

# Function to save Markdown file
def save_markdown(report: str, filename: str):
    """Saves the Markdown report to the specified file path."""
    output_path = Path("output_from_streamlet")
    output_path.mkdir(parents=True, exist_ok=True)
    with open(output_path / filename, "w", encoding="utf-8") as f:
        f.write(report)


st.set_page_config(
    page_title="CSV Profiling Report",
    layout="wide",
)


st.title("CSV profiler")
uploaded = st.file_uploader("upload a csv ", type="csv")



if st.button("Predict"):
    # Send request to FastAPI
    response = requests.post(
        "http://127.0.0.1:5522",
        json={"text": uploaded}
    )

    if response.status_code == 200:
        st.success(response.json()["message"])
    else:
        st.error("Failed to connect to backend.")

if uploaded is not None:
    text = uploaded.getvalue().decode('utf-8-sig')
    rows = list(csv.DictReader(StringIO(text)))
    if len(rows) == 0:
        st.error("CSV has no data. Upload a CSV with at least 1 row.")
        st.stop()
    if len(rows[0]) == 0:
        st.warning("CSV has no headers (no columns detected).")
    df = pd.DataFrame(rows)
    st.write("Filename:", uploaded.name)
    st.write("rows:", len(rows))

    csv_profiler = new_basic_profile(rows)
    markdown_profiler = to_markdown(csv_profiler)
    df_profiler = pd.DataFrame(csv_profiler)

    st.write("Profiling Results:")


    tab1, tab2, tab3 = st.tabs(["Markdown", "json", "dataframe"])

    with tab1:
        st.header("markdown report")
        cols = st.columns([2.5,1])
        with cols[0]:
            st.download_button(
                label="Download Markdown Report",
                data=markdown_profiler,
                file_name="profiling_report.md",
                mime="text/markdown"
            )
            if st.button("Save Report in local files", key="save_markdown"):
                save_markdown(markdown_profiler, "profiling_report.md")
                st.success("Reports saved to the 'output_from_streamlit/' directory.")
            st.markdown(markdown_profiler)

        with cols[1]:
            st.header(f"CSV file: {uploaded.name}")
            st.write(df)

    with tab2:
        st.header("json report")

        cols = st.columns([2.5,1])
        with cols[0]:
            # 2. Download JSON Button
            st.download_button(
                label="Download JSON Report",
                data=json.dumps(csv_profiler, indent=2, ensure_ascii=False),
                file_name="profiling_report.json",
                mime="application/json"
            )
            if st.button("Save Report in local file", key="save_json"):
                save_json(csv_profiler, "profiling_report.json")
                st.success("Reports saved to the 'output_from_streamlit' directory.")

            st.write(csv_profiler)

        with cols[1]:
            st.header(f"CSV file: {uploaded.name}")
            st.write(df)
    # with tab3:
    #     st.header("dataframe report")
    #     cols = st.columns([2.5,1])
    #     with cols[0]:
    #
    #         st.write(pd.DataFrame(csv_profiler))










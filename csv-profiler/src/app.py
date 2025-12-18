import streamlit as st
import csv
from io import StringIO
import pandas as pd
st.set_page_config(
    page_title="CSV Profiling Report",
    layout="wide",
)
st.sidebar.header("input")
source = st.sidebar.selectbox("data source", ["upload", "local path"])
st.write("selected: ",source)

st.title("CSV profiler")
st.caption("week 01 - Day 4 - streamlit GUI")
x = [{'name': 'Aisha', 'age': '23', 'city': 'Riyadh', 'salary': '12000'},
     {'name': 'Fahad', 'age': '', 'city': 'Jeddah', 'salary': '9000'},
     {'name': 'Noor', 'age': '29', 'city': '', 'salary': ''},
     {'name': 'salem', 'age': '31', 'city': 'Dammam', 'salary': '15000'},{'name': 'Aisha', 'age': '23', 'city': 'Riyadh', 'salary': '12000'},
     {'name': 'Fahad', 'age': '', 'city': 'Jeddah', 'salary': '9000'},
     {'name': 'Noor', 'age': '29', 'city': '', 'salary': ''},
     {'name': 'salem', 'age': '31', 'city': 'Dammam', 'salary': '15000'},{'name': 'Aisha', 'age': '23', 'city': 'Riyadh', 'salary': '12000'},
     {'name': 'Fahad', 'age': '', 'city': 'Jeddah', 'salary': '9000'},
     {'name': 'Noor', 'age': '29', 'city': '', 'salary': ''}, {'name': 'Fahad', 'age': '', 'city': 'Jeddah', 'salary': '9000'},
     {'name': 'Noor', 'age': '29', 'city': '', 'salary': ''},
     {'name': 'salem', 'age': '31', 'city': 'Dammam', 'salary': '15000'},{'name': 'Aisha', 'age': '23', 'city': 'Riyadh', 'salary': '12000'},
     {'name': 'Fahad', 'age': '', 'city': 'Jeddah', 'salary': '9000'},
     {'name': 'Noor', 'age': '29', 'city': '', 'salary': ''}, {'name': 'Fahad', 'age': '', 'city': 'Jeddah', 'salary': '9000'},
     {'name': 'Noor', 'age': '29', 'city': '', 'salary': ''},
     {'name': 'salem', 'age': '31', 'city': 'Dammam', 'salary': '15000'},{'name': 'Aisha', 'age': '23', 'city': 'Riyadh', 'salary': '12000'},
     {'name': 'Fahad', 'age': '', 'city': 'Jeddah', 'salary': '9000'},
     {'name': 'Noor', 'age': '29', 'city': '', 'salary': ''}, {'name': 'Fahad', 'age': '', 'city': 'Jeddah', 'salary': '9000'},
     {'name': 'Noor', 'age': '29', 'city': '', 'salary': ''},
     {'name': 'salem', 'age': '31', 'city': 'Dammam', 'salary': '15000'},{'name': 'Aisha', 'age': '23', 'city': 'Riyadh', 'salary': '12000'},
     {'name': 'Fahad', 'age': '', 'city': 'Jeddah', 'salary': '9000'},
     {'name': 'Noor', 'age': '29', 'city': '', 'salary': ''}, {'name': 'Fahad', 'age': '', 'city': 'Jeddah', 'salary': '9000'},
     {'name': 'Noor', 'age': '29', 'city': '', 'salary': ''},
     {'name': 'salem', 'age': '31', 'city': 'Dammam', 'salary': '15000'},{'name': 'Aisha', 'age': '23', 'city': 'Riyadh', 'salary': '12000'},
     {'name': 'Fahad', 'age': '', 'city': 'Jeddah', 'salary': '9000'},
     {'name': 'Noor', 'age': '29', 'city': '', 'salary': ''}, {'name': 'Fahad', 'age': '', 'city': 'Jeddah', 'salary': '9000'},
     {'name': 'Noor', 'age': '29', 'city': '', 'salary': ''},
     {'name': 'salem', 'age': '31', 'city': 'Dammam', 'salary': '15000'},{'name': 'Aisha', 'age': '23', 'city': 'Riyadh', 'salary': '12000'},
     {'name': 'Fahad', 'age': '', 'city': 'Jeddah', 'salary': '9000'},
     {'name': 'Noor', 'age': '29', 'city': '', 'salary': ''},
     {'name': 'salem', 'age': '31', 'city': 'Dammam', 'salary': '15000'}]

# df = pd.DataFrame(x)
#
# st.subheader("1- interactve dataframe")
# st.write("this version allow user to sort columns and resize the table.")
# st.dataframe(df)

# st.subheader("2- sort by age")
# st.write("this is a traditional, non-interactive table")
# st.table(df)

uploaded = st.file_uploader("upload a csv ", type="csv")
show_preview = st.checkbox("show loaded:", value=True)
show_markdown = st.checkbox("show_markdown", value=True)

if uploaded is not None:
    text = uploaded.getvalue().decode('utf-8-sig')
    rows = list(csv.DictReader(StringIO(text)))
    df = pd.DataFrame(rows)

    st.write("Filename:", uploaded.name)
    st.write("rows:", len(rows))


    if show_preview:
        cols = st.columns(2)
        cols[0].metric("slide 1", 1200)
        cols[1].metric("slide 2", 9)
        with cols[0]:
            st.write(rows[:5])

        with cols[1]:
            st.table(df)
            st.markdown(rows[:5], unsafe_allow_html=True)
    else :
        st.info("uploaded a csv to begin ")


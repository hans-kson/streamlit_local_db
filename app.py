#streamlit run app.py

import streamlit as st
import pyodbc

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
        + st.secrets["server"]
        + ";DATABASE="
        + st.secrets["database"]
        + ";UID="
        + st.secrets["username"]
        + ";PWD="
        + st.secrets["password"]
    )

conn = init_connection()

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

# title
st.header("Streamlit connecting with local ms sql server db app")

#some text describing app
st.text("App that connects to a local db and shows entries in a table.")

# Input bar 1
num_records_to_see = st.number_input("Enter number entries you want to see", min_value=1, step=1)

# change query as needed f.ex. table name
# rows = run_query("SELECT * from mytable;")
# rows = run_query("SELECT TOP(10)[name],[pet] FROM mytable;")
rows = run_query(f"SELECT TOP({num_records_to_see})[name],[pet] FROM mytable;")


# Print results on button press
if st.button('See entries from top in table'):
    for row in rows:
        st.write(f"{row[0]} has a :{row[1]}:")
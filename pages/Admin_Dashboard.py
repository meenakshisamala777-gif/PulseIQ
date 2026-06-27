import streamlit as st
import sqlite3
import pandas as pd

st.title("🏥 Hospital Admin Dashboard")

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

df = pd.read_sql_query("SELECT * FROM hospitals", conn)

hospital = st.selectbox(
    "Select Hospital",
    df["hospital_name"]
)

selected = df[df["hospital_name"] == hospital].iloc[0]

beds = st.number_input(
    "Available Beds",
    value=int(selected["available_beds"]),
    min_value=0
)

icu = st.number_input(
    "Available ICU Beds",
    value=int(selected["available_icu"]),
    min_value=0
)

ambulances = st.number_input(
    "Available Ambulances",
    value=int(selected["ambulances"]),
    min_value=0
)

if st.button("Update Resources"):

    cursor.execute("""
    UPDATE hospitals
    SET
    available_beds=?,
    available_icu=?,
    ambulances=?
    WHERE hospital_name=?
    """,
    (
        beds,
        icu,
        ambulances,
        hospital
    ))

    conn.commit()

    st.success("Resources Updated Successfully!")

conn.close()
import streamlit as st
import sqlite3
import pandas as pd
from database.init_db import initialize_database

initialize_database()
def load_css():
    with open("styles/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Page configuration
st.set_page_config(
    page_title="Emergency Care Resource Allocator",
    page_icon="🚑",
    layout="wide"
)

st.title("🚑 AI-Powered Emergency Care Resource Allocator")
st.markdown("### Real-Time Hospital Resource Dashboard")

# Connect to database
conn = sqlite3.connect("database.db")
df = pd.read_sql_query("SELECT * FROM hospitals", conn)

# Statistics
total_hospitals = len(df)
total_beds = df["available_beds"].sum()
total_icu = df["available_icu"].sum()
total_ambulances = df["ambulances"].sum()

# Dashboard cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🏥 Hospitals", total_hospitals)

with col2:
    st.metric("🛏 Available Beds", total_beds)

with col3:
    st.metric("❤️ ICU Beds", total_icu)

with col4:
    st.metric("🚑 Ambulances", total_ambulances)

st.divider()

st.subheader("Hospital Resource Availability")

st.dataframe(
    df[
        [
            "hospital_name",
            "location",
            "available_beds",
            "available_icu",
            "ambulances",
            "specialists",
        ]
    ],
    use_container_width=True,
)

conn.close()
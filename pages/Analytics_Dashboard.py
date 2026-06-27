import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Analytics Dashboard", layout="wide")

st.title("📊 Hospital Analytics Dashboard")

# Database Connection
conn = sqlite3.connect("database.db")

# Read Hospital Data
df = pd.read_sql_query("SELECT * FROM hospitals", conn)

conn.close()

# ==========================
# Metrics
# ==========================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🏥 Total Hospitals", len(df))

with col2:
    st.metric("🛏 Total Available Beds", df["available_beds"].sum())

with col3:
    st.metric("🚑 Total Ambulances", df["ambulances"].sum())

st.divider()

# ==========================
# Beds Chart
# ==========================

st.subheader("🛏 Available Beds by Hospital")

fig1 = px.bar(
    df,
    x="hospital_name",
    y="available_beds",
    color="available_beds",
    text="available_beds",
    title="Available Beds"
)

st.plotly_chart(fig1, use_container_width=True)

# ==========================
# ICU Chart
# ==========================

st.subheader("❤️ ICU Beds Availability")

fig2 = px.bar(
    df,
    x="hospital_name",
    y="available_icu",
    color="available_icu",
    text="available_icu",
    title="ICU Beds"
)

st.plotly_chart(fig2, use_container_width=True)

# ==========================
# Ambulance Pie Chart
# ==========================

st.subheader("🚑 Ambulance Distribution")

fig3 = px.pie(
    df,
    names="hospital_name",
    values="ambulances",
    title="Ambulances"
)

st.plotly_chart(fig3, use_container_width=True)

# ==========================
# Hospital Data Table
# ==========================

st.subheader("📋 Hospital Resources")

st.dataframe(df, use_container_width=True)
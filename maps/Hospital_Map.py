import streamlit as st
import sqlite3
import pandas as pd
import folium
from streamlit_folium import st_folium

st.title("🗺️ Hospital Resource Map")

conn = sqlite3.connect("database.db")

df = pd.read_sql_query(
    "SELECT * FROM hospitals",
    conn
)

conn.close()

# Hyderabad center
hospital_map = folium.Map(
    location=[17.3850, 78.4867],
    zoom_start=11
)

for _, row in df.iterrows():

    popup = f"""
    <b>{row['hospital_name']}</b><br>
    Beds: {row['available_beds']}<br>
    ICU: {row['available_icu']}<br>
    Ambulances: {row['ambulances']}<br>
    Specialists: {row['specialists']}
    """

    folium.Marker(
        location=[row["latitude"], row["longitude"]],
        popup=popup,
        tooltip=row["hospital_name"],
        icon=folium.Icon(color="red", icon="plus-sign")
    ).add_to(hospital_map)

st_folium(
    hospital_map,
    width=1200,
    height=650
)
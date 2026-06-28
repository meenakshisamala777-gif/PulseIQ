import streamlit as st
import sqlite3

st.set_page_config(
    page_title="Admin Login",
    page_icon="🔐"
)

st.title("🔐 Admin Login")
st.write("Please enter your admin credentials.")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM admins
        WHERE username=? AND password=?
        """,
        (username, password)
    )

    admin = cursor.fetchone()

    conn.close()

    if admin:
        st.success("✅ Login Successful")
        st.session_state["logged_in"] = True
        st.balloons()
    else:
        st.error("❌ Invalid Username or Password")
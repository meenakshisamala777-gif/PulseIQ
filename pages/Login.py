import streamlit as st

st.set_page_config(page_title="Admin Login", page_icon="🔐")

st.title("🔐 Admin Login")

st.write("Enter your admin credentials.")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):

    if username == "admin" and password == "admin123":
        st.success("✅ Login Successful")
        st.info("Go to the Admin Dashboard page from the left sidebar.")
    else:
        st.error("❌ Invalid Username or Password")
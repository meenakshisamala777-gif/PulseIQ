
import streamlit as st
import sqlite3
import pandas as pd

from utils.ai_recommendation import recommend_hospital
from utils.pdf_generator import generate_pdf
from utils.emergency_priority import get_priority
from utils.qrcode_generator import create_qr
from utils.severity_predictor import predict_severity

st.set_page_config(
    page_title="Emergency Request",
    page_icon="🚨",
    layout="wide"
)

st.title("🚨 AI Emergency Care Resource Allocator")

st.write("Fill in the patient details to find the best hospital.")

# -----------------------------
# Database Connection
# -----------------------------

conn = sqlite3.connect("database.db")

df = pd.read_sql_query(
    "SELECT * FROM hospitals",
    conn
)

# -----------------------------
# Patient Details
# -----------------------------

patient_name = st.text_input(
    "👤 Patient Name"
)

emergency_type = st.selectbox(
    "🚑 Emergency Type",
    [
        "Heart Attack",
        "Stroke",
        "Accident",
        "Burn Injury",
        "Pregnancy",
        "General Emergency"
    ]
)

location = st.text_input(
    "📍 Current Location"
)

submit = st.button(
    "🔍 Find Best Hospital"
)
# -----------------------------
# Find Best Hospital
# -----------------------------

if submit:

    if patient_name.strip() == "":
        st.error("Please enter the patient name.")
        st.stop()

    if location.strip() == "":
        st.error("Please enter the current location.")
        st.stop()

    available = df[df["available_beds"] > 0]

    if available.empty:
        st.error("❌ No hospitals with available beds.")
        st.stop()

    # AI Recommendation
    best = recommend_hospital(
        available,
        emergency_type
    )

    # Emergency Priority
    priority = get_priority(emergency_type)
    st.subheader("🤖 AI Severity Prediction")

st.success(f"Predicted Severity: {priority}")

    # Specialist
specialist = best["specialists"]

    # Google Maps Link
maps_link = (
        f"https://www.google.com/maps?q="
        f"{best['latitude']},{best['longitude']}"
    )

    # Generate QR Code
qr_path = create_qr(
        maps_link,
        f"{patient_name}_QR"
    )

st.success("✅ Best Hospital Found")

st.info(f"🚨 Priority Level : {priority}")

st.markdown(f"### 🏥 {best['hospital_name']}")

col1, col2 = st.columns(2)

with col1:

        st.write("📍 Location :", best["location"])

        st.write("🛏 Available Beds :", best["available_beds"])

        st.write("❤️ ICU Beds :", best["available_icu"])

with col2:

        st.write("🚑 Ambulances :", best["ambulances"])

        st.write("👨‍⚕ Specialists :", specialist)

        st.markdown(
            f"[📍 Open in Google Maps]({maps_link})"
        )
            # -----------------------------
    # Save Emergency Request
    # -----------------------------

cursor = conn.cursor()

cursor.execute(
        """
        INSERT INTO emergency_requests
        (
            patient_name,
            emergency_type,
            location,
            assigned_hospital,
            status
        )

        VALUES(?,?,?,?,?)
        """,
        (
            patient_name,
            emergency_type,
            location,
            best["hospital_name"],
            "Assigned"
        )
    )

conn.commit()

st.success("✅ Emergency Request Saved Successfully!")

    # -----------------------------
    # Generate PDF
    # -----------------------------

pdf_file = generate_pdf(
        patient_name=patient_name,
        emergency_type=emergency_type,
        priority=priority,
        location=location,
        hospital=best["hospital_name"],
        specialist=specialist,
        beds=best["available_beds"],
        icu=best["available_icu"],
        ambulance=best["ambulances"],
        maps_link=maps_link,
        qr_path=qr_path
    )

st.success("📄 PDF Report Generated Successfully!")

with open(pdf_file, "rb") as pdf:

        st.download_button(
            label="📥 Download Emergency Report",
            data=pdf,
            file_name=f"{patient_name}_Emergency_Report.pdf",
            mime="application/pdf"
        )

# -----------------------------
# Close Database Connection
# -----------------------------

conn.close()
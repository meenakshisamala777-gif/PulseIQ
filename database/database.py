import sqlite3

# Connect to the database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Create hospitals table
cursor.execute("""
CREATE TABLE IF NOT EXISTS hospitals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hospital_name TEXT,
    location TEXT,
    latitude REAL,
    longitude REAL,
    total_beds INTEGER,
    available_beds INTEGER,
    icu_beds INTEGER,
    available_icu INTEGER,
    ambulances INTEGER,
    specialists TEXT
)
""")

# Create emergency requests table
cursor.execute("""
CREATE TABLE IF NOT EXISTS emergency_requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_name TEXT,
    emergency_type TEXT,
    location TEXT,
    assigned_hospital TEXT,
    status TEXT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    role TEXT
)
""")

# Save changes and close
conn.commit()
conn.close()

print("Database created successfully!")
import sqlite3
import os

def initialize_database():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Hospitals table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS hospitals(
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

    # Emergency Requests table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS emergency_requests(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_name TEXT,
        emergency_type TEXT,
        location TEXT,
        assigned_hospital TEXT,
        status TEXT
    )
    """)

    # Admin table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS admins(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
    """)

    # Insert hospital data only if table is empty
    cursor.execute("SELECT COUNT(*) FROM hospitals")

    if cursor.fetchone()[0] == 0:

        hospitals = [

            ("Apollo Hospital","Hyderabad",17.4239,78.4116,300,120,60,25,15,"Cardiology, Neurology"),

            ("Yashoda Hospital","Hyderabad",17.4273,78.4571,250,80,40,18,12,"Orthopedics, Cardiology"),

            ("KIMS Hospital","Hyderabad",17.4357,78.4483,350,160,70,30,20,"Neurology, Trauma"),

            ("Care Hospital","Hyderabad",17.4412,78.4983,200,90,35,12,10,"Emergency Medicine"),

            ("AIG Hospital","Hyderabad",17.4355,78.3715,180,75,30,10,8,"Gastroenterology"),

            ("Sunshine Hospital","Hyderabad",17.4946,78.3917,220,100,45,20,14,"Cardiology"),

            ("Medicover Hospital","Hyderabad",17.4337,78.4485,240,95,38,16,11,"Pulmonology"),

            ("Continental Hospital","Hyderabad",17.4174,78.3415,280,140,55,28,18,"Multi Speciality"),

            ("Rainbow Hospital","Hyderabad",17.4198,78.4487,160,70,25,9,7,"Pediatrics"),

            ("Global Hospital","Hyderabad",17.3984,78.4792,260,110,48,19,13,"Trauma, Neurology")

        ]

        cursor.executemany("""
        INSERT INTO hospitals(
            hospital_name,
            location,
            latitude,
            longitude,
            total_beds,
            available_beds,
            icu_beds,
            available_icu,
            ambulances,
            specialists
        )
        VALUES(?,?,?,?,?,?,?,?,?,?)
        """, hospitals)

    # Create default admin if none exists
    cursor.execute("SELECT COUNT(*) FROM admins")

    if cursor.fetchone()[0] == 0:
        cursor.execute("""
        INSERT INTO admins(username,password)
        VALUES('admin','admin123')
        """)

    conn.commit()
    conn.close()
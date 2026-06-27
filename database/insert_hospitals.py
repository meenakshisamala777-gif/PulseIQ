import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

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
VALUES (?,?,?,?,?,?,?,?,?,?)
""", hospitals)

conn.commit()
conn.close()

print("Hospital data inserted successfully!")
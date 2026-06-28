import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

try:
    cursor.execute("SELECT * FROM admins")
    admins = cursor.fetchall()

    print("Admins in database:")
    for admin in admins:
        print(admin)

except Exception as e:
    print("Error:", e)

conn.close()
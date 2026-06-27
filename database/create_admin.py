import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

try:
    cursor.execute("""
    INSERT INTO users (username, password, role)
    VALUES (?, ?, ?)
    """, ("admin", "admin123", "Admin"))

    conn.commit()
    print("✅ Admin account created successfully!")

except sqlite3.IntegrityError:
    print("ℹ️ Admin account already exists.")

except Exception as e:
    print("❌ Error:", e)

finally:
    conn.close()
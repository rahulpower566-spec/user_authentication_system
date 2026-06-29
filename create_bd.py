import sqlite3

# Connect to database (file create avthundi if not exists)
conn = sqlite3.connect("database.db")
c = conn.cursor()

# ---------------- USERS TABLE ----------------
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
''')

# ---------------- STUDENTS TABLE ----------------
c.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    course TEXT
)
''')

# Save changes
conn.commit()
conn.close()

print("✅ Database Created Successfully!")
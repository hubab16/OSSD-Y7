import sqlite3

con = sqlite3.connect("project.db")
cursor = con.cursor()

# Create students table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id      INTEGER PRIMARY KEY AUTOINCREMENT,
        name    TEXT    NOT NULL,
        age     INTEGER,
        grade   TEXT
    )
""")

con.commit()
con.close()

print("Database and table created successfully.")

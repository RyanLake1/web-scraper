import datetime
import sqlite3

# 1. Connect with type parsing enabled
conn = sqlite3.connect("app.db", detect_types=sqlite3.PARSE_DECLTYPES)
cursor = conn.cursor()

# 2. Define the column as TIMESTAMP or DATE
cursor.execute("""
    CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY,
        name TEXT,
        created_at TIMESTAMP
    )
""")
conn.commit()

# 3. Insert a native Python datetime object directly
now = datetime.datetime.now(datetime.timezone.utc)

cursor.execute(
    "INSERT INTO events (name, created_at) VALUES (?, ?)", 
    ("Launch Event", now)
)
conn.commit()

# 4. Query data - it comes back as a Python datetime object automatically!
cursor.execute("SELECT name, created_at FROM events")
row = cursor.fetchone()

print(row[0])  # Output: Launch Event
print(type(row[1]))  # Output: <class 'datetime.datetime'>
print(row[1])

# don't know how i will store date / datetime yet
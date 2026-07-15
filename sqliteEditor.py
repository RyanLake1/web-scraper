import sqlite3

# SQLite: https://docs.python.org/3/library/sqlite3.html#sqlite3-tutorial


connect = sqlite3.connect("scraped.db")
cursor = connect.cursor()

connect.execute("PRAGMA foreign_keys = ON;")
# need to test that foreign keys is actually active, can once im later in design (see testforeignkey.py)




# show tables
res = cursor.execute("SELECT name FROM sqlite_master")
print(f"{res.fetchall()}")

# cursor.execute("""
#     INSERT INTO movie VALUES
#         ('Monty Python and the Holy Grail', 1975, 8.2),
#         ('And Now for Something Completely Different', 1971, 7.5)
# """)
# connect.commit()

# res = cursor.execute("SELECT score FROM movie")
# print(f"{res.fetchall()}")
connect.close()

# Type notes: 
# No BOOLEAN Type: SQLite stores booleans as INTEGER (1 for true, 0 for false).
# No DATETIME Type: Dates must be manually managed and stored as TEXT (ISO-8601 strings), INTEGER (Unix timestamps), or REAL (Julian days).

# Tables created:
# cursor.execute("" \
#     "CREATE TABLE scp_stories (" \
#     "link TEXT PRIMARY KEY," \
#     " title TEXT," \
#     " author TEXT," \
#     " series_hub TEXT)" \
# "")
# cursor.execute("" \
#     "CREATE TABLE story_to_date (" \
#     "id INTEGER PRIMARY KEY," \
#     " story_link TEXT NOT NULL," \
#     " date TEXT NOT NULL," \
#     " FOREIGN KEY (story_link) REFERENCES scp_stories(link))" \
# "")
# cursor.execute("" \
#     "CREATE TABLE story_to_tag (" \
#     "id INTEGER PRIMARY KEY," \
#     " story_link TEXT NOT NULL," \
#     " tag TEXT NOT NULL," \
#     " FOREIGN KEY (story_link) REFERENCES scp_stories(link))" \
# "")
# cursor.execute("" \
#     "CREATE TABLE story_to_location (" \
#     "id INTEGER PRIMARY KEY," \
#     " story_link TEXT NOT NULL," \
#     " location TEXT NOT NULL," \
#     " FOREIGN KEY (story_link) REFERENCES scp_stories(link))" \
# "")
# cursor.execute("" \
#     "CREATE TABLE story_to_character (" \
#     "id INTEGER PRIMARY KEY," \
#     " story_link TEXT NOT NULL," \
#     " character TEXT NOT NULL," \
#     " FOREIGN KEY (story_link) REFERENCES scp_stories(link))" \
# "")
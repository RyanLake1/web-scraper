import sqlite3

# SQLite: https://docs.python.org/3/library/sqlite3.html#sqlite3-tutorial


connect = sqlite3.connect("scraped.db")
cursor = connect.cursor()

connect.execute("PRAGMA foreign_keys = ON;")
# need to test that foreign keys is actually active, can once im later in design (see testforeignkey.py)

# Foreign key needs to be enabled from now on whenever I enter or retrieve input? Figure out when testing later.
# Only when I am entering info into a table that has a foreign key


# cursor.execute("""
#     INSERT INTO scp_stories VALUES
#         ("link2", "title", "author", "series hub link")
# """)
# connect.commit()

# implement a catch for:
#   sqlite3.IntegrityError: UNIQUE constraint failed: scp_stories.link
# if you are inserting information for the same link
# or I could check if the link is in the table first.
# I could potentially just replace the info in the table if I am going over the same link.

# show tables
res = cursor.execute("SELECT name FROM sqlite_master")
print(f"{res.fetchall()}")

# res = cursor.execute("SELECT link FROM scp_stories")
# print(f"{res.fetchall()}")
connect.close()

# Easy commands:
# cursor.execute("DROP TABLE table")

# Type notes: 
# No BOOLEAN Type: SQLite stores booleans as INTEGER (1 for true, 0 for false).
# No DATETIME Type: Dates must be manually managed and stored as TEXT (ISO-8601 strings), INTEGER (Unix timestamps), or REAL (Julian days).

# Tables created:
# cursor.execute("""
#     CREATE TABLE scp_stories (
#         link TEXT PRIMARY KEY,    # base site is https://scp-wiki.wikidot.com
#         title TEXT, 
#         author TEXT, 
#         series_hub_link TEXT      # base site is https://scp-wiki.wikidot.com
#     )
# """)
# NOTES**** base site is https://scp-wiki.wikidot.com don't store it, only store the path
# cursor.execute(""""
#     CREATE TABLE story_to_date (
#         id INTEGER PRIMARY KEY,
#         story_link TEXT NOT NULL,
#         date TEXT NOT NULL,
#         FOREIGN KEY (story_link) REFERENCES scp_stories(link)
#     )
# """)
# cursor.execute(""""
#     CREATE TABLE story_to_tag (
#         id INTEGER PRIMARY KEY,
#         story_link TEXT NOT NULL,
#         tag TEXT NOT NULL,
#         FOREIGN KEY (story_link) REFERENCES scp_stories(link)
#     )
# """)
# cursor.execute(""""
#     CREATE TABLE story_to_location (
#         id INTEGER PRIMARY KEY,
#         story_link TEXT NOT NULL,
#         location TEXT NOT NULL,
#         FOREIGN KEY (story_link) REFERENCES scp_stories(link)
#     )
# """)
# cursor.execute(""""
#     CREATE TABLE story_to_character (
#         id INTEGER PRIMARY KEY,
#         story_link TEXT NOT NULL,
#         character TEXT NOT NULL,
#         FOREIGN KEY (story_link) REFERENCES scp_stories(link)
#     )
# """)
import requests
import sqlite3
from bs4 import BeautifulSoup
# Download requests: https://pypi.org/project/requests/
# Download Beautiful Soup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# SQLite: https://docs.python.org/3/library/sqlite3.html#sqlite3-tutorial

# NOTES**** base site is https://scp-wiki.wikidot.com don't store it, only store the path

URL = "https://scp-wiki.wikidot.com/a-betamax-suicide-note"

response = requests.get(URL)

if response.status_code == 200:
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find elements by their HTML tags and classes
    title = soup.find(class_="meta-title").text.strip()
    series_hub_link = soup.find(class_="pseudocrumbs").find("a").get('href')
    author = soup.find("div", id="page-content").find(class_="collection").find(class_="collapsible-block-unfolded").find(class_="namerow").find(class_="list-pages-item").text.strip()
    author = author[:-8]
    URL = URL.replace("https://scp-wiki.wikidot.com", "")
        
    # Save extracted data into scraped.db
    connect = sqlite3.connect("scraped.db")
    cursor = connect.cursor()

    cursor.execute("""
        INSERT INTO scp_stories VALUES
            (?, ?, ?, ?)
    """, (URL, title, author, series_hub_link))
    connect.commit()
        
    print(f"Successfully scraped {URL} URL!")

    # scraped and added to database, next time test to make sure can retrieve content

    connect.close()
else:
    print(f"Failed to access site. Status code: {response.status_code}")

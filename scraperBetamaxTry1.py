import requests
import sqlite3
from bs4 import BeautifulSoup

# Download requests: https://pypi.org/project/requests/
# Download Beautiful Soup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# SQLite: https://docs.python.org/3/library/sqlite3.html#sqlite3-tutorial

# Target URL
URL = "https://scp-wiki.wikidot.com/a-betamax-suicide-note"

response = requests.get(URL)

if response.status_code == 200:
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find elements by their HTML tags and classes
    title = soup.find("div", class_="meta-title").text.strip()
    #
    # scraped_data = []
    # for book in books:
    #     title = book.find("h3").text.strip()
    #     price = book.find("p", class_="price_color").text.strip()
    #     scraped_data.append([title, price])
        
    # Save extracted data into a separate file
        
    print(f"Successfully scraped {title} title!")
else:
    print(f"Failed to access site. Status code: {response.status_code}")
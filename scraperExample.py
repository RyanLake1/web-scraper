import csv
import requests
from bs4 import BeautifulSoup

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# Define target URL and headers to mimic a real browser session
URL = "https://example-shop-books.com"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

# Step 1: Download the page source
response = requests.get(URL, headers=HEADERS)

if response.status_code == 200:
    # Step 2: Parse the raw HTML text
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Step 3: Find elements by their HTML tags and classes
    books = soup.find_all("div", class_="product-pod")
    
    scraped_data = []
    for book in books:
        title = book.find("h3").text.strip()
        price = book.find("p", class_="price_color").text.strip()
        scraped_data.append([title, price])
        
    # Step 4: Save extracted data into a clean spreadsheet
    with open("books.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Price"])  # Headers
        writer.writerows(scraped_data)
        
    print(f"Successfully scraped {len(scraped_data)} items!")
else:
    print(f"Failed to access site. Status code: {response.status_code}")
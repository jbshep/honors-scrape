import requests
from bs4 import BeautifulSoup
import time

def scrape_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        books = []

        for book in soup.find_all('article'):
            title = book.find('img')['alt']
            price_text = book.find('p', class_='price_color').get_text()  # e.g. '£53.74'
            price = float(price_text.replace('£', ''))

            books.append((title, price))

            #print(f"{title} - £{price}")

        # Find the most expensive book
        if books:
            most_expensive = max(books, key=lambda x: x[1])
            print("\n The Most Expensive Book Is:")
            print(f"{most_expensive[0]} - £{most_expensive[1]}")
        else:
            print("No books found.")

        time.sleep(2)
    else:
        print(f"Failed to retrieve page. Status code: {response.status_code}")

scrape_page('https://books.toscrape.com')
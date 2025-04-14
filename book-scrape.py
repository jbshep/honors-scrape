import requests
from bs4 import BeautifulSoup
import time

def scrape_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    # Check if the page was successfully fetched
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # keep track of most expensive book price and title
        most_title = ''
        most_price = 0.00

        for book in soup.find_all('article'):
            #print(book.find('img')['alt'])
            #print(book.find('p', 'price_color').get_text())

            price = book.find('p', 'price_color').get_text()
            price = float(price[1:])

            if price > most_price:
                most_price = price
                most_title = book.find('img')['alt']

        # Respectful delay
        time.sleep(2)  # Avoid overloading the server
    
        print(most_title)
        print(most_price)

    else:
        print(f"Failed to retrieve page. Status code: {response.status_code}")

scrape_page('https://books.toscrape.com')


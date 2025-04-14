import requests
from bs4 import BeautifulSoup
import time

book_titles = []
book_prices = []

#def scrape_page(url):
def scrape_page(num):
    url = f"https://books.toscrape.com/catalogue/page-{num}.html"
    print(f"Scraping {url}")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    # Check if the page was successfully fetched
    if response.status_code == 200 and num != 10:
        soup = BeautifulSoup(response.content, 'html.parser')


        for book in soup.find_all('article'):
            book_titles.append(book.find('img')['alt'])
            book_prices.append(book.find('p', 'price_color').get_text())

        # Respectful delay
        time.sleep(2)  # Avoid overloading the server

        # Scrape the next page
        scrape_page(num + 1)
    else:
        print(f"Failed to retrieve page. Status code: {response.status_code}")
        print("I guess we are done.")

#scrape_page('https://books.toscrape.com')
scrape_page(1)

print(len(book_titles))

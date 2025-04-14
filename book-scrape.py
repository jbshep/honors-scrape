import requests
from bs4 import BeautifulSoup
import time

def scrape_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    title = ""
    price =0.0
    # Check if the page was successfully fetched
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')


        for book in soup.find_all('article'):
            if(price<float(book.find('p', 'price_color').get_text().replace("£", ""))):
                price = float(book.find('p', 'price_color').get_text().replace("£", ""))
                title = book.find('img')['alt']
            #print(book.find('img')['alt'])
            #print(book.find('p', 'price_color').get_text())

        # Respectful delay
        time.sleep(2)  # Avoid overloading the server
        print(title)
        print(price)
    else:
        print(f"Failed to retrieve page. Status code: {response.status_code}")

scrape_page('https://books.toscrape.com')


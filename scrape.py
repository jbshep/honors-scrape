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
        # Extract and print data
        #for item in soup.find_all('h1'):
        for item in soup.find_all("div", "link-feature__ind-element__description--wrapper"):
            print(item.get_text())

        # Respectful delay
        time.sleep(2)  # Avoid overloading the server
    else:
        print(f"Failed to retrieve page. Status code: {response.status_code}")

scrape_page('https://bvu.edu/')


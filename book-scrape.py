import requests
from bs4 import BeautifulSoup
import time
price = 0

def scrape_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    # Check if the page was successfully fetched
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        highest_price = 0
        highest_title = "None"
        for book in soup.find_all('article'):
            assign_tit = book.find('img')['alt']
            title = str(assign_tit)
            print(book.find('img')['alt'])
            print(book.find('p', 'price_color').get_text())
        #Get rid of pound sign
            assign_var = book.find('p', 'price_color').get_text()
            prices_str = (assign_var.strip().replace('£', ''))
            price= float(prices_str)
#            # print(prices)

        #Comparing prices
            if highest_price <= price:
                highest_price = price
                highest_title = title
                
        print("")
        print(f"The most expensive book is {highest_title} at £{highest_price}.")
        
        # Respectful delay
        time.sleep(2)  # Avoid overloading the server
    else:
        print(f"Failed to retrieve page. Status code: {response.status_code}")

scrape_page('https://books.toscrape.com')


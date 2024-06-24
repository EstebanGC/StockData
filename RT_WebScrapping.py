import requests
from bs4 import BeautifulSoup

url = 'https://www.bloomberg.com/markets/currencies/americas'

response = requests.get(url)

if response.status_code == 200:
    print("Succesful request!")
else:
        print("Error getting page:", response.status_code)
        exit()

soup = BeautifulSoup(response.content, 'html.parser')

element_price = soup.find("span", class_='data-table-row-cell')

bitcoin_price = element_price.text.strip()

print("Bitcoin price:", bitcoin_price)
print("Whatever again")
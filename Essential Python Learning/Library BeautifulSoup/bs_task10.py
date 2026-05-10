# From the following URL:

# https://coinmarketcap.com/

# 10. Get the name and Price.


from bs4 import BeautifulSoup
import requests


url = 'https://coinmarketcap.com/'

r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

records = soup.tbody.contents
prices = {}

# Due to technical difficulties we use only first 10 records
for record in records[:10]:
    name, price = record.contents[2:4]
    fixed_name = name.p.string
    fixed_price = price.span.string

    prices[fixed_name] = fixed_price

print(prices)

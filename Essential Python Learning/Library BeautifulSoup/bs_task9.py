# 8. Find the price


from bs4 import BeautifulSoup
import re

with open("index2.html", 'r') as f:
    soup = BeautifulSoup(f, "html.parser")

# Finding the price

pattern = re.compile(r'\$.*')
prices = soup.find_all(string=pattern, limit=1)
for price in prices:
    print(price.strip())
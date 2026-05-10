# From index2.html 
# 6. Find the first option Tag and change the value attribute to "new value"

from bs4 import BeautifulSoup

with open("index2.html", 'r') as f:
    soup = BeautifulSoup(f, "html.parser")

first_option = soup.find('option')
print(first_option)

# Changing the value attribute:

first_option['value'] = "new value"
print(first_option)

# Creating new color attribute:

first_option['color'] = 'blue'
print(first_option)

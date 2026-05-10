# From index.html:
# 2. Change the Title tags text content to "Mir Shawkat Ali"

from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    soup = BeautifulSoup(f, features="html.parser")

title = soup.title
title.string = "Mir Shawkat Ali"

# Getting the Title Tag
print(title)

# Getting the Text of the Title Tag
print(title.string)
print(title.text)

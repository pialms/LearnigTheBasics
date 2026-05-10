# From index.html:
# 1. Find title tag and text within it

from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    soup = BeautifulSoup(f, features="html.parser")

title = soup.title

# Getting the Title Tag
print(title)

# Getting the Text of the Title Tag
print(title.string)
print(title.text)

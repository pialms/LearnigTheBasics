# 2. Get the image from the above site and save into the folder.

import requests
from bs4 import BeautifulSoup
import re

r = requests.get("https://xkcd.com/363/")
soup = BeautifulSoup(r.text, "html.parser")

# Creating a list of a Tags:
a_tags = soup.find_all('a')

# Creating a Pattern to catch the desired png link
pattern = re.compile(r'https://imgs\.[^\s]+\.png')
png_url = ""

# Looping Throug the list of a Tags and trying to get the required png url:
for a in a_tags:
    match = pattern.findall(a['href'])
    if match:
        png_url = match[0]

# Making a request with the png url:
png_r = requests.get(png_url)

# Saving the png file as comic.png into the folder

with open('comic.png', 'wb') as f:
    f.write(png_r.content)

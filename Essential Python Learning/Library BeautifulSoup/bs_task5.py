# 5. Find the Price of the Graphics Card from the given URL: https://www.newegg.ca/gigabyte-windforce-gv-n5080wf3-16gd-geforce-rtx-5080-16gb-graphics-card-triple-fans/p/N82E16814932780

from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.ca/gigabyte-windforce-gv-n5080wf3-16gd-geforce-rtx-5080-16gb-graphics-card-triple-fans/p/N82E16814932780"

r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
print(soup.find_all(string='$')[0].parent.find('strong').string)
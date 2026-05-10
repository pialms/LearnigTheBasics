# From index.html:
# 3. Find All `<P>` Tags

from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    soup = BeautifulSoup(f, "html.parser")

all_p_tags = soup.find_all('p')
print(all_p_tags[0])
print(f'Total number of Main P tags is: {len(all_p_tags)}')
print('There is many nested P tags')


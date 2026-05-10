# From index.html:
# 4. Find All `<b>` Tags of first Main `<p>` Tags

from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    soup = BeautifulSoup(f, "html.parser")

all_p_tags = soup.find_all('p')
b_tagsOfFirst_p_tag = all_p_tags[0].find_all('b')
print(b_tagsOfFirst_p_tag)

for b in b_tagsOfFirst_p_tag:
    print(b.string)
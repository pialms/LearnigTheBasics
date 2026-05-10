# 7. find 
#     - all p and div tag
#     - option tag that has undergraduate text


from bs4 import BeautifulSoup

with open("index2.html", 'r') as f:
    soup = BeautifulSoup(f, "html.parser")

# Finding all p and div tag

p_div_tag = soup.find_all(['p', 'div'])
print(len(p_div_tag))

# Finding option tag that has undergraduate text

option_tag = soup.find_all(['option'], string='Undergraduate')
print(option_tag)


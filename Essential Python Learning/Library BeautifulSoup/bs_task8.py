# 8. Find the tag elements that has 'btn-item' class name


from bs4 import BeautifulSoup

with open("index2.html", 'r') as f:
    soup = BeautifulSoup(f, "html.parser")

# Finding the tag elements that has 'btn-item' class name

class_btn_item = soup.find_all(class_= 'btn-item')
print(class_btn_item)

for item in class_btn_item:
    print(item.string)
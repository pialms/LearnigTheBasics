# From text-to-search.txt File find the following pattern:
# 12. Find all 03 E-mail ID

import re

with open('text_to_search.txt', 'r') as f:
    text_to_search = f.read()

pattern = re.compile(r'[\w.-]+@[\w-]+\.[\w]+')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
    
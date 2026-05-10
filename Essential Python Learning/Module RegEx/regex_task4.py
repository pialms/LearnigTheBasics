# From text-to-search.txt File find the following pattern:
# 4. From data.txt Find the Phone Numbers and print how many Phone Numbers were found

import re

with open('data.txt', 'r', encoding='utf-8') as g:
    content = g.read()

pattern4 = re.compile(r'\d{3}.\d{3}.\d{4}')
matches = pattern4.finditer(content)

length = 0

for match in matches:
    print(match)
    length += 1

print(f'Total Number of Phone Numbers Found {length}')
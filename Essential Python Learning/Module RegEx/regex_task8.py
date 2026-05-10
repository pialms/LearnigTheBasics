# From text-to-search.txt File find the following pattern:
# 8. Find cat, mat , pat but not bat

import re

with open('text_to_search.txt', 'r') as f:
    text_to_search = f.read()

pattern = re.compile(r'[^b]at')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
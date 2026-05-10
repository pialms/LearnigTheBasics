# From text-to-search.txt File find the following pattern:
# 11. Find all 05 Names

import re

with open('text_to_search.txt', 'r') as f:
    text_to_search = f.read()

pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
    
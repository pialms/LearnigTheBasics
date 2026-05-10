# From text-to-search.txt File find the following pattern:
# 7. From data.txt Find the Phone Numbers That Starts with 800 & 900

import re

with open('data.txt', 'r') as f:
    text_to_search = f.read()

pattern = re.compile(r'[89]00[-.]\d{3}[-.]\d{4}')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
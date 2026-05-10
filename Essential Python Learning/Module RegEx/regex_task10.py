# From text-to-search.txt File find the following pattern:
# 10. Find Mr and Mr. with their full Name

import re

with open('text_to_search.txt', 'r') as f:
    text_to_search = f.read()

pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
    
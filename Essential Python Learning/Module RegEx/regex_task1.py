# From text-to-search.txt File find the following pattern:
# 1. Find: abc

import re

with open('text_to_search.txt', 'r') as f:
    text_to_search = f.read()

pattern1 = re.compile(r'abc')
matches = pattern1.finditer(text_to_search)

for match in matches:
    print(match)

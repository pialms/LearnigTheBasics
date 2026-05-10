# From text-to-search.txt File find the following pattern:
# 2. Find: . (dot/fullstop) and Count the number of occurance.

import re

with open('text_to_search.txt', 'r') as f:
    text_to_search = f.read()


pattern = re.compile(r'\.')
matches = pattern.finditer(text_to_search)

length = 0

for match in matches:
    print(match)
    length += 1

print(f'Number of Match found {length} times')

# From text-to-search.txt File find the following pattern:
# 3. Find the Phone Number (which has unique Pattern).

import re

with open('text_to_search.txt', 'r') as f:
    text_to_search = f.read()


pattern3 = re.compile(r'\d{3}.\d{3}.\d{4}')
matches = pattern3.finditer(text_to_search)
length = 0

for match in matches:
    print(match)
    length += 1

print(f'Number of Phone number found is {length}')
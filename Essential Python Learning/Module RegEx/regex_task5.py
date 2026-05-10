# From text-to-search.txt File find the following pattern:
# 5. Find the Phone Numbers That only has - or .
import re

with open('text_to_search.txt', 'r') as f:
    text_to_search = f.read()


pattern5 = re.compile(r'\d{3}[.-]\d{3}[.-]\d{4}')
matches = pattern5.finditer(text_to_search)
count = 0

for match in matches:
    print(match)
    count += 1
print(f'Number of match found {count}')
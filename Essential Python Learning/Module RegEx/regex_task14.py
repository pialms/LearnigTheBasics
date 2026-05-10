# From text-to-search.txt File find the following pattern:
# 14. Find only Domain Name (Domain + Top Level Domain) from the URLs

import re

with open('text_to_search.txt', 'r') as f:
    text_to_search = f.read()

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match.group(2) + match.group(3))
    
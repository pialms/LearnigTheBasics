# From text-to-search.txt File find the following pattern:
# 15. Find only Domain Name (Domain + Top Level Domain) from the URLs (Important: Use Group Method and `re.sub()` Methcod)

import re

with open('text_to_search.txt', 'r') as f:
    text_to_search = f.read()

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
subbed_urls = pattern.sub(r'\2\3', text_to_search)

print(subbed_urls)
    
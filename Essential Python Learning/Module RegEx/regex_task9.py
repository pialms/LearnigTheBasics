# From text-to-search.txt File find the following pattern:
# 9. Find Mr and Mr.

import re

with open('text_to_search.txt', 'r') as f:
    text_to_search = f.read()

pattern = re.compile(r'Mr\.?')
matches = pattern.finditer(text_to_search)

for match in matches:
    x= match.span(0)[0]
    y= match.span(0)[1]
    
    print(match)
    print(text_to_search[x:y+5])





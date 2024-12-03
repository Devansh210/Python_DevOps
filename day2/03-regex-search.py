import re

text="The little white fox is running"
pattern= r"white"

search=re.search(pattern,text)

if search:
    print("Pattern found:",search.group())
else:
    print("Pattern not found")    
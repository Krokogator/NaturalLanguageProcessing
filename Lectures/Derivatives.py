import re

filepath = "odm.txt"

with open(filepath, encoding='utf8') as f:
    content = f.readlines()

regex = re.compile(r'.*,.*')

filtered = list(filter(lambda i: regex.search(i), content))

i = 0
while i < filtered.__len__():
    print(filtered[i])
    i += 1

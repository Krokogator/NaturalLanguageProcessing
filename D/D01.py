import re

filepath = "test"

file = open(filepath, encoding='utf8').read()

regex1 = '\d+ (\d+) (\d+)\s+[^\s]+\s+[^\s]+puddle\s+(NP)'
regex2 = '\d+ \d+ \d+\s+.+text\s+(.+)TEXT'
regex3 = r'_'

text = re.search(regex2, file).group(1)
text = re.sub(regex3, ' ', text)

for word in set(re.findall(regex1, file)):
    beg = int(word[0])
    len = int(word[1])
    print(text[beg: beg+len])
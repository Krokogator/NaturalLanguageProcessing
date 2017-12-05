import nltk
import re

filepath = "Assets/D04_13"

tadek = open(filepath, encoding='utf8').read().lower()

tokens = nltk.word_tokenize(tadek)

regex = re.compile(r'\b[a-zęóąśłżźćń]{3,}\b')

filtered = filter(lambda i: regex.search(i), tokens)

for idx, word in enumerate(nltk.FreqDist(filtered).most_common(50)):
    print(word)


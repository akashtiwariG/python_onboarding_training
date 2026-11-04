words=["car","bike","car","plane","car","bike"]
dict={}
for word in words:
    dict[word]=dict.get(word,0)+1
print(dict)

from collections import Counter
print(Counter(words))
print(Counter(words).most_common(2))
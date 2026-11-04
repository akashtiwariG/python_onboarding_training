import re

words=["banana","kiwi","apple","fig"]

print(sorted(words,key=len))
print(sorted(words,key=len,reverse=True))
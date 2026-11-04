import time
words = ["Hey","Hi"]*2000
print(len(words))

start=time.time()
s=""
for w in words:
    s += w
end = time.time()
print(end-start)

start = time.time()
s = " ".join(words)
wns = time.time()
print(end-start)
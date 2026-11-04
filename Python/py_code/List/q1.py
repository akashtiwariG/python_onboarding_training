s="akafdrgsuyuo"
count=0
s1="listen"
s2="silent"
for x in s:
    if x == 'a' or x=='e' or x=='i' or x=='o' or x=='u':
        count+=1

print(count)

print(sorted(s1) == sorted(s2))

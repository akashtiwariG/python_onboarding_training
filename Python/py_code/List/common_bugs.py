list_1 = [0]*3
id(list_1)

bad=[[0]*3]*3
for row in bad:
    print(id(row))

print(bad)
bad[0][0]=-1
print(bad)

good=[[0]*3 for suman in range(3)]
good[0][0]=99
print(good)

for row in good:
    print(id(row))
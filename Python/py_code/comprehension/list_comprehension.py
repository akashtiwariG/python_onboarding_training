lst = [i*i for i in range(1,11)]
print(lst)

lst2 = [i*i for i in range(1,11) if i%2==0]
print(lst2)

lst3 = ["even" if n%2 == 0 else "odd" for n in range(1,11)]
print(lst3)

products=["ford town car","alfa romeo","grand touring sedan"]

print([p.title() for p in products])
print([len(p) for p in products])
print([p for p in products if "car" in p])
print([p.split()[0] for p in products])
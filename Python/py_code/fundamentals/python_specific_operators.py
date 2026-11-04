list_a = [1,2,3]
list_b = [1,2,3]

print(list_a is list_b)
print(list_a == list_b) 

list_c = list_a
print(list_c is list_a)

d=257
e=257
print(d is e)

x=255
y=255
z=255
print(d is e)

print(id(x))
print(id(y))
print(id(z))

print(x is None)
print(None is None)
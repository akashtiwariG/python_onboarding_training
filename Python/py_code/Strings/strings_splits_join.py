s = "classic cars"

slits = s.split()
print(slits)
print(type(slits))

print("a-b-c".split("-"))
print("a,b,ccc".split(","))

print("-".join(["a","b","c"]))
print("-".join(slits))
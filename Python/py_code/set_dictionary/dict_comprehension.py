names=["Aditi","Sneha","Rahul"]
names_len={name:len(name) for name in names}
print(names_len)

scores={"Aditi":88,"Rahul":76,"Sneha":92,"Aditya":76}
print({k:v for k,v in scores.items() if v >=85})
print({k.upper(): v for k,v in scores.items()})
print({v:k for k,v in scores.items()})

print({k:v for k,v in zip(names,[88,76,92,100])})

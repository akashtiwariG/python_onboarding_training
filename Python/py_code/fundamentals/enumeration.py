fruits = ["Apple","Banana","Cherry","Date","Elderberry"]

for i,value in enumerate(fruits,start=1):
    print(i,value)

names=["Aditi","Rahul"]
scores=[88,79]
for name,score in zip(names,scores):
    print(f"{name}:{score}")

pairs = [("a",1),("b",2),("c",3)]
letters,numbers = zip(*pairs)
print(letters)
print(numbers)
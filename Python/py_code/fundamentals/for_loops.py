fruits = ["Apple", "Banana", "Cherry","Date", "Elderberry"]

for fruit in fruits:
    print(fruit)

num=11
for i in range(3,num+1,2):
    print(i)

numbers=[2,4,6,8]
target=9

for num in numbers:
    if num == target:
        print(f"found {target}")
        break
    else:
        print(f"{target} not found in the list ")
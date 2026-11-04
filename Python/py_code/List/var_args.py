def total_sum(*numbers):
    print(type(numbers))
    return sum(numbers)

sum1 = total_sum(5,4,15,1,5,1,54)
print(sum1)


person=("Alice",30,"Engineer")
print(person)
name,age,profession=person
print(name)
print(age)
print(person)
print()

nums=(1,2,3,4,5)
first,*rest=nums
print(first)
print(rest)
print(type(rest))
print()

nums=(1,2,3,4,5)
first,*middle,last=nums
print(first)
print(middle)
print(last)
print()



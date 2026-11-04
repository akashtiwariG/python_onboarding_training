def square(x):
    return x*x
print(id(square))
print(type(square))

sqr = square
#print(square(3))
#print(sqr(3))

def apply_twice(func,value):
    return func(func(value))

print(apply_twice(square,5))
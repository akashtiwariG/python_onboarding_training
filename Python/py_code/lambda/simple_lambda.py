def square(x):
    return x*x
square_lambda=lambda x:x*x
print(square(8),square_lambda(8))
power_lambda=lambda a,b:a**b
print(power_lambda(5,4))

greet = lambda name,greetings="Hello":f"{greetings},{name}"
print(greet(("Suman")))
print(greet("Suman","Happy Diwali"))
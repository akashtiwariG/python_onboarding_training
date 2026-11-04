def show():
    print("Hello world")

def greet(name):
    """function to greet a person with his name"""
    return f"Hello, {name}"

greeting=greet("Alice")
print(greeting)
print(greet.__doc__)
print(zip.__doc__)
print(show())
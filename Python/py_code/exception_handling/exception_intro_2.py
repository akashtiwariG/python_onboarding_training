def divide_unsafe2(a,b):

    try:
        return a/b
    except ZeroDivisionError as e :
        print(e)
        return None
    except TypeError as e :
        print(e)
        return None

print(divide_unsafe2(8,2),end="\n\n")
print(divide_unsafe2(0,0),end="\n\n")
print(divide_unsafe2(10,2),end="\n\n")
print(divide_unsafe2(10,0),end="\n\n")
print(divide_unsafe2(10,5),end="\n\n")
print(divide_unsafe2(10,5),end="\n\n")
print(divide_unsafe2("0",0))
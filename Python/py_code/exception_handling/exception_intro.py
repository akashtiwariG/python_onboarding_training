print("STATRT")

def divide_unsafe2(a,b):
    res=0
    try:
        res=a/b
    except ZeroDivisionError as e :
        print(e)

def divide_unsafe(a,b):
    return a/b



try:
    print(divide_unsafe2(8,0))
except ZeroDivisionError as e:
    print("yes")
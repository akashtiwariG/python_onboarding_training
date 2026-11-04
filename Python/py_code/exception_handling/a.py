def proces(value):
    try:
        res=value/100
    except ZeroDivisionError:
        print("except Division by 0")
    except TypeError as e:
        print(e)
    else:
        print(res)
    finally:
        print("finally block cleanup")

    proces(4)

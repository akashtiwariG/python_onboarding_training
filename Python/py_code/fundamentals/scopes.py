x="global"

def show_scope():
    global x
    x="local to x"
    #y="local_y"
    print(x)
    #print(y)

show_scope()
print(x)
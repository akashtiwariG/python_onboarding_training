counter=0

def increment():
    counter+=1
    print(counter)

#increment()
def helper(num):
    num+=1
    return num


counter=helper(counter)
counter=helper(counter)
counter=helper(counter)
counter=helper(counter)

print(counter)
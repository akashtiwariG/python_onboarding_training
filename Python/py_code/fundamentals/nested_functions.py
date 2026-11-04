def multiplier(n):
    def inner(val):
        return val*n
    return inner

doubler=multiplier(2)
tripler=multiplier(3)

print(doubler(100))
print(tripler(100))


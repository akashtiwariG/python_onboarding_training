import sys
list_comp=[n**2 for n in range(100_00)]
print(type(list_comp))

gen_exp=(n**2 for n in range(100_00))
print(type(gen_exp))

print(sys.getsizeof(list_comp))
print(sys.getsizeof(gen_exp))

print(sum(gen_exp))
print(sum(gen_exp))

print(sum(n**2 for n in range(1000)))
print(max(len(w) for w in ["car","bicyce","van"]))
print(any(n>100 for n in [5,50,500]))
print(all(n>0 for n in [5,50,500]))
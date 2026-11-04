import copy


original=[1,2,3,4,5]
alias=original
alias.append(6)
print(original)
print(original is alias)
print()

copy_of_original=original.copy()
copy_of_original.append(9)
print(original)
print(copy_of_original)
print(original is copy_of_original)
print()

copy_of_original_2 = original[:]
copy_of_original_2.append(10)
print(original)
print(copy_of_original_2)

copy_of_original_3 = list(original)
copy_of_original_3.append(10)
print(original)
print(copy_of_original_3)

nested=[[1,2],[3,4]]

print(nested)
print(id(nested))

shallow_copy=nested.copy()
print(id(shallow_copy))

deep_copy=copy.deepcopy(nested)
print(id(deep_copy))
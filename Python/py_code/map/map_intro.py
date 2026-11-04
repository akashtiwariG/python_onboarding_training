nums=[1,2,3,4,5]

mapped=map(lambda x:x*x,nums)

generated=(x*x for x in nums)

print(next(mapped))
print(next(generated))

list_of_maps=list(mapped)
print(list_of_maps)

list_of_generated=list(generated)
print(list_of_generated)

lst=[x*x for x in nums]
print(lst)
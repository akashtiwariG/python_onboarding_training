from functools import reduce

nums=[1,2,3,4,5]

sum_reduce_obj=reduce(lambda a,b:a+b,nums)
print(sum_reduce_obj)
print(type(sum_reduce_obj))

print(reduce(lambda a,b:a if a>b else b,nums))

print(reduce(lambda a,b:a+b,nums,100))

print(sum(nums),max(nums))
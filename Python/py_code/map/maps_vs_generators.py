nums=[1,2,3,4,5]
mapped_str=map(str,nums)
generated_str=(str(num) for num in nums)

print(list(mapped_str))
print(list(generated_str))

even_squares=(x*x for x in nums if x%2 == 0)
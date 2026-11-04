nums=[1,2,3,4]
print(sum(nums))


def total_sum(*numbers):
    """Function to calculate the sum of any number of arguments"""
    print(type(numbers))
    return sum(numbers)

def total_sum2(num,*numbers):
    """Function to calculate the sum of any number of arguments"""
    print(type(numbers))
    return sum(numbers)

sum1=total_sum(5,4,15,6,7,4,5)
print(sum1)
sum2=total_sum2(12,3,4,5,6)
print(sum2)
print("START")
nums=[2,43,54,65,90]

def safe_lookup(data,index):
    try:
        return data[index]
    except(KeyError,IndexError,TypeError) as e:
        print(type(e))
        return e
print(safe_lookup(nums,9))
print(safe_lookup({"a":"apple","b":"ball"},"c"))
print(safe_lookup(None,"a"))
print("END")

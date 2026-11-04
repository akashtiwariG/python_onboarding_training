customer={"name":"rahul"}
customer["name"]="John"
customer["age"]=30

print(customer)
customer.update({"country":"USA","age":30,"balance":1000})
print(customer)

balance = customer.pop("balance")
print(balance)
print(customer)
print(customer.pop("balance","key not found"))
print(customer)
print(customer.popitem())
print(customer)
customer.setdefault("name","Jane Smith")
print(customer)

data={"a":1}

if "b" in data:
    print(data["b"])
else:
    print("key not present")

try:
    value=data["b"]
except KeyError as e:
    print("key not present")

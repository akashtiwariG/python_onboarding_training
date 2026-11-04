products=[
    {"name":"Ford Town Car","price":121.64,"line":"Vintage Cars"},
    {"name":"Alpha Romeo","price":92.03,"line":"Vintage Cars"},
    {"name":"Harley","price":95.70,"line":"Motorcycles"}
]
sorted_products=sorted(products,key=lambda p:p["price"],reverse=True)
print(sorted_products)

sorted_products_2factor=sorted(products,key=lambda p:(p["line"],-p["price"]))
print(sorted_products_2factor)
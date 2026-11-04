
def order(product,quantity=2,price=0.5):
    total=quantity*price
    print(f"order:{product} , Quantity:{quantity}, price:{price}")

order("Apple",5,0.8)
order("Banana",10)
order("Cherry")
order(quantity=3,product="Date",price=1.2)
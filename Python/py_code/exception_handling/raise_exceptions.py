def apply_discount(price,pct):
    if not isinstance(price,(int,float)):
        raise TypeError("price must be numeric")
    if price < 0:
        raise ValueError("price cannot be negative")
    if not 0 <= pct <= 100:
        raise ValueError(f"pct must be within 0 to 100 got {pct}")
    return price*(1-pct/100)


for args in [(1000,50),(1000,150),(-5,10),("x",10)]:
    try:
        apply_discount(args[0],args[1])
    except (ValueError,TypeError) as e:
        print(f"{args} -> {type(e).__name__}:{e}")
    
print("END")
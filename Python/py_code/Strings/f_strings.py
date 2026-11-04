name,qty,price = "Ford Town Car", 5551 , 121.647

print(f"{name}:{qty} units at ${price} each")
print(f"{name}:{qty} units at ${price:.1f} each")
print(f"{name}:{qty} units at ${price:.2f} each")
print(f"{name}:{qty} units at ${price:.3f} each")

print(f"Total cost: ${qty*price}")
print(f"Total cost: ${qty*price:.2f}")
print(f"Total cost: ${qty*price:,.2f}")

print(f"{name:<20}|{qty:>10}|")
print(f"{price:>10.2f}")

print(f"{0.4567:.2%}")
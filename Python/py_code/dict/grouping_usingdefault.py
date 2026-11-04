from collections import defaultdict
products=[
    {"name":"a","line":"ddc","price":10},
    {"name":"b","line":"ddc","price":20},
    {"name":"c","line":"ddc","price":30},
    {"name":"d","line":"efg","price":40}
]

grouped=defaultdict(list)

for product in products:
    grouped[product["line"]].append(product["name"])

print(grouped)

for line,names in grouped.items():
    print(line,len(names))
    for n in names:
        print("    -",n)

totals=defaultdict(float)
counts=defaultdict(int)

for p in products:
    totals[p["line"]] += p["price"]
    counts[p["line"]] += 1

print(totals)
print(counts)

print()
for line in totals:
    print(f"{totals[line]:.3f},{totals[line]/counts[line]:0.2f}")
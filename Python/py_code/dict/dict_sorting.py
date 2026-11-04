scores={"Aditi":88,"Rahul":76,"Aditya":88,"Arpit":76}
print(sorted(scores))

print(max(scores,key=scores.get))
print(min(scores,key=scores.get))

print(sum(scores.values()),round(sum(scores.values())/len(scores),1))

print({v:k for k,v in scores.items() })


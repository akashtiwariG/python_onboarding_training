import os

with open("order_details.csv") as fi:
    print(fi.read())

with open("order_details.csv") as fi:
    print(fi.read())

with open("order_details.csv") as fi:
    print(fi.readline())
    print(fi.readine())

with open("order_details.csv") as f:
    while(True):
        line = f.readline()

        if not line:
            break
            print(line.strip())

with open("order_details.csv") as fi:
    for line in f :
        print(line.strip())

with open("order_details.csv") as fi:
    lines=f.readlines()
    print(type(lines))
    print(lines)
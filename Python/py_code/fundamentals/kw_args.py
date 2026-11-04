def describe(**details):
    print(type(details))

    for k,v in details.items():
        print(f"{k}:{v}")

    return None

describe(name="Suman",age=30,citizen_ship="IND")
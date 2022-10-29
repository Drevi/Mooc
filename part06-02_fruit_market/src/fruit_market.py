# write your solution here


def read_fruits():
    fruits = {}
    with open("fruits.csv") as csv:
        for line in csv:
            line = line.replace("\n", "")
            parts = line.split(";")            
            fruits[parts[0]] = float(parts[1])
    return fruits
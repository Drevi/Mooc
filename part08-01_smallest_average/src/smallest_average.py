# Write your solution here



def smallest_average(person1: dict, person2: dict, person3: dict):
    avg1 = (person1["result1"] + person1["result2"] + person1["result3"]) / 3
    avg2 = (person2["result1"] + person2["result2"] + person2["result3"]) / 3
    avg3 = (person3["result1"] + person3["result2"] + person3["result3"]) / 3
    if avg1 < avg2 and avg1 < avg3:
        return person1
    elif avg2 < avg3 and avg2 < avg1:
        return person2
    else: 
        return person3
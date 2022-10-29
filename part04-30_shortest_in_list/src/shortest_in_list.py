# Write your solution here

def shortest(my_list):
    shortest = my_list[0]
    for word in my_list:
        if len(word) < len(shortest):
            shortest = word
    return shortest

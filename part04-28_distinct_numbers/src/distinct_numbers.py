# Write your solution here

def distinct_numbers(my_list):
    new = []
    for i in my_list:
        if i not in new:
            new.append(i)
    return sorted(new)

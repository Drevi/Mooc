# Write your solution here

def formatted(my_list):
    new = []
    for item in my_list:
        new.append(f"{item:.2f}")
    return new
# Write your solution here

def even_numbers(my_list):
    even_list = []
    for i in my_list:
        if i % 2 == 0:
            even_list.append(i)
    return even_list

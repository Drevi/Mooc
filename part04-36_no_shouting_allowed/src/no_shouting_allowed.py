# Write your solution here

def no_shouting(my_list):
    new_list = []
    for word in my_list:
        if not word.isupper():
            new_list.append(word)
    return new_list

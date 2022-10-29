# Write your solution here

def length_of_longest(my_list):
    longest = 0
    for word in my_list:
        if len(word) > longest:
            longest = len(word)
    return (longest)
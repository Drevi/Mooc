# Write your solution here

def all_the_longest(my_list):
    longest = 0
    new = []
    
    for word in my_list:
        if len(word) > longest:
            longest = len(word)
    for word in my_list:
        if len(word) >= longest:
            new.append(word)
        
    return (new)
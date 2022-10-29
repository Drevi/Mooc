# Write your solution here

def most_common_character(my_string):
    most_common = my_string[0]

    for character in my_string:
        if character != " " and my_string.count(character) > my_string.count(most_common):            
            most_common = character
    
    return most_common
            

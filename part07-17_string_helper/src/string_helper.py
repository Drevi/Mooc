# Write your solution here
import string

def change_case(orig_string: str):
    new_string =""
    for char in orig_string:
        if char in string.ascii_letters:    
            if char.islower():
                new_string += char.upper()
            elif char.isupper():
                new_string += char.lower()
        else:
            new_string += char
    
    return new_string


def split_in_half(orig_string: str):
    div = len(orig_string) // 2
    return (orig_string[0:div], orig_string[div:])


def remove_special_characters(orig_string: str):
    new_string =""
    for char in orig_string:
        if char not in string.ascii_letters and char not in string.digits and char != " ":               
            continue
        new_string += char

    return new_string

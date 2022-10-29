# Write your solution here

def no_vowels(my_string):
    vowels = "aeiou"
    new_string = my_string

    for vowel in vowels:
        new_string = new_string.replace(vowel, "")
    return new_string


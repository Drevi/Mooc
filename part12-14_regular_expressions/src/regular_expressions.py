# Write your solution here
import re

def is_dotw(my_string: str):
    dotw = "Mon|Tue|Wed|Thu|Fri|Sat|Sun"
    if re.search(dotw, my_string):
        return True
    return False

def all_vowels(my_string: str):
    test = re.findall("a|e|i|o|u", my_string)
    return len(test) == len(my_string)


def time_of_day(my_string: str):
    totd = "^([02][03]+(:[05][09]+)+)$"
    if re.search(totd, my_string):
        return True
    return False
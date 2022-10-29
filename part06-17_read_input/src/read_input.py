# Write your solution here

from ast import Try


def read_input(ask, low, high):
    while True:
        try:
            in_num = int(input(ask))
            if in_num >= low and in_num <= high:
                return in_num 
        except ValueError:
            pass   
        print(f"You must type in an integer between {low} and {high}")    
# Write your solution here

from random import sample

def lottery_numbers(amount: int, lower: int, upper: int):    
    return sorted(sample(list(range(lower, upper)), amount))
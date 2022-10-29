# Write your solution here

from fractions import Fraction

def fractionate(amount: int):
    list_fractions = []
    for i in range(amount):
        list_fractions.append(Fraction(1,amount))
    return list_fractions
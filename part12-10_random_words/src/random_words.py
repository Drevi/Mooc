# Write your solution here:
from random import choice
 
def word_generator(letters: str, length: int, amount:int):
    return ("".join([choice(letters ) for i in range(length)]) for j in range(amount))
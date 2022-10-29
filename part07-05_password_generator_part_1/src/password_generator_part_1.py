# Write your solution here

from string import ascii_lowercase
from random import randint

def generate_password(lenght: int):
    password = ""
    for i in range(lenght):
        password += ascii_lowercase[randint(0,25)]
    return password
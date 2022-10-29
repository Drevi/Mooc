# Write your solution here

import string
import random

def generate_strong_password(lenght: int, numbers: bool, specials: bool):
    chars = string.ascii_lowercase
    password = random.choice(chars)
    if numbers:
        password += random.choice(string.digits)
        chars += string.digits
    if specials:
        password += random.choice("!?=+-()#")
        chars += "!?=+-()#"
    for i in range(len(password), lenght):
        password += random.choice(chars)

    return password

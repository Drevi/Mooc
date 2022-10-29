# Write your solution here

from copy import copy


def prime_numbers():
    number = 2

    while True:
        orig_number = number
        for i in range(2, number):
            if number % i == 0:
                number += 1
                break
        if orig_number == number:
            yield number
            number += 1

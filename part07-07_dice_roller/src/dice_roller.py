# Write your solution here

from random import choice

def roll(die: str):
    dies = {"A": [3, 3, 3, 3, 3, 6], "B": [2, 2, 2, 5, 5, 5], "C": [1, 4, 4, 4, 4, 4]}
    return choice(dies[die])


def play(die1: str, die2: str, times: int):
    dies = {"A": [3, 3, 3, 3, 3, 6], "B": [2, 2, 2, 5, 5, 5], "C": [1, 4, 4, 4, 4, 4]}
    results = {"die1": 0, "die2": 0, "tie": 0}

    for i in range(times):
        die1_roll = choice(dies[die1])
        die2_roll = choice(dies[die2])
        if die1_roll > die2_roll:
            results["die1"] += 1
        elif die1_roll < die2_roll:
            results["die2"] += 1
        else:
            results["tie"] += 1

    return (results["die1"], results["die2"], results["tie"])
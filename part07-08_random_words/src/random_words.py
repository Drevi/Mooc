# Write your solution here

from random import shuffle

def words(n: int, beginning: str):
    possible_words = []
    with open("words.txt", "r") as file:
        for word in file:
            if word.startswith(beginning):
                possible_words.append(word)
    if n > len(possible_words):            
        raise ValueError
    shuffle(possible_words)
    return possible_words[0:n]

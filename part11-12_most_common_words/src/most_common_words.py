# WRITE YOUR SOLUTION HERE:
import string

def most_common_words(filename: str, lower_limit: int):
    words = []
    with open(filename, 'r') as file:        
        for line in file:
            words.extend([word.strip(".,\n") for word in line.split(" ")])
    
    return {word: words.count(word) for word in words if words.count(word) >= lower_limit}



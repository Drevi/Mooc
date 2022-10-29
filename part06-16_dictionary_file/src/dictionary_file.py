# Write your solution here

dictionary = "dictionary.txt"

def add_word(dict: str):
    finish = input("The word in Finnish: ")
    english = input("The word in English: ")
    with open(dict, "a") as file:
        file.write(f"{finish};{english}\n")
    print("Dictionary entry added")


def read_dictionary(dict: str):
    word_list = []
    with open(dict, "r") as file:
        for line in file:
            word_list.append(line.strip().split(";"))
    return word_list          
               

def seach_word(dict: str, word: str):
    word_list = read_dictionary(dict)
    for word_pair in word_list:
        if word in word_pair[0] or word in word_pair[1]:
            print(f"{word_pair[0]} - {word_pair[1]}")    


while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    in_function = input("Function: ")
    if in_function == "3":
        break
    if in_function == "1":
        add_word(dictionary)    
    elif in_function == "2":
        word = input("Search term: ")
        seach_word(dictionary, word)

print("Bye!")
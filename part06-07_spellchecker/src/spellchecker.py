# write your solution here

dictionary = []

with open("wordlist.txt") as file:
    for line in file:
        dictionary.append(line.strip())

text = input("Write text: ")
checked_text =""

for word in text.split(" "):
    if word.lower() in dictionary:
        checked_text += word + " "
    else:
        checked_text += "*"+word+"* "





print(checked_text)
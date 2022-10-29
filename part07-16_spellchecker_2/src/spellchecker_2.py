# Write your solution here
from difflib import get_close_matches

text = input("write text: ")
wordlist = []
corrected_text = ""
suggestions = {}

with open("wordlist.txt", "r") as f:
    for line in f:
        wordlist.append(line.strip())

for word in text.split(" "):
    if word.lower() not in wordlist:
        corrected_text += "*"+word+"* "
        suggestions[word] = get_close_matches(word, wordlist)
    else:
        corrected_text += word+" "    

print(corrected_text)
print("suggestions:")
for miss_word, suggestion in suggestions.items():
     print(f"{miss_word}: {', '.join(suggestion)} ")
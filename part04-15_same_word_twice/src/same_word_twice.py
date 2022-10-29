# Write your solution here
words = []
while True:
    word = input("Word: ")    
    if word in words:
        break
    words.append(word)    
print(f"You typed in {len(words)} different words")


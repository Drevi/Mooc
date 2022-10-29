# Write your solution here

def first_word(sentence):
    space = sentence.find(" ")
    return sentence[0:space]

def second_word(sentence):
    start = sentence.find(" ") + 1
    end = start
    while end < len(sentence):        
        if sentence[end] == " ":
            return sentence[start:end]
        end +=1    
    return sentence[start:end]


def last_word(sentence):
    end = len(sentence)
    start = end - 1
    while start > 0:        
        if sentence[start] == " ":
            return sentence[start+1:]
        start -= 1
    return sentence[start+1:]








# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))
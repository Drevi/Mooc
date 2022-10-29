# Write your solution here

def find_words(search_term: str):
    words = []
    with open("words.txt", "r") as file:
        for line in file:
            words.append(line.strip())
    results =[]

    if search_term[0] == "*":        
        for word in words:
            if word.endswith(search_term.replace("*", "")):
                results.append(word)

    elif search_term[-1] == "*":        
        for word in words:
            if word.startswith(search_term.replace("*", "")):
                results.append(word) 

    elif "." in search_term:
        for word in words:            
            if len(word) != len(search_term):
                continue
            same = True
            for i in range(0,len(word)):
                if search_term[i] == ".":
                    continue
                if search_term[i] != word[i]:
                    same = False                         
            if same:
                results.append(word)
    
    else:
        for word in words:
            if search_term == word:
                results.append(word)

    
    return results    

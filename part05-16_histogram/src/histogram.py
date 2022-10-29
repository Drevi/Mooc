# Write your solution here

def histogram(string):
    hstgrm = {}

    for char in string:
        if char not in hstgrm:
            hstgrm[char] = 0
        
        hstgrm[char] += 1
    for key, value in hstgrm.items():
        print(key, value*"*")


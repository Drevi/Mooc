# Write your solution here

def factorials(n: int):
    fact = {}
    for i in range(1, n + 1):
        fact[i] = 1
        for b in range(1, i + 1):
            fact[i] *= b         
    return fact
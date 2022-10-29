# Write your solution here

def list_sum(list_a, list_b):
    sum = []
    for i in range(len(list_a)):
        sum.append(list_a[i]+list_b[i])        
    return sum


if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) 
# write your solution here

def largest():
    largest = 0
    with open("numbers.txt") as file:
        for line in file:
            if int(line) > largest:
                largest = int(line)
    return largest
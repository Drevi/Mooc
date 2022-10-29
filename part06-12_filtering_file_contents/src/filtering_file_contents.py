# Write your solution here

def filter_solutions():
    correct = []
    incorrect = []
    with open("solutions.csv", "r") as file:
        for line in file:
            parts = line.split(";")
            if eval(parts[1]) == int(parts[2]):
                correct.append(parts)
            else:
                incorrect.append(parts)
    
    with open("correct.csv", "w") as file:
        for solution in correct:
            file.write(f"{solution[0]};{solution[1]};{solution[2]}")

    with open("incorrect.csv", "w") as file:
        for solution in incorrect:
            file.write(f"{solution[0]};{solution[1]};{solution[2]}")



# def main():
#     filter_solutions()

# main()            
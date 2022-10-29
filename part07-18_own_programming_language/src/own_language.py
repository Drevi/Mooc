# Write your solution here

def operators(a, operator, b):
    if operator == "==":
        return a == b
    if operator == "!=":
        return a != b
    if operator == "<":
        return a < b    
    if operator == "<=":
        return a <= b
    if operator == ">":
        return a > b 
    if operator == ">=":
        return a >= b

def data(x, variables):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if x in characters:
        return variables[characters.index(x)]
    else:
        return int(x)

def run(program: list):
    variables = [0]*26
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
               
    result = []
    step = 0
    while step < len(program):
        instructions = program[step].split(" ")

        if instructions[0] == "IF":            
            if operators(data(instructions[1],variables),instructions[2],data(instructions[3],variables)):
                del instructions[:4]
            else:
                step += 1
                continue           

        if instructions[0] == "MOV":
            variables[characters.index(instructions[1])] = data(instructions[2], variables)

        elif instructions[0] == "PRINT":
            result.append(data(instructions[1], variables))

        elif instructions[0] == "ADD": 
            variables[characters.index(instructions[1])] += data(instructions[2], variables)

        elif instructions[0] == "SUB": 
            variables[characters.index(instructions[1])] -= data(instructions[2], variables)    

        elif instructions[0] == "MUL": 
            variables[characters.index(instructions[1])] *= data(instructions[2], variables)

        elif instructions[0] == "JUMP":
            step = program.index(instructions[1]+":") 

        elif instructions[0] == "END":
            break        
        
        step += 1

    return result

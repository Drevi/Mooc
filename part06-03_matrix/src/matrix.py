# write your solution here

def file_to_list(filename):
    matrix = []
    with open(filename, "r") as f:
       for line in f:            
            list_str = line.split(",")
            list_int = []
            for number in list_str:                
                list_int.append(int(number))
            matrix.append(list_int)
    return matrix

def matrix_sum():
    total = 0
    matrix = file_to_list("matrix.txt")
    for row in matrix:
        total += sum(row)
    return total


def matrix_max():
    max = 0
    matrix = file_to_list("matrix.txt")
    for row in matrix:
        for number in row:
            if number > max:
                max = number        
    return max

def row_sums():
    total = []
    matrix = file_to_list("matrix.txt")
    for row in matrix:
        total.append(sum(row))
    return total







# def main():
#     print(matrix_sum())


# main()
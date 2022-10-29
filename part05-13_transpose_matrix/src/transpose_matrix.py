# Write your solution here

def transpose(matrix: list):
    copy_matrix = [row[:] for row in matrix]

    for x in range(len(copy_matrix)):
        for y in range(len(copy_matrix)):
            matrix[x][y] = copy_matrix[y][x]


# Write your solution here

def row_correct(sudoku: list, row_no: int):

    for i in range(1, 10):
        count = 0
        for column in sudoku[row_no]:
            if column == i:
                count += 1
            if count > 1:
                return False
    return True




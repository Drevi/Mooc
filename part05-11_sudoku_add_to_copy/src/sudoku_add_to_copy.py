# Write your solution here

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    copy_sudoku = [row[:] for row in sudoku]
    copy_sudoku[row_no][column_no] = number
    return copy_sudoku
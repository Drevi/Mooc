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

def column_correct(sudoku: list, column_no: int):
    
    for i in range(1, 10) : 
        count = 0
        for row in range(0, 9):             
            if sudoku[row][column_no] == i:
                count += 1
            if count > 1:
                return False
                
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):

    for i in range(1, 10):
        count = 0
        for row in range(row_no, row_no + 3):
            for col in range(column_no, column_no + 3):
                if sudoku[row][col] == i:
                    count += 1
            if count > 1:
                return False
    return True

def sudoku_grid_correct(sudoku: list):

    for i in range(0,9):
        if not row_correct(sudoku, i):
            return False
        if not column_correct(sudoku, i):
            return False

        for row in range(0,7,3):
            for col in range(0,7,3):
                if not block_correct(sudoku, row, col):
                    return False

    return True

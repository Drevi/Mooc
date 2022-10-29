# Write your solution here

def print_sudoku(sudoku: list):
    print_list = sudoku[:]
    for row in range(0,9):
        for col in range(0,9):            
            if print_list[row][col] == 0:
                print_list[row][col] = "_"
            print(f"{print_list[row][col]} ", end = "")  
            if col == 2 or col == 5:
                print(" ", end = "")
        print()
        if row == 2 or row == 5:
            print()


def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number












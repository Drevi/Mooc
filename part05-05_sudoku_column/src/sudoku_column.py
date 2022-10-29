# Write your solution here

def column_correct(sudoku: list, column_no: int):
    
    for i in range(1, 10) : 
        count = 0
        for row in range(0, 9):             
            if sudoku[row][column_no] == i:
                count += 1
            if count > 1:
                return False
                
    return True




















if __name__ == "__main__":

    sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]]

    print(column_correct(sudoku, 0))
    print(column_correct(sudoku, 1))
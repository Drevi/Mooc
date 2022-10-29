# Write your solution here

def  count_matching_elements(my_matrix: list, element: int):
    matching = 0
    for row in my_matrix:
        for col in row:
            if col == element:
                matching += 1
    return matching

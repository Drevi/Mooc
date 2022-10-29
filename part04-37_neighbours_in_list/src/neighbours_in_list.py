# Write your solution here

def longest_series_of_neighbours(my_list):
    long = 0
    longest = 0

    for i in range(1,len(my_list),1):        
        if my_list[i] == my_list[i-1] -1 or my_list[i] == my_list[i-1] +1:
            if long == 0:
                long +=2
            else:
                long +=1
        else:
            if long >= longest:
                longest = long
                long = 0
    if long >= longest:
                longest = long
    return longest

if __name__ == "__main__":
    print(longest_series_of_neighbours([1, 3, 5, 7, 10, 11, 14, 15, 19, 20, 21, 22, 23, 24, 25]))
    #                                  [0, 1, 2, 3, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15]
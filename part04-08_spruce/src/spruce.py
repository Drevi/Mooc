# Write your solution here
# You can test your function by calling it within the following block

def blanks_stars(blanks, stars):
    print(" "*blanks, end="")
    print("*"*stars, end="")    
    print()


def spruce(height):
    print("a spruce!")
    a = 1
    b = height - 1
    c = 1
    while a <= height:
        blanks_stars(b, c)
        b -= 1
        a += 1
        c += 2
    blanks_stars(height-1, 1)





if __name__ == "__main__":
    spruce(5)

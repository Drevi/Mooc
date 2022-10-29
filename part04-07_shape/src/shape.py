# Copy here code of line function from previous exercise and use it in your solution
# You can test your function by calling it within the following block
def line(length, text):
    if text == "":
        print("*"*length)
    else:
        print(text[0]*length)

def triangle(size, filler):
    i = 1
    while i <= size:
        line(i, filler)
        i += 1

def rectangle(height, width, filler):
    i = 1
    while i <= height:
        line(width, filler)
        i += 1





def shape(size, filler, height, filler2):
    triangle(size, filler)
    rectangle(height, size, filler2)







if __name__ == "__main__":
    shape(5, "x", 5, "o")
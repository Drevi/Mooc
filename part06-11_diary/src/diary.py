# Write your solution here

def read_diary(diary):
    print("Entries:")
    with open(diary, "r") as file:
        for line in file:
            print(line)


def write_diary(diary, text):
    with open(diary, "a") as file:
        file.write(text + '\n')
        print("Diary saved")

while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    choice = input("Function: ")
    if choice == "0":
        break
    elif choice == "1":
        write_diary("diary.txt", input("Diary entry: "))
        
    elif choice == "2":        
        read_diary("diary.txt")    

print("Bye now!")
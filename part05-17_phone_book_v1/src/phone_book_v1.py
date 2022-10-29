# Write your solution here

phonebook = {}

while True:    
    inpt = input("command (1 search, 2 add, 3 quit): ")
    if inpt == "3":
        break

    if inpt == "2":
        name = input("name: ")
        phone = input("phone: ")        
        phonebook[name] = phone
        print("ok!")
    
    if inpt == "1":
        name = input("name: ")
        if name not in phonebook:
            print("no number")
        else:
            print(phonebook[name])
    
    


print("quitting...")
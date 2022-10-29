# Write your solution here

phonebook = {}

while True:    
    inpt = input("command (1 search, 2 add, 3 quit): ")
    if inpt == "3":
        break

    if inpt == "2":
        name = input("name: ")
        phone = input("phone: ")        
        if name not in phonebook:
            phonebook[name] = []        
        phonebook[name].append(phone)    
        print("ok!")
    
    if inpt == "1":
        name = input("name: ")
        if name not in phonebook:
            print("no number")
        else:
            for phone in phonebook[name]:
                print(phone)

print("quitting...")
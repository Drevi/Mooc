# Write your solution here

lista = []

while True:
    print(f"The list is now {lista}")
    action = input("a(d)d, (r)emove or e(x)it: ")    
    if action == "x":
        break    
    if action == "d":        
        if len(lista)   != 0:
            lista.append(1+len(lista))
        else:
            lista.append(1)
    if action == "r":
        lista.pop(len(lista)-1)

print("Bye!")

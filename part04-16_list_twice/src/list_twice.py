# Write your solution here

lista = []
while True:
    item = int(input("New item: "))
    if item == 0:
        break
    lista.append(item)    
    print("The list now:", lista)
    print("The list in order:", sorted(lista))
print("Bye!")    
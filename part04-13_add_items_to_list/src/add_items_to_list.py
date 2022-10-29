# Write your solution here

times = int(input("How many items:"))
list = []
i = 1
while i <= times:
    list.append(int(input(f"Item {i}: ")))
    i += 1
print(list)
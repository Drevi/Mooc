# Write your solution here


name = input("Whom shoul I sign this to: ")

with open(input("Where shall I save it: "), "w") as file:
    file.write(f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")
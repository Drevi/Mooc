# WRITE YOUR SOLUTION HERE:
class Employee:
    def __init__(self, name: str):
        self.name = name
        self.subordinates = []

    def add_subordinate(self, employee: 'Employee'):
        self.subordinates.append(employee)


def count_subordinates(employee: Employee):
    subordinates = len(employee.subordinates)
    
    if len(employee.subordinates) > 0:
        for employee in employee.subordinates:
            subordinates += count_subordinates(employee)
    
    return subordinates
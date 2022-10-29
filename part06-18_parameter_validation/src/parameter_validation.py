# Write your solution here

def new_person(name: str, age: int):
    if len(name) > 40 or len(name.split(" ")) < 2 or len(name) == 0:
        raise ValueError("Name must be at least 2 words and less than 40 characters")
    if age < 0 or age > 150:
        raise ValueError("Age must be between 0 and 150")
    return (name, age)
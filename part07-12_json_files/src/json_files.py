# Write your solution here
import json


def print_persons(filename: str):
    with open(filename, 'r') as file:
        data = file.read()
    people = json.loads(data)

    for person in people:            
        text = f'{person["name"]} {person["age"]} years ('
        text += ', '.join(person['hobbies']) + ")"
        print(text)



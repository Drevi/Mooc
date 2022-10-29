# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height
        

    def __str__(self):
        return self.name


class Room:
    def __init__(self):
        self.persons = []

    def is_empty(self):
        return len(self.persons) == 0
    
    def add(self, person: "Person"):
        self.persons.append(person)
    
    def print_contents(self):
        if not self.is_empty():
            combined_height = 0
            for person in self.persons:
                combined_height += person.height

            print(f"There are {len(self.persons)} persons in the room, and their combined height is {combined_height} cm")
            for person in self.persons:
                print(f"{person.name} ({person.height} cm)")
        
    def shortest(self):
        shortest = None
        shortest_height = 500
        for person in self.persons:
            if person.height < shortest_height:
                shortest_height = person.height
                shortest = person
        return shortest

    def remove_shortest(self):
        if not self.is_empty():
            shortest = self.shortest()
            self.persons.remove(shortest)
            return shortest



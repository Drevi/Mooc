# Write your solution here:

class Pet:
    def __init__(self, name: str, species: str, year_of_birth: int):
        self.species = species
        self.year_of_birth = year_of_birth
        self.name = name


def new_pet(name: str, species: str, year_of_birth: int):
    new_pet = Pet(name, species, year_of_birth)

    return new_pet
    

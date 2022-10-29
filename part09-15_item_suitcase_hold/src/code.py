# Write your solution here:

class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight    
    
    def name(self):
        return self.__name    
    
    def weight(self):
        return self.__weight
    
    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"


class Suitcase:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__stored_items = []        

    def add_item(self, item: Item):
        if self.weight() + item.weight() <= self.__max_weight:            
            self.__stored_items.append(item)
    
    def __str__(self) -> str:
        if len(self.__stored_items) == 1:
            return f"{len(self.__stored_items)} item ({self.weight()} kg)"
        else:
            return f"{len(self.__stored_items)} items ({self.weight()} kg)"

    def print_items(self):
        for item in self.__stored_items:
            print(item)

    def weight(self):
        weight = 0
        for item in self.__stored_items:
            weight += item.weight()
        return weight

    
    def heaviest_item(self):
        heaviest_item = None
        heaviest_weight = 0

        for item in self.__stored_items:
            if item.weight() > heaviest_weight:
                heaviest_weight = item.weight()
                heaviest_item = item
        return heaviest_item

    
class CargoHold:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__stored_suitcases = []        

    def add_suitcase(self, suitcase: Suitcase):
        if self.weight() + suitcase.weight() <= self.__max_weight:            
            self.__stored_suitcases.append(suitcase)   

    def weight(self):
        weight = 0
        for suitcase in self.__stored_suitcases:
            weight += suitcase.weight()
        return weight

    def __str__(self) -> str:
        if len(self.__stored_suitcases) == 1:
            return f"{len(self.__stored_suitcases)} suitcase, space for {self.__max_weight - self.weight()} kg"
        else:
            return f"{len(self.__stored_suitcases)} suitcases, space for {self.__max_weight - self.weight()} kg"

    def print_items(self):
        for suitcase in self.__stored_suitcases:
            suitcase.print_items()

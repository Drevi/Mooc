# WRITE YOUR SOLUTION HERE:

class Car:
    def __init__(self):
        self.__petrol = 0
        self.__odometer = 0

    def fill_up(self):
        self.__petrol = 60
    
    def drive(self, km: int):
        max_distance = min(self.__petrol, km)
        self.__petrol -= max_distance
        self.__odometer += max_distance
    
    def __str__(self) -> str:
        return f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__petrol} litres"

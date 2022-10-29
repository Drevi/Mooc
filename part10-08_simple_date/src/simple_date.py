# WRITE YOUR SOLUTION HERE:

class SimpleDate:
    def __init__(self, day:int, month:int, year:int):
        self.year = year
        self.month = month
        self.day = day
    
    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"

    def _to_days(self):
        return self.year * 360 + self.month * 30 + self.day
    
    def _to_date(self, days: int):
        months = days // 30
        years = months // 12
        days -= months * 30
        months -= years * 12
        return SimpleDate(days, months, years)    

    def __gt__(self, other: "SimpleDate"):
        return self._to_days() > other._to_days()

    def __lt__(self, other: "SimpleDate"):
        return self._to_days() < other._to_days()

    def __eq__(self, other: "SimpleDate"):
        return self._to_days() == other._to_days()

    def __ne__(self, other: "SimpleDate"):
        return self._to_days() != other._to_days()
        
    def __add__(self, days: int):
        return self._to_date(self._to_days() + days)

    def __sub__(self, other: "SimpleDate"):           
        return abs(self._to_days() - other._to_days())



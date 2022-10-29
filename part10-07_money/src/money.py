# TEE RATKAISUSI TÄHÄN:
class Money:
    
    def __init__(self, euros: int, cents: int):
        self._euros = euros
        self._cents = cents
    
    def _value(self):
        return self._euros + self._cents / 100

    def __str__(self):
        return f"{self._value():.2f} eur"

    def __eq__(self, another):
        return self._value() == another._value()
    
    def __lt__(self, another):
        return self._value() < another._value()

    def __gt__(self, another):
        return self._value() > another._value()

    def __ne__(self, another):
        return self._value() != another._value()

    def __sub__(self, another):
        import math
        result = self._value() - another._value()
        if result >= 0:
            euros = math.floor(result)
            cents = round((result - euros)*100)
            new_money = Money(euros, cents)
            return new_money
        else:
            raise ValueError("a negative result is not allowed")

    def __add__(self, another):
        import math
        result = self._value() + another._value()        
        euros = math.floor(result)
        cents = round((result - euros)*100)
        new_money = Money(euros, cents)
        return new_money
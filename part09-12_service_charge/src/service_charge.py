# WRITE YOUR SOLUTION HERE:

class BankAccount:
    def __init__(self, owner: str, account: str, balance: float):
        self.__owner = owner
        self.__account = account
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance
        
    def deposit(self, amount: float):
        self.__balance += amount
        self.__service_charge()

    def withdraw(self, amount: float):
        self.__balance -= amount
        self.__service_charge()

    def __service_charge(self):
        self.__balance *= 0.99




from abc import ABC, abstractmethod

from project.validation.validation import Validation


class Meal(ABC):

    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validation.valid_not_empty_string(value,"Name cannot be an empty string!")
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        Validation.valid_price(value, "Invalid price!")
        self.__price = value

    @abstractmethod
    def details(self):
        pass

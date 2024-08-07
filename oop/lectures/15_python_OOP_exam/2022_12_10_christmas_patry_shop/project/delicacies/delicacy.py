from project.valaidation.validation import Validation
from abc import ABC, abstractmethod


class Delicacy(ABC):
    def __init__(self, name: str, portion: int, price: float):
        self.name = name
        self.portion = float(portion)  # represents the portion of a delicacy in grams.
        self.price = float(price)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validation.valid_white_space_empty_string(value, "Name cannot be null or whitespace!")
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        Validation.valid_price(value, "Price cannot be less or equal to zero!")
        self.__price = value

    @abstractmethod
    def details(self):
        pass

from abc import ABC, abstractmethod
from project.validators import *


class Drink(ABC):
    @abstractmethod
    def __init__(self, name: str, portion: float, price: float, brand: str):
        self.name = name
        self.portion = portion
        self.price = price
        self.brand = brand

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        validate_non_empty_string(value, "Name cannot be empty string or white space!")
        self.__name = value

    @property
    def portion(self):
        return self.__portion

    @portion.setter
    def portion(self, value):
        validation_positive_value(value, "Portion cannot be less than or equal to zero!")
        self.__portion = value

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        validate_non_empty_string(value, "Brand cannot be empty string or white space!")
        self.__brand = value

    def __repr__(self):
        return f" - {self.name} {self.brand} - {(self.portion):.2f}ml - {(self.price):.2f}lv"


# try:
#     boza = Drink("Kotancho", 250.58, 2.50, "Extra")
#     print(repr(boza))
# except ValueError as e:
#     print(e)

# # result
# - Kotancho Extra - 250.58ml - 2.50lv

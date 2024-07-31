from abc import ABC, abstractmethod
from project.Validators.validators import Validation


class BakedFood(ABC):
    @abstractmethod
    def __init__(self, name: str, portion: float, price: float):
        self.name = name  # Set the name using the setter method
        self.portion = portion
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validation.validate_non_empty_string(value, "Name cannot be empty string or white space!")
        self.__name = value

    @property
    def portion(self):
        return self.__portion

    @portion.setter
    def portion(self, value):
        self.__portion = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        Validation.validation_positive_value(value, "Price cannot be less than or equal to zero!")
        self.__price = value

    def __repr__(self):
        return f" - {self.name}: {self.portion:.2f}g - {self.price:.2f}lv"


# try:
#     food = BakedFood(name="Topal Leb", portion=200, price=1)
#     print(repr(food))
# except ValueError as e:
#     print(e)
#
# # result:
# # - Topal Leb: 200.00g - 1.00lv

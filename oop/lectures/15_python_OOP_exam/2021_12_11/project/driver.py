from typing import List

from project.car.car import Car
from project.validation.validation import Validation


class Driver:

    def __init__(self, name: str):
        self.name = name
        self.car = None         # One driver drives ONLY one car.
        self.number_of_wins = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validation.valid_driver_name(value, "Name should contain at least one character!")
        self.__name = value

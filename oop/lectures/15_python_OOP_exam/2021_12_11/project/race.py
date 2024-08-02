from typing import List

from project.driver import Driver
from project.validation.validation import Validation


class Race:

    def __init__(self, name:str):
        self.name = name
        self.drivers: List[Driver] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validation.valid_driver_name(value, "Name cannot be an empty string!")
        self.__name = value



from abc import ABC, abstractmethod
from project.validation.validation import Validation
class Horse(ABC):

    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken = False       # one horse can have only one rider

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validation.valid_horse_name(value, f"Horse name {value} is less than 4 symbols!")
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        Validation.valid_horse_speed(value, self.MAX_SPEED, "Horse speed is too high!")
        self.__speed = value

    @abstractmethod
    def train(self):
        pass
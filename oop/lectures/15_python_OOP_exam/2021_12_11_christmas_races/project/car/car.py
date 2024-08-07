from abc import ABC, abstractmethod
from project.validation.validation import Validation

class Car(ABC):
    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False  # One car can be driven by ONLY one driver.

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        Validation.valid_model(value, f"Model {value} is less than 4 symbols!")
        self.__model = value

    @abstractmethod
    def min_speed_limit(self):
        pass

    @abstractmethod
    def max_speed_limit(self):
        pass

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        Validation.valid_speed(value, self.min_speed_limit(), self.max_speed_limit(),
                               f"Invalid speed limit! Must be between {self.min_speed_limit()} and {self.max_speed_limit()}!")
        self.__speed_limit = value

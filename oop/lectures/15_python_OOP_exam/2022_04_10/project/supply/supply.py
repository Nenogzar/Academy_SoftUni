from abc import ABC, abstractmethod
from project.vadidation.validation import Validation


class Supply(ABC):
    def __init__(self, name: str, energy: int):
        self.name = name
        self.energy = energy

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validation.valid_name(value, "Name cannot be an empty string.")
        self.__name = value

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):
        Validation.valid_positive_energi(value, "Energy cannot be less than zero.")
        self.__energy = value

    @abstractmethod
    def details(self):
        pass

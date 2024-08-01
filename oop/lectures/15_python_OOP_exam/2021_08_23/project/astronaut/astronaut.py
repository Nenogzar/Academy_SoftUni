from abc import ABC, abstractmethod

from project.Validation.validation import Validate


class Astronaut(ABC):
    Take_breath = 10

    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []  # In the backpack, each astronaut will collect items while on a mission

    @property
    def name(self):
        return

    @name.setter
    def name(self, value):
        Validate.validation_empty_str_whitespace(value, "Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    @abstractmethod
    def breathe(self):
        """Each time an astronaut takes a breath, their oxygen decreases by 10 units.
        Note: some types of astronauts need more oxygen units while breathing."""
        pass


    def increase_oxygen(self, amount: int):
        """Increases the oxygen with the given amount."""
        pass

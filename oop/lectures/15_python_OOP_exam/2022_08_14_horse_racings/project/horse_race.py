from typing import List

from project.jockey import Jockey
from project.validation.validation import Validation


class HorseRace:
    _valid_type = ["Winter", "Spring", "Autumn", "Summer"]
    def __init__(self, race_type: str):
        self.race_type = race_type
        self.jockeys: List[Jockey] = []


    @property
    def race_type(self):
        return self.__race_type

    @race_type.setter
    def race_type(self, value):
        Validation.valid_type(value, self._valid_type, "Race type does not exist!")
        self.__race_type = value

from abc import ABC, abstractmethod

from project.peaks.base_peak import BasePeak


class BaseClimber(ABC):
    INCREASES_POINT = 15

    def __init__(self, name: str, strength: float):
        self.name = name
        self.strength = strength
        self.conquered_peaks = []  # store a sequence of peaks conquered by each climber
        self.is_prepared = True  # epresenting that the climber has the required gear.

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" or value.isspace():
            raise ValueError("Climber name cannot be null or empty!")
        self.__name = value

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, value):
        if value <= 0:
            raise ValueError("A climber cannot have negative strength or strength equal to 0!")
        self.__strength = value

    @abstractmethod
    def can_climb(self):
        pass

    @abstractmethod
    def climb(seld, peak: BasePeak):
        pass

    def rest(self):
        self.strength += self.INCREASES_POINT

    def __str__(self):

        return f"{self.__class__.__name__}: /// Climber name: {self.name} * " \
               f"Left strength: {self.strength:.1f} * " \
               f"Conquered peaks: {', '.join(sorted(self.conquered_peaks))} ///"

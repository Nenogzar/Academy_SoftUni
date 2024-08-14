from abc import ABC, abstractmethod
from project.fish.base_fish import BaseFish

class BaseDiver(ABC):
    REDUCE_PERCENT = 1

    def __init__(self, name: str, oxygen_level: float):
        self.name = name  # name of the diver
        self.oxygen_level = oxygen_level  # oxygen level remaining, in seconds.
        self.catch = []  # store a sequence of fish, caught by a specific diver
        self.competition_points = 0.00  # total points accumulated by a diver
        self.has_health_issue = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" or value.isspace():
            raise ValueError("Diver name cannot be null or empty!")
        self.__name = value

    @property
    def oxygen_level(self):
        return self.__oxygen_level

    @oxygen_level.setter
    def oxygen_level(self, value):
        if value < 0:
            raise ValueError("Cannot create diver with negative oxygen level!")
        self.__oxygen_level = value

    @abstractmethod
    def miss(self, time_to_catch: int):
        pass

    @abstractmethod
    def renew_oxy(self):
        pass

    def hit(self, fish: BaseFish):
        if self.oxygen_level - fish.time_to_catch < 0:
            self.oxygen_level = 0

        elif self.oxygen_level - fish.time_to_catch >= 0:
            self.competition_points += fish.points
            self.oxygen_level -= fish.time_to_catch
            self.catch.append(fish)

        if self.oxygen_level == 0:
            self.update_health_status()

    def update_health_status(self):
        self.has_health_issue = not self.has_health_issue

    def __str__(self):
        return f"{self.__class__.__name__}: [Name: {self.name}, " \
               f"Oxygen level left: {self.oxygen_level}, " \
               f"Fish caught: {len(self.catch)}, " \
               f"Points earned: {self.competition_points:.1f}]"

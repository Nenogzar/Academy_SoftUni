from abc import ABC, abstractmethod

from project.equipment.base_equipment import BaseEquipment

from typing import List


class BaseTeam(ABC):
    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins = 0.00
        self.equipment: List[BaseEquipment] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" or value.isspace():
            raise ValueError("Team name cannot be empty!")
        self.__name = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        if len(value) < 2:
            raise ValueError("Team country cannot be less than 2 characters!")
        self.__country = value

    @property
    def advantage(self):
        return

    @advantage.setter
    def advantage(self, value):
        if value <= 0:
            raise ValueError("Advantage must be greater than zero!")
        self.__advantage = value

    @abstractmethod
    def win(self):
        pass

    def get_statistics(self):
        info = [f"Name: {self.name}",
                f"Country: {self.country}",
                f"Advantage: {self.__advantage} points",
                f"Budget: {self.budget:.2f}EUR",
                f"Wins: {self.wins}",
                f"Total Equipment Price: {sum(e.price for e in self.equipment):.2f}",
                f"Average Protection: {int(sum(p.protection for p in self.equipment) / len(self.equipment)) if self.equipment else 0}"]

        return '\n'.join(info)

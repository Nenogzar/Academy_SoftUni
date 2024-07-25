from abc import ABC, abstractmethod

class BaseTeam(ABC):
    valid_team_types = {
        'OutdoorTeam': 'OutdoorTeam',
        'IndoorTeam': 'IndoorTeam'
    }

    teams = {
        "OutdoorTeam": {"budget": 1000.0, "advantage": 115},
        "IndoorTeam": {"budget": 500.0, "advantage": 145}
    }

    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins = 0
        self.equipment = []

    @staticmethod
    def check_name(value):
        return value.replace(" ", "").isalnum()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not self.check_name(value):
            raise ValueError("Team name cannot be empty!")
        self._name = value

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        if len(value) < 2:
            raise ValueError("Team country should be at least 2 symbols long!")
        self._country = value

    @property
    def advantage(self):
        return self._advantage

    @advantage.setter
    def advantage(self, value):
        if int(value) <= 0:
            raise ValueError('Advantage must be greater than zero!')
        self._advantage = value

    def win(self):
        team_type = self.__class__.__name__
        self._advantage += BaseTeam.teams[team_type]["advantage"]
        self.wins += 1

    def get_statistics(self):
        total_equipment_price = sum(eq.price for eq in self.equipment)
        avg_protection = sum(eq.protection for eq in self.equipment) / len(self.equipment) if self.equipment else 0
        avg_protection = int(avg_protection)

        return (
            f"Name: {self.name}\n"
            f"Country: {self.country}\n"
            f"Advantage: {self.advantage} points\n"
            f"Budget: {self.budget:.2f}EUR\n"
            f"Wins: {self.wins}\n"
            f"Total Equipment Price: {total_equipment_price:.2f}\n"
            f"Average Protection: {avg_protection}"
        )

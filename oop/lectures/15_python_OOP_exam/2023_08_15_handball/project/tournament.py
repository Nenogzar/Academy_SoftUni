from typing import List

from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self._name = value
    @property
    def types_equipment(self):
        return {"KneePad": KneePad,
                "ElbowPad": ElbowPad}

    @property
    def types_teams(self):
        return {"OutdoorTeam": OutdoorTeam,
                "IndoorTeam": IndoorTeam}

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.types_equipment:
            raise Exception("Invalid equipment type!")
        equipment_class = self.types_equipment[equipment_type]
        new_equipment = equipment_class()  # Създай нов обект от класа
        self.equipment.append(new_equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.types_teams:
            raise Exception("Invalid team type!")

        if self.capacity <= len(self.teams):
            return Exception("Not enough tournament capacity.")

        team_class = self.types_teams[team_type]
        new_team = team_class(team_name, country, advantage)
        self.teams.append(new_team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        equipment_of_type = [e for e in self.equipment if e.__class__.__name__ == equipment_type]

        equip = equipment_of_type[-1]

        team = next((t for t in self.teams if t.name == team_name), None)

        if equip.price > team.budget:
            raise Exception("Budget is not enough!")

        self.equipment.remove(equip)
        team.budget -= equip.price
        team.equipment.append(equip)

        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = next((t for t in self.teams if t.name == team_name), None)

        if team is None:
            raise Exception("No such team!")

        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        equipment_class = self.types_equipment[equipment_type]
        count = 0
        for eq in self.equipment:
            if isinstance(eq, equipment_class):
                eq.increase_price()
                count += 1

        return f"Successfully changed {count}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = next((t for t in self.teams if t.name == team_name1), None)
        team2 = next((t for t in self.teams if t.name == team_name2), None)

        if type(team1) != type(team2):
            raise Exception("Game cannot start! Team types mismatch!")

        total1 = team1.advantage + sum(eq.protection for eq in team1.equipment)
        total2 = team2.advantage + sum(eq.protection for eq in team2.equipment)

        if total1 > total2:
            team1.win()
            return f"The winner is {team_name1}."
        elif total2 > total1:
            team2.win()
            return f"The winner is {team_name2}."
        else:
            return "No winner in this game."

    def get_statistics(self):
        stats = [
            f"Tournament: {self.name}",
            f"Number of Teams: {len(self.teams)}",
            "Teams:"
        ]

        sorted_teams = sorted(self.teams, key=lambda t: t.wins, reverse=True)
        for team in sorted_teams:
            stats.append(team.get_statistics())

        return "\n".join(stats)

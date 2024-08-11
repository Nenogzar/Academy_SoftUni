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
        return

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")

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
        new_equipment = self.types_equipment[equipment_type]
        self.equipment.append(new_equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.types_teams:
            return Exception("Invalid team type!")

        if self.capacity < len(self.teams) + 1:
            return Exception("Not enough tournament capacity.")

        new_team = self.types_teams[team_type]
        self.teams.append(new_team(team_name, country, advantage))
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        equip = next((e for e in reversed(self.equipment) if e.__class__.__name__ == equipment_type))

        team = next((t for t in self.teams if t.name == team_name))

        if equip.price > team.budget:
            raise Exception("Budget is not enough!")

        self.equipment.remove(equip)
        team.budget -= equip.price
        team.equipment.append(equip)

        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        pass

    def increase_equipment_price(self, equipment_type: str):
        pass

    def play(self, team_name1: str, team_name2: str):
        pass

    def get_statistics(self):
        pass

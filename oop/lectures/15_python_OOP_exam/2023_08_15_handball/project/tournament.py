from project.equipment.base_equipment import BaseEquipment
from project.teams.base_team import BaseTeam
from project.teams.outdoor_team import OutdoorTeam
from project.teams.indoor_team import IndoorTeam
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad


class Tournament:
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment = []
        self.teams = []

    @property
    def equipment_types(self):
        return {
            "KneePad": KneePad,
            "ElbowPad": ElbowPad
        }

    @property
    def team_types(self):
        return {
            "OutdoorTeam": OutdoorTeam,
            "IndoorTeam": IndoorTeam
        }


    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.equipment_types:
            raise Exception("Invalid equipment type!")
        equipment_class = self.equipment_types[equipment_type]
        equipment = equipment_class()
        self.equipment.append(equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.team_types:
            raise Exception("Invalid team type!")

        if len(self.teams) >= self.capacity:
            return 'Not enough tournament capacity.'

        if any(team.name == team_name for team in self.teams):
            raise Exception('Team name already exists!')

        team_class = self.team_types[team_type]
        budget = BaseTeam.teams[team_type]["budget"]

        self.teams.append(team_class(team_name, country, advantage, budget))
        return f'{team_type} was successfully added.'


    def sell_equipment(self, equipment_type: str, team_name: str):
        self.validate_equipment_type(equipment_type)
        team = next((t for t in self.teams if t.name == team_name), None)
        if not team:
            raise Exception("No such team!")

        equipment_class = self.equipment_types[equipment_type]
        equipment = next((eq for eq in reversed(self.equipment) if isinstance(eq, equipment_class)), None)

        if not equipment:
            raise Exception("No such equipment!")

        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")

        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price

        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = next((t for t in self.teams if t.name == team_name), None)

        if not team:
            raise Exception("No such team!")

        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        self.capacity += 1
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        self.validate_equipment_type(equipment_type)
        equipment_class = self.equipment_types[equipment_type]
        count = 0
        for eq in self.equipment:
            if isinstance(eq, equipment_class):
                eq.increase_price()
                count += 1

        return f"Successfully changed {count}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = next((t for t in self.teams if t.name == team_name1), None)
        team2 = next((t for t in self.teams if t.name == team_name2), None)

        if not team1 or not team2:
            raise Exception("No such team!")

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

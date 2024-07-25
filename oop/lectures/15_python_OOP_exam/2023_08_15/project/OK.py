from collections import defaultdict
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam
from project.equipment.base_equipment import BaseEquipment
from project.equipment.knee_pad import KneePad
from project.equipment.elbow_pad import ElbowPad


class Tournament:

    def __init__(self, name: str, capacity: int):

        self.name = name

        self.capacity = capacity

        self.equipment = []

        self.teams = []

    @property
    def name(self):

        return self._name

    @name.setter
    def name(self, value):

        if not value.replace(" ", "").isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")

        self._name = value

    def add_equipment(self, equipment_type: str):

        if equipment_type == "KneePad":

            equipment = KneePad()

        elif equipment_type == "ElbowPad":

            equipment = ElbowPad()

        else:

            raise Exception("Invalid equipment type!")

        self.equipment.append(equipment)

        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):

        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."

        if team_type == "OutdoorTeam":

            team = OutdoorTeam(name=team_name, country=country, advantage=advantage)

        elif team_type == "IndoorTeam":

            team = IndoorTeam(name=team_name, country=country, advantage=advantage)

        else:

            raise Exception("Invalid team type!")

        if any(t.name == team_name for t in self.teams):
            raise ValueError("Team name must be unique!")

        self.teams.append(team)

        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):

        team = next((t for t in self.teams if t.name == team_name), None)

        if team is None:
            raise Exception("Team not found!")

        equipment = next((e for e in reversed(self.equipment) if e.__class__.__name__ == equipment_type), None)

        if equipment is None:
            raise Exception("Equipment not found!")

        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")

        self.equipment.remove(equipment)

        team.equipment.append(equipment)

        team.budget -= equipment.price

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

        if equipment_type not in {"KneePad", "ElbowPad"}:
            raise Exception("Invalid equipment type!")

        equipment_to_update = [e for e in self.equipment if e.__class__.__name__ == equipment_type]

        for equipment in equipment_to_update:
            equipment.increase_price()

        return f"Successfully changed {len(equipment_to_update)}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):

        team1 = next((t for t in self.teams if t.name == team_name1), None)

        team2 = next((t for t in self.teams if t.name == team_name2), None)

        if team1 is None or team2 is None:
            raise Exception("One or both teams do not exist!")

        if type(team1) != type(team2):
            raise Exception("Game cannot start! Team types mismatch!")

        team1_result = team1.advantage + sum(e.protection for e in team1.equipment)

        team2_result = team2.advantage + sum(e.protection for e in team2.equipment)

        if team1_result > team2_result:

            team1.win()

            return f"The winner is {team_name1}."

        elif team2_result > team1_result:

            team2.win()

            return f"The winner is {team_name2}."

        else:

            return "No winner in this game."

    def get_statistics(self):

        stats = [f"Tournament: {self.name}"]

        stats.append(f"Number of Teams: {len(self.teams)}")

        stats.append("Teams:")

        sorted_teams = sorted(self.teams, key=lambda t: t.wins, reverse=True)

        for team in sorted_teams:
            stats.append(team.get_statistics())

        return "\n".join(stats)

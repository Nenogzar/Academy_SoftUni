from project.teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):
    TEAM_BUDGET = 1000
    INCREASES_ADVANTAGE = 115

    def __init__(self, name, country: str, advantage: int):
        super().__init__(name, country, advantage, self.TEAM_BUDGET)
        self.wins = 0

    def win(self):
        self.advantage += self.INCREASES_ADVANTAGE
        self.wins += 1

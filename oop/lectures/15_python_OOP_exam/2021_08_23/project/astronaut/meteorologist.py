from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    Take_breath = 15
    OXIGEN = 90

    def __init__(self, name: str):
        super().__init__(name, self.OXIGEN)


    def breathe(self):
        self.oxygen -= self.Take_breath

    def increase_oxygen(self, amount: int):
        self.oxygen += amount


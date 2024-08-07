from project.horse_specification.horse import Horse
from project.validation.validation import Validation

class Appaloosa(Horse):
    MAX_SPEED = 120

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        self.speed = Validation.adjust_horse_speed(self.speed, 2, self.MAX_SPEED)

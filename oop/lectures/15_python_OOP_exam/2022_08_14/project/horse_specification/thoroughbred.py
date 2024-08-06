from project.horse_specification.horse import Horse
from project.validation.validation import Validation

class Thoroughbred(Horse):
    MAX_SPEED = 140

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        self.speed = Validation.adjust_horse_speed(self.speed, 3, self.MAX_SPEED)

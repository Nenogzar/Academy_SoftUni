from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):
    weight_gain = 3

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, weight=9)

    def eating(self):
        self.weight += self.weight_gain

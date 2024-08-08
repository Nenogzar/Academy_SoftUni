from project.services.base_service import BaseService


class SecondaryService (BaseService):
    max_capacity = 15

    def __init__(self, name: str):
        super().__init__(name, capacity=self.max_capacity)

    def details(self):
        if not self.robots:
            robots_str = "none"
        else:
            robots_str = " ".join(robot.name for robot in self.robots)

        return f"{self.name} Secondary Service:\nRobots: {robots_str}"

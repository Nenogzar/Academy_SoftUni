from project.services.base_service import BaseService


class MainService(BaseService):
    max_capacity = 30

    def __init__(self, name: str):
        super().__init__(name, capacity=self.max_capacity)

    def details(self):
        if not self.robots:
            robots_str = "none"
        else:
            robots_str = " ".join(robot.name for robot in self.robots)

        return f"{self.name} Main Service:\nRobots: {robots_str}"

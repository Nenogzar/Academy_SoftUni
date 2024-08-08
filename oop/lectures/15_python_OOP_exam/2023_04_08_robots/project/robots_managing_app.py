from typing import List

from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    @property
    def type_robots_mapper(self):
        return {"FemaleRobot": FemaleRobot,
                "MaleRobot": MaleRobot}

    @property
    def type_service_mapper(self):
        return {"MainService": MainService,
                "SecondaryService": SecondaryService}

    def add_service(self, service_type: str, name: str):
        if service_type not in self.type_service_mapper:
            raise Exception("Invalid service type!")

        new_service = self.type_service_mapper[service_type](name)
        self.services.append(new_service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.type_robots_mapper:
            raise Exception("Invalid robot type!")

        new_robot = self.type_robots_mapper[robot_type](name, kind, price)
        self.robots.append(new_robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = next(r for r in self.robots if r.name == robot_name)
        service = next(s for s in self.services if s.name == service_name)

        if isinstance(robot, FemaleRobot) and not isinstance(service, SecondaryService):
            return "Unsuitable service."
        if isinstance(robot, MaleRobot) and not isinstance(service, MainService):
            return "Unsuitable service."

        if len(service.robots) >= service.capacity:
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)

        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = next(s for s in self.services if s.name == service_name)
        robot = next((r for r in service.robots if r.name == robot_name), None)

        if robot is None:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)

        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = next(s for s in self.services if s.name == service_name)

        for robot in service.robots:
            robot.eating()

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = next(s for s in self.services if s.name == service_name)

        total_price = sum(robot.price for robot in service.robots)
        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        service_details = [service.details() for service in self.services]

        return "\n".join(service_details)

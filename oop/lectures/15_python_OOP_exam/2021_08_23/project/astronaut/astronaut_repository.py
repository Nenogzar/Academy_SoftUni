from typing import List

from project.astronaut.astronaut import Astronaut


class AstronautRepository:
    def __init__(self):
        self.astronauts: List[Astronaut] = []

    def add(self, astronaut: Astronaut):
        # if astronaut not in self.astronaut:
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        # if astronaut in self.astronaut:
        self.astronauts.remove(astronaut)

    def find_by_name(self, name: str):
        for ast in self.astronauts:
            if name == ast.name:
                return ast

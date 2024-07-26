from typing import List

from project.additional.additional_functions import Additional
from project.software.software import Software


class Hardware():
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components: List[name] = []

    def install(self, software: Software):
        Additional.enough_capacity(self.capacity,
                                   self.memory,
                                   self.software_components,
                                   software,
                                   "Software cannot be installed")

        self.software_components.append(software)

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)


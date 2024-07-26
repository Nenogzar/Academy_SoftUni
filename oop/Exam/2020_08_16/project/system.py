from typing import List
from project import software
from project.hardware import hardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware


class System:
    _hardware: List[hardware] = []
    _software: List[software] = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        # System._hardware.append(PowerHardware(name, capacity, memory))
        ...

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        # System._hardware.append(HeavyHardware(name, capacity, memory))
        ...

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        ...

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        ...

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        ...

    @staticmethod
    def analyze():
        ...

    @staticmethod
    def system_split():
        ...

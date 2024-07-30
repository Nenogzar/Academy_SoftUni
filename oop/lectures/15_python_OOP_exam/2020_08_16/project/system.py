from project import hardware
from project.additional_methods.additional import Aditional
from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []  # storing all the hardware components
    _software = []  # storing all the software components

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        new_hardware = Aditional.hardware_exist(hardware_name, System._hardware, "Hardware does not exist")

        if isinstance(new_hardware, str):
            return new_hardware

        express_soft = ExpressSoftware(name, capacity_consumption, memory_consumption)

        new_hardware.install(express_soft)
        System._software.append(express_soft)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        new_hardware = Aditional.hardware_exist(hardware_name, System._hardware, "Hardware does not exist")
        if isinstance(new_hardware, str):
            return new_hardware

        light_soft = LightSoftware(name, capacity_consumption, memory_consumption)

        new_hardware.install(light_soft)
        System._software.append(light_soft)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hard = Aditional.search_exist(hardware_name, System._hardware)
        soft = Aditional.search_exist(software_name, System._software)

        if isinstance(hard, str) or isinstance(soft, str):
            return "Some of the components do not exist"

        hard.uninstall(soft)
        System._software.remove(soft)

    @staticmethod
    def analyze():
        soft_memory = sum(s.memory_consumption for s in System._software)
        hard_memory = sum(h.memory for h in System._hardware)
        sof_capacity = sum(s.capacity_consumption for s in System._software)
        hard_capacity = sum(h.capacity for h in System._hardware)

        output = ["System Analysis",
                  f"Hardware Components: {len(System._hardware)}",
                  f"Software Components: {len(System._software)}",
                  f"Total Operational Memory: {soft_memory} / {hard_memory}",
                  f"Total Capacity Taken: {sof_capacity} / {hard_capacity}"]

        return "\n".join(output)

    @staticmethod
    def system_split():
        return "\n".join(str(h) for h in System._hardware)

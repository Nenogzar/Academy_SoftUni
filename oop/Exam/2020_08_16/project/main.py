from project.software.software import Software
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware

from system import System


def zero_test():
    System.register_power_hardware("HDD", 200, 200)
    System.register_heavy_hardware("SSD", 400, 400)
    print(System.analyze())
    System.register_light_software("HDD", "Test", 0, 10)
    print(System.register_express_software("HDD", "Test2", 100, 100))
    System.register_express_software("HDD", "Test3", 50, 100)
    System.register_light_software("SSD", "Windows", 20, 50)
    System.register_express_software("SSD", "Linux", 50, 100)
    System.register_light_software("SSD", "Unix", 20, 50)
    print(System.analyze())
    System.release_software_component("SSD", "Linux")
    print(System.system_split())


if __name__ == "__main__":
    zero_test()


soft3 = ExpressSoftware("HDD",100,100)
print(soft3)
print(soft3.name)
print(soft3.capacity_consumption)
print(soft3.memory_consumption)
print(soft3.software_type)

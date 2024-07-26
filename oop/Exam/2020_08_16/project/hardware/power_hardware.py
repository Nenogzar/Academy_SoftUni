from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    __TYPE = "Power"
    __CAPACITY = 0.25
    __MEMORY = 1.75

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name,
                         PowerHardware.__TYPE,
                         int(PowerHardware.__CAPACITY * capacity),
                         int(PowerHardware.__MEMORY * memory))

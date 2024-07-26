from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    __TYPE = "Heavy"
    __CAPACITY = 2
    __MEMORY = 0.75

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name,
                         HeavyHardware.__TYPE,
                         int(capacity * HeavyHardware.__CAPACITY),
                         int(memory * HeavyHardware.__MEMORY))

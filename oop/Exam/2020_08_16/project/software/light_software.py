from project.software.software import Software


class LightSoftware(Software):
    __TYPE = "Light"
    __CAPACITY = 1.5
    __MEMORY = 0.5

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name,
                         LightSoftware.__TYPE,
                         int(capacity_consumption * LightSoftware.__CAPACITY),
                         int(memory_consumption * LightSoftware.__MEMORY))

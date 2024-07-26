from project.software.software import Software


class ExpressSoftware(Software):
    __TYPE = "Express"
    __MEMORY = 2
    
    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name,
                         ExpressSoftware.__TYPE,
                         capacity_consumption,
                         int(memory_consumption * ExpressSoftware.__MEMORY))

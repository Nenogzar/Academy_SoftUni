from project.supply.supply import Supply


class Drink(Supply):
    units_of_energy = 15

    def __init__(self, name: str, energy = units_of_energy):
        super().__init__(name, energy)

    def details(self):
        return f"{self.__class__.__name__}: {self.name}, {self.energy}"

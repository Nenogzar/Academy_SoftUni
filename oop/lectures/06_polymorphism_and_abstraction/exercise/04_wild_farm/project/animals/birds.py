from project.animals.animal import Bird, Animal, Mammal
from project.food import Food, Vegetable, Fruit, Meat, Seed

class Owl(Bird):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

class Hen(Bird):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

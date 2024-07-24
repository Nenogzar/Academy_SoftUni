from project.animals.animal import Bird
from project.food import Food, Vegetable, Fruit, Meat, Seed


class Owl(Bird):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    def eat(self, food: Food):
        if isinstance(food, Meat):
            self.food_eaten += food.quantity
            self.weight += food.quantity * 0.25
        else:
            print(f"{self.__class__.__name__} does not eat {food.__class__.__name__}!")

    def feed(self, food: Food):
        if isinstance(food, Meat):
            self.food_eaten += food.quantity
            self.weight += food.quantity * 0.25
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Hen(Bird):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    def eat(self, food: Food):
        self.food_eaten += food.quantity
        self.weight += food.quantity * 0.35

    def feed(self, food: Food):
        self.food_eaten += food.quantity
        self.weight += food.quantity * 0.35

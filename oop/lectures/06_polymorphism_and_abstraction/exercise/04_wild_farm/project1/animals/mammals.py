from project1.animals.animal import Mammal
from project1.food import Food, Vegetable, Fruit, Meat, Seed

class Mouse(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    def eat(self, food: Food):
        if isinstance(food, (Vegetable, Fruit)):
            self.food_eaten += food.quantity
            self.weight += food.quantity * 0.10
        else:
            print(f"{self.__class__.__name__} does not eat {food.__class__.__name__}!")

    def feed(self, food: Food):
        if isinstance(food, (Vegetable, Fruit)):
            self.food_eaten += food.quantity
            self.weight += food.quantity * 0.10
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

class Dog(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    def eat(self, food: Food):
        if isinstance(food, Meat):
            self.food_eaten += food.quantity
            self.weight += food.quantity * 0.40
        else:
            print(f"{self.__class__.__name__} does not eat {food.__class__.__name__}!")

    def feed(self, food: Food):
        if isinstance(food, Meat):
            self.food_eaten += food.quantity
            self.weight += food.quantity * 0.40
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

class Cat(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    def eat(self, food: Food):
        if isinstance(food, (Vegetable, Meat)):
            self.food_eaten += food.quantity
            self.weight += food.quantity * 0.30
        else:
            print(f"{self.__class__.__name__} does not eat {food.__class__.__name__}!")

    def feed(self, food: Food):
        if isinstance(food, (Vegetable, Meat)):
            self.food_eaten += food.quantity
            self.weight += food.quantity * 0.30
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

class Tiger(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    def eat(self, food: Food):
        if isinstance(food, Meat):
            self.food_eaten += food.quantity
            self.weight += food.quantity * 1.00
        else:
            print(f"{self.__class__.__name__} does not eat {food.__class__.__name__}!")

    def feed(self, food: Food):
        if isinstance(food, Meat):
            self.food_eaten += food.quantity
            self.weight += food.quantity * 1.00
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

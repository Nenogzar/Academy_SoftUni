from abc import ABC, abstractmethod
from project.food import Food

data_dic = {
    "Hen": {
        "food": ["Vegetable", "Fruit", "Meat", "Seed"],
        "weight increase": 0.35,
        "sound": "Cluck"
    },
    "Owl": {
        "food": ["Meat"],
        "weight increase": 0.25,
        "sound": "Hoot Hoot"
    },
    "Mouse": {
        "food": ["Vegetable", "Fruit"],
        "weight increase": 0.10,
        "sound": "Squeak"
    },
    "Cat": {
        "food": ["Vegetable", "Meat"],
        "weight increase": 0.30,
        "sound": "Meow"
    },
    "Dog": {
        "food": ["Meat"],
        "weight increase": 0.40,
        "sound": "Woof!"
    },
    "Tiger": {
        "food": ["Meat"],
        "weight increase": 1.00,
        "sound": "ROAR!!!"
    }
}


class Animal(ABC):
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0
        self.animal_type = self.__class__.__name__

    @abstractmethod
    def make_sound(self):
        pass

    def make_sound(self):
        return data_dic[self.animal_type]["sound"]

    def feed(self, food: Food):
        animal_data = data_dic[self.animal_type]
        if type(food).__name__ in animal_data["food"]:
            self.food_eaten += food.quantity
            self.weight += food.quantity * animal_data["weight increase"]
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

    @abstractmethod
    def __repr__(self):
        pass


class Bird(Animal):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"

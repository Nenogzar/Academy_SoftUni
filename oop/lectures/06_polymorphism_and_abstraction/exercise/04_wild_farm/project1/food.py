from abc import ABC

class Food(ABC):
    def __init__(self, quantity: int):
        self.quantity = quantity

class Vegetable(Food):
    def __repr__(self):
        return "Vegetable"

class Fruit(Food):
    def __repr__(self):
        return "Fruit"

class Meat(Food):
    def __repr__(self):
        return "Meat"

class Seed(Food):
    def __repr__(self):
        return "Seed"

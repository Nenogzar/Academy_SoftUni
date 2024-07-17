from project.dough import Dough
from project.topping import Topping

class Pizza:

    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int):
        if not name:
            raise ValueError("The name cannot be an empty string")
        self.__name = name

        if dough is None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = dough

        if max_number_of_toppings <= 0:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")
        self.__max_number_of_toppings = max_number_of_toppings

        self.__toppings = {}  # empty dictionary to store toppings


    @property
    def name(self):
        return self.__name

    @property
    def dough(self):
        return self.__dough

    @property
    def max_number_of_toppings(self):
        return self.__max_number_of_toppings

    @property
    def toppings(self):
        return self.__toppings

    def add_topping(self, topping: Topping):
        if self.max_number_of_toppings == len(self.toppings):
            raise ValueError("Not enough space for another topping")
        self.toppings[topping.topping_type] = self.toppings.get(topping.topping_type, 0) + topping.weight

    def calculate_total_weight(self):
        return self.dough.weight + sum(self.toppings.values())

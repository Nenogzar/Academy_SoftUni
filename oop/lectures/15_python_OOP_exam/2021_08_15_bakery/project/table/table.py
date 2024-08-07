from abc import ABC, abstractmethod
from typing import List
from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink
from project.Validators.validators import Validation


class Table(ABC):
    @abstractmethod
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity  # the table's seat capacity.
        self.food_order: List[BakedFood] = []  # contain every food order made from the table.
        self.drink_orders: List[Drink] = []  # contain every drink order made from the table.
        self.number_of_people = 0  # count of people who sit at the table
        self.is_reserved = False  # Returns True if the table is reserved

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        Validation.validation_positive_value(value, "Capacity has to be greater than 0!")
        self.__capacity = value

    def reserve(self, number_of_people: int):
        self.number_of_people = number_of_people
        self.is_reserved = True

    def order_food(self, baked_food: BakedFood):
        self.food_order.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        food_price = sum(food.price for food in self.food_order)
        drink_price = sum(drink.price for drink in self.drink_orders)
        return food_price + drink_price

    def clear(self):
        self.food_order = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        if not self.is_reserved:
            return f"Table: {self.table_number}\n" \
                   f"Type: {self.__class__.__name__}\n" \
                   f"Capacity: {self.capacity}"

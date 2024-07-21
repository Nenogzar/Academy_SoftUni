# ******* Class and Static Methods ******* #

# *******  2_shop  ******* #

# *******  TASK CONDITION  ******* #
"""
https://judge.softuni.org/Contests/2430/Static-and-Class-Methods-Lab

Create a class called Shop. Upon initialization, it should receive a name (str), type (str), and capacity (int).
    The store should also have an attribute called items
    (an empty dictionary that stores the name of an item and its quantity).

    The class should have 4 methods:

•	small_shop(name: str, type: str)
        - a new shop with a capacity of 10 should be created

•	add_item(item_name: str)
        - adds 1 to the quantity of the given item.

            On success, the method should
                return "{item_name} added to the shop".
            If the addition is not possible, the following message should be
                return "Not enough capacity in the shop"

•	remove_item(item_name:str, amount:int)
        - removes the given amount from the item.
            On success, it should
                return "{amount} {item_name} removed from the shop".
            Otherwise, the method should
                return "Cannot remove {amount} {item_name}"

o	If the item quantity reaches 0, the item should be removed from the items' dictionary.
•	__repr__() - returns a string representation in the format
        "{shop_name} of type {shop_type} with capacity {shop_capacity}"

"""

##########: SOLUTION :##########
from typing import Dict


class Shop:
    def __init__(self, name: str, type: str, capacity: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items: Dict[str, int] = {}

    @classmethod
    def small_shop(cls, name: str, type: str):
        return cls(name, type, capacity=10)

    def add_item(self, item_name: str):
        if self.capacity > sum(self.items.values()):
            if item_name not in self.items:
                self.items[item_name] = 0
            self.items[item_name] += 1
            return f"{item_name} added to the shop"
        return "Not enough capacity in the shop"

    def remove_item(self, item_name: str, amount: int):
        if item_name not in self.items:
            return f"Cannot remove {amount} {item_name}"
        if self.items[item_name] < amount:
            return f"Cannot remove {amount} {item_name}"

        self.items[item_name] -= amount
        if self.items[item_name] <= 0:
            del self.items[item_name]

        return f"{amount} {item_name} removed from the shop"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


##########: TEST CODE :##########

fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
print(fresh_shop)
print(small_shop)

print(fresh_shop.add_item("Bananas"))
print(fresh_shop.remove_item("Tomatoes", 2))

print(small_shop.add_item("Jeans"))
print(small_shop.add_item("Jeans"))
print(small_shop.remove_item("Jeans", 2))
print(small_shop.items)

"""
Output:
Fresh Shop of type Fruit and Veg with capacity 50
Fashion Boutique of type Clothes with capacity 10
Bananas added to the shop
Cannot remove 2 Tomatoes
Jeans added to the shop
Jeans added to the shop
2 Jeans removed from the shop
{}

 """
##########: UNITTEST :##########

import unittest

class ShopTests(unittest.TestCase):
    def setUp(self):
        self.fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)

    def test_add_item_success(self):
        result = self.fresh_shop.add_item("Bananas")
        self.assertEqual(self.fresh_shop.items["Bananas"], 1)
        self.assertEqual(result, "Bananas added to the shop")

    def test_remove_item_success(self):
        self.fresh_shop.add_item("Bananas")
        result = self.fresh_shop.remove_item("Bananas", 1)
        self.assertEqual(result, "1 Bananas removed from the shop")

    def test_remove_item_unsuccessful(self):
        self.fresh_shop.add_item("Bananas")
        result = self.fresh_shop.remove_item("Tomatoes", 2)
        self.assertEqual(result, "Cannot remove 2 Tomatoes")

    def test_repr(self):
        self.assertEqual(repr(self.fresh_shop), "Fresh Shop of type Fruit and Veg with capacity 50")


if __name__ == "__main__":
    unittest.main()
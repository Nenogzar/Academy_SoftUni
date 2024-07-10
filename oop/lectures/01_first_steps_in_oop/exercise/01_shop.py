# ******* Exercise: First Steps in OOP ******* #

# *******  01_shop  ******* #

# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Compete/Index/1935#0

Create a class called Shop.
Upon initialization, it should receive a name (string) and items (list).
Create a method called get_items_count() which should return the number of items in the store.

Examples

Test Code
shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
print(shop.get_items_count())

Output
3

"""
##########: variant 1 :##########

#  използвам any за да гарантирам че листа ще може да се пълни с всякакъв тип елементи
from typing import List, Any


class Shop:
    def __init__(self, name: str, items: List[Any]):
        self.name = name
        self.items = items

    def get_items_count(self):
        return len(self.items)


shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
print(shop.get_items_count())

##########: variant 2 :##########
#  или str когата съм сигурен че ще се подават само стингове
from typing import List


class Shop:
    def __init__(self, name: str, items: List[str]):
        self.name = name
        self.items = items

    def get_items_count(self):
        return len(self.items)


shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
print(shop.get_items_count())

##########: variant 3 solution SoftUni :##########

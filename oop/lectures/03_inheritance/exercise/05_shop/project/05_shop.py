# ******* Inheritance - Exercise ******* #

# *******  05_shop  ******* #

# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Compete/Index/1941
Maria is expanding her business, and today, she is opening a grocery shop. You are hired
to write a program that keeps track of the shop's inventory

drink.py
food.py
product.py
product_repository.py

In the product.py file, the class Product should be implemented.
    It is a base class for any type of food and drink.

The class should receive name: str, and quantity: int upon initialization.
    It should also have 3 additional methods:
        •	decrease(quantity: int) - decreases the quantity of the product only if there is enough

        •	increase(quantity: int) - increases the quantity of the product
        •	__repr__() - override the method, so it returns the name of the product
In the file drink.py,
    the class Drink should be implemented.
    The class should inherit from the Product class. An instance of the Drink class will have a name and a quantity of 10.

In the food.py file,
    the Food class should be implemented.
    The class should inherit from the Product class. An instance of the Food class will have a name and a quantity of 15.

In the product_repository.py file,
    the class ProductRepository should be implemented.
    It is a repository for all products that are delivered to the grocery shop.

The class should have products:
    list - an empty list, which will contain all products (objects).
    Also, the class should have 4 additional methods:

        •	add(product: Product) - adds a product to the repository
        •	find(product_name: str) - returns a product (object) with that name
        •	remove(product_name) - removes a product from the repository
        •	__repr__() - override the method, so it returns information for all products in the repository:

            "{product_name1}: {quantity1}"
            {product_name2}: {quantity2}
            …
            {product_nameN}: {quantityN}"
"""
from project.drink import Drink
from project.food import Food
from project.product import Product
from project.product_repository import ProductRepository

##########: TEST CODE :##########
food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(repo)

"""
Output:

[apple, water]
water
apple: 10
water: 10

 """
##########: UNITTEST :##########

import unittest




class Tests(unittest.TestCase):
    def setUp(self):
        self.product = Product('product', 150)
        self.drink = Drink('drink')
        self.food = Food('food')
        self.repo = ProductRepository()

    def test_init_of_product(self):
        self.assertEqual(self.product.name, 'product')
        self.assertEqual(self.product.quantity, 150)

    def test_decrease_product(self):
        self.product.decrease(10)
        self.assertEqual(self.product.quantity, 140)

    def test_increase_product(self):
        self.product.increase(10)
        self.assertEqual(self.product.quantity, 160)

    def test_drink_init(self):
        self.assertEqual(self.drink.name, 'drink')
        self.assertEqual(self.drink.quantity, 10)
        self.assertEqual(self.drink.__class__.__base__.__name__, 'Product')

    def test_decrease_drink(self):
        self.drink.decrease(10)
        self.assertEqual(self.drink.quantity, 0)

    def test_increase_drink(self):
        self.drink.increase(10)
        self.assertEqual(self.drink.quantity, 20)

    def test_food_init(self):
        self.assertEqual(self.food.name, 'food')
        self.assertEqual(self.food.quantity, 15)
        self.assertEqual(self.food.__class__.__base__.__name__, 'Product')

    def test_decrease_food(self):
        self.food.decrease(10)
        self.assertEqual(self.food.quantity, 5)

    def test_increase_food(self):
        self.food.increase(10)
        self.assertEqual(self.food.quantity, 25)

    def test_init_repo(self):
        self.assertEqual(self.repo.products, [])

    def test_repo_add(self):
        self.repo.add(self.food)
        self.repo.add(self.drink)
        self.assertEqual(len(self.repo.products), 2)
        self.assertEqual(self.repo.products[0], self.food)
        self.assertEqual(self.repo.products[1], self.drink)

    def test_repo_remove(self):
        self.repo.products = [self.drink, self.food]
        self.repo.remove('drink')
        self.assertEqual(self.repo.products[0], self.food)
        self.repo.remove('drink')
        self.assertEqual(self.repo.products[0], self.food)

    def test_repo_repr(self):
        self.repo.add(self.food)
        self.repo.add(self.drink)
        actual = str(self.repo)
        expected = 'food: 15\ndrink: 10'
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

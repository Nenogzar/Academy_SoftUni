# ******* Inheritance - Lab ******* #

# *******  5_hierarchical_inheritance  ******* #
 
# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/1940#4

In a folder called project create three files: animal.py, dog.py, and cat.py.
In each file, create its corresponding class - Animal, Dog, and Cat:
•	Animal with a single method eat() that returns: "eating..."
•	Dog with a single method bark() that returns: "barking..."
•	Cat with a single method meow() that returns: "meowing..."
Both Dog and Cat should inherit from Animal.
Submit in Judge a zip file of the folder project.

"""

##########: SOLUTION :##########



##########: TEST CODE :##########



"""
Output:

 """
##########: UNITTEST :##########


import unittest

from project.animal import Animal
from project.cat import Cat
from project.dog import Dog


class Tests(unittest.TestCase):
    def test_animal(self):
        a = Animal()
        self.assertEqual(a.eat(), "eating...")

    def test_dog(self):
        a = Dog()
        self.assertEqual(a.bark(), "barking...")
        self.assertEqual(a.__class__.__bases__[0].__name__, "Animal")

    def test_cat(self):
        a = Cat()
        self.assertEqual(a.meow(), "meowing...")
        self.assertEqual(a.__class__.__bases__[0].__name__, "Animal")


if __name__ == "__main__":
    unittest.main()

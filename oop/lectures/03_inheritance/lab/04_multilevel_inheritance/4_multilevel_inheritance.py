# ******* Inheritance - Lab ******* #

# *******  4_multilevel_inheritance  ******* #
 
# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/1940#3
In a folder called project create three files: vehicle.py and car.py, and sports_car.py.
In each file, create its corresponding class - Vehicle, Car, and SportsCar:
•	Vehicle with a single method move() that returns: "moving..."
•	Car with a single method drive() that returns: "driving..."
•	SportsCar with a single method race() that returns: "racing...".
SportsCar should inherit from Car and Car should inherit from Vehicle.
Submit in Judge a zip file of the folder project.

"""

##########: SOLUTION :##########



##########: TEST CODE :##########



"""
Output:

 """
##########: UNITTEST :##########
import unittest

from project.car import Car
from project.sports_car import SportsCar
from project.vehicle import Vehicle


class Tests(unittest.TestCase):
    def test_vehicle(self):
        v = Vehicle()
        self.assertEqual(v.move(), "moving...")

    def test_car(self):
        c = Car()
        self.assertEqual(c.drive(), "driving...")
        self.assertEqual(c.__class__.__bases__[0].__name__, "Vehicle")

    def test_sports_car(self):
        s = SportsCar()
        self.assertEqual(s.race(), "racing...")
        self.assertEqual(s.__class__.__bases__[0].__name__, "Car")


if __name__ == "__main__":
    unittest.main()


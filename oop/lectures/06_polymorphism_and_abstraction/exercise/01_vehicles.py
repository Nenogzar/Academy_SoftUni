# ******* Polymorphism and Abstraction - Exercise ******* #

# *******  01_vehicles  ******* #

# *******  TASK CONDITION  ******* #
"""
https://judge.softuni.org/Contests/Compete/Index/1943
Create an abstract class called Vehicle that should have abstract methods drive and refuel.
Create 2 vehicles that inherit the Vehicle class (a Car and a Truck) and simulate driving and refueling them.

Car and Truck both receive fuel_quantity and fuel_consumption in liters per km upon initialization.

They both can be driven a given distance: drive(distance) and refueled with a given amount of fuel: refuel(fuel).
It is summer, so both vehicles use air conditioners,
    and their fuel consumption per km when driving is increased by 0.9 liters for the car and 1.6 liters for the truck.
    Also, the Truck has a tiny hole in its tank, and when it is refueled, it keeps only 95% of the given fuel.
    The car has no problems and adds all the given fuel to its tank.
    If a vehicle cannot travel the given distance, its fuel does not change.
Note: Submit all your classes and imports in the judge system

"""

##########: SOLUTION :##########
from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def drive(self, distance: int):
        pass

    @abstractmethod
    def refuel(self, fuel: int):
        pass


class Car(Vehicle):
    AC_CONSUMPTION = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity

        self.fuel_consumption = fuel_consumption

    def drive(self, distance: int):
        fuel_needed = distance * (self.fuel_consumption + self.AC_CONSUMPTION)

        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AC_CONSUMPTION = 1.6
    FUEL_COEFFICIENT = 0.95

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity

        self.fuel_consumption = fuel_consumption

    def drive(self, distance: int):
        fuel_needed = distance * (self.fuel_consumption + self.AC_CONSUMPTION)

        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel * self.FUEL_COEFFICIENT


##########: TEST CODE :##########
# 1
car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

# 2
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)

"""
Output:
#1
2.299999999999997
12.299999999999997

#2
17.0
64.5

 """
##########: UNITTEST :##########

# test car
import unittest


class VehiclesTests(unittest.TestCase):
    def test_first_zero(self):
        car = Car(20, 5)
        car.drive(3)
        self.assertEqual(car.fuel_quantity, 2.299999999999997)
        car.refuel(10)
        self.assertEqual(car.fuel_quantity, 12.299999999999997)

    # second zero test

    def test_second_zero(self):
        truck = Truck(100, 15)
        truck.drive(5)
        self.assertEqual(truck.fuel_quantity, 17.0)
        truck.refuel(50)
        self.assertEqual(truck.fuel_quantity, 64.5)


if __name__ == '__main__':
    unittest.main()

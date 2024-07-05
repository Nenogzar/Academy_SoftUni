# ******* Lab: Classes and Objects ******* #

# *******  1_vehicle  ******* #
 
# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/1936#0
Create a class called Vehicle. Upon initialization, it should receive max_speed
(integer, optional; 150 by default) and mileage (number).
Create an instance variable called gadgets - an empty list by default.

"""

##########: variant 1 :##########

class Vehicle:
    def __init__(self, mileage, max_speed=150):
        self.max_speed = max_speed
        self.mileage = mileage
        self.gadgets = []


##########: TEST CODE :##########

car = Vehicle(20)
print(car.max_speed)
print(car.mileage)
print(car.gadgets)
car.gadgets.append('Hudly Wireless')
print(car.gadgets)


"""
Output:

150
20
[]
['Hudly Wireless']
"""


##########: UNITTEST :##########

# import unittest
#
# class Tests(unittest.TestCase):
#     def test_init(self):
#         car = Vehicle(20)
#         self.assertEqual(car.max_speed, 150)
#         self.assertEqual(car.mileage, 20)
#         self.assertEqual(car.gadgets, [])
#
#     def test_add_gadget(self):
#         car = Vehicle(20)
#         car.gadgets.append('Hudly Wireless')
#         self.assertEqual(car.gadgets, ['Hudly Wireless'])
#
# if __name__ == "__main__":
#     unittest.main()

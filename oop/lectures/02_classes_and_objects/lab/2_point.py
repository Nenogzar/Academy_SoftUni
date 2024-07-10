# ******* Lab: Classes and Objects ******* #

# *******  2_point  ******* #

# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/1936#1
Create a class called Point.
Upon initialization, it should receive x and y (numbers).


Create 3 instance methods:
-	set_x(new_x) - changes the x value of the point
-	set_y(new_y) - changes the y value of the point
-	__str__() - returns the coordinates of the point in the format
-	"The point has coordinates ({x},{y})"

"""


##########: variant 1 :##########

class Point:
    def __init__(self, num1:int, num2:int):
        self.x = num1
        self.y = num2

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y


    def __str__(self):
        return f"The point has coordinates ({self.x},{self.y})"



##########: TEST CODE :##########

p = Point(2, 4)
print(p)
p.set_x(3)
p.set_y(5)
print(p)

"""
Output:

The point has coordinates (2,4)
The point has coordinates (3,5)
"""

##########: UNITTEST :##########

import unittest

class Tests(unittest.TestCase):
    def test_init(self):
        p = Point(20, 40)
        self.assertEqual(p.x, 20)
        self.assertEqual(p.y, 40)

    def test_set_x(self):
        p = Point(10, 20)
        p.set_x(7)
        self.assertEqual(p.x, 7)

    def test_set_y(self):
        p = Point(10, 20)
        p.set_y(18)
        self.assertEqual(p.y, 18)

    def test_distance(self):
        p = Point(10, 11)
        res = p.__str__()
        self.assertEqual(res, 'The point has coordinates (10,11)')

if __name__ == "__main__":
    unittest.main()

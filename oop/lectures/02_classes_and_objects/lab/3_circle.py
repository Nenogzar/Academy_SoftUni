# ******* Lab: Classes and Objects ******* #

# *******  3_circle  ******* #

# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/1936#2

Create a class called Circle.
Upon initialization, it should receive a radius (number).

Create a class attribute called pi which should be equal to 3.14.

Create 3 instance methods:
-	set_radius(new_radius) - changes the radius
-	get_area() - returns the area of the circle
-	get_circumference() - returns the circumference of the circle

"""


##########: variant 1 :##########


class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = float(radius)

    def set_radius(self, new_radius):
        self.radius = float(new_radius)

    def get_area(self):
        return Circle.pi * self.radius ** 2

    def get_circumference(self):
        return Circle.pi * 2 * self.radius




##########: Test Code :##########

circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())

"""
output:

452.16
75.36
"""

##########: UNITTEST :##########
# import unittest
#
#
# class Tests(unittest.TestCase):
#     def test_init(self):
#         c = Circle(15)
#         self.assertEqual(c.radius, 15)
#
#     def test_class_attributes(self):
#         self.assertEqual(Circle.pi, 3.14)
#
#     def test_set_radius(self):
#         c = Circle(15)
#         c.set_radius(160)
#         self.assertEqual(c.radius, 160)
#
#     def test_get_area(self):
#         c = Circle(4)
#         self.assertEqual(c.get_area(), 50.24)
#
#     def test_get_circumference(self):
#         c = Circle(11)
#         self.assertEqual(c.get_circumference(), 69.08)
#
#
# if __name__ == "__main__":
#     unittest.main()

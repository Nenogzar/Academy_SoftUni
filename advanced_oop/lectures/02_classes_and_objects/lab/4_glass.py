# ******* Lab: Classes and Objects ******* #

# *******  4_glass  ******* #

# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/1936#3
Create a class called Glass.
Upon initialization, it will not receive any parameters.

You must create an instance attribute called content which should be equal to 0.
You should also create a class attribute called capacity which should be 250 ml.


Create 3 instance methods:
-	fill(ml) - fills the glass with the given milliliters if there is enough space in it and returns
        "Glass filled with {ml} ml", otherwise returns "Cannot add {ml} ml"

-	empty() - empties the glass and returns
        "Glass is now empty"

-	info() - returns info about the glass in the format
        "{space_left} ml left"

"""


##########: variant 1 :##########
class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, ml):
        current_content = self.content
        self.content += ml

        if self.content <= Glass.capacity:
            return f"Glass filled with {ml} ml"
        else:
            self.content = current_content
            return f"Cannot add {ml} ml"

    def empty(self):
        self.content = 0
        return f"Glass is now empty"

    def info(self):
        return f"{Glass.capacity - self.content} ml left"





##########: variant 2 :##########

class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, ml):
        if self.content + ml <= self.capacity:
            self.content += ml
            return f"Glass filled with {ml} ml"
        return f"Cannot add {ml} ml"

    def empty(self):
        self.content = 0
        return f"Glass is now empty"

    def info(self):
        return f"{Glass.capacity - self.content} ml left"


##########: TEST CODE :##########

glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())


"""
OUTPUT:

Glass filled with 100 ml
Cannot add 200 ml
Glass is now empty
Glass filled with 200 ml
50 ml left

"""


##########: UNITTEST :##########

import unittest

class Tests(unittest.TestCase):
    def test_init(self):
        glass = Glass()
        self.assertEqual(glass.content, 0)
        self.assertEqual(Glass.capacity, 250)

    def test_fill_successfull(self):
        glass = Glass()
        res = glass.fill(100)
        self.assertEqual(res, "Glass filled with 100 ml")
        self.assertEqual(glass.content, 100)

    def test_fill_unsuccessfull(self):
        glass = Glass()
        res = glass.fill(251)
        self.assertEqual(res, "Cannot add 251 ml")
        self.assertEqual(glass.content, 0)

    def test_empty(self):
        glass = Glass()
        glass.fill(150)
        res = glass.empty()
        self.assertEqual(res, "Glass is now empty")
        self.assertEqual(glass.content, 0)

    def test_info(self):
        glass = Glass()
        glass.fill(50)
        res = glass.info()
        self.assertEqual(res, "200 ml left")
if __name__ == "__main__":
    unittest.main()

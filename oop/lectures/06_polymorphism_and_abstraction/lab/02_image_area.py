# ******* Polymorphism and Abstraction - Lab ******* #

# *******  02_image_area  ******* #

# *******  TASK CONDITION  ******* #
"""
https://judge.softuni.org/Contests/Practice/Index/1942

Create a class called ImageArea which will store the width and the height of an image.
Create a method called get_area() which will return the area of the image.
We have also to implement all the magic methods for the comparison of two image
areas (>, >=, <, <=, ==, !=), which will compare their areas.

for more info:
https://docs.python.org/3/reference/datamodel.html

"""


##########: SOLUTION :##########
class ImageArea:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other, ImageArea):
            return self.get_area() == other.get_area()
        return False

    # def __ne__(self, other):
    #     return not self.__eq__(other)

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    # def __gt__(self, other):
    #     return self.get_area() > other.get_area()
    #
    # def __le__(self, other):
    #     return self.get_area() <= other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

##########: TEST CODE :##########

# 1
a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 == a2)
print(a1 != a3)

# 2
b1 = ImageArea(7, 10)
b2 = ImageArea(35, 2)
b3 = ImageArea(8, 9)
print(b1 != b2)
print(b1 >= b3)

# 3
c1 = ImageArea(7, 10)
c2 = ImageArea(35, 2)
c3 = ImageArea(8, 9)
print(c1 <= c2)
print(c1 < c3)


"""
Output:
True 
True

False
False

True 
True
 """
##########: UNITTEST :##########

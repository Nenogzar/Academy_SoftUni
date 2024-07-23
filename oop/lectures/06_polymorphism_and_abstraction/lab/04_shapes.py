# ******* Polymorphism and Abstraction - Lab ******* #

# *******  04_shapes  ******* #
 
# *******  TASK CONDITION  ******* #
"""
https://judge.softuni.org/Contests/Practice/Index/1942
Create an abstract class Shape with abstract methods:
    calculate_area
    and
    calculate_perimeter.

    Create classes Circle (receives radius upon initialization) and
    Rectangle (receives height and width upon initialization)
        that implement those methods (returning the result).

        The fields of Circle and Rectangle should be private.

Submit all the classes and your imports in the judge system
"""

##########: SOLUTION :##########

class Shape:
    pass

    def calculate_are(self):
        pass

class Circle:
    pass

class Rectangle:
    pass


##########: TEST CODE :##########
# 1

circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter()

# 2

rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())

"""
Output:
#1
78.53981633974483 
31.4159265358979

#2
200 
60
 """
##########: UNITTEST :##########



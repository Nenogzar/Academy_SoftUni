# ******* Class and Static Methods ******* #

# *******  1_calculator  ******* #
 
# *******  TASK CONDITION  ******* #
"""
https://judge.softuni.org/Contests/2430/Static-and-Class-Methods-Lab
Create a class called Calculator that has the following static methods:
•	add(*args) - sums all the arguments passed to the function and returns the result
•	multiply(*args) - multiplies all the numbers and returns the result
•	divide(*args) - divides all the numbers (starting from the first one) and returns the result
•	subtract(*args) - subtracts all the numbers (starting from the first one) and returns the result

"""

##########: SOLUTION :##########

from functools import reduce


class Calculator:
    @staticmethod
    def add(*args):
        return reduce(lambda a, b: a + b, args)

    @staticmethod
    def multiply(*args):
        return reduce(lambda a, b: a * b, args)

    @staticmethod
    def divide(*args):
        return reduce(lambda a, b: a / b, args)

    @staticmethod
    def subtract(*args):
        return reduce(lambda a, b: a - b, args)

##########: TEST CODE :##########
print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))


"""
Output:
19
30
50.0
70

 """
##########: UNITTEST :##########



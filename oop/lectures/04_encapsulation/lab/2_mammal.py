# ******* Lab: Encapsulation ******* #

# *******  2_mammal  ******* #

# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/1938/Encapsulation-Lab

Create a class called Mammal.

Upon initialization, it should receive a name, a type, and a sound.


Create a class attribute called kingdom which should not be accessed outside the class and set it to "animals".


Create three more instance methods:
•	make_sound() - returns a string in the format "{name} makes {sound}"
•	get_kingdom() - returns the private kingdom attribute
•	info() - returns a string in the format "{name} is of type {type}"

"""


##########: SOLUTION :##########

class Mammal:
    __kingdom = "animals"

    def __init__(self, name, type, sound):
        self.name = name
        self.type = type
        self.sound = sound

    def make_sound(self):
        return f"{self.name} makes {self.sound}"

    def get_kingdom(self):
        return Mammal.__kingdom
        # or
        # return self.__kingdom

    def info(self):
        return f"{self.name} is of type {self.type}"


##########: TEST CODE :##########
mammal = Mammal("Dog", "Domestic", "Bark")
print(mammal.make_sound())
print(mammal.get_kingdom())
print(mammal.info())

"""
Output:

Dog makes Bark
animals
Dog is of type Domestic

 """
##########: UNITTEST :##########

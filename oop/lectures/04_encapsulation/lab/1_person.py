# ******* Lab: Encapsulation ******* #

# *******  1_person  ******* #
 
# *******  TASK CONDITION  ******* #
"""
https://judge.softuni.org/Contests/1938/Encapsulation-Lab
Create a class called Person.
Upon initialization, it should receive a name and an age.
Name mangle the name and the age attributes (should not be accessed outside the class).
Create two instance methods called get_name and get_age to return the values of the private attributes.

"""


##########: SOLUTION :##########
class Person:

    def __init__(self, name:str, age:int):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name



    def get_age(self):
        return self.__age


##########: TEST CODE :##########
person = Person("George", 65)
print(person.get_name())
print(person.get_age())



"""
Output:

George
32

 """
##########: UNITTEST :##########



# ******* Inheritance - Exercise ******* #

# *******  01_person  ******* #
 
# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Compete/Index/1941
You are asked to model an application for storing data about people.
You should be able to have a Person and a Child.
Every person receives name and age upon initialization.
Your task is to model the application.
Create a Child class that inherits a Person and has the same constructor definition.
However, do not copy the code from the Person class - reuse the Person class's constructor.
Submit in judge a zip file named project, containing a separate file (person.py and child.py) for each of the classes.

"""

##########: SOLUTION :##########



##########: TEST CODE :##########
from project.person import Person
from project.child import Child


person = Person("Peter", 25)
child = Child("Peter Junior", 5)
print(person.name)
print(person.age)
print(child.name)
print(child.age)
print(f"The father's name is {person.name} hi is a  {person.age} old")
print(f"The child's name is {child.name} hi is a  {child.age} old")
print(f"{person.name} became a father at the age of {person.age - child.age}")

print(child.__class__.__bases__[0].__name__)

"""
Output:

 """
##########: UNITTEST :##########

# zero test

import unittest

class Tests(unittest.TestCase):
   def test(self):
      person = Person("Peter", 25)
      child = Child("Peter Junior", 5)
      self.assertEqual(person.name, "Peter")
      self.assertEqual(person.age, 25)
      self.assertEqual(child.__class__.__bases__[0].__name__, "Person")

if __name__ == "__main__":
   unittest.main()

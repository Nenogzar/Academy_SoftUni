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



"""
Output:

 """
##########: UNITTEST :##########

# zero test
from project.person import Person
from project.child import Child
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

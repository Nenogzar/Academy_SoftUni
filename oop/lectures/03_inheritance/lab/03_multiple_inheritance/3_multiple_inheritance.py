# ******* Inheritance - Lab ******* #

# *******  3_multiple_inheritance  ******* #
 
# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/1940#2
In a folder called project create three files: person.py, employee.py, and teacher.py.

In each file, create its corresponding class - Person, Employee, and Teacher:

•	Person with a single method sleep() that returns: "sleeping..."
•	Employee with a single method get_fired() that returns: "fired..."
•	Teacher with a single method teach() that returns: "teaching...".
Teacher should inherit from Person and Employee.
Submit in Judge a zip file of the folder project.

"""

##########: SOLUTION :##########



##########: TEST CODE :##########



"""
Output:

 """
##########: UNITTEST :##########
# test person
import unittest

from project.employee import Employee
from project.person import Person
from project.teacher import Teacher


class Tests(unittest.TestCase):
    def test_person(self):
        p = Person()
        res = p.sleep()
        self.assertEqual(res, "sleeping...")

    def test_empl(self):
        p = Employee()
        res = p.get_fired()
        self.assertEqual(res, "fired...")

    def test_teacher(self):
        p = Teacher()
        res = p.teach()
        self.assertEqual(res, "teaching...")
        parents = [x.__name__ for x in p.__class__.__bases__]
        self.assertTrue("Person" in parents)
        self.assertTrue("Employee" in parents)


if __name__ == "__main__":
    unittest.main()



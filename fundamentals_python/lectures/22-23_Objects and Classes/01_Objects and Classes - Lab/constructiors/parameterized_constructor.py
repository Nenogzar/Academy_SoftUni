# Parameterized Constructor

# The parameterized constructor, takes one or more arguments along with self.
# It is useful when you want to create an object with custom values for its attributes.
# The parameterized constructor allows us to specify the values of the object’s attributes when the object is created.
from dir_checker import *
class Family:
    members = 10

    def __init__(self, count):
        self.members = count

    def disply(self):
       return f"Number of members is {self.members}"

    def item_content(self):
        return dir(self)

    def item_all_content(self):
        return [item for item in self.item_content()]

    def class_method_names(self):
        return [item for item in self.item_content() if callable(getattr(self, item))]

    def class_attributes(self):
        return [item for item in self.item_content() if not callable(getattr(self, item))]


joy_family = Family(25)
print(joy_family.disply())

print(f"All Atributer and Method is :  {joy_family.item_all_content()}")
print(len(joy_family.item_all_content()))

print(f"The Methods is :  {joy_family.class_method_names()}")
print(len(joy_family.class_method_names()))

print(f"The Atributer is :  {joy_family.class_attributes()}")
print(len(joy_family.class_attributes()))

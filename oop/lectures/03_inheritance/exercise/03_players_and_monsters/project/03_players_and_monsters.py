# ******* Inheritance - Exercise ******* #

# *******  03_players_and_monsters  ******* #

# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Compete/Index/1941
Your task is to create the following game hierarchy

        -           Hero                -
        |           |                   |
       Elf        Wizard             Knight
        |           |                   |
    MuseElf      DarkWizard         DarkKnight
                    |                   |
                SoulMaster          BladeKnight

Create a class Hero. It should contain the following attributes:
•	username: string
•	level: int
Override the __str__() method of the base class so it returns: "{name} of type {class_name} has level {level}"

hero.py
blade_knight.py
dark_knight.py
dark_wizard.py
elf.py
hero.py
knight.py
muse_elf.py
soul_master.py
wizart.py



"""
from    project.elf import Elf
from    project.knight import Knight
from    project.muse_elf import MuseElf
from    project.wizard import Wizard
from    project.dark_knight import DarkKnight
from    project.blade_knight import BladeKnight
from    project.dark_wizard import DarkWizard
from    project.soul_master import SoulMaster
from    project.hero import Hero
##########: SOLUTION :##########

"""
def __str__(self):
   return f"{self.username} of type {self.__class__.__name__} has level {self.level}"
                                       |
OR                                     |
                                       |
on every fail                          |
def __str__(self):                     |
   return f"{self.username} of type {Class Name.__name__} has level {self.level}"

"""
##########: TEST CODE :##########

hero = Hero("Hero", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("Elenko", 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)


"""
Output:

H
4
H of type Hero has level 4
E of type Elf has level 4
Hero
E
4

 """
##########: UNITTEST :##########

# zero test
from project.hero import Hero
from project.elf import Elf
import unittest

class Tests(unittest.TestCase):
   def test(self):
      hero = Hero("H", 4)
      self.assertEqual(hero.username, "H")
      self.assertEqual(hero.level, 4)
      self.assertEqual(str(hero), "H of type Hero has level 4")
      elf = Elf("E", 4)
      self.assertEqual(str(elf), "E of type Elf has level 4")
      self.assertEqual(elf.__class__.__bases__[0].__name__, "Hero")
      self.assertEqual(elf.username, "E")
      self.assertEqual(elf.level, 4)

if __name__ == "__main__":
   unittest.main()
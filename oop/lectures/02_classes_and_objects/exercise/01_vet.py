# ******* Classes and Objects - Exercise ******* #

# *******  01_vet  ******* #

# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Compete/Index/1937#1

Create a class called Vet.
The Vet class represents a veterinary doctor in an animal clinic.
Upon initialization, it should receive a name (string - the name of the vet doctor).
It should also have an instance attribute called animals (empty list by default).

There should also be 2 class attributes:
    animals (empty list) which will store the total amount of animals for all vet doctors;
    and space (5 by default, representing the total capacity of the clinic).

You should create 3 additional instance methods:
    -	register_animal(animal_name)
        o	If there is available space in the vet clinic, add the animal to both animals' lists and return a message:
            "{name} registered in the clinic"
        o	Otherwise, return
            "Not enough space"
    -	unregister_animal(animal_name)
        o	If the animal is in the clinic, remove it from both animals' lists and return
            "{animal} unregistered successfully"
        o	Otherwise, return
            "{animal} not in the clinic"
    -	info()
        o	Return info about the vet doctor, the number of animals on his/her list,
        and the available space left in the clinic:
            "{vet_name} has {number_animals} animals. {space_left_in_clinic} space left in clinic"
Examples


"""

##########: SOLUTION :##########

class Vet:
    animals = []
    space = 5       # representing the total capacity of the clinic

    def __init__(self, doctor:str):
        self.name = doctor     # the name of the vet doctor
        self.animals = []       # empty list by default

    def register_animal(self, animal_name):
        if Vet.space > 0:
            Vet.animals.append(animal_name)
            self.animals.append(animal_name)
            Vet.space -= 1
            return f"{animal_name} registered in the clinic"
        return f"Not enough space"

    def unregister_animal(self, animal_name):
        if animal_name in self.animals and animal_name in Vet.animals:
            Vet.animals.remove(animal_name)
            self.animals.remove(animal_name)
            Vet.space +=1
            return f"{animal_name} unregistered successfully"
        return f"{animal_name} not in the clinic"

    def info(self):
        return f"{self.name} has {len(self.animals)} animals. {Vet.space} space left in clinic"


##########: TEST CODE :##########

peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())


"""
Output: 

Tom registered in the clinic
Cory registered in the clinic
Fishy registered in the clinic
Bobby registered in the clinic
Kay registered in the clinic
Cory unregistered successfully
Silky registered in the clinic
Molly not in the clinic
Tom unregistered successfully
Peter has 3 animals. 1 space left in clinic
George has 1 animals. 1 space left in clinic

"""

##########: UNITTEST :##########

import unittest
#
#
# class Tests(unittest.TestCase):
#     def test_init(self):
#         vet = Vet("Bob")
#         Vet.animals = []
#         Vet.space = 5
#         self.assertEqual(vet.name, "Bob")
#         self.assertEqual(vet.animals, [])
#         self.assertEqual(Vet.animals, [])
#         self.assertEqual(Vet.space, 5)
#
#     def test_register_successfull(self):
#         vet = Vet("Bob")
#         Vet.animals = []
#         Vet.space = 5
#         vet2 = Vet("Peter")
#         res = vet.register_animal("Doggy")
#         self.assertEqual(res, "Doggy registered in the clinic")
#         self.assertEqual(vet.animals, ["Doggy"])
#         self.assertEqual(vet.animals, ["Doggy"])
#         self.assertEqual(vet2.animals, [])
#
#     def test_register_unsuccessfull(self):
#         vet = Vet("Bob")
#         Vet.animals = []
#         Vet.space = 5
#         for i in range(6):
#             vet.register_animal(str(i))
#         res = vet.register_animal("Doggy")
#         self.assertEqual(res, "Not enough space")
#         self.assertEqual(len(Vet.animals), 5)
#         self.assertEqual(len(vet.animals), 5)
#
#     def test_unregister_successfull(self):
#         vet = Vet("Bob")
#         Vet.animals = []
#         Vet.space = 5
#         vet.register_animal("Kitty")
#         res = vet.unregister_animal("Kitty")
#         self.assertEqual(res, "Kitty unregistered successfully")
#         self.assertEqual(vet.animals, [])
#         self.assertEqual(Vet.animals, [])
#
#
# if __name__ == "__main__":
#     unittest.main()

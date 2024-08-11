# ******* Exercise: Encapsulation ******* #

# *******  1_wild_cat_zoo  ******* #
 
# *******  TASK CONDITION  ******* #
"""
https://judge.softuni.org/Contests/1939/Encapsulation-Exercise
Create a separate file for each class as shown below and submit a
zip file containing all files (zip the whole project folder/module)
- it is important to include all files in the project module to make proper imports.

- project
- - 123.py
- - animal
- - caretaker
- - cheetah
- - keeper
- -  lion
- - tiger
- - vet
- - worker
- - zoo

The Animal class is a base class for any type of animal in the zoo.
Upon initialization, it should receive four public attributes:
    a name (string), a gender (str), an age (int), and a money_for_care (int).

The Animal class should also have 1 additional method:
•	__repr__() - returns string representation of the animal in the format: "Name: {name}, Age: {age}, Gender: {gender}"

The Lion, the Tiger, and the Cheetah classes should inherit from the Animal class.
Each of these animals costs a certain amount of money to be cared for:
•	A lion needs 50
•	A tiger needs 45
•	A cheetah needs 60


The Worker class is a base class for any type of employee in the zoo. It should receive three public attributes - a name (string), an age (int), and a salary (int) upon initialization.
The Worker class should also have one method:
•	__repr__() - returns string representation of the workers in the format: "Name: {name}, Age: {age}, Salary: {salary}"
The Keeper, the Caretaker, and the Vet classes should inherit from the Worker class.

The Zoo class should receive 4 attributes upon initialization:
•	Public attribute name: string
•	Private attribute budget: int
•	Private attribute animal_capacity: int
•	Private attribute workers_capacity: int
It should also have 2 instance attributes:
•	Public attribute animals: list - (empty upon initialization)
•	Public attribute workers: list - (empty upon initialization)
The Zoo class should also have 8 methods:
•	add_animal(animal, price)
o	If you have enough budget and capacity add the animal (instance of Lion/Tiger/Cheetah) to the animals' list, reduce the budget, and return "{name} the {type of animal (Lion/Tiger/Cheetah)} added to the zoo"
o	If you have the capacity, but no budget, return "Not enough budget"
o	In any other case, you do not have space, and you should return "Not enough space for animal"
•	hire_worker(worker)
o	If you have not exceeded the capacity of workers in the zoo for the worker (instance of Keeper/Caretaker/Vet), add him to the workers and return "{name} the {type(Keeper/Vet/Caretaker)} hired successfully"
o	Otherwise, return "Not enough space for worker"
•	fire_worker(worker_name)
o	If there is a worker with that name in the workers' list, remove him and return "{worker_name} fired successfully"
o	Otherwise, return "There is no {worker_name} in the zoo"
•	pay_workers()
o	If you have enough budget to pay the workers (sum their salaries) pay them and return "You payed your workers. They are happy. Budget left: {left_budget}"
o	Otherwise, return "You have no budget to pay your workers. They are unhappy"
•	tend_animals()
o	If you have enough budget to take care of the animals, reduce the budget and return "You tended all the animals. They are happy. Budget left: {left_budget}"
o	Otherwise, return "You have no budget to tend the animals. They are unhappy."
•	profit(amount)
o	Increase the budget with the given amount of profit
•	animals_status()
o	Returns the following string (Hint: use the __repr__ methods of the animals to print them on the console):
"You have {total_animals_count} animals
----- {amount_of_lions} Lions:
{lion1}
…
{lionN}
----- {amount_of_tigers} Tigers:
{tiger1}
…
{tigerN}
----- {amount_of_cheetahs} Cheetahs:
{cheetah1}
…
{cheetahN}"
•	workers_status()
o	Returns the following string (Hint: use the __repr__ methods of the workers to print them on the console):
"You have {total_workers_count} workers
----- {amount_of_keepers} Keepers:
{keeper1}
…
{keeperN}
----- {amount_of_caretakers} Caretakers:
{caretaker1}
…
{caretakerN}
----- {amount_of_vetes} Vets:
{vet1}
…
{vetN}"


"""

##########: SOLUTION :##########



##########: TEST CODE :##########

from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.zoo import Zoo


zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())



"""
Output:
Cheeto the Cheetah added to the zoo
Cheetia the Cheetah added to the zoo
Simba the Lion added to the zoo
Zuba the Tiger added to the zoo
Tigeria the Tiger added to the zoo
Not enough space for animal
John the Keeper hired successfully
Adam the Keeper hired successfully
Anna the Keeper hired successfully
Bill the Caretaker hired successfully
Marie the Caretaker hired successfully
Stacy the Caretaker hired successfully
Peter the Vet hired successfully
Kasey the Vet hired successfully
Not enough space for worker
You tended all the animals. They are happy. Budget left: 1779
You payed your workers. They are happy. Budget left: 611
Adam fired successfully
You have 5 animals
----- 1 Lions:
Name: Simba, Age: 4, Gender: Male
----- 2 Tigers:
Name: Zuba, Age: 3, Gender: Male
Name: Tigeria, Age: 1, Gender: Female
----- 2 Cheetahs:
Name: Cheeto, Age: 2, Gender: Male
Name: Cheetia, Age: 1, Gender: Female
You have 7 workers
----- 2 Keepers:
Name: John, Age: 26, Salary: 100
Name: Anna, Age: 31, Salary: 95
----- 3 Caretakers:
Name: Bill, Age: 21, Salary: 68
Name: Marie, Age: 32, Salary: 105
Name: Stacy, Age: 35, Salary: 140
----- 2 Vets:
Name: Peter, Age: 40, Salary: 300
Name: Kasey, Age: 37, Salary: 280

 """
##########: UNITTEST :##########


from project.worker import Worker
from project.animal import Animal
from project.lion import Lion
from project.tiger import Tiger
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.vet import Vet
from project.caretaker import Caretaker
from project.zoo import Zoo

import unittest

class Tests(unittest.TestCase):
    def test_lion_init(self):
      l = Lion("a", "m", 4)
      self.assertEqual(l.name, "a")
      self.assertEqual(l.gender, "m")
      self.assertEqual(l.age, 4)

    def test_lion_get_needs(self):
      l = Lion("b", "f", 2)
      res = l.money_for_care
      self.assertEqual(res, 50)

    def test_lion_repr(self):
      l = Lion("b", "f", 2)
      res = str(l)
      self.assertEqual(res, "Name: b, Age: 2, Gender: f")

    def test_tiger_init(self):
      t = Tiger("z", "m", 1)
      self.assertEqual(t.name, "z")
      self.assertEqual(t.gender, "m")
      self.assertEqual(t.age, 1)

    def test_tiger_get_needs(self):
      t = Tiger("v", "f", 7)
      res = t.money_for_care
      self.assertEqual(res, 45)

    def test_tiger_repr(self):
      t = Tiger("w", "f", 3)
      res = str(t)
      self.assertEqual(res, "Name: w, Age: 3, Gender: f")

    def test_cheetah_init(self):
      c = Cheetah("l", "f", 3)
      self.assertEqual(c.name, "l")
      self.assertEqual(c.gender, "f")
      self.assertEqual(c.age, 3)

    def test_cheetah_get_needs(self):
      c = Cheetah("r", "m", 6)
      res = c.money_for_care
      self.assertEqual(res, 60)

    def test_cheetah_repr(self):
      c = Cheetah("n", "f", 2)
      res = str(c)
      self.assertEqual(res, "Name: n, Age: 2, Gender: f")

    def test_keeper_init(self):
      k = Keeper("john", 21, 200)
      self.assertEqual(k.name, "john")
      self.assertEqual(k.age, 21)
      self.assertEqual(k.salary, 200)

    def test_keeper_repr(self):
      k = Keeper("ally", 36, 190)
      res = str(k)
      self.assertEqual(res, "Name: ally, Age: 36, Salary: 190")

    def test_vet_init(self):
      k = Vet("john", 21, 200)
      self.assertEqual(k.name, "john")
      self.assertEqual(k.age, 21)
      self.assertEqual(k.salary, 200)

    def test_vet_repr(self):
      k = Vet("ally", 36, 190)
      res = str(k)
      self.assertEqual(res, "Name: ally, Age: 36, Salary: 190")

    def test_caretaker_init(self):
      k = Caretaker("john", 21, 200)
      self.assertEqual(k.name, "john")
      self.assertEqual(k.age, 21)
      self.assertEqual(k.salary, 200)

    def test_caretaker_repr(self):
      k = Caretaker("ally", 36, 190)
      res = str(k)
      self.assertEqual(res, "Name: ally, Age: 36, Salary: 190")


    def test_zoo_init(self):
      z = Zoo("My Zoo", 1500, 6, 10)
      self.assertEqual(z._Zoo__animal_capacity, 6)
      self.assertEqual(z._Zoo__workers_capacity, 10)
      self.assertEqual(z._Zoo__budget, 1500)
      self.assertEqual(z.name, "My Zoo")
      self.assertEqual(z.animals, [])
      self.assertEqual(z.workers, [])


    def test_zoo_add_animal_success(self):
      z = Zoo("My Zoo", 1500, 6, 10)
      res = z.add_animal(Lion("Neo", "Male", 2), 1000)
      self.assertEqual(res, "Neo the Lion added to the zoo")
      self.assertEqual(len(z.animals), 1)
      self.assertEqual(z._Zoo__budget, 500)

    def test_zoo_add_animal_no_budget(self):
      z = Zoo("My Zoo", 500, 6, 10)
      res = z.add_animal(Lion("Neo", "Male", 2), 1000)
      self.assertEqual(res, "Not enough budget")
      self.assertEqual(len(z.animals), 0)
      self.assertEqual(z._Zoo__budget, 500)

    def test_zoo_add_animal_no_space(self):
      z = Zoo("My Zoo", 1500, 0, 10)
      res = z.add_animal(Lion("Neo", "Male", 2), 1000)
      self.assertEqual(res, "Not enough space for animal")
      self.assertEqual(len(z.animals), 0)
      self.assertEqual(z._Zoo__budget, 1500)

    def test_zoo_hire_worker_success(self):
      z = Zoo("Some Zoo", 1500, 1, 1)
      res = z.hire_worker(Vet("I am Vet", 20, 500))
      self.assertEqual(res, "I am Vet the Vet hired successfully")
      self.assertEqual(len(z.workers), 1)
      self.assertEqual(z._Zoo__workers_capacity, 1)

    def test_zoo_hire_worker_no_space(self):
      z = Zoo("Some Zoo", 1500, 1, 0)
      res = z.hire_worker(Vet("I am Vet", 20, 500))
      self.assertEqual(res, "Not enough space for worker")
      self.assertEqual(len(z.workers), 0)
      self.assertEqual(z._Zoo__workers_capacity, 0)

    def test_zoo_fire_worker_success(self):
      z = Zoo("Zoo", 1500, 1, 1)
      z.hire_worker(Keeper("K", 45, 100))
      res = z.fire_worker("K")
      self.assertEqual(res, "K fired successfully")
      self.assertEqual(z.workers, [])

    def test_zoo_fire_worker_unsuccessful(self):
      z = Zoo("Zoo", 1500, 1, 1)
      res = z.fire_worker("K")
      self.assertEqual(res, "There is no K in the zoo")
      self.assertEqual(z.workers, [])

    def test_zoo_pay_worker_success(self):
      z = Zoo("Zoo", 1500, 2, 2)
      z.hire_worker(Vet("John", 23, 100))
      z.hire_worker(Keeper("Bill", 28, 150))
      res = z.pay_workers()
      self.assertEqual(z._Zoo__budget, 1250)
      self.assertEqual(res, "You payed your workers. They are happy. Budget left: 1250")

    def test_zoo_pay_worker_no_budget(self):
      z = Zoo("Zoo", 200, 2, 2)
      z.hire_worker(Vet("John", 23, 100))
      z.hire_worker(Keeper("Bill", 28, 150))
      res = z.pay_workers()
      self.assertEqual(res, "You have no budget to pay your workers. They are unhappy")

    def test_zoo_tend_animal_success(self):
      z = Zoo("Zoo", 500, 2, 2)
      z.add_animal(Lion("John", "m", 2), 100)
      z.add_animal(Tiger("Bill", "f", 4), 100)
      res = z.tend_animals()
      self.assertEqual(z._Zoo__budget, 205)
      self.assertEqual(res, "You tended all the animals. They are happy. Budget left: 205")

    def test_zoo_tend_animal_no_budget(self):
      z = Zoo("Zoo", 250, 2, 2)
      z.add_animal(Lion("John", "m", 2), 100)
      z.add_animal(Tiger("Bill", "f", 4), 100)
      res = z.tend_animals()
      self.assertEqual(res, "You have no budget to tend the animals. They are unhappy.")

    def test_zoo_profit(self):
      z = Zoo("Mine", 250, 2, 2)
      z.profit(250)
      self.assertEqual(z._Zoo__budget, 500)

    def test_animal_status(self):
      z = Zoo("My Zoo", 500, 3, 3)
      z.add_animal(Lion("Leo", "Male", 3), 100)
      z.add_animal(Tiger("Tigy", "Female", 4), 100)
      z.add_animal(Cheetah("Chi", "Female", 2), 100)
      res = z.animals_status()
      self.assertEqual(res, "You have 3 animals\n----- 1 Lions:\nName: Leo, Age: 3, Gender: Male\n----- 1 Tigers:\nName: Tigy, Age: 4, Gender: Female\n----- 1 Cheetahs:\nName: Chi, Age: 2, Gender: Female")

    def test_worker_status(self):
      z = Zoo("My Zoo", 500, 3, 3)
      z.hire_worker(Vet("Leo", 35, 100))
      z.hire_worker(Keeper("Tigy", 40, 100))
      z.hire_worker(Caretaker("Chi", 24, 100))
      res = z.workers_status()
      self.assertEqual(res, "You have 3 workers\n----- 1 Keepers:\nName: Tigy, Age: 40, Salary: 100\n----- 1 Caretakers:\nName: Chi, Age: 24, Salary: 100\n----- 1 Vets:\nName: Leo, Age: 35, Salary: 100")

if __name__ == "__main__":
   unittest.main()

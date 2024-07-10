# ******* Lab: Classes and Objects ******* #

# *******  5_smartphone  ******* #

# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/1936#4

Create a class called Smartphone.
Upon initialization, it should receive a memory (number).

It should also have 2 other instance attributes: apps (empty list by default) and is_on (False by default).

Create 3 methods:
-	power() - sets is_on to True if the phone is off, otherwise sets it to False

-	install(app, app_memory)
    o	If there is enough memory on the phone and it is on, install the app
        (add it to apps and decrease the memory of the phone) and
            return "Installing {app}"
    o	If there is enough memory, but the phone is off,
            return "Turn on your phone to install {app}"
    o	Otherwise,
            return "Not enough memory to install {app}"

-	status() -
            return "Total apps: {total_apps_count}. Memory left: {memory_left}"

"""


##########: variant 1 :##########
class Smartphone:

    def __init__(self, memory: int, start=False):
        self.memory = memory
        self.is_on = start
        self.apps = []

    def power(self):
        if not self.is_on:
            self.is_on = True

    def install(self, app, app_memory):
        if self.memory >= app_memory:
            if self.is_on:
                self.memory -= app_memory
                self.apps.append(app)
                return f"Installing {app}"
            else:
                return f"Turn on your phone to install {app}"
        else:
            return f"Not enough memory to install {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"


##########: TEST CODE :##########
smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())




"""
Turn on your phone to install Facebook
Installing Facebook
Installing Messenger
Not enough memory to install Instagram
Total apps: 2. Memory left: 20

"""


##########: INITTEST :##########

# import unittest
#
# class Tests(unittest.TestCase):
#     def test_init(self):
#         phone = Smartphone(50)
#         self.assertEqual(phone.apps, [])
#         self.assertEqual(phone.memory, 50)
#         self.assertEqual(phone.is_on, False)
#
#     def test_power(self):
#         phone = Smartphone(50)
#         self.assertEqual(phone.is_on, False)
#         phone.power()
#         self.assertEqual(phone.is_on, True)
#
#     def test_install_successfull(self):
#         phone = Smartphone(25)
#         phone.power()
#         res = phone.install("Spotify", 10)
#         self.assertEqual(res, "Installing Spotify")
#
#     def test_install_unsuccessfull_not_on(self):
#         phone = Smartphone(25)
#         res = phone.install("Word", 10)
#         self.assertEqual(res, "Turn on your phone to install Word")
#
#     def test_install_unsuccessfull_no_memory(self):
#         phone = Smartphone(25)
#         phone.power()
#         res = phone.install("Excel", 30)
#         self.assertEqual(res, "Not enough memory to install Excel")
#
#     def test_status(self):
#         phone = Smartphone(200)
#         phone.power()
#         phone.install("Powerpoint", 40)
#         res = phone.status()
#         self.assertEqual(res, "Total apps: 1. Memory left: 160")
#
#
# if __name__ == "__main__":
#    unittest.main()

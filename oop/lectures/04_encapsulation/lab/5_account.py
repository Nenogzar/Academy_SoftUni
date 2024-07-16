# ******* Lab: Encapsulation ******* #

# *******  5_account  ******* #

# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/1938/Encapsulation-Lab


Create a class called Account. Upon initialization, it should receive an id, a balance, and a pin (all numbers).
    The pin and the id should be private instance attributes, and the balance should be a public attribute.
    Create two public instance methods:

•   get_id(pin) - if the given pin is correct, return the id, otherwise, return "Wrong pin"

•	change_pin(old_pin, new_pin) - if the old pin is correct, change it to the new one and return
    "Pin changed", otherwise return "Wrong pin"

"""


##########: SOLUTION :##########
class Account:

    def __init__(self, id: int, balance: int, pin: int):
        self.__id = id
        self.balance = balance
        self.__pin = pin

    def get_id(self, pin):
        if pin == self.__pin:
            return self.__id
        return "Wrong pin"

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            return f"Pin changed"
        return "Wrong pin"


##########: TEST CODE :##########
account = Account(8827312, 100, 3421)
print(account.get_id(1111))
print(account.get_id(3421))
print(account.balance)
print(account.change_pin(2212, 4321))
print(account.change_pin(3421, 1234))

"""

Output:
Wrong pin
8827312
100
Wrong pin
Pin changed

 """
##########: UNITTEST :##########
import unittest


class Tests(unittest.TestCase):
    def test_init(self):
        a = Account(1234, 44, 4444)
        self.assertEqual(a._Account__id, 1234)
        self.assertEqual(a.balance, 44)
        self.assertEqual(a._Account__pin, 4444)

    def test_get_id_unsuccessfull(self):
        a = Account(1234, 44, 4444)
        res = a.get_id(1234)
        self.assertEqual(res, "Wrong pin")

    def test_get_id_successfull(self):
        a = Account(1234, 44, 4444)
        res = a.get_id(4444)
        self.assertEqual(res, 1234)

    def test_get_balance(self):
        a = Account(1234, 44, 4444)
        res = a.balance
        self.assertEqual(res, 44)

    def test_change_pin_successfull(self):
        a = Account(1234, 44, 4444)
        res = a.change_pin(4444, 1234)
        self.assertEqual(res, "Pin changed")
        self.assertEqual(a._Account__pin, 1234)


if __name__ == "__main__":
    unittest.main()

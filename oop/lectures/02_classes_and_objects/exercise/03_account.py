# ******* Classes and Objects - Exercise ******* #

# *******  03_account  ******* #

# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Compete/Index/1937#2
Create a class called Account.
Upon initialization, it should receive an id (number), a name (string), and a balance (integer; optional; 0 by default).


The class should also have 3 additional instance methods:
-	credit(amount) - adds the amount to the balance and returns the new balance

-	debit(amount) - if the amount is less than or equal to the balance,
    reduce the balance by the amount and return the new balance. Otherwise, return
        "Amount exceeded balance"

-	info() - returns "User {name} with account {id} has {balance} balance"

"""


##########: SOLUTION :##########
class Account:
    def __init__(self, _id: int, user_name:str, balance = 0):
        self.id = _id
        self.name = user_name
        self.balance = balance

    def credit(self, amount):
        self.balance += amount
        return self.balance

    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        return f"Amount exceeded balance"

    def info(self):
        return f"User {self.name} with account {self.id} has {self.balance} balance"


##########: TEST CODE :##########



account = Account(1234, "George", 1000)
print(account.credit(500))
print(account.debit(1500))
print(account.info())

"""
Outout:

1500
0
User George with account 1234 has 0 balance

"""

account = Account(5411256, "Peter")
print(account.debit(500))
print(account.credit(1000))
print(account.debit(500))
print(account.info())

"""
Outout:

Amount exceeded balance
1000
500
User Peter with account 5411256 has 500 balance


"""

##########: UNITTEST :##########
import unittest


class Tests(unittest.TestCase):
    def test_init_with_balance(self):
        a = Account(1, "A", 10)
        self.assertEqual(a.id, 1)
        self.assertEqual(a.name, "A")
        self.assertEqual(a.balance, 10)

    def test_init_without_balance(self):
        a = Account(1, "A")
        self.assertEqual(a.id, 1)
        self.assertEqual(a.name, "A")
        self.assertEqual(a.balance, 0)

    def test_credit(self):
        a = Account(123, "B", 10)
        res = a.credit(10)
        self.assertEqual(res, 20)
        self.assertEqual(a.balance, 20)

    def test_debit_successfull(self):
        a = Account(333444, "X", 1000)
        res = a.debit(999)
        self.assertEqual(res, 1)
        self.assertEqual(a.balance, 1)

    def test_debit_unsuccessfull(self):
        a = Account(5555, "N", 500)
        res = a.debit(1000)
        self.assertEqual(res, "Amount exceeded balance")
        self.assertEqual(a.balance, 500)

    def test_info(self):
        a = Account(4321, "ABC", 400)
        res = a.info()
        self.assertEqual(res, "User ABC with account 4321 has 400 balance")


if __name__ == "__main__":
    unittest.main()
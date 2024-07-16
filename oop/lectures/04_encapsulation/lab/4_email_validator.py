# ******* Lab: Encapsulation ******* #

# *******  4_email_validator  ******* #

# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/1938/Encapsulation-Lab
Create a class called EmailValidator. Upon initialization, it should receive:
    •	min_length (of the username; example:  in "peter@gmail.com" "peter" is the username)
    •	mails (list of the valid mails; example: "gmail", "abv")
    •	domains (list of valid domains; example: "com", "net")

Create three methods that should not be accessed outside the class:
        •	is_name_valid(name) -
            returns whether the name is greater than or equal to the min_length (True/False)
        •	is_mail_valid(mail) -
            returns whether the mail is in the possible mails list (True/False)
        •	is_domain_valid(domain) -
            returns whether the domain is in the possible domains list (True/False)

Create one public method:
•	validate(email) - using the three methods returns whether the email is valid (True/False)

"""
from typing import List


##########: SOLUTION :##########
class EmailValidator:

    def __init__(self, min_length: int, mails: List[str], domains: List[str]):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail:str):
        return mail in self.mails

    def __is_domain_valid(self, domain):
        return domain in self.domains

    def validate(self, email):
        name, main_data = email.split("@")
        mail, domain = main_data.split(".")
        return self.__is_name_valid(name) and self.__is_mail_valid(mail) and self.__is_domain_valid(domain)

##########: TEST CODE :##########

mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))

"""
Output:
True
False
False
False

 """
##########: UNITTEST :##########


import unittest


class Tests(unittest.TestCase):
    def test_init(self):
        ev = EmailValidator(5, ["me"], ["you", "he"])
        self.assertEqual(ev.min_length, 5)
        self.assertEqual(ev.mails, ["me"])
        self.assertEqual(ev.domains, ["you", "he"])

    def test_private_validate_name(self):
        ev = EmailValidator(5, ["me"], ["you", "he"])
        self.assertEqual(ev._EmailValidator__is_name_valid("abc"), False)
        self.assertEqual(ev._EmailValidator__is_name_valid("abcdef"), True)

    def test_private_validate_mail(self):
        ev = EmailValidator(5, ["me"], ["you", "he"])
        self.assertEqual(ev._EmailValidator__is_mail_valid("me"), True)
        self.assertEqual(ev._EmailValidator__is_mail_valid("you"), False)

    def test_private_validate_domain(self):
        ev = EmailValidator(5, ["me"], ["you", "he"])
        self.assertEqual(ev._EmailValidator__is_domain_valid("he"), True)
        self.assertEqual(ev._EmailValidator__is_domain_valid("she"), False)

    def test_validate(self):
        ev = EmailValidator(5, ["me"], ["you", "he"])
        self.assertEqual(ev.validate("itsme@me.you"), True)
        self.assertEqual(ev.validate("me@me.you"), False)
        self.assertEqual(ev.validate("itsme@me.she"), False)
        self.assertEqual(ev.validate("itsme@you.he"), False)


if __name__ == "__main__":
    unittest.main()

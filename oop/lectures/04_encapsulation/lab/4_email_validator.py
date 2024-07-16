# ******* Lab: Encapsulation ******* #

# *******  4_email_validator  ******* #
 
# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/1938/Encapsulation-Lab
Create a class called EmailValidator. Upon initialization, it should receive:
    •	min_length (of the username; example:
        in "peter@gmail.com" "peter" is the username)
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

##########: SOLUTION :##########



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



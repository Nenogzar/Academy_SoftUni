# ******* First Steps in OOP - Exercise ******* #

# *******  03_employee  ******* #

# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Compete/Index/1935


Create class Employee. Upon initialization,
it should receive id (number), first_name (string), last_name (string), and salary (number).

Create 3 additional instance methods:
-	get_full_name() - returns "{first_name} {last_name}"
-	get_annual_salary() - returns the total salary for 12 months
-	raise_salary(amount) - increases the salary by the given amount and returns the new salary
Examples


Test Code:

employee = Employee(744423129, "John", "Smith", 1000)
print(employee.get_full_name())
print(employee.raise_salary(500))
print(employee.get_annual_salary())

Output:

John Smith
1500
18000


"""


##########: variant 1 :##########

class Employee:
    def __init__(self, _id: str, first_name: str, last_name: str, salary: str):
        self.id = _id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_annual_salary(self):
        total_salary = self.salary * 12
        return total_salary

    def raise_salary(self, amount):
        self.salary += amount
        return self.salary

##########: variant 2 :##########


##########: variant 3 solution SoftUni :##########

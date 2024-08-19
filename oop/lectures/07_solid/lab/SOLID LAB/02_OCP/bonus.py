class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return self.salary * 0.1

class Manager(Employee):
    def calculate_bonus(self):
        return self.salary * 0.2



employee = Employee("John Doe", 50000)
manager = Manager("Jane Smith", 80000)

print(employee.salary, "- employee salary")

print(manager.salary, "- manager salary")

print(manager.calculate_bonus(), "- manager bonus")
print(employee.calculate_bonus(), "- employee bonus")

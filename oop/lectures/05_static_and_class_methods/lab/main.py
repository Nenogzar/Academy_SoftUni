class Person:

    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name

    @staticmethod
    def is_adult(age):
        return age >= 18

person = Person("Name")
print(person.name)
person.change_name("New name")
print(person.name)
print(person.is_adult(20))
print(person.is_adult(17))
print(f"Is {person.name} have a valid age ")

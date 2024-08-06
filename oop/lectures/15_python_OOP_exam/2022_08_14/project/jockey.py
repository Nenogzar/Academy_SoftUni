from project.validation.validation import Validation

class Jockey:
    MIN_AGE = 18
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.horse = None   # one jockey can ride only one horse


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validation.valid_empty_str_or_white_space(value, "Name should contain at least one character!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Validation.valid_age(value, self.MIN_AGE, f"Jockeys must be at least {self.MIN_AGE} to participate in the race!")
        self.__age = value
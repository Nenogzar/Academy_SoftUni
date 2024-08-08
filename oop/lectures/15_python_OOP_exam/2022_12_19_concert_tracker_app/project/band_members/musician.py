from abc import ABC, abstractmethod

from project.validation.validation import Validation


class Musician(ABC):
    valid_age = 16
    def __init__(self,name: str, age: int):
        self.name = name
        self.age = age
        self.skills = []    # contain all skills a musician has


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validation.valid_str_or_white_space(value, 1, "Musician name cannot be empty!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Validation.valid_number(value,self.valid_age,"Musicians should be at least 16 years old!")
        self.__age = value

    @abstractmethod
    def learn_new_skill(self, new_skill: str):
        pass

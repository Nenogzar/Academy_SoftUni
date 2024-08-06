from abc import ABC, abstractmethod

from project.user import User
from project.validation.validation import Validation


class Movie(ABC):

    def __init__(self,title: str, year: int, owner: object, age_restriction: int):
        self.title = title
        self.year = year
        self.owner = owner
        self.age_restriction = age_restriction
        self.likes = 0


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        Validation.valid_empty_str(value,"The title cannot be empty string!")
        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        Validation.valid_number(value,1888,"Movies weren't made before 1888!")
        self.__year = value

    
    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        Validation.movie_owner(value)
        self.__owner = value


    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        Validation.valid_number(value, self._restrict_age, self._message)  #  todo
        self.__age_restriction = value

    @abstractmethod
    def details(self):
        pass

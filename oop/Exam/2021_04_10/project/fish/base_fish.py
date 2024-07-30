from abc import ABC, abstractmethod


class BaseFish(ABC):
    INCREASES_SIZE = 5
    @abstractmethod
    def __init__(self, name: str, species: str, size: int, price: float):
        self.name = name
        self.species = species
        self.size = size
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        """Ако name е празен низ, хвърля ValueError"""
        if not value:
            raise ValueError("Fish name cannot be an empty string.")
        self.__name = value

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value: str):
        """Ако type е празен низ, хвърля ValueError"""
        if not value:
            raise ValueError("Fish species cannot be an empty string.")
        self.__species = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: float):
        """Ако цената е равна или под 0, хвърля ValueError"""
        if value <= 0:
            raise ValueError("Price cannot be equal to or below zero.")
        self.__price = value

    @abstractmethod
    def eat(self):
        pass

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_species(self):
        pass


class Dog(Animal):
    def get_species(self):
        return "woof-woof"


class Cat(Animal):
    def get_species(self):
        return "meaw"


class Pig(Animal):
    def get_species(self):
        return "gruh gruh"


class Turtle(Animal):
    def get_species(self):
        return "turtle sound"


def animal_sound(animals: list):
    for animal in animals:
        print(animal.get_species())


animals = [Cat("Tom"), Dog("Bob"), Turtle("Toni"), Pig("Leonardo")]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]

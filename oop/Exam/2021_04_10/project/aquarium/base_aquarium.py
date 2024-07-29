from abc import ABC, abstractmethod
from typing import List
from project.decoration.base_decoration import BaseDecoration
from project.fish.base_fish import BaseFish

class BaseAquarium(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity  # Represents the number of fish an aquarium can have.
        self.decorations: List[BaseDecoration] = []  # List of decoration objects.
        self.fish: List[BaseFish] = []  # List of fish objects.

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        """If name is an empty string, raise a ValueError"""
        if not value:
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self) -> int:
        """Returns the sum of each decoration’s comfort in the Aquarium."""
        return sum(decoration.comfort for decoration in self.decorations)

    def add_fish(self, fish: BaseFish) -> str:
        """
        Adds a fish object in the Aquarium and returns a message:
            "Not enough capacity." - if there is not enough capacity to add the fish
            "Successfully added {fish_type} to {aquarium_name}." - if the fish is added successfully
            Possible fish types are: "FreshwaterFish" and "SaltwaterFish".
        """
        if len(self.fish) >= self.capacity:
            return "Not enough capacity."

        self.fish.append(fish)
        return f"Successfully added {type(fish).__name__} to {self.name}."

    def remove_fish(self, fish: BaseFish):
        """Removes a fish object from the Aquarium."""
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration: BaseDecoration):
        """Adds a decoration object in the Aquarium."""
        self.decorations.append(decoration)

    def feed(self):
        """The feed() method feeds all fish in the aquarium."""
        for fish in self.fish:
            fish.eat()

    def __str__(self) -> str:
        """
        Returns a String with information about the Aquarium in the following format:
        If the Aquarium does not have fish,
            replace the fish names with the word "none" instead.
        :return: String with aquarium details.
        """
        fish_names = " ".join(fish.name for fish in self.fish) if self.fish else "none"
        return (f"{self.name}:\n"
                f"Fish: {fish_names}\n"
                f"Decorations: {len(self.decorations)}\n"
                f"Comfort: {self.calculate_comfort()}")

    @abstractmethod
    def some_abstract_method(self):
        pass

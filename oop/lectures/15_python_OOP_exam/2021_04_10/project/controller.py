from typing import List, Type
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.aquarium.base_aquarium import BaseAquarium
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums: List[BaseAquarium] = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        aquarium_mapping = {
            "FreshwaterAquarium": FreshwaterAquarium,
            "SaltwaterAquarium": SaltwaterAquarium
        }

        if aquarium_type in aquarium_mapping:

            aquarium_class = aquarium_mapping[aquarium_type]
            aquarium = aquarium_class(aquarium_name)
            self.aquariums.append(aquarium)
            return f"Successfully added {aquarium_type}."
        else:
            return "Invalid aquarium type."

    def add_decoration(self, decoration_type: str):
        decoration_mapping = {
            "Ornament": Ornament,
            "Plant": Plant
        }

        if decoration_type in decoration_mapping:
            decoration_class = decoration_mapping[decoration_type]
            decoration = decoration_class()
            self.decorations_repository.add(decoration)
            return f"Successfully added {decoration_type}."
        else:
            return "Invalid decoration type."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium = next((a for a in self.aquariums if a.name == aquarium_name), None)
        decoration = next((d for d in self.decorations_repository.decorations if type(d).__name__ == decoration_type),
                          None)

        if decoration == "None":
            return f"There isn't a decoration of type {decoration_type}."

        if aquarium:
            aquarium.add_decoration(decoration)
            self.decorations_repository.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        valid_types = {
            "FreshwaterFish": FreshwaterFish,
            "SaltwaterFish": SaltwaterFish
        }

        # Проверка дали типът на рибата е валиден
        if fish_type not in valid_types:
            return f"There isn't a fish of type {fish_type}."

        aquarium = next(a for a in self.aquariums if a.name == aquarium_name)

        # Проверка дали аквариумът е пълен
        if len(aquarium.fish) >= aquarium.capacity:
            return "Not enough capacity."

        # Проверка дали водата е подходяща за рибата
        if (fish_type == "SaltwaterFish" and aquarium.__class__.__name__ == "FreshwaterAquarium") or \
           (fish_type == "FreshwaterFish" and aquarium.__class__.__name__ == "SaltwaterAquarium"):
            return "Water not suitable."

        # Създаване на рибата и добавяне в аквариума
        create_fish = valid_types[fish_type](fish_name, fish_species, price)
        aquarium.add_fish(create_fish)

        return f"Successfully added {fish_type} to {aquarium_name}."


    def feed_fish(self, aquarium_name: str):
        aquarium = next((a for a in self.aquariums if a.name == aquarium_name), None)

        if aquarium:
            for fish in aquarium.fish:
                fish.eat()

            return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str) -> str:
        aquarium = next((a for a in self.aquariums if a.name == aquarium_name), None)

        if aquarium:
            fish_price = sum(fish.price for fish in aquarium.fish)
            decoration_price = sum(decor.price for decor in aquarium.decorations)
            total_value = fish_price + decoration_price
            return f"The value of Aquarium {aquarium_name} is {total_value:.2f}."


    def report(self) -> str:
        result = []
        for aquarium in self.aquariums:
            result.append(str(aquarium))
        return '\n'.join(result)


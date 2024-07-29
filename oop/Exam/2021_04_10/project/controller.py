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
        self.decorations_repository = DecorationRepository()  # Инициализиране на нова репота за декорации
        self.aquariums: List[BaseAquarium] = []  # Списък за съхранение на всички аквариуми

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
        if not decoration:
            return f"There isn't a decoration of type {decoration_type}."

        aquarium.add_decoration(decoration)
        self.decorations_repository.remove(decoration)
        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        aquarium = next((a for a in self.aquariums if a.name == aquarium_name), None)
        fish_mapping = {
            "FreshwaterFish": FreshwaterFish,
            "SaltwaterFish": SaltwaterFish
        }

        if fish_type in fish_mapping:
            fish_class = fish_mapping[fish_type]
            fish = fish_class(fish_name, fish_species, price)
        else:
            return f"There isn't a fish of type {fish_type}."

        # Проверете капацитета
        if len(aquarium.fish) >= aquarium.capacity:
            return "Not enough capacity."

        # Проверете дали аквариума е от правилния тип
        if isinstance(aquarium, FreshwaterAquarium) and fish_type == "SaltwaterFish":
            return "Water not suitable."
        if isinstance(aquarium, SaltwaterAquarium) and fish_type == "FreshwaterFish":
            return "Water not suitable."

        # Добавям рибата
        result = aquarium.add_fish(fish)
        return f"Successfully added {fish_type} to {aquarium_name}." if result == f"Successfully added {fish_type} to {aquarium_name}." else result

    def feed_fish(self, aquarium_name: str):
        aquarium = next((a for a in self.aquariums if a.name == aquarium_name), None)

        fed_count = 0
        for fish in aquarium.fish:
            fish.eat()
            fed_count += 1

        return f"Fish fed: {fed_count}"

    def calculate_value(self, aquarium_name: str) -> str:
        aquarium = next((a for a in self.aquariums if a.name == aquarium_name), None)
        fish_price = sum(fish.price for fish in aquarium.fish)
        decoration_price = sum(decoration.price for decoration in aquarium.decorations)
        total_value = fish_price + decoration_price

        # Форматирайте стойността до 2 десетични знака
        return f"The value of Aquarium {aquarium_name} is {total_value:.2f}."


    def report(self) -> str:
        result = []
        for aquarium in self.aquariums:
            result.append(str(aquarium))
        return '\n'.join(result)


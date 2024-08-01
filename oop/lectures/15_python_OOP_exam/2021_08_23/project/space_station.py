from project.Validation.validation import Validate
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet_repository import PlanetRepository
from project.astronaut.astronaut_repository import AstronautRepository
from project.planet.planet import Planet


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful = 0
        self.not_successful = 0

    @property
    def type_astronaut_maper(self):
        return {"Biologist": Biologist,
                "Geodesist": Geodesist,
                "Meteorologist": Meteorologist}

    def add_astronaut(self, astronaut_type: str, name: str):
        if any(name == a.name for a in self.astronaut_repository.astronauts):
            return f"{name} is already added."

        Validate.space_station_astronaut_types(astronaut_type)

        new_astro = self.type_astronaut_maper[astronaut_type](name)
        self.astronaut_repository.add(new_astro)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        new_planet = Planet(name)
        new_planet.items += items.split(", ")
        self.planet_repository.add(new_planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        old_astro = self.astronaut_repository.find_by_name(name)
        if not old_astro:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(old_astro)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astro in self.astronaut_repository.astronauts:
            astro.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if not planet:
            raise Exception("Invalid planet name!")

        best_equip = [a for a in self.astronaut_repository.astronauts if a.oxygen >= 30]

        if len(best_equip) == 0:
            raise Exception("You need at least one astronaut to explore the planet!")

        five_astronaut = sorted(best_equip, key=lambda a: -a.oxygen)[:5]
        for astro in five_astronaut:
            while astro.oxygen > 0 and planet.items:
                astro.backpack.append(planet.items.pop())
                astro.breathe()

        if planet.items:
            self.not_successful += 1
            return "Mission is not completed."

        self.successful += 1
        return f"Planet: {planet_name} was explored. {len([a for a in five_astronaut if a.backpack])} astronauts participated in collecting items."


    def report(self):
        output = [f"{self.successful} successful missions!",
                  f"{self.not_successful} missions were not completed!",
                  "Astronauts' info:",
                  ]

        for astro in self.astronaut_repository.astronauts:
            output.append(f"Name: {astro.name}")
            output.append(f"Oxygen: {astro.oxygen}")

            if astro.backpack:
                output.append(f"Backpack items: {', '.join(astro.backpack)}")
            elif not astro.backpack:
                output.append(f"Backpack items: none")

        return '\n'.join(output)

from project.Validation.validation import Validate
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet_repository import PlanetRepository
from project.astronaut.astronaut_repository import AstronautRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

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
        pass

    def retire_astronaut(self, name: str):
        pass

    def recharge_oxygen(self):
        pass

    def send_on_mission(self, planet_name: str):
        pass

    def report(self):
        pass

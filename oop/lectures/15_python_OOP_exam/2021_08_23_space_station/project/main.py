from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.astronaut.astronaut_repository import *
from project.planet.planet import Planet
from project.space_station import SpaceStation

# try:
#     ast = Meteorologist("Ivan")
# except ValueError as e:
#     print(e)
#
# astro = Meteorologist("Mars")
# print(astro.oxygen)
#
# astro.increase_oxygen(10)
# print(astro.oxygen)
#
# astro.breathe()
# print(astro.oxygen)
#
# astro.increase_oxygen(5)
# print(astro.oxygen)
# astro.breathe()
#
# astro.breathe()
# print(astro.oxygen)
#
#
# try:
#     planet = Planet("Mars")
#     print(planet.name)
# except ValueError as e:
#     print(e)

try:
    print("---------------------------------")
    print("add_planet")

    app = SpaceStation()
    print(app.add_astronaut("Biologist", "Ivan"))
    print(app.add_astronaut("Geodesist", "Dragan"))
    print(app.add_astronaut("Meteorologist", "Zoro"))
    print(f"Number of Astronaut is:{len(app.astronaut_repository.astronauts)}")

    print("---------------------------------")
    print("add_planet")
    print(app.add_planet("Mars", "Kirka"))
    print(app.add_planet("Mars", "Lopata"))
    print(f"Number of Planets is:{len(app.planet_repository.planets)}")

    print("---------------------------------")
    print("retire_astronaut")
    print(app.retire_astronaut("Zoro"))
    print(f"Number of Astronaut is:{len(app.astronaut_repository.astronauts)}")
    print("---------------------------------")
    print("recharge_oxygen")

    print(app.recharge_oxygen())



except ValueError as e:
    print(e)


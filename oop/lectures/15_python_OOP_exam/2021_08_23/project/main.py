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


app = SpaceStation()
print(app.add_astronaut("Biologist", "Ivan"))
print(app.add_astronaut("Biologist", "Ivan"))
print(app.astronaut_repository.astronauts)



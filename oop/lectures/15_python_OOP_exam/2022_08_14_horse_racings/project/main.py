from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey

# try:
#     j = Jockey("Koko", 18)
# except ValueError as e:
#     print(e)
#
# print("-----------------")
# print("Appaloosa")
# try:
#     h = Appaloosa("Runo", 100)
#     print(h.MAX_SPEED, "MAX SPEED")
#     print(h.speed)
#     h.train()
#     print(f"Speed after training: {h.speed}")
# except ValueError as e:
#     print(e)
# print("-----------------")
# print("Thoroughbred")
# try:
#     h = Thoroughbred("Runo", 140)
#     print(h.MAX_SPEED, "MAX SPEED")
#     print(h.speed)
#     h.train()
#     print(f"Speed after training: {h.speed}")
# except ValueError as e:
#     print(e)


from project.horse_race_app import HorseRaceApp

horseRaceApp = HorseRaceApp()
print(horseRaceApp.add_horse("Appaloosa", "Spirit", 80))
print(horseRaceApp.add_horse("Thoroughbred", "Rocket", 110))
print(horseRaceApp.add_jockey("Peter", 19))
print(horseRaceApp.add_jockey("Mariya", 21))
print(horseRaceApp.create_horse_race("Summer"))
print(horseRaceApp.add_horse_to_jockey("Peter", "Appaloosa"))
print(horseRaceApp.add_horse_to_jockey("Peter", "Thoroughbred"))
print(horseRaceApp.add_horse_to_jockey("Mariya", "Thoroughbred"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Peter"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
print(horseRaceApp.start_horse_race("Summer"))

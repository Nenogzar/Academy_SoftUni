from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert
from project.concert_tracker_app import ConcertTrackerApp

# print("Class - Singer")
# print("****************")
# try:
#     s = Singer("Alisa", 16)
#     print(s.skills)
#     print(s.posible_skills)
#     print(s.learn_new_skill("sing low pitch notes"))
#     print(s.skills)
#     print(s.learn_new_skill("dranka"))
#     print(s.skills)
#
# except ValueError as e:
#     print(e)
# except Exception as a:
#     print(a)
#
# print("---------------")
# print("Class - Drummer")
# print("****************")
# try:
#     s = Drummer("Vasko", 16)
#     print(s.skills)
#     print(s.posible_skills)
#     print(s.learn_new_skill("read sheet music"))
#     print(s.skills)
#     print(s.learn_new_skill("play the drums with drum brushes"))
#     print(s.skills)
#     print(s.learn_new_skill("dranka"))
#     print(s.skills)
# except ValueError as e:
#     print(e)
# except Exception as a:
#     print(a)
#
# print("---------------")
# print("Class - Guitarist")
# print("****************")
# try:
#     s = Guitarist("Slash", 16)
#     print(s.skills)
#     print(s.posible_skills)
#     print(s.learn_new_skill("play rock"))
#     print(s.skills)
#     print(s.learn_new_skill("play metal"))
#     print(s.skills)
#     print(s.learn_new_skill("dranka"))
#     print(s.skills)
# except ValueError as e:
#     print(e)
# except Exception as a:
#     print(a)
#
# print("---------------")
# print("class - Concert")
# print("****************")
#
# try:
#     c = Concert("Rock", 4, 5, 6, "Arena")
#     print(str(c))
# except ValueError as c:
#     print(c)
#
#
# print("---------------")
# print("class - Concert")
# print("****************")
#
# try:
#     m = ConcertTrackerApp()
#
#     print(m.create_musician("Guitarist", "Slash", 25))
#     print(m.create_musician("Drummer", "Bombata", 25))
#     print(m.create_musician("Singer", "Axell", 35))
#     print(m.musicians, "List Musicians")
#     print("---------------")
#     print(m.create_band("Guns 'n Rosses"))
#     print(m.create_band("Metalica"))
#     print(m.bands, "List Bands")
#     print("---------------")
#     print(m.create_concert("Metal", 2000, 25.5, 10000, "Arena Sofia"))
#     print(m.create_concert("Rock", 1500, 25.0, 9000, "Arena Burgas"))
#     print(m.create_concert("Jazz", 680, 15.0, 3500, "Arena Sozopol"))
#     print("---------------")
#     print(m.add_musician_to_band("Axell","Guns 'n Rosses"))
#     print(m.add_musician_to_band("Bombata","Guns 'n Rosses"))
#     print(m.add_musician_to_band("Slash","Guns 'n Rosses"))
#     print(m.remove_musician_from_band("Bombata","Guns 'n Rosses"))
#     print("---------------")
#
#
#
# except ValueError as a:
#     print(a)
# except Exception  as b:
#     print(b)


from project.concert_tracker_app import ConcertTrackerApp

musician_types = ["Singer", "Drummer", "Guitarist"]
names = ["George", "Alex", "Lilly"]

app = ConcertTrackerApp()

for i in range(3):
    print(app.create_musician(musician_types[i], names[i], 20))

print(app.musicians[0].learn_new_skill("sing high pitch notes"))
print(app.musicians[1].learn_new_skill("play the drums with drumsticks"))
print(app.musicians[2].learn_new_skill("play rock"))

print(app.create_band("RockName"))
for i in range(3):
    print(app.add_musician_to_band(names[i], "RockName"))

print(app.create_concert("Rock", 20, 5.20, 56.7, "Sofia"))

print(list(map(lambda a: a.__class__.__name__, app.bands[0].members)))
print(app.start_concert("Sofia", "RockName"))

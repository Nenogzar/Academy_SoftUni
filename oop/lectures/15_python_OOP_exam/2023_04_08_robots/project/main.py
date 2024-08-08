from project.robots.male_robot import MaleRobot
from project.robots.female_robot import FemaleRobot
from project.robots_managing_app import RobotsManagingApp
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService

# print("***************")
# print("class MaleRobot")
# try:
#     rm = MaleRobot("R2D2", "Stone", 125.5)
#     print(rm.weight_gain, "- weight_gain" )
#     print(rm.weight, "Weight")
#     rm.eating()
#     print(rm.weight, "Weight")
#
# except ValueError as r:
#     print(r)
#
#
# print("***************")
# print("class FemaleRobot")
# try:
#     rm = FemaleRobot("R4F2", "Flay", 258.80)
#     print(rm.weight_gain, "- weight_gain" )
#     print(rm.weight, "Weight")
#     rm.eating()
#     print(rm.weight, "Weight")
#
#
# except ValueError as r:
#     print(r)
#
#
# print("***************")
# print("class MainService")
# try:
#     s = MainService("Service 1")
#     print(s.details())
#     print(s.capacity)
#
# except ValueError as r:
#     print(r)
#
# print("***************")
# print("class SecondaryService")
# try:
#     s = SecondaryService("Service 2")
#     print(s.details())
#     print(s.capacity)
#
# except ValueError as r:
#     print(r)
#
# print("***************")
# print("class RobotsManagingApp")

# try:
#     cl = RobotsManagingApp()
#     cl.add_service("SecondaryService", "Service 1")
#     cl.add_service("MainService", "Service 2")
#     print(len(cl.services))
#     cl.add_robot("FemaleRobot","R4F2", "Flay", 258.80)
#     cl.add_robot("MaleRobot","R2D2", "Stone", 125.5)
#     print(len(cl.robots))
# except ValueError as c:
#     print(c)
# except Exception as l:
#     print(l)

main_app = RobotsManagingApp()
print(main_app.add_service('SecondaryService', 'ServiceRobotsWorld'))
print(main_app.add_service('MainService', 'ServiceTechnicalsWorld'))
print(main_app.add_robot('FemaleRobot', 'Scrap', 'HouseholdRobots', 321.26))
print(main_app.add_robot('FemaleRobot', 'Sparkle', 'FunnyRobots', 211.11))

print(main_app.add_robot_to_service('Scrap', 'ServiceRobotsWorld'))
print(main_app.add_robot_to_service('Sparkle', 'ServiceRobotsWorld'))

print(main_app.feed_all_robots_from_service('ServiceRobotsWorld'))
print(main_app.feed_all_robots_from_service('ServiceTechnicalsWorld'))

print(main_app.service_price('ServiceRobotsWorld'))
print(main_app.service_price('ServiceTechnicalsWorld'))

print(str(main_app))

print(main_app.remove_robot_from_service('Scrap', 'ServiceRobotsWorld'))
print(main_app.service_price('ServiceRobotsWorld'))
print(main_app.service_price('ServiceTechnicalsWorld'))

print(str(main_app))

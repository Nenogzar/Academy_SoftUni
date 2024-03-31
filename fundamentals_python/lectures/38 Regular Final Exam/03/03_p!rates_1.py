
""" Time: 0.080 s """

# info_city = input()
# city_dict = {}
#
# while info_city != 'Sail':
#     city, population, gold = info_city.split("||")
#     city_info = city_dict.get(city)
#     if city_info:
#         city_info['population'] += int(population)
#         city_info['gold'] += int(gold)
#     else:
#         city_dict[city] = {
#             'population': int(population),
#             'gold': int(gold)
#         }
#     info_city = input()
#
# event = input()
# while event != "End":
#     split_event = event.split("=>")
#     action, city = split_event[0], split_event[1]
#
#     if action == "Plunder":
#         people, stolen_gold = int(split_event[2]), int(split_event[3])
#         if city in city_dict:
#             city_dict[city]['population'] -= people
#             city_dict[city]['gold'] -= stolen_gold
#             print(f"{city} plundered! {stolen_gold} gold stolen, {people} citizens killed.")
#             if city_dict[city]['population'] <= 0 or city_dict[city]['gold'] <= 0:
#                 del city_dict[city]
#                 print(f"{city} has been wiped off the map!")
#     elif action == "Prosper":
#         added_gold = int(split_event[2])
#         if added_gold < 0:
#             print("Gold added cannot be a negative number!")
#         else:
#             if city in city_dict:
#                 city_dict[city]['gold'] += added_gold
#                 print(f"{added_gold} gold added to the city treasury. {city} now has {city_dict[city]['gold']} gold.")
#
#     event = input()
#
# if city_dict:
#     print(f"Ahoy, Captain! There are {len(city_dict)} wealthy settlements to go to:")
#     for city, items in city_dict.items():
#         print(f"{city} -> Population: {items['population']} citizens, Gold: {items['gold']} kg")
# else:
#     print("Ahoy, Captain! All targets have been plundered and destroyed!")


""" Time: 0.050 s """

from collections import defaultdict
# import sys

def add_city(city_name, population, gold, cities):
    cities[city_name]['population'] += population
    cities[city_name]['gold'] += gold

def plunder_city(city_name, people, gold, cities):
    print(f"{city_name} plundered! {gold} gold stolen, {people} citizens killed.")
    cities[city_name]['population'] -= people
    cities[city_name]['gold'] -= gold

    if cities[city_name]['population'] <= 0 or cities[city_name]['gold'] <= 0:
        print(f"{city_name} has been wiped off the map!")
        cities.pop(city_name)

def prosper_city(city_name, gold, cities):
    if gold < 0:
        print(f"Gold added cannot be a negative number!")
    else:
        cities[city_name]['gold'] += gold
        print(f"{gold} gold added to the city treasury. {city_name} now has {cities[city_name]['gold']} gold.")

def process_commands(command, cities):
    action, city_name = command.split('=>')[0], command.split('=>')[1]

    if action == "Plunder":
        people, gold = map(int, command.split('=>')[2:])
        plunder_city(city_name, people, gold, cities)
    elif action == "Prosper":
        gold = int(command.split('=>')[2])
        prosper_city(city_name, gold, cities)


cities = defaultdict(lambda: {'population': 0, 'gold': 0})
info = input() # sys.stdin.readline().strip()

while info != "Sail":
    city_name, population, gold = info.split("||")
    add_city(city_name, int(population), int(gold), cities)
    info = input() # sys.stdin.readline().strip()

command = input() # sys.stdin.readline().strip()
while command != "End":
    process_commands(command, cities)
    command = input() # sys.stdin.readline().strip()

if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city, city_info in cities.items():
        print(f"{city} -> Population: {city_info['population']} citizens, Gold: {city_info['gold']} kg")
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")

cities = {}
info = input()

while info != "Sail":
    info_split = info.split("||")
    city_name, population, gold = info_split[0], info_split[1], info_split[2]
    if city_name in cities:
        cities[city_name]['population'] += int(population)
        cities[city_name]['gold'] += int(gold)
    else:
        cities[city_name] = {
            'population': int(population),
            'gold': int(gold)
        }
    info = input()

command = input()
while command != "End":
    action = command.split('=>')
    act, city_name = action[0], action[1]
    if act == "Plunder":
        people, gold = int(action[2]), int(action[3])
        if city_name in cities:
            print(f"{city_name} plundered! {gold} gold stolen, {people} citizens killed.")
            cities[city_name]['population'] -= people
            cities[city_name]['gold'] -= gold

        if cities[city_name]['population'] <= 0 or cities[city_name]['gold'] <= 0:
            print(f"{city_name} has been wiped off the map!")
            del cities[city_name]

    elif act == "Prosper":
        gold = int(action[2])
        if city_name in cities:
            if gold < 0:
                print(f"Gold added cannot be a negative number!")
            else:
                cities[city_name]['gold'] += gold
                print(f"{gold} gold added to the city treasury. {city_name} now has {cities[city_name]['gold']} gold.")
                if cities[city_name]['population'] <= 0:
                    print(f"{city_name} has been wiped off the map!")
                    del cities[city_name]
    command = input()

if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city, city_info in cities.items():
        print(f"{city} -> Population: {city_info['population']} citizens, Gold: {city_info['gold']} kg")
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")


""" whit Function"""
# def add_city(city_name, population, gold, cities):
#     if city_name in cities:
#         cities[city_name]['population'] += int(population)
#         cities[city_name]['gold'] += int(gold)
#     else:
#         cities[city_name] = {
#             'population': int(population),
#             'gold': int(gold)
#         }
#
# def plunder_city(city_name, people, gold, cities):
#     if city_name in cities:
#         print(f"{city_name} plundered! {gold} gold stolen, {people} citizens killed.")
#         cities[city_name]['population'] -= people
#         cities[city_name]['gold'] -= gold
#
#         if cities[city_name]['population'] <= 0 or cities[city_name]['gold'] <= 0:
#             print(f"{city_name} has been wiped off the map!")
#             del cities[city_name]
#
# def prosper_city(city_name, gold, cities):
#     if city_name in cities:
#         if gold < 0:
#             print(f"Gold added cannot be a negative number!")
#         else:
#             cities[city_name]['gold'] += gold
#             print(f"{gold} gold added to the city treasury. {city_name} now has {cities[city_name]['gold']} gold.")
#             if cities[city_name]['population'] <= 0:
#                 print(f"{city_name} has been wiped off the map!")
#                 del cities[city_name]
#
# def process_commands(command, cities):
#     action = command.split('=>')
#     act, city_name = action[0], action[1]
#
#     if act == "Plunder":
#         people, gold = int(action[2]), int(action[3])
#         plunder_city(city_name, people, gold, cities)
#     elif act == "Prosper":
#         gold = int(action[2])
#         prosper_city(city_name, gold, cities)
#
# cities = {}
# info = input()
#
# while info != "Sail":
#     city_name, population, gold = info.split("||")
#     add_city(city_name, population, gold, cities)
#     info = input()
#
# command = input()
# while command != "End":
#     process_commands(command, cities)
#     command = input()
#
# if cities:
#     print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
#     for city, city_info in cities.items():
#         print(f"{city} -> Population: {city_info['population']} citizens, Gold: {city_info['gold']} kg")
# else:
#     print(f"Ahoy, Captain! All targets have been plundered and destroyed!")

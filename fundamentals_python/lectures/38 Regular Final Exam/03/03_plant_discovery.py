# def add_plant(plants, plant, rarity):
#     plants[plant] = {'rarity': rarity, 'ratings': []}
#
#
# def rate_plant(plants, plant, rating):
#     if plant in plants:
#         plants[plant]['ratings'].append(rating)
#     else:
#         continue
#
#
# def update_rarity(plants, plant, new_rarity):
#     if plant in plants:
#         plants[plant]['rarity'] = new_rarity
#     else:
#         continue
#
#
# def reset_ratings(plants, plant):
#     if plant in plants:
#         plants[plant]['ratings'] = []
#     else:
#         continue
#
#
# def print_exhibition(plants):
#     print("Plants for the exhibition:")
#     for plant, info in sorted(plants.items()):
#         rarity = info['rarity']
#         ratings = info['ratings']
#         if ratings:
#             average_rating = sum(ratings) / len(ratings)
#         else:
#             average_rating = 0
#         print(f"- {plant}; Rarity: {rarity}; Rating: {average_rating:.2f}")
#
#
# plants = {}
# n = int(input())
#
# for _ in range(n):
#     plant, rarity = input().split("<->")
#     rarity = int(rarity)
#     add_plant(plants, plant, rarity)
#
# command = input()
# while command != "Exhibition":
#     tokens = command.split(": ")
#     action, data = tokens[0], tokens[1].split(" - ")
#     plant = data[0]
#     if action == "Rate":
#         rating = int(data[1])
#         rate_plant(plants, plant, rating)
#     elif action == "Update":
#         new_rarity = int(data[1])
#         update_rarity(plants, plant, new_rarity)
#     elif action == "Reset":
#         reset_ratings(plants, plant)
#     command = input()
#
# print_exhibition(plants)

###########################################################
# from icecream import ic

number_of_plants = int(input())

plant_info = {}

for plant in range(number_of_plants):
    plant_name, plant_rarity = input().split("<->")
    plant_info[plant_name] = plant_info.get(plant_name, {})
    plant_info[plant_name]["rarity"] = float(plant_rarity)
    plant_info[plant_name]["rating"] = []


def check_plant_name(plant_name):
    if plant_name not in plant_info:
        print("error")
        return
    return True


def rate_plant(plant, rating):
    if check_plant_name(plant):
        plant_info[plant]["rating"].append(rating)



def update_plant(plant, new_rarity):
    if check_plant_name(plant):
        plant_info[plant]["rarity"] = new_rarity



def reset_plant(plant):
    if check_plant_name(plant):
        plant_info[plant]["rating"] = []



def show_result():
    print("Plants for the exhibition:")
    for plant in plant_info:
        average = 0.00
        if sum(plant_info[plant]["rating"]) != 0:
            average = sum(plant_info[plant]["rating"]) / len(plant_info[plant]["rating"])
        print(f"- {plant}; Rarity: {plant_info[plant]['rarity']:.0f}; Rating: {average:.2f}")


command = input()
while command != "Exhibition":
    if "Reset" in command:
        _, plant = command.split(": ")
        reset_plant(plant)
        command = input()
        continue
    plant, rating_or_new_rarity = [float(x) if x.isdigit() else x for x in command.split(": ")[1].split(" - ")]
    # ic(plant, rating_or_new_rarity)
    if "Rate" in command:
        rate_plant(plant, rating_or_new_rarity)
    elif "Update" in command:
        update_plant(plant, rating_or_new_rarity)

    command = input()

show_result()
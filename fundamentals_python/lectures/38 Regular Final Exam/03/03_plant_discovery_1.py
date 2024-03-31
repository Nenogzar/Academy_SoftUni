
""" Time: 0.090 s """

# number_discovery = int(input())
# discovery_dict = {}
#
# for _ in range(number_discovery):
#     plant, rarity = input().split("<->")
#     discovery_dict[plant] = {'rarity': int(rarity), 'ratings': []}
#
# info_discovery = input()
# while info_discovery != "Exhibition":
#     action, plant_info = info_discovery.split(": ")
#     info_split = plant_info.split(" - ")
#     plant = info_split[0]
#
#     if plant not in discovery_dict:
#         print('error')
#     elif action == "Rate" or action == "Update":
#         rest = info_split[1]
#         if action == "Rate":
#             rating = int(rest)
#             discovery_dict[plant]['ratings'].append(rating)
#         elif action == "Update":
#             new_rarity = int(rest)
#             discovery_dict[plant]['rarity'] = new_rarity
#     elif action == "Reset":
#         discovery_dict[plant]['ratings'] = []
#
#     info_discovery = input()
#
# print("Plants for the exhibition:")
# for plant, details in discovery_dict.items():
#     avg_rating = sum(details['ratings']) / len(details['ratings']) if details['ratings'] else 0
#     print(f"- {plant}; Rarity: {details['rarity']}; Rating: {avg_rating:.2f}")

""" Time: 0.050 s """

# number_discovery = int(input())
# discovery_dict = {}
#
# for _ in range(number_discovery):
#     plant, rarity = input().split("<->")
#     discovery_dict[plant] = {'rarity': int(rarity), 'ratings': []}
#
# info_discovery = input()
# while info_discovery != "Exhibition":
#     action, plant_info = info_discovery.split(": ")
#     info_split = plant_info.split(" - ")
#     plant = info_split[0]
#     if action == "Rate" or action == "Update":
#         rest = info_split[1]
#         if plant not in discovery_dict:
#             print('error')
#         else:
#             if action == "Rate":
#                 rating = int(rest)
#                 discovery_dict[plant]['ratings'].append(rating)
#             elif action == "Update":
#                 new_rarity = int(rest)
#                 discovery_dict[plant]['rarity'] = new_rarity
#     elif action == "Reset":
#         if plant not in discovery_dict:
#             print('error')
#         else:
#             discovery_dict[plant]['ratings'] = []
#
#     info_discovery = input()
#
# print("Plants for the exhibition:")
# for plant, details in discovery_dict.items():
#     avg_rating = sum(details['ratings']) / len(details['ratings']) if details['ratings'] else 0
#     print(f"- {plant}; Rarity: {details['rarity']}; Rating: {avg_rating:.2f}")

""" Time: 0.070 s """
# number_discovery = int(input())
# discovery_dict = {}
#
# for _ in range(number_discovery):
#     plant, rarity = input().split("<->")
#     discovery_dict[plant] = {'rarity': int(rarity), 'ratings': []}
#
# info_discovery = input()
# while info_discovery != "Exhibition":
#     action, plant_info = info_discovery.split(": ")
#     info_split = plant_info.split(" - ")
#     plant = info_split[0]
#     if action == "Rate" or action == "Update":
#         rest = info_split[1]
#         if action == "Rate":
#             rating = int(rest)
#             if plant not in discovery_dict:
#                 print('error')
#             else:
#                 discovery_dict[plant]['ratings'].append(rating)
#         elif action == "Update":
#             new_rarity = int(rest)
#             if plant not in discovery_dict:
#                 print('error')
#             else:
#                 discovery_dict[plant]['rarity'] = new_rarity
#     elif action == "Reset":
#         if plant not in discovery_dict:
#             print('error')
#         else:
#             discovery_dict[plant]['ratings'] = []
#
#     info_discovery = input()
#
# print("Plants for the exhibition:")
# for plant, details in discovery_dict.items():
#     avg_rating = sum(details['ratings']) / len(details['ratings']) if details['ratings'] else 0
#     print(f"- {plant}; Rarity: {details['rarity']}; Rating: {avg_rating:.2f}")
""" whit deque"""
# from collections import deque
#
# water_dispenser = int(input())
# list_of_names = deque()
# names = input()
# while names != "Start":
#     list_of_names.append(names)
#     names = input()
#
# command = input()
# while command != "End":
#     command = command.split(" ")
#     if len(command) < 2:
#         liters = int(command[0])
#         while liters > 0 and list_of_names:
#             person_name = list_of_names.popleft()
#             if liters <= water_dispenser:
#                 print(f"{person_name} got water")
#                 water_dispenser -= liters
#                 liters = 0
#             else:
#                 print(f"{person_name} must wait")
#                 # break
#     else:
#         refill_liters = int(command[1])
#         water_dispenser += refill_liters
#     command = input()
#
# print(f"{water_dispenser} liters left")

""" OR """
# water_dispenser = int(input())
# name_list = []
# refill_liters = 0
# name = input()
# while name != "Start":
#     name_list.append(name)
#     name = input()
# action = input()
# while action != "End":
#     action = action.split(" ")
#     if len(action) == 1:
#         liters = int(action[0])
#         while liters > 0 and name_list:
#             person = name_list.pop(0)
#             if liters <= water_dispenser:
#                 print(f"{person} got water")
#                 water_dispenser -= liters
#                 liters = 0
#             else:
#                 print(f"{person} must wait")
#     else:
#         refill_liters = int(action[1])
#         water_dispenser += refill_liters
#     action = input()
# print(f"{water_dispenser} liters left")


""" class"""

# from collections import deque
#
#
# class WaterDispenser:
#     quantity = 0
#     water_line = deque()
#
#     def add_person_to_q(self, name: str):
#         self.water_line.append(name)
#
#     def refill(self, litters: int):
#         self.quantity += litters
#
#     def get_water(self, litters: int):
#         if litters <= self.quantity:
#             self.quantity -= litters
#             return f"{self.water_line.popleft()} got water"
#         return f"{self.water_line.popleft()} must wait"
#
#
# dispenser = WaterDispenser()
#
# dispenser.quantity = int(input())
# person = input()
#
# while person != "Start":
#     dispenser.add_person_to_q(person)
#     person = input()
#
# command = input()
# while command != "End":
#     if command.isdigit():
#         print(dispenser.get_water(int(command)))
#     else:
#         _, litters_to_refill = command.split()
#         dispenser.refill(int(litters_to_refill))
#     command = input()
#
# print(f"{dispenser.quantity} liters left")

""" TANER """

from collections import deque

water_in_dispenser = int(input())
queue_for_water = deque()
name = input()

while name != "Start":
    queue_for_water.append(name)
    name = input()
command = input()
while command != "End":
    if command.isdigit():
        liter_per_person = int(command)
        if water_in_dispenser >= liter_per_person:
            print(f"{queue_for_water.popleft()} got water")
            water_in_dispenser -= liter_per_person
        elif water_in_dispenser < liter_per_person:
            print(f"{queue_for_water.popleft()} must wait")
    elif not command.isdigit():
        _, liters_refill = [int(item) if item.isdigit() else item for item in command.split()]
        water_in_dispenser += liters_refill
    command = input()
print(f"{water_in_dispenser} liters left")
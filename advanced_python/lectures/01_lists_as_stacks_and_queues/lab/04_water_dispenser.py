#################################### TASK CONDITION ############################
"""
                     4.	Water Dispenser
Write a program that keeps track of people getting water from a 
dispenser and the amount of water left at the end. On the first 
line, you will receive the starting quantity of water (integer) 
in a dispenser. Then, on the following lines, you will be given 
the names of some people who want to get water (each on a separate line) 
until you receive the command "Start". Add those people in a queue. 
Finally, you will receive some commands until the command "End":
-	"{liters}" - litters (integer) that the current person in the 
queue wants to get. Check if there is enough water in the dispenser for that person.

o	If there is enough water, print "{person_name} got water" 
and remove him/her from the queue.
o	Otherwise, print "{person_name} must wait" and remove the person 
from the queue without reducing the water in the dispenser.
-	"refill {liters}" - add the given litters in the dispenser.
In the end, print how many liters of water have left 
in the format: "{left_liters} liters left".

____________________________________________________________________________________________
Example_01

Input
2
Peter
Amy
Start
2
refill 1
1
End	

Output
Peter got water
Amy got water
0 liters left	

Explanation
We create a queue with Peter and Amy. 
After the start command, we see that 
Peter wants 2 liters of water (and he gets them). 
The water dispenser is left with 0 liters. 
After refilling, there is 1 liter in the dispenser.
So when Amy wants 1 liter, she gets it, and there are 
0 liters left in the dispenser.


____________________________________________________________________________________________
Example_02

Input
10
Peter
George
Amy
Alice
Start
2
3
3
3
End	

Output
Peter got water
George got water
Amy got water
Alice must wait
2 liters left	

"""


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


""" qceka88  """

from collections import deque


class WaterDispenser:

    def __init__(self):
        self.water = int(input())
        self.people = deque()
        self.message = []

    def fill_people_deque(self):
        command = input()
        while command != 'Start':
            self.people.append(command)
            command = input()

    def return_message(self):
        print('\n'.join(self.message))

    def drink_water(self):
        self.fill_people_deque()
        while True:
            command = input()
            if 'End' in command:
                self.message.append(f'{self.water} liters left')
                break

            if 'refill' in command:
                current_liters = int(command.split()[1])
                self.water += current_liters
            else:
                thirst = int(command)
                person_name = self.people.popleft()
                if thirst <= self.water:
                    self.water -= thirst
                    self.message.append(f'{person_name} got water')
                else:
                    self.message.append(f'{person_name} must wait')

        self.return_message()


if __name__ == '__main__':
    WaterDispenser().drink_water()

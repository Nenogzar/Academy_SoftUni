from collections import deque

water_dispenser = int(input())
list_of_names = deque()
names = input()
while names != "Start":
    list_of_names.append(names)
    names = input()

command = input()
while command != "End":
    command = command.split(" ")
    if len(command) < 2:
        liters = int(command[0])
        while liters > 0 and list_of_names:
            person_name = list_of_names.popleft()
            if liters <= water_dispenser:
                print(f"{person_name} got water")
                water_dispenser -= liters
                liters = 0
            else:
                print(f"{person_name} must wait")
                # break
    else:
        refill_liters = int(command[1])
        water_dispenser += refill_liters
    command = input()

print(f"{water_dispenser} liters left")

""" 1 """
# energy = int(input())
# distance_to_enemy = input()
# win_counter = 0
#
# while distance_to_enemy != "End of battle":
#
#     distance_to_enemy = int(distance_to_enemy)
#
#     if distance_to_enemy <= energy:
#         energy -= distance_to_enemy
#         win_counter += 1
#     else:
#         print(f"Not enough energy! Game ends with {win_counter} won battles and {energy} energy")
#         break
#
#     if win_counter % 3 == 0:
#         energy += win_counter
#
#     distance_to_enemy = input()
#
# if distance_to_enemy == "End of battle":
#     print(f"Won battles: {win_counter}. Energy left: {energy}")


""" 2 """

def check_win_counter(energy, distance_to_enemy, win_counter):
    if distance_to_enemy <= energy:
        energy -= distance_to_enemy
        win_counter += 1
    else:
        return print(f"Not enough energy! Game ends with {win_counter} won battles and {energy} energy")
        # return False

    if win_counter % 3 == 0:
        energy += win_counter

    return win_counter, energy


energy = int(input())
distance_to_enemy = input()
win_counter = 0

while distance_to_enemy != "End of battle":
    distance_to_enemy = int(distance_to_enemy)

    result = check_win_counter(energy, distance_to_enemy, win_counter)
    if not result:
        break  # exit the loop if the game ends

    win_counter, energy = result

    distance_to_enemy = input()

if distance_to_enemy == "End of battle":
    print(f"Won battles: {win_counter}. Energy left: {energy}")


""" 3 """

import sys

def check_win_counter(energy, distance_to_enemy, win_counter):
    if distance_to_enemy <= energy:
        energy -= distance_to_enemy
        win_counter += 1
    else:
        print(f"Not enough energy! Game ends with {win_counter} won battles and {energy} energy")
        sys.exit()  # Излизаме от програмата

    if win_counter % 3 == 0:
        energy += win_counter

    return win_counter, energy

energy = int(input())
distance_to_enemy = input()
win_counter = 0

while distance_to_enemy != "End of battle":
    distance_to_enemy = int(distance_to_enemy)

    win_counter, energy = check_win_counter(energy, distance_to_enemy, win_counter)

    distance_to_enemy = input()

print(f"Won battles: {win_counter}. Energy left: {energy}")

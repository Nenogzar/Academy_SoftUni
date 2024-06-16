# ******* Advanced Retake Exam - 14 December 2022 ******* #

# *******  02_navy_battle  ******* #
 
# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/3744#1

1914, September 22 – German submarine U-9 sinks three unescorted British armored cruisers HMS Aboukir,
HMS Hogue, and HMS Cressy in approximately one hour.
Imagine that they had the technology to make themselves a navigational program
for the submarine and you are chosen to implement the logic.

Navigate U-9 through the battlefield, find and sink the British cruisers in the dark night,
    avoiding the floating mines all over the North Sea.

You will be given an integer n for the size of the battlefield (square shape).

On the next n lines, you will receive the rows of the battlefield.

The submarine will start at a random position, marked with the letter 'S'.
    The submarine surveys the surrounding area through its periscope, so it has to climb up to periscope depth,
        where it might run across naval mines.

When the submarine receives direction, it goes deep and moves one position toward the given direction.
    On each turn, you will be guiding the submarine and giving it the direction, in which it should move.
    The commands will be "up", "down", "left" and "right".

When a new position is reached,  the submarine climbs up to periscope depth to search for a cruiser:
•	If a position with '-' (dash) is reached, it means that the field is empty and the submarine awaits its next direction.
•	If it runs across a naval mine ('*'), the submarine takes serious damage. When a mine is blown, the position of the mine will be marked with '-' (dash). U-9 can withstand two hits from naval mines.  The third time the submarine is hit by a mine, it disappears and the mission is failed. The battle is over and the following message should be printed on the Console: "Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!"
•	If a battle cruiser is reached ('C'), the submarine destroys it and the position of the destroyed cruiser will be marked with '-' (dash).
•	If this is the last (third) battle cruiser on the battlefield, the battle is over and the following message should be printed on the Console: "Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!"
The program will end when the battle is over (All battle cruisers are destroyed or the submarine hits mines three times).
Input
•	On the first line, you are given the integer n – the size of the matrix (wall).
•	The next n lines hold the values for every row (NOT separated by anything).
•	On each of the next lines you will get a direction command.
Output
•	If all battle cruisers are destroyed, print: "Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!"
•	If U-9 is hit by a mine three times, print: "Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!".
•	At the end, print the final state of the matrix (battlefield) with the last known U-9’s position on it.
Constraints
•	The size of the square matrix (battlefield) will be between [4…10].
•	U-9’s starting position will always be marked with 'S'.
•	There will be always three battle cruisers - fields marked with 'C'.
•	There will be always enough mines on the battlefield to destroy the submarine.
•	The commands given will direct the submarine only in the limits of the battlefield.


Examples

Input

5
*--*-
-S-*C
-*---
-----
-C-*C
right
down
left
up
right
right
right
down
down
down
up
left
left
left
down


Output
Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!
*--*-
-----
-----
-----
-S-*-


Input
5
*--*-
-S-*C
-*---
-----
*C-*C
right
right
up
left
left
left


Output
Mission failed, U-9 disappeared! Last known coordinates [0, 0]!
S----
----C
-*---
-----
*C-*C


"""
##########: variant 1 :##########

# def directions(position, direction, size):
#     row, col = position
#     if direction == "up":
#         row -= 1
#     elif direction == "down":
#         row += 1
#     elif direction == "left":
#         col -= 1
#     elif direction == "right":
#         col += 1
#     return (row, col)
#
#
# START, EMPTY, MINE, CRUISER = 'S', '-', '*', 'C'
# hits, battle = 0, 0
#
# # Read the size of the battlefield
# square_shape = int(input())
#
# # Read the battlefield matrix
# battlefield = [list(input().strip()) for _ in range(square_shape)]
#
# # Find starting position of the submarine
# for r in range(square_shape):
#     for c in range(square_shape):
#         if battlefield[r][c] == START:
#             position = (r, c)
#
# end_battle = False
#
# # Read directions until the end of the battle
# while not end_battle:
#     if hits >= 3:
#         print(f"Mission failed, U-9 disappeared! Last known coordinates [{position[0]}, {position[1]}]!")
#         break
#
#     if battle >= 3:
#         print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
#         break
#
#     direction = input().strip()
#
#     # Calculate new position
#     new_position = directions(position, direction, square_shape)
#     new_r, new_c = new_position
#
#     # Check if new position is within bounds
#     if 0 <= new_r < square_shape and 0 <= new_c < square_shape:
#         if battlefield[new_r][new_c] == EMPTY:
#             position = new_position
#         elif battlefield[new_r][new_c] == MINE:
#             hits += 1
#             battlefield[new_r][new_c] = EMPTY
#             if hits == 3:
#                 print(f"Mission failed, U-9 disappeared! Last known coordinates [{new_r}, {new_c}]!")
#                 end_battle = True
#         elif battlefield[new_r][new_c] == CRUISER:
#             battle += 1
#             battlefield[new_r][new_c] = EMPTY
#             if battle == 3:
#                 print(f"Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
#                 end_battle = True
#
# # Print the final state of the battlefield
# battlefield[position[0]][position[1]] = START
# for row in battlefield:
#     print("".join(row))

##########: variant 1 :##########

START, CRUISER, MINE, EMPTY = "S", "C", "*", "-"
mines_hits, cruiser_hits = 0, 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

size_of_battlefield = int(input())

battlefield = []
position = None
for r in range(size_of_battlefield):
    line = [x for x in input()]
    if START in line:
        position = [r, line.index(START)]
    battlefield.append(line)


while True:
    direction = input()
    r0, c0 = position
    row = r0 + directions[direction][0]
    col = c0 + directions[direction][1]

    if battlefield[row][col] == MINE:
        mines_hits += 1
    elif battlefield[row][col] == CRUISER:
        cruiser_hits += 1

    battlefield[r0][c0] = EMPTY
    battlefield[row][col] = START
    position = [row, col]

    if mines_hits == 3:
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!")
        break
    elif cruiser_hits == 3:
        print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
        break

[print("".join(battlefield[r])) for r in range(size_of_battlefield)]

##########: variant 2 solution CEO:##########

battlefield_size = int(input())

lives, enemy_cruiser, battlefield, submarine_row, submarine_col = 2, [], [], 0, 0
directions = {"right": (0, 1), "left": (0, -1), "up": (-1, 0), "down": (1, 0)}


for x in range(battlefield_size):
    battlefield.append(list(input()))

    if "S" in battlefield[x]:
        submarine_row, submarine_col = x, battlefield[x].index("S")
        battlefield[submarine_row][submarine_col] = "-"

    if "C" in battlefield[x]:
        [enemy_cruiser.append([x, i]) for i in range(battlefield_size) if "C" == battlefield[x][i]]

while enemy_cruiser:

    if lives < 0:
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{submarine_row}, {submarine_col}]!")
        break

    row_to_add, col_to_add = directions[input()]
    submarine_row, submarine_col = submarine_row + row_to_add, submarine_col + col_to_add

    if battlefield[submarine_row][submarine_col] == "*":
        lives -= 1

    elif battlefield[submarine_row][submarine_col] == "C":
        enemy_cruiser.remove([submarine_row, submarine_col])

    battlefield[submarine_row][submarine_col] = "-"

else:
    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")

battlefield[submarine_row][submarine_col] = "S"
[print(*row, sep="") for row in battlefield]

##########: variant 3 solution TANER :##########

def find_ship_on_field():
    for row in range(matrix_size):
        for col in range(matrix_size):
            if matrix[row][col] == "S":
                matrix[row][col] = "-"
                return row, col


def check_current_square(row, col):
    if matrix[row][col] == "*":
        battle_field_info['mines limit'] -= 1
    elif matrix[row][col] == "C":
        battle_field_info['enemy'] -= 1
    matrix[row][col] = "-"


matrix_size = int(input())
matrix = [[col for col in input()] for row in range(matrix_size)]
directions = {
    'up': {'row': -1, 'col': 0},
    'down': {'row': 1, 'col': 0},
    'left': {'row': 0, 'col': -1},
    'right': {'row': 0, 'col': 1},
}
battle_field_info = {
    'enemy': 3,
    'mines limit': 3
}
current_row, current_col = find_ship_on_field()
while battle_field_info['enemy'] and battle_field_info['mines limit']:
    command = input()
    current_row, current_col = current_row + directions[command]['row'], current_col + directions[command]['col']
    check_current_square(current_row, current_col)
if not battle_field_info['enemy']:
    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
if not battle_field_info['mines limit']:
    print(f"Mission failed, U-9 disappeared! Last known coordinates [{current_row}, {current_col}]!")
matrix[current_row][current_col] = "S"
[print(''.join(matrix[row])) for row in range(matrix_size)]


##########: variant 3 solution SoftUni :##########


battlefield_size = int(input())

matrix = []
cruisers = []
hits_counter = 0
for i in range(battlefield_size):
    row = list(input())
    matrix.append(row)
    if 'S' in row:
        start_position = [i, row.index('S')]
    if 'C' in row:
        for c_index in range(len(row)):
            if row[c_index] == 'C':
                cruisers.append([i, c_index])

while True:
    command = input()
    next_position = []
    if command == 'up':
        next_position = [start_position[0] - 1, start_position[1]]
    elif command == 'down':
        next_position = [start_position[0] + 1, start_position[1]]
    elif command == 'left':
        next_position = [start_position[0], start_position[1] - 1]
    elif command == 'right':
        next_position = [start_position[0], start_position[1] + 1]

    row, col = next_position[0], next_position[1]
    matrix[start_position[0]][start_position[1]] = '-'

    if matrix[row][col] == '*':
        matrix[row][col] = 'S'
        hits_counter += 1
        if hits_counter > 2:
            print(f'Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!')
            break
    elif matrix[row][col] == 'C':
        matrix[row][col] = 'S'
        position = [row, col]
        cruisers.pop(cruisers.index(position))
        if not cruisers:
            print('Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!')
            break

    matrix[row][col] = 'S'
    start_position = next_position

for row in matrix:
    print(''.join(row))

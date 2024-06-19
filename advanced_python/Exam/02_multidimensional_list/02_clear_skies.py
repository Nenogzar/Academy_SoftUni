# ******* Advanced Exam - 17 February 2024 ******* #

# *******  02_clear_skies  ******* #

# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/4527#1

You will be given an integer n for the size of the protected airspace (square-shaped matrix).
On the next n lines, you will receive the rows of the airspace.

    The jetfighter will start at a random position, marked with the letter 'J'.
    In random positions also, enemy aircraft will be marked with the letter 'E'.
    There will also be repair points marked with the letter 'R'.
    All of the empty positions will be marked with the symbol'-'.

    The jetfighter has an initial armor value of 300 units.
When it receives a command, it moves one position towards the given direction.

The program will end when аll enemy planes are shot down or the jetfighter’s armor becomes 0.
The final state of the airspace must always be printed on the console at the end.
On each turn, you will be guiding the jetfighter and giving it the direction, to move towards. The commands will be "up", "down", "left" and "right".
	If a position with '-' (dash) is reached, it means that the field is empty and the jetfighter awaits its next direction.
	If it encounters an enemy aircraft marked with 'E', a battle begins:
	The jetfighter shoots down the enemy plane (the position of the destroyed enemy plane will be marked with '-' (dash)
	In case this is the last enemy, the program ends and the following message should be displayed on the console: "Mission accomplished, you neutralized the aerial threat!"
o	Do not forget the final state of the airspace.
	In case this is not the last enemy, the jetfighter takes damage – its armor loses 100 units.
o	If its armor reaches zero, it crashes and the mission fails. The program ends and the following message should be displayed on the console: "Mission failed, your jetfighter was shot down! Last coordinates [{row}, {col}]!"
o	Do not forget the final state of the airspace.
	If a position marked with 'R' is reached your plane is repaired and restores its armor to 300 units.
o	The position must be marked with '-' (dash).

Input
•	On the first line, you are given the integer n – the size of the matrix (airspace).
•	The next n lines hold the values for every row.
•	On each of the next lines, you will get a direction command.
Output
•	If all enemy planes are shot down, print:
o	"Mission accomplished, you neutralized the aerial threat!"
•	If your jetfighter is hit by an enemy plane three times, print:
o	"Mission failed, your jetfighter was shot down! Last coordinates [{row}, {col}]!".
•	At the end, print the final state of the matrix (airspace) with the last known position of your jetfighter on it.
Constraints
•	The size of the square matrix (airspace) will be between [4…10].
•	The jetfighter starting position will always be marked with 'J'.
•	There will be always four enemy aircraft - fields marked with 'E'.
•	There will be always a random count (1…5) fields marked with 'R' (repair).
•	The commands given will direct the jetfighter only within the limits of the matrix (airspace).
•	There will be always two output scenarios - either the enemy shoots down your plane or your plane shoots down all the enemy planes.
•	You will always receive enough commands to end the battle.

Examples

Input
5
-R---
-J--E
-E---
--E-E
-R---
up
down
down
down
right
right
right

Output
Mission failed, your jetfighter was shot down! Last coordinates [3, 4]!
-----
----E
-----
----J
-R---



Input
4
-R--
-JEE
-E-R
--E-
right
right
down
left
left
down
right


Output
Mission accomplished, you neutralized the aerial threat!
-R--
----
----
--J-


Input
5
-J--E
-R--E
-E--R
--R-E
-R---
right
right
right
down
down
down
left
left
left
up


Output
Mission accomplished, you neutralized the aerial threat!
-----
-R---
-J---
-----
-R---





5
-JEEE
-REEE
-E--R
--R-E
-R---


"""


##########: variant 1 :##########


def update_jetfighter_position(matrix, r, c):
    matrix[r][c] = 'J'


def directions(position, direction, matrix):
    row, col = position
    matrix[row][col] = "-"
    moves = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
    }

    d_row, d_col = moves[direction]
    row += d_row
    col += d_col

    return row, col, matrix


jetfighter, enemy, repair, empty, armor = "J", "E", "R", "-", 300
protected_airspace = []
position = (-1, -1)
rows = int(input())
enemy_counter = 0

for row_ in range(rows):
    line = list(input())
    if jetfighter in line:
        position = row_, line.index(jetfighter)
    enemy_counter += line.count(enemy)
    protected_airspace.append(line)


def update_jetfighter_position(matrix, r, c):
    matrix[r][c] = 'J'


while enemy_counter > 0 and armor > 0:
    direction = input()
    if not direction:
        break

    new_r, new_c, protected_airspace = directions(position, direction, protected_airspace)
    new_position = (new_r, new_c)

    if protected_airspace[new_r][new_c] == enemy:
        armor -= 100
        enemy_counter -= 1
        if enemy_counter == 0:
            update_jetfighter_position(protected_airspace, new_r, new_c)
            print("Mission accomplished, you neutralized the aerial threat!")
            break
        elif armor == 0:
            update_jetfighter_position(protected_airspace, new_r, new_c)
            print(f"Mission failed, your jetfighter was shot down! Last coordinates [{new_r}, {new_c}]!")
            break

    if protected_airspace[new_r][new_c] == repair:
        armor = 300

    update_jetfighter_position(protected_airspace, new_r, new_c)
    position = new_position

for row in protected_airspace:
    print("".join(row))

##########: variant 2 solution CEO :##########

matrix_size = int(input())
matrix = []
movements = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}
jet_fighter = {
    'armor': 300,
    'position': [0, 0],
    'enemies': 0
}

for row in range(matrix_size):
    matrix.append(list(input()))
    if 'J' in matrix[row]:
        index_of_jet = matrix[row].index('J')
        jet_fighter['position'] = [row, index_of_jet]
        matrix[row][index_of_jet] = '-'
    jet_fighter['enemies'] += matrix[row].count('E')

while jet_fighter['armor'] > 0:
    command = input()

    jet_fighter['position'] = [movements[command][0] + \
        jet_fighter['position'][0], movements[command][1] + \
        jet_fighter['position'][1]]
    step_on = matrix[jet_fighter['position'][0]][jet_fighter['position'][1]]

    if step_on == '-':
        continue

    if step_on == 'R':
        jet_fighter['armor'] = 300
        matrix[jet_fighter['position'][0]][jet_fighter['position'][1]] = '-'
        continue

    if step_on == 'E':
        jet_fighter['enemies'] -= 1
        matrix[jet_fighter['position'][0]][jet_fighter['position'][1]] = '-'

    if jet_fighter['enemies'] == 0:
        print('Mission accomplished, you neutralized the aerial threat!')
        matrix[jet_fighter['position'][0]][jet_fighter['position'][1]] = 'J'
        break

    jet_fighter['armor'] -= 100

else:
    matrix[jet_fighter['position'][0]][jet_fighter['position'][1]] = 'J'
    print(
        f"Mission failed, your jetfighter was shot down! Last coordinates {jet_fighter['position']}!")
[print(*row, sep='') for row in matrix]

##########: variant 3 solution SoftUni :##########

def find_start_position(size, airspace):
    for i in range(size):
        for j in range(size):
            if airspace[i][j] == 'J':
                return [i, j]
    return None


def handle_current_position(position, airspace, armor, enemy_planes):
    current_char = airspace[position[0]][position[1]]

    if current_char == 'E':
        if enemy_planes != 1:
            armor -= 100
        enemy_planes -= 1
    elif current_char == 'R':
        if armor < 300:
            armor = 300

    airspace[position[0]][position[1]] = 'J'

    return armor, enemy_planes


def move_plane(command, position, airspace):
    row, col = position

    airspace[row][col] = '-'

    if command == "up":
        position[0] -= 1
    elif command == "down":
        position[0] += 1
    elif command == "left":
        position[1] -= 1
    elif command == "right":
        position[1] += 1

    return position


def print_final_state(airspace):
    for row in airspace:
        print(''.join(row))


def clear_skies():
    armor = 300
    enemy_planes = 4

    size = int(input())
    airspace = [list(input()) for _ in range(size)]

    current_position = find_start_position(size, airspace)

    while True:
        if armor <= 0:
            assert current_position is not None
            print(
                f"Mission failed, your jetfighter was shot down! Last coordinates [{current_position[0]}, {current_position[1]}]!")
            break

        if enemy_planes == 0:
            print("Mission accomplished, you neutralized the aerial threat!")
            break

        command = input()
        assert current_position is not None
        move_plane(command, current_position, airspace)
        armor, enemy_planes = handle_current_position(current_position, airspace, armor, enemy_planes)

    print_final_state(airspace)


clear_skies()



##########: variant 4 solution TANER :##########

rows = int(input())
start_row, start_col = 0, 0
armor = 300
enemies = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

matrix = []
for row in range(rows):
    current_row = list(input())

    if "J" in current_row:
        start_row = row
        start_col = current_row.index("J")
        current_row[start_col] = "-"

    if "E" in current_row:
        enemies += current_row.count("E")

    matrix.append(current_row)

while enemies and armor > 0:
    command = input()

    start_row += directions[command][0]
    start_col += directions[command][1]

    if matrix[start_row][start_col] == "-":
        continue

    if matrix[start_row][start_col] == "R":
        armor = 300
        matrix[start_row][start_col] = "-"

    elif matrix[start_row][start_col] == "E":
        enemies -= 1
        matrix[start_row][start_col] = "-"

        if enemies:
            armor -= 100

if not enemies:
    print("Mission accomplished, you neutralized the aerial threat!")
elif armor <= 0:
    print(f"Mission failed, your jetfighter was shot down! Last coordinates [{start_row}, {start_col}]!")

matrix[start_row][start_col] = "J"
for row in matrix:
    print("".join(row))

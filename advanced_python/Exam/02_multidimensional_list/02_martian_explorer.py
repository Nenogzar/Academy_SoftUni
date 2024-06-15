# ******* Advanced Retake Exam - 14 April 2022 ******* #

# *******  02_martian_explorer  ******* #

# *******  TASK CONDITION  ******* #
"""
https://judge.softuni.org/Contests/Practice/Index/3430#1

Your rover has landed on Mars, and it needs to find resources to start humanity's first interplanetary colony.
You will receive a 6x6 field on separate lines with:

•	One rover - marked with the letter "E"
•	Water deposit (one or many) - marked with the letter "W"
•	Metal deposit (one or many) - marked with the letter "M"
•	Concrete deposit (one or many) - marked with the letter "C"
•	Rock (one or many) - marked with the letter "R"
•	Empty positions will be marked with "-"

After that, you will be given the commands for the rover's movement on one line separated by a comma and a space (", ").
    Commands can be: "up", "down", "left", or "right".
For each command, the rover moves in the given directions with one step,
    and it can land on one of the given types of deposit or a rock:
•	When it lands on a deposit,
        you must print the coordinates of that deposit in the format shown below and increase its value by 1.
•	If the rover lands on a rock, it gets broken.
        Print the coordinates where it got broken in the format shown below, and the program ends.
•	If the rover goes out of the field, it should continue from the opposite side in the same direction.

Example:
    If the rover is at position (3, 0) and it needs to move left (outside the matrix),
            it should be placed at position (3, 5).

The rover needs to find at least one of each deposit to consider the area suitable to start our colony.
Stop the program if you run out of commands or the rover gets broken.

Input
•	On the first 6 lines, you will receive the matrix.
•	On the following line, you will receive the commands for the rover separated by a comma and a space.

Output

•	For each deposit found while you go through the commands, print out on the console:
    "{Water, Metal or Concrete} deposit found at ({row}, {col})"
•	If the rover hits a rock, print the coordinates where it got broken in the format:
    "Rover got broken at ({row}, {col})"
After you go through all the commands or the rover gets broken, print out on the console:
•	If the rover has found at least one of each deposit, print on the console:
    "Area suitable to start the colony."
•	Otherwise, print on the console:
    "Area not suitable to start the colony."
See examples for more clarification.

Examples

Input
- R - - - -
- - - - - R
- E - R - -
- W - - - -
- - - C - -
M - - - - -
down, right, down, right, down, left, left, left

Output
Water deposit found at (3, 1)
Concrete deposit found at (4, 3)
Metal deposit found at (5, 0)
Area suitable to start the colony.

Input
R - - - - -
- - C - - -
- - - - M -
- - W - - -
- E - W - R
- - - - - -
up, right, down, right, right, right

Output
Water deposit found at (3, 2)
Water deposit found at (4, 3)
Rover got broken at (4, 5)
Area not suitable to start the colony.

Input
R - - - - -
- - C - - -
- - - - M -
C - M - R M
- E - W - -
- - - - - -
right, right, up, left, left, left, left, left


Output
Water deposit found at (4, 3)
Metal deposit found at (3, 2)
Concrete deposit found at (3, 0)
Metal deposit found at (3, 5)
Rover got broken at (3, 4)
Area suitable to start the colony.

"""

##########: variant 1 :##########
size = 6
place = []

rock, rover = "R", "E"
empty_position = "-"
deposit = {
    "W": [0, "Water"],
    "M": [0, "Metal"],
    "C": [0, "Concrete"]
}

start_r, start_c = -1, -1
for r in range(size):
    root = input().split()

    for c, item in enumerate(root):
        if item == rover:
            start_r, start_c = r, c

    place.append(root)

movement_command = list(map(str, input().split(", ")))

current_r, current_c = start_r, start_c

for command in movement_command:
    if command == "left":
        current_c = (current_c - 1) % size
    elif command == "right":
        current_c = (current_c + 1) % size
    elif command == "up":
        current_r = (current_r - 1) % size
    elif command == "down":
        current_r = (current_r + 1) % size

    current_position = place[current_r][current_c]

    if current_position == rock:
        print(f"Rover got broken at ({current_r}, {current_c})")
        break
    elif current_position in deposit:
        deposit[current_position][0] += 1
        print(f"{deposit[current_position][1]} deposit found at ({current_r}, {current_c})")
        place[current_r][current_c] = empty_position

if all(deposit[dep][0] > 0 for dep in deposit):
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")

##########: variant 2 solution TANER :##########
def find_rover():
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == "E":
                return row, col


def explore(row, col):
    deposits = {
        "W": "Water",
        "M": "Metal",
        "C": "Concrete"
    }
    symbol = matrix[row][col]
    if symbol in deposits:
        rover_resources['deposits'].add(symbol)
        print(f"{deposits[symbol]} deposit found at ({row}, {col})")
    elif symbol == "R":
        rover_resources['rock'] = True
        print(f"Rover got broken at ({row}, {col})")


def check_boundary(row, col):
    if col < 0:
        col = matrix_size - 1
    elif col >= matrix_size:
        col = 0
    elif row < 0:
        row = matrix_size - 1
    elif row >= matrix_size:
        row = 0
    return row, col
    # for c_pos, n_pos in ((-1, 5), (6, 0)):
    #     if col == c_pos:
    #         col = n_pos
    #     if row == c_pos:
    #         row = n_pos
    # return row, col


matrix_size = 6
matrix = [[col for col in input().split()] for row in range(matrix_size)]
directions = input().split(", ")
rover_resources = {
    'deposits': set(),
    'rock': False
}
possible_directions = (
    ('up', -1, 0),
    ('down', 1, 0),
    ('left', 0, -1),
    ('right', 0, 1)
)
rover_row, rover_col = find_rover()
while directions and not rover_resources['rock']:
    current_direction = directions.pop(0)
    for direction, row, col in possible_directions:
        if direction == current_direction:
            rover_row, rover_col = rover_row + row, rover_col + col
            rover_row, rover_col = check_boundary(rover_row, rover_col)
            explore(rover_row, rover_col)
            break
if len(rover_resources['deposits']) == 3:  # if the rover found all the deposits
    print("Area suitable to start the colony.")
elif len(rover_resources['deposits']) != 3:
    print("Area not suitable to start the colony.")


##########: variant 3 solution SoftUni :##########
def check_deposit_or_rock(current_matrix, rover, current_deposits):
    position = current_matrix[rover[0]][rover[1]]
    if position in ['W', 'M', 'C']:
        print(f"{current_deposits[position][0]} deposit found at ({rover[0]}, {rover[1]})")
        current_deposits[position][1] += 1
    elif position == 'R':
        return 'broken'
    return current_deposits


matrix = []
deposits = {'W': ['Water', 0], 'M': ['Metal', 0], 'C': ['Concrete', 0]}
rover_coordinates = []
is_broken = False

for _ in range(6):
    matrix.append((input().split()))

for row in range(6):
    found_rover = False
    for col in range(6):
        if matrix[row][col] == 'E':
            rover_coordinates = [row, col]
            found_rover = True
            break
    if found_rover:
        break

commands = input().split(", ")
for c in commands:
    if c == 'up':
        if rover_coordinates[0] > 0:
            rover_coordinates[0] -= 1
        else:
            rover_coordinates[0] = 5
    if c == 'down':
        if rover_coordinates[0] < 5:
            rover_coordinates[0] += 1
        else:
            rover_coordinates[0] = 0
    if c == 'left':
        if rover_coordinates[1] > 0:
            rover_coordinates[1] -= 1
        else:
            rover_coordinates[1] = 5
    if c == 'right':
        if rover_coordinates[1] < 5:
            rover_coordinates[1] += 1
        else:
            rover_coordinates[1] = 0
    result_after_checking_the_land = check_deposit_or_rock(matrix, rover_coordinates, deposits)
    if result_after_checking_the_land == 'broken':
        is_broken = True
        break
    deposits = result_after_checking_the_land

if is_broken:
    print(f"Rover got broken at ({rover_coordinates[0]}, {rover_coordinates[1]})")
if deposits['W'][1] >= 1 and deposits['M'][1] >= 1 and deposits['C'][1] >= 1:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")

##########: variant 2 solution TANER :##########

from collections import deque

water, concrete, metal, row, col = 0, 0, 0, 0, 0
matrix = []
for row_ in range(6):
    matrix.append(input().split())
    if "E" in matrix[row_]:
        row, col = row_, matrix[row_].index("E")

commands = deque(input().split(', '))

while commands:
    command = commands.popleft()

    if command == "up":
        row -= 1
    elif command == "down":
        row += 1
    elif command == "left":
        col -= 1
    elif command == "right":
        col += 1

    for c_pos, n_pos in ((-1, 5), (6, 0)):
        if col == c_pos:
            col = n_pos
        if row == c_pos:
            row = n_pos

    step_on = matrix[row][col]

    if step_on == "W":
        water += 1
        print(f"Water deposit found at ({row}, {col})")
    elif step_on == "M":
        metal += 1
        print(f"Metal deposit found at ({row}, {col})")
    elif step_on == "C":
        concrete += 1
        print(f"Concrete deposit found at ({row}, {col})")
    elif step_on == "R":
        print(f"Rover got broken at ({row}, {col})")
        break

if metal and water and concrete:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")

##########: variant 4 solution CEO :##########

from collections import deque

MATRIX_SIZE, matrix, rouver_row, rouver_col = 6, [], 0, 0
for row in range(MATRIX_SIZE):
    matrix.append(input().split())
    if "E" in matrix[row]:
        rouver_row = row
        rouver_col = matrix[row].index("E")

commands = deque(input().split(", "))
directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
found_materials = {"Water": False, "Concrete": False, "Metal": False}
borders, alive_rover = ((-1, 5), (6, 0)), [True]


def movement(row, col, direction):
    new_positions = [row + directions[direction][0], col + directions[direction][1]]
    for pos in range(len(new_positions)):
        for out_of_border, return_to_other_side_of_border in borders:
            if new_positions[pos] == out_of_border:
                new_positions[pos] = return_to_other_side_of_border
    return new_positions[0], new_positions[1]


def getting_materials(row, col, material):
    found_materials[material] = True
    print(f"{material} deposit found at ({row}, {col})")


def rock(row, col, _):
    print(f"Rover got broken at ({row}, {col})")
    alive_rover[0] = False


information = {"W": (getting_materials, "Water"), "M": (getting_materials, "Metal"),
               "C": (getting_materials, "Concrete"), "R": (rock, "_")}

while commands and alive_rover[0]:
    direction = commands.popleft()
    rouver_row, rouver_col = movement(rouver_row, rouver_col, direction)
    rouver_step_field = matrix[rouver_row][rouver_col]
    if rouver_step_field != "-":
        information[rouver_step_field][0](rouver_row, rouver_col, information[rouver_step_field][1])

if all(found_materials.values()):
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
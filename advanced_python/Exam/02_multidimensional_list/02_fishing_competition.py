# ******* Advanced Exam - 22 October 2023 ******* #

# *******  02_fishing_competition  ******* #

# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/4193#1

You are a longtime captain of an old fishing vessel.
The new fishing season begins and you prepare your ship to set sail in search of the big catch…

You will be given an integer n for the size of the fishing area with a square shape.
On the next n lines, you will receive the rows of the fishing area.
You will be placed in a random position, marked with the letter 'S'.
    There will be fishing passages on random positions, marked with a single digit.

There will be whirlpools marked with 'W'.
All of the empty positions will be marked with '-'.

Each turn until the "collect the nets" command is received you will be given commands for your movement.
Move commands will be: "up", "down", "left", and "right".

•	If you move to a fish passage,
    you collect the amount equal to the digit there, the passage disappears and should be replaced by '-'.
•	If you fall into a whirlpool – the ship sinks and loses its catch, the program ends.
•	If you leave the fishing area (go out of the boundaries of the matrix)
        depending on the move command you will be moved to the opposite side of the one you were on.
/Example: In a 3x3 matrix you are at position [1,2] and receive the command "right"
    you will be moved to position [1,0]./

 You need at least 20 tons of fish to be considered a successful season.
    Keep in mind that even if the quota is reached the ship continues to move.


Input
•	On the first line, you are given the integer n – the size of the square matrix.
•	The next n lines hold the values for every row.
•	On each of the next lines, you will get a move command.

Output
•	On the first line:
    	If the ship falls into a whirlpool, print only this message and stop the program:
o	"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [n,n]"

	If the ship reaches the quota:
    o	"Success! You managed to reach the quota!"

	If the ship did not reach the quota:
o	"You didn't catch enough fish and didn't reach the quota! You need {lack of fish} tons of fish more."

•	On the next lines.
	If the catch quantity is bigger than zero, print:
o	"Amount of fish caught: {quantity} tons."

else: do not print anything.

	If you didn't get into a whirlpool, print the matrix.
Constraints
•	The size of the square matrix will be between [2…10].
•	Only the letters 'S' and 'W' will be present in the matrix.
•	The fish passages are represented by single positive digits /tons/ between [1…9].
•	It is expected that there will only be either zero or one whirpool present, marked with the letter - 'W'.
•	Your position will be marked with 'S'.
Examples

Input
4
---S
----
9-5-
34--
down
down
right
down
collect the nets


Output
You didn't catch enough fish and didn't reach the quota! You need 8 tons of fish more.
Amount of fish caught: 12 tons.
----
----
--5-
S4--


Comment
The first command is "down".
The ship moves to position [1,3] followed by the command "down" [2,3] and then the command "right".
The ship leaves the matrix's boundaries and transfers to the opposite side at position [2,0].
The ship comes across a fish passage with a quantity of 9 tons and gets it.
After executing the third command, the fishing area will appear as follows:
----
----
S-5-
34--
Then you receive the command "down" again. You move to the passage of 3 tons and add them to the others 9.
Your catch is 9 + 3 = 12 tons. In the end, you get the command "collect the nets" and the program ends.



Input
5
S---9
777-1
W333-
11111
-----
down
down
right
down
collect the nets


Output
You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [2,0]


Comment
The first command is "down". The ship moves to position [1,0] and gets 7 tons of fish.
Follow the command "down" -> [2,0] The ship falls into a whirlpool and sinks.
You lose the entire catch and the program ends.


Input
5
S---9
777-1
--5--
11W11
988--
down
down
down
down
down
down
right
right
right
collect the nets


Output
Success! You managed to reach the quota!
Amount of fish caught: 31 tons.
----9
---S1
--5--
-1W11
-88--


Comment
Result is: 7 + 1 + 9 +7 + 7 = 31. You succeeded!



"""


##########: variant 1 :##########

# def directions(position, direction, rows, matrix):
#     row, col = position
#     matrix[row][col] = "-"
#
#     if direction == "up":
#         row = (row - 1) % rows
#     elif direction == "down":
#         row = (row + 1) % rows
#     elif direction == "left":
#         col = (col - 1) % rows
#     elif direction == "right":
#         col = (col + 1) % rows
#
#     return row, col, matrix


def directions(position, direction, matrix):
    row, col = position
    matrix[row][col] = "-"

    moves = {'up': (-1, 0),
             'down': (1, 0),
             'left': (0, -1),
             'right': (0, 1)}

    d_row, d_col = moves[direction]
    row = (row + d_row) % len(matrix[row]) # row = (row + d_row) % rows
    col = (col + d_col) % len(matrix[row]) # col = (col + d_col) % rows
    return row, col, matrix


def print_matrix(matrix):
    for row in matrix:
        print("".join(row))


rows = int(input())
fishing_area = []
captain, whirlpool, empty, passage, quota = "S", "W", "-", 0, 20
position = None

for row_ in range(rows):
    line = list(input())
    if captain in line:
        position = (row_, line.index(captain))
    fishing_area.append(line)

direction = input()

while direction != "collect the nets":
    n_row, n_col, fishing_area = directions(position, direction, fishing_area)
    new_position = n_row, n_col

    step = fishing_area[n_row][n_col]

    if step.isdigit():
        passage += int(step)

    if step == whirlpool:
        passage = 0
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
              f"Last coordinates of the ship: [{n_row},{n_col}]")
        exit()

    fishing_area[n_row][n_col] = captain
    position = new_position
    direction = input()

if passage >= quota:
    print(f"Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {quota - passage} tons of fish more.")
if passage > 0:
    print(f"Amount of fish caught: {passage} tons.")

print_matrix(fishing_area)


##########: variant 2 solution TANER :##########

from typing import Tuple


def valid_index(row: int, col: int) -> bool:
    return 0 <= row < matrix_size and 0 <= col < matrix_size


def traverse_ship(row: int, col: int) -> Tuple[int, int]:
    if row < 0:
        row = matrix_size - 1

    elif row >= matrix_size:
        row = 0

    if col < 0:
        col = matrix_size - 1

    elif col >= matrix_size:
        col = 0

    return row, col


ship_symbol = "S"
end_program_command = "collect the nets"
whirlpool_symbol = "W"
empty_symbol = "-"
quota_goal = 20

matrix_size = int(input())
matrix = []
start_row, start_col = 0, 0

for i in range(matrix_size):
    row = list(input())

    if ship_symbol in row:
        col = row.index(ship_symbol)
        start_row, start_col = i, col
        row[col] = empty_symbol

    matrix.append(row)

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

collected_fish = 0
has_sank = False

command = input()
while command != end_program_command:
    start_row += directions[command][0]
    start_col += directions[command][1]

    if not valid_index(start_row, start_col):
        start_row, start_col = traverse_ship(start_row, start_col)

    curr_pos = matrix[start_row][start_col]
    if curr_pos.isdigit():
        collected_fish += int(curr_pos)

    if curr_pos == whirlpool_symbol:
        has_sank = True
        collected_fish = 0
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{start_row},{start_col}]")
        break

    matrix[start_row][start_col] = empty_symbol

    command = input()


if collected_fish >= quota_goal:
    print("Success! You managed to reach the quota!")

elif not has_sank and collected_fish < quota_goal:
    tons_needed = quota_goal - collected_fish
    print(f"You didn't catch enough fish and didn't reach the quota! You need {tons_needed} tons of fish more.")

if collected_fish:
    print(f"Amount of fish caught: {collected_fish} tons.")

matrix[start_row][start_col] = ship_symbol

if not has_sank:
    for m_row in matrix:
        print("".join(m_row))

##########: variant 3 solution SoftUni :##########

def find_starting_position(size, fishing_area):
    for i in range(size):
        for j in range(size):
            if fishing_area[i][j] == 'S':
                return [i, j]
    return None


def move(command, position, fishing_area):
    row, col = position
    fishing_area[row][col] = '-'

    if command == "up":
        position[0] -= 1
    elif command == "down":
        position[0] += 1
    elif command == "left":
        position[1] -= 1
    elif command == "right":
        position[1] += 1

    return position


def handle_boundaries(position, size):
    for i in range(2):
        if position[i] < 0:
            position[i] = size - 1
        elif position[i] >= size:
            position[i] = 0


def handle_whirlpool(position):
    print(
        f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{position[0]},{position[1]}]")


def handle_results(quota, vortex, fishing_area):
    if quota >= 20:
        print("Success! You managed to reach the quota!")
    elif not vortex:
        lack = 20 - quota
        print(f"You didn't catch enough fish and didn't reach the quota! You need {lack} tons of fish more.")

    if quota > 0:
        print(f"Amount of fish caught: {quota} tons.")

    if not vortex:
        for row in fishing_area:
            print("".join(row))


size = int(input())
fishing_area = []

# Read the fishing area configuration
for _ in range(size):
    row = list(input())
    fishing_area.append(row)

current_position = find_starting_position(size, fishing_area)
quota = 0
whirlpool = False

while True:
    command = input()

    if command == "collect the nets":
        break

    current_position = move(command, current_position, fishing_area)
    handle_boundaries(current_position, size)

    current_char = fishing_area[current_position[0]][current_position[1]]

    if current_char.isdigit():
        quota += int(current_char)
    elif current_char == 'W':
        handle_whirlpool(current_position)
        whirlpool = True
        quota = 0
        break
    fishing_area[current_position[0]][current_position[1]] = 'S'

# Print the final results
handle_results(quota, whirlpool, fishing_area)



##########: variant 2 solution CEO :##########

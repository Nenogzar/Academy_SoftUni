# ******* Advanced Retake Exam - 12 April 2023 ******* #

# *******  02_the_squirrel  ******* #
 
# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/3893#1

An intern from a big company must solve the game - "The squirrel".
He doesn’t have enough experience, so he needs your help.
Here are the rules of the game:

The game starts with 0 collected hazelnuts. Your goal is to collect 3 of them.
You get as input the size of the field, which will be always a square shape.
After that, you will receive the directions in which the squirrel can move – "left", "right", "down", and "up"
in a sequence, each value separated by a comma and a space (", "). On the next rows, you will receive the field.

Possible characters in the field:
•	s - represents the squirrel's position.
•	h – represents a hazelnut.
•	* – the asterisk represents an empty position.
•	t – represents a trap.

The squirrel starts from the s - position.

•	If the squirrel steps on a hazelnut, you have to increase them by 1.
    The position should be marked with an asterisk (*).
o	If the squirrel collects all 3 hazelnuts, the game ends.
•	Asterisk (*) does nothing, so nothing happens if the squirrel steps on it.
•	If it steps on a trap, the game ends.
•	If the squirrel moves out of the field, the game ends.
After all commands you will have 4 possible results:
•	You win if the squirrel collects 3 of the hazelnuts.
•	The squirrel collects less than 3 hazelnuts.
•	The squirrel steps on a trap.
•	The squirrel moves out of the field.
Input
•	On the first line, you will receive the length of the field – an integer number in the range [3, 5].
•	On the second line, you will receive the commands to move the squirrel – an array of strings separated by ", ".
•	In the next N lines, you will receive the values for every row.
Output
•	On the first line:
o	If the squirrel goes out of the field - "The squirrel is out of the field.".
o	If the squirrel steps on a trap - "Unfortunately, the squirrel stepped on a trap...".
o	If the squirrel hasn’t collected all hazelnuts - "There are more hazelnuts to collect.".
o	If the squirrel has collected all hazelnuts - "Good job! You have collected all hazelnuts!".
•	On the second line, print the number of collected hazelnuts - "Hazelnuts collected: {hazelnutsCount}"
Constraints
•	The size of the field will be between [3,5].
•	There could be one or no trap on the field.
•	There will always be 3 hazelnuts on the field.
Examples

Input
5
left, left, up, right, up, up
**h**
t****
*h***
*h*s*
*****

Output
Good job! You have collected all hazelnuts!
Hazelnuts collected: 3

Comments
The squirrel moves 2 times to the left and collects its first hazelnut. After that collect the second one.
Finally, with the last "up" command, the squirrel collects its final hazelnut.

Input
4
down, down, right, right
*s*h
***h
***t
h***

Output
Unfortunately, the squirrel stepped on a trap...
Hazelnuts collected: 0

Input
4
down, down, right, right
h***
***h
*s*t
**h*


Output
The squirrel is out of the field.
Hazelnuts collected: 0

"""

##########: variant 1 :##########

def directions(position, direction, rows):
    row, col = position
    if direction == "up":
        row -= 1
    elif direction == "down":
        row += 1
    elif direction == "left":
        col -= 1
    elif direction == "right":
        col += 1

    position = row, col
    return position if row in range(rows) and col in range(rows) else None

hazelnuts, squirrel, empty, trap = "h", "s", "*", "t"
hazel_count = 0

rows = int(input())
directions_list = list(map(str, input().split(", ")))
field = []

for r in range(rows):
    line = [x for x in input()]
    if squirrel in line:
        position = [r, line.index(squirrel)]
    field.append(line)

command_index = 0
while command_index < len(directions_list):
    command = directions_list[command_index]
    command_index += 1

    new_position = directions(position, command, rows)

    if new_position is None:
        print("The squirrel is out of the field.")
        break

    position = new_position
    row, col = position

    if field[row][col] == hazelnuts:
        hazel_count += 1
        field[row][col] = empty
        if hazel_count == 3:
            print("Good job! You have collected all hazelnuts!")
            break

    elif field[row][col] == trap:
        print("Unfortunately, the squirrel stepped on a trap...")
        break

else:

    if hazel_count < 3:
        print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazel_count}")


##########: variant 2 solution TANER :##########


def create_field(field_size: int):
    field = []
    start_r, start_c = 0, 0

    for i in range(field_size):
        current_row = list(input())

        field.append(current_row)
        if "s" in current_row:
            squirrel_col = current_row.index("s")

            start_r, start_c = i, squirrel_col
            field[start_r][start_c] = "*"

    return field, start_r, start_c


def valid_index(row: int, col: int):
    return 0 <= row < matrix_size and 0 <= col < matrix_size


def can_step_on_square(field: list, row: int, col: int):
    return field[row][col] in ("h", "*")


def check_if_hazelnut(field: list, row: int, col: int):
    return field[row][col] == "h"


matrix_size = int(input())
commands = input().split(", ")

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "down": (1, 0),
    "up": (-1, 0),
}

collected_hazelnuts = 0
GOAL_OF_HAZELNUTS = 3

matrix, row, col = create_field(matrix_size)

game_over_messages = []
for command in commands:
    m_row, m_col = row + directions[command][0], col + directions[command][1]

    if not valid_index(m_row, m_col):
        game_over_messages.append("The squirrel is out of the field.")
        break

    row, col = m_row, m_col

    if not can_step_on_square(matrix, row, col):
        game_over_messages.append("Unfortunately, the squirrel stepped on a trap...")
        break

    if check_if_hazelnut(matrix, row, col):
        matrix[row][col] = "*"
        collected_hazelnuts += 1

        if collected_hazelnuts == GOAL_OF_HAZELNUTS:
            break


if game_over_messages:
    print(game_over_messages[0])

elif collected_hazelnuts < GOAL_OF_HAZELNUTS:
    print("There are more hazelnuts to collect.")

elif collected_hazelnuts >= GOAL_OF_HAZELNUTS:
    print("Good job! You have collected all hazelnuts!")


print(f"Hazelnuts collected: {collected_hazelnuts}")


##########: variant 3 solution YAVOR :##########


SQUIRREL, HAZELNUT, EMPTY, TRAP = "s", "h", "*", "t"

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

field_size = int(input())
commands = input().split(", ")

squirrel_position = None
field = []
for r in range(field_size):
    row = input()
    if SQUIRREL in row:
        squirrel_position = [r, row.index(SQUIRREL)]
    field.append(list(row))

hazelnuts_collected = 0
message = ""
for command in commands:
    r0, c0 = squirrel_position
    row = r0 + directions[command][0]
    col = c0 + directions[command][1]
    if not (0 <= row < field_size and 0 <= col < field_size):
        print("The squirrel is out of the field.")
        break
    if field[row][col] == TRAP:
        print("Unfortunately, the squirrel stepped on a trap...")
        break
    if field[row][col] == HAZELNUT:
        hazelnuts_collected += 1
        if hazelnuts_collected == 3:
            print("Good job! You have collected all hazelnuts!")
            break
    field[r0][c0] = EMPTY
    field[row][col] = SQUIRREL
    squirrel_position = [row, col]
else:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts_collected}")



##########: variant 4 solution SoftUni :##########

def make_a_move(row_, col_, matrix):
    found_hazelnuts = 0
    if not (0 <= row_ < len(matrix) and 0 <= col_ < len(matrix)):
        print("The squirrel is out of the field.")
        return
    if matrix[row_][col_] == 't':
        print("Unfortunately, the squirrel stepped on a trap...")
        return
    if matrix[row_][col_] == 'h':
        found_hazelnuts += 1
    matrix[row_][col_] = '*'
    return found_hazelnuts, matrix


rows = int(input())
commands = input().split(", ")
field = []
hazelnuts = 0
die = False

for _ in range(rows):
    field.append(list(input()))

squirrel_position = []
for row in range(rows):
    for col in range(rows):
        if field[row][col] == 's':
            squirrel_position = [row, col]

field[squirrel_position[0]][squirrel_position[1]] = "*"

for command in commands:
    if command == 'left':
        squirrel_position[1] -= 1
    elif command == 'right':
        squirrel_position[1] += 1
    elif command == 'down':
        squirrel_position[0] += 1
    elif command == 'up':
        squirrel_position[0] -= 1
    result = make_a_move(squirrel_position[0], squirrel_position[1], field)
    if not result:
        die = True
        break
    count_hazelnuts, field = result[0], result[1]
    hazelnuts += count_hazelnuts
    if hazelnuts == 3:
        print("Good job! You have collected all hazelnuts!")
        break

if not die and hazelnuts < 3:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts}")

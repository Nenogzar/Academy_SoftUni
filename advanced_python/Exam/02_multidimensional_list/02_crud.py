# ******* Advanced Retake Exam - 18 August 2022 ******* #

# *******  02_crud  ******* #

# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/3534#1

The abbreviation CRUD expands to Create, Read, Update and Delete.
These are the four fundamental operations in a database.

In the beginning, you will be given a matrix with 6 rows and 6 columns representing a table with information.
It consists of:
•	Letters - on one or many positions in the table
•	Numbers - on one or many positions in the table
•	Empty positions - marked with "."

Next, you will receive your first position on the table in the format "({row}, {column})"
On the following lines, until you receive "Stop" you will be receiving commands in the format:

•	"Create, {direction}, {value}"
    o	The direction could be "up", "down", "left" or "right"
    o	If you step in an empty position, create the given value on that position. E.g., if the given value is "A", and the position is empty (".") - change it to "A"
    o	If the position is NOT empty, do NOT create a value on that position

•	"Update, {direction}, {value}"
    o	The direction could be "up", "down", "left" or "right"
    o	If you step on a letter or number, update the position with the given value. E.g., if the given value is "h", and the position's value is "12" - change it to "h"
    o	If the position is empty, do NOT update the value on that position

•	"Delete, {direction}"
    o	The direction could be "up", "down", "left" or "right"
    o	If you step on a letter or number, delete it, and empty the position. E.g., if the given position's value is "h" - change it to "."
    o	If the position is already empty, do NOT delete it

•	"Read, {direction}"
    o	The direction could be "up", "down", "left" or "right"
    o	If you step on a letter or number, print it on the console
    o	If the position is empty, do NOT read it

You can make only ONE move at a time in the given direction for each command given.
In the end, print the final matrix.

Input
•	On the first 6 lines - a matrix with positions separated by a single space
    o	Letters are in the range [a-zA-Z]
    o	Numbers are in the range [-100, 100]
•	On the next line - your first position in the format: "({row}, {column})"
•	On the following lines until you receive the command "Stop" - commands in the format shown above

Output
•	In the end, print the final matrix, each row on a new line, each position separated by a single space.
Constraints
•	You will always receive valid coordinates
•	You will always receive directions in the range of the table
•	You will always receive letters or numbers

Examples

Input
. . . . . .
. 6 . . . .
G . S . t S
. . 10 . . .
. 95 . . 8 .
. . P . . .
(1, 1)
Create, down, r
Update, right, e
Create, right, a
Read, right
Delete, right
Stop

Output
t
. . . . . .
. 6 . . . .
G r e a t .
. . 10 . . .
. 95 . . 8 .
. . P . . .


Input
. . . . . .
. 6 . . . .
. T . D . O
. . 10 A . .
. 95 . 80 5 .
. . P . t .
(2, 3)
Create, down, o
Delete, right
Read, up
Create, left, 20
Update, up, P
Stop

Output
. . . . . .
. 6 . . . .
. T . D . O
. . 10 A . .
. 95 . 80 5 .
. . P . t .


Input
H 8 . . . .
70 i . . . .
t . . . B .
50 . 16 . C .
. . . t . .
. 25 . . . .
(0, 0)
Read, right
Read, down
Read, left
Delete, down
Create, right, 10
Read, left
Stop


Output
8
i
70
H 8 . . . .
70 i . . . .
. 10 . . B .
50 . 16 . C .
. . . t . .
. 25 . . . .

"""


##########: variant 1 :##########
def directions(r_pos, c_pos, size, command):
    if command == "up":
        r_pos -= 1
    elif command == "down":
        r_pos += 1
    elif command == "left":
        c_pos -= 1
    elif command == "right":
        c_pos += 1
    if 0 <= r_pos < size and 0 <= c_pos < size:
        return r_pos, c_pos


def create(r_pos, c_pos, value, db):
    if db[r_pos][c_pos] == ".":
        db[r_pos][c_pos] = value


def update(r_pos, c_pos, value, db):
    if db[r_pos][c_pos] != ".":
        db[r_pos][c_pos] = value


def delete(r_pos, c_pos, db):
    if db[r_pos][c_pos] != ".":
        db[r_pos][c_pos] = "."


def read(r_pos, c_pos, db):
    if db[r_pos][c_pos] != ".":
        print(db[r_pos][c_pos])


commands_dict = {
    "Create": create,
    "Update": update,
    "Read": read,
    "Delete": delete
}

size_db = 6

db = [list(map(str, input().split())) for _ in range(size_db)]

r_pos, c_pos = map(int, input().strip("()").split(", "))

crud = input()
while crud != "Stop":
    commands = crud.split(", ")
    command = commands[0]
    direction = commands[1]

    new_r_pos, new_c_pos = directions(r_pos, c_pos, size_db, direction)

    if command in commands_dict:
        if len(commands) == 3:
            value = commands[2]
            commands_dict[command](new_r_pos, new_c_pos, value, db)
        else:
            commands_dict[command](new_r_pos, new_c_pos, db)

    r_pos, c_pos = new_r_pos, new_c_pos
    crud = input()

for row in db:
    print(" ".join(row))

##########: variant 2 solutuin CIO :##########


matrix = [input().split() for _ in range(6)]

row, col = [int(x) for x in input()[1:-1].split(", ")]
# info = input()
# row, col = int(info[1]), int(info[-1])
# row, col = [int(x) for x in input().replace("(", "").replace(")", "").split(", ")]

command = input()

while command != "Stop":
    command_type, direction, *value = command.split(", ")

    if direction == "up":
        row -= 1
    elif direction == "down":
        row += 1
    elif direction == "left":
        col -= 1
    elif direction == "right":
        col += 1

    step_on = matrix[row][col]

    if command_type == "Create" and step_on == ".":
        step_on = value[0]

    elif not step_on.isalnum():
        pass

    elif command_type == "Update":
        step_on = value[0]

    elif command_type == "Delete":
        step_on = "."

    elif command_type == "Read":
        print(step_on)

    matrix[row][col] = step_on
    command = input()

[print(*row) for row in matrix]


##########: variant 3 solution SoftUni :##########

def move(direction_, position_):
    if direction_ == 'up':
        position_[0] -= 1
    elif direction_ == 'down':
        position_[0] += 1
    elif direction_ == 'left':
        position_[1] -= 1
    elif direction_ == 'right':
        position_[1] += 1
    return position_


matrix = []
for _ in range(6):
    matrix.append(input().split())

position = list(map(int, input().strip("(").strip(")").split(", ")))

while True:
    command = input()
    if command == 'Stop':
        break
    current_command = command.split(", ")
    position = move(current_command[1], position)
    if current_command[0] == 'Create':
        if matrix[position[0]][position[1]] == '.':
            matrix[position[0]][position[1]] = current_command[2]
    elif current_command[0] == 'Update':
        if matrix[position[0]][position[1]] != '.':
            matrix[position[0]][position[1]] = current_command[2]
    elif current_command[0] == 'Delete':
        if matrix[position[0]][position[1]] != '.':
            matrix[position[0]][position[1]] = '.'
    elif current_command[0] == 'Read':
        if matrix[position[0]][position[1]] != '.':
            print(matrix[position[0]][position[1]])

for row in matrix:
    print(' '.join(row))

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

"""
def directions(poss, size, command):
    if command == "up" or command == "left":
        poss -= 1
    elif command == "right" or command == "down":
        poss += 1
"""


##########: variant 1 :##########

def directions(poss, size, command):
    row, col = poss
    if command == "up":
        row -= 1
    elif command == "down":
        row += 1
    elif command == "left":
        col -= 1
    elif command == "right":
        col += 1

    if 0 <= row < size and 0 <= col < size:
        return row, col
    return poss


def create(position, value, db):
    row, col = position
    if db[row][col] == ".":
        db[row][col] = value


def update(position, value, db):
    row, col = position
    if db[row][col] != ".":
        db[row][col] = value


def delete(position, db):
    row, col = position
    if db[row][col] != ".":
        db[row][col] = "."


def read(position, db):
    row, col = position
    if db[row][col] != ".":
        print(db[row][col])



size_db, db, numbers, alpha = 6, [], {}, {}

for i in range(size_db):
    row = input().split()
    row = [int(el) if el.isdigit() or (el[0] == '-' and el[1:].isdigit()) else el for el in row]
    db.append(row)

position = list(map(int, input().strip("()").split(", ")))


crud = input()
while crud != "Stop":
    commands = crud.split(", ")

    if len(commands) == 2:
        command, direction = commands[0], commands[1]
        new_position = directions(position, size_db, direction)
        if command == "Read":
            read(new_position, db)
        elif command == "Delete":
            delete(new_position, db)
    elif len(commands) == 3:
        command, direction, value = commands[0], commands[1], commands[2]
        new_position = directions(position, size_db, direction)
        if command == "Create":
            create(new_position, value, db)
        elif command == "Update":
            update(new_position, value, db)

    position = new_position
    crud = input()

for row in db:
    print(" ".join(map(str, row)))

##########: variant 2 :##########


##########: variant 3 solution SoftUni :##########

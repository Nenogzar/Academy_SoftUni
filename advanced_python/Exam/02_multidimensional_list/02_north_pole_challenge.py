# ******* Advanced Retake Exam - 15 December 2021 ******* #

# *******  02_north_pole_challenge  ******* #

# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/3306#1

You are visiting Santa Claus' workshop, and it is complete chaos.
    You will need to help Santa find all items scattered around the workshop.

You will be given the size of the matrix in the format "{rows}, {columns}".
    It is the Santa's workshop represented as some symbols separated by a single space:

•	Your position is marked with the symbol "Y"
•	Christmas decorations are marked with the symbol "D"
•	Gifts are marked with the symbol "G"
•	Cookies are marked with the symbol "C"
•	All of the empty positions will be marked with "."

After the field state, you will be given commands until you receive the command "End".
    The commands will be in the format "right/left/up/down-{steps}".
    You should move in the given direction with the given steps and collect all the items that come across.
    If you go out of the field, you should continue to traverse the field from the opposite side in the same direction.
    You should mark your path with "x". Your current position should always be marked with "Y".
Keep track of all collected items.
If you've collected all items at any point, end the program and print: "Merry Christmas!".

Input
•	On the first line, you will receive the number of rows and columns in the format "{rows}, {columns}"
•	On the next lines, you will receive each row with its columns - symbols, separated by a single space.
•	On the following lines, you will receive commands in the format described above
    until you receive the command "End" or until you collect all items.
Output
•	On the first line, if you have collected all items, print:
    o	"Merry Christmas!"
    o	Otherwise, skip the line


•	Next, print the number of collected items in the format:
    o	"You've collected:
    o	- {number_of_decoration} Christmas decorations
    o	- {number_of_gifts} Gifts
    o	- {number_of_cookies} Cookies"

•	Finally, print the field, as shown in the examples.

Constrains
•	All the commands will be valid
•	There will always be at least one item
•	The dimensions of the matrix will be integers in the range [1, 20]
•	The field will always have only one "Y"
•	On the field, there will always be only the symbols shown above.

Examples
Input
6, 5
. . . . .
C . . G .
. C . . .
G . . C .
. D . . D
Y . . . G
left-3
up-1
left-2
right-7
up-1
End

Output
You've collected:
- 2 Christmas decorations
- 1 Gifts
- 0 Cookies
. . . . .
C . . G .
. C . . .
G . Y C .
x x x x x
x . x x x




Input
5, 6
. . . . . .
. . . . . .
Y C D D . .
. . . C . .
. . . C . .
right-3
down-3


Output
Merry Christmas!
You've collected:
- 2 Christmas decorations
- 0 Gifts
- 3 Cookies
. . . . . .
. . . . . .
x x x x . .
. . . x . .
. . . Y . .


Input
5, 2
. .
. .
. Y
. .
. G
up-1
left-11
down-10
End


Output
You've collected:
- 0 Christmas decorations
- 0 Gifts
- 0 Cookies
x .
Y x
x x
x .
x G

"""

##########: variant 1 :##########

current_position, empty_position, last_position, workshop = "Y", ".", "x", []
rows, cols = map(int, input().split(", "))

collected_items = {"D": [0, 0], "G": [0, 0], "C": [0, 0]}

for row in range(rows):
    line = input().split()
    workshop.append(line)

    for col, cell in enumerate(line):
        if cell in collected_items:
            collected_items[cell][0] += 1

start_row, start_col = -1, -1
for row in range(rows):
    for col in range(cols):
        if workshop[row][col] == current_position:
            start_row, start_col = row, col
            break
    if start_row != -1:
        break

while True:
    distination = input().strip()
    if distination.lower() == 'end':
        break

    direction, steps = distination.split('-')
    steps = int(steps)

    for _ in range(steps):
        new_row, new_col = start_row, start_col

        if direction == "up":
            new_row -= 1
        elif direction == "down":
            new_row += 1
        elif direction == "left":
            new_col -= 1
        elif direction == "right":
            new_col += 1

        if new_row < 0:
            new_row = rows - 1
        elif new_row >= rows:
            new_row = 0
        if new_col < 0:
            new_col = cols - 1
        elif new_col >= cols:
            new_col = 0

        if (new_row, new_col) != (start_row, start_col):
            workshop[start_row][start_col] = last_position

        new_cell = workshop[new_row][new_col]
        if new_cell in collected_items:
            collected_items[new_cell][1] += 1
            workshop[new_row][new_col] = empty_position

        workshop[new_row][new_col] = current_position
        start_row, start_col = new_row, new_col

        all_items_collected = True
        for key in collected_items:
            if collected_items[key][0] != collected_items[key][1]:
                all_items_collected = False
                break

        if all_items_collected:
            break

    if all_items_collected:
        break
if all_items_collected:
    print("\nMerry Christmas!")
print("You've collected:")
print(f"- {collected_items['D'][1]} Christmas decorations")
print(f"- {collected_items['G'][1]} Gifts")
print(f"- {collected_items['C'][1]} Cookies")

for line in workshop:
    print(" ".join(line))

##########: variant 1 whit Function :##########

def validate_coordinate(item, limit):
    return item if 0 <= item < limit else (limit - 1 if item < 0 else 0)

def move_y(start_row, start_col, collected_items):

    for _ in range(steps):
        new_row, new_col = start_row, start_col

        if direction == "up":
            new_row -= 1
        elif direction == "down":
            new_row += 1
        elif direction == "left":
            new_col -= 1
        elif direction == "right":
            new_col += 1

        new_row = validate_coordinate(new_row, rows)
        new_col = validate_coordinate(new_col, cols)

        new_cell = workshop[new_row][new_col]
        if new_cell in collected_items:
            collected_items[new_cell][1] += 1
            workshop[new_row][new_col] = empty_position

        if (new_row, new_col) != (start_row, start_col):
            workshop[start_row][start_col] = last_position

        workshop[new_row][new_col] = current_position
        start_row, start_col = new_row, new_col

        all_items_collected = all(collected_items[key][0] == collected_items[key][1] for key in collected_items)
        if all_items_collected:
            break

    return start_row, start_col, all_items_collected


current_position, empty_position, last_position = "Y", ".", "x"
workshop = []
collected_items = {"D": [0, 0], "G": [0, 0], "C": [0, 0]}

rows, cols = map(int, input().split(", "))

for row in range(rows):
    line = input().split()
    workshop.append(line)

    for col, cell in enumerate(line):
        if cell in collected_items:
            collected_items[cell][0] += 1

start_row, start_col = -1, -1
for row in range(rows):
    for col in range(cols):
        if workshop[row][col] == current_position:
            start_row, start_col = row, col
            break
    if start_row != -1:
        break

distination = input()
while distination.lower() != 'end':

    direction, steps = distination.split('-')
    steps = int(steps)

    start_row, start_col, all_items_collected = move_y(start_row, start_col, collected_items)

    if all_items_collected:
        print("\nMerry Christmas!")
        break
    distination = input()

print("You've collected:")
print(f"- {collected_items['D'][1]} Christmas decorations")
print(f"- {collected_items['G'][1]} Gifts")
print(f"- {collected_items['C'][1]} Cookies")

for line in workshop:
    print(" ".join(line))

##########: variant 2  solution CEO :##########

rows, cols = [int(x) for x in input().split(", ")]
matrix, santa_row, santa_col, items, keys = [], 0, 0, \
    {"Christmas decorations": [0, 0], "Gifts": [0, 0], "Cookies": [0, 0]}\
    , {"D": "Christmas decorations", "G": "Gifts", "C": "Cookies"}
directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

for row in range(rows):
    matrix.append(input().split())
    items["Christmas decorations"][0] += matrix[row].count("D")
    items["Gifts"][0] += matrix[row].count("G")
    items["Cookies"][0] += matrix[row].count("C")
    if "Y" in matrix[row]:
        santa_row, santa_col = row, matrix[row].index("Y")


def check_traverse(*args):
    row, col = args[0]
    for c_row, new_row in ((-1, rows - 1), (rows, 0)):
        if c_row == row:
            row = new_row
    for c_col, new_col in ((-1, cols - 1), (cols, 0)):
        if c_col == col:
            col = new_col
    return row, col


def moving_step(row, col, direction):
    return row + directions[direction][0], col + directions[direction][1]


def santo_on_the_move(row, col, direction, steps):
    for step in range(steps):
        step_row, step_col = check_traverse(moving_step(row, col, direction))
        found_symbol = matrix[step_row][step_col]
        if found_symbol not in ".x":
            items[keys[found_symbol]][0] -= 1
            items[keys[found_symbol]][1] += 1
        matrix[row][col] = "x"
        matrix[step_row][step_col] = "Y"
        row, col = step_row, step_col
        check_for_merry_christmas()
    return row, col


def check_for_merry_christmas():
    if sum(x for x, _ in items.values()) == 0:
        print("Merry Christmas!")
        show_result()


def show_result():
    print("You've collected:")
    for key, (_, value) in items.items():
        if key != "keys":
            print(f"- {value} {key}")
    [print(*matrix[row]) for row in range(rows)]
    exit()


command = input()

while command != "End":
    position, steps = [int(x) if x.isdigit() else x for x in command.split("-")]
    santa_row, santa_col = santo_on_the_move(santa_row, santa_col, position, steps)
    command = input()

show_result()

##########: variant 3 solution TANER :##########
def move_in_direction(row, col, direction, steps):
    for _ in range(steps):
        row = row + movement[direction][0]
        col = col + movement[direction][1]

        row, col = check_for_traverse(row, col)

        food = check_for_food(row, col)
        matrix[row][col] = "x"
        if food:
            collected_items[food]["count"] -= 1
            collected_items[food]["collected"] += 1
            if all(info["count"] == 0 for info in collected_items.values()):
                break

    return row, col


def check_for_food(row, col):
    symbol = matrix[row][col]
    if symbol in "DGC":
        return symbol

    return False


def check_for_traverse(row, col):
    if row == rows:
        row = 0

    elif row == -1:
        row = rows - 1

    elif col == cols:
        col = 0

    elif col == -1:
        col = cols - 1

    return row, col


rows, cols = [int(x) for x in input().split(", ")]

m_row, m_col = 0, 0

collected_items = {
    "D": {"count": 0, "collected": 0, "item_name": "Christmas decorations"},
    "G": {"count": 0, "collected": 0, "item_name": "Gifts"},
    "C": {"count": 0, "collected": 0, "item_name": "Cookies"},
}

matrix = []
for row in range(rows):
    current_row = input().split()

    if "Y" in current_row:
        m_row, m_col = row, current_row.index("Y")
        current_row[m_col] = "x"

    for symbol in current_row:
        if symbol in "DGC":
            collected_items[symbol]["count"] += 1

    matrix.append(current_row)

movement = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0),
}

command = input()
while command != "End":
    command, steps = [x if x.isalpha() else int(x) for x in command.split("-")]

    m_row, m_col = move_in_direction(m_row, m_col, command, steps)

    if all(info["count"] == 0 for info in collected_items.values()):
        break

    command = input()

matrix[m_row][m_col] = "Y"

if all(info["count"] == 0 for info in collected_items.values()):
    print("Merry Christmas!")

print("You've collected:")
for info in collected_items.values():
    print(f"- {info['collected']} {info['item_name']}")

for row in range(rows):
    print(" ".join(matrix[row]))
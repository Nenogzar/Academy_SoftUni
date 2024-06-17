# ******* Advanced Exam - 18 February 2023 ******* #

# *******  02_blind_man's_buff  ******* #

# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/3889#1


Blind man's buff is played in a spacious area, such as outdoors or in a large room, in which one player,
is blindfolded and gropes around attempting to touch the other players without being able to see them…

You will be given N and M – integers, indicating the playground’s dimensions.
On the next N lines, you will receive the rows of the playground, with M columns.

You will be marked with the letter 'B', and placed in a random position.

In random positions, furniture or other obstacles will be marked with the letter 'O'.
    The other players (opponents) will be marked with the letter 'P'.
    There will always be three other players participating in the game.
    All of the empty positions will be marked with '-'.

Your goal is to touch as many players as possible during the game,
    without leaving the playground or stepping on an obstacle.
On the next few lines, until you receive the command "Finish",
    you will receive a few lines with commands representing which direction you need to move.
The possible directions are "up", " down", "right", and "left".
    If the direction leads you out of the field, you need to stay in position inside the field(do NOT make the move).
    If you have an obstacle, towards the direction, do NOT make the move and wait for the next command.

You need to keep track of the count of touched opponents and the moves you’ve made.
In case you step on a position marked with '-', increase the count of the moves made.
When you receive a command with direction, you check the position you need to step on for an obstacle or opponent.
If there is an opponent, you touch him and the position is marked with '-'
    (increase the count of the touched opponents and moves made), and this is your new position.
The game is over when you manage to touch all other opponents or the given command is "Finish".
A game report is printed on the Console:
"Game over!"
"Touched opponents: {count} Moves made: {count}"

Input
•	On the first line, you'll receive the dimensions of the playground in the format: "N M",
        where N is the number of rows, and M is the number of columns. They'll be separated by a single space (" ").
•	On the next N lines, you will receive a string representing the respective row of the playground.
        The positions in every string will be separated by a single space (" ").
•	On the next few lines, until you receive the command "Finish", you will be given directions (up, down, right, left).
 
Output
•	When the game is over, the following output should be printed on the Console:
"Game over!"
"Touched opponents: {count} Moves made: {count}"
Constraints
•	The playground size will be a 32-bit integer in the range [2 … 2 147 483 647].
•	The playground will always have three opponents in it - 'P'.
•	The obstacles on the playground will always be random count, and there will be cases without any obstacles.
Examples

Input
5 8
- - - O - P - O
- P - O O - - -
- - - - - - O -
- P B - O - - O
- - - O - - - -
up
up
left
Finish


Output
Game over!
Touched opponents: 1 Moves made: 3


Comments

   1. up	               2. up	               3. left

- - - O - P - O         - - - O - P - O        - - - O - P - O
- P - O O - - -         - - P B O O - -        - B - O O - - -
- - B - - - O -         - - - - - - O -        - - - - - - O -
- P - - O - - O         - P - - O - - O        - P - - O - - O
- - - O - - - -         - - - O - - - -        - - - O - - - -


Input
4 4
O B O -
- P O P
- - P -
- - - -
left
right
down
right
down
right
up
right
up
down
Finish


Output
Game over!
Touched opponents: 3 Moves made: 5


Comments
1. left
Obstacle ahead - stays in the same position.
2. right
Obstacle ahead - stays in the same position.
3. down
O - O -
- B O P
- - P -
- - - -
Move made – increase moves counter
Opponent touched – increase opponents touched counter
4. right
Obstacle ahead - stays in the same position.
5. down
O - O -
- - O P
- B P -
- - - -
Move made – increase moves counter
6. right
O - O -
- - O P
- - B -
- - - -
Move made – increase moves counter
Opponent touched – increase opponents touched counter
7. up
Obstacle ahead - stays in the same position.
8. right
O - O -
- - O P
- - - B
- - - -
Move made – increase moves counter
6. up
O - O -
- - O B
- - - -
- - - -
Move made – increase moves counter
Opponent touched – increase opponents touched counter
This is the last opponent in the playground, so the game is over and the output is printed on the Console



"""


##########: variant 1 :##########

def directions(position, direction, rows, cols):
    row, col = position
    if direction == "up":
        row -= 1
    elif direction == "down":
        row += 1
    elif direction == "left":
        col -= 1
    elif direction == "right":
        col += 1
    return (row, col) if row in range(rows) and col in range(cols) else position


# return (row, col) if 0 <= row < rows and 0 <= col < cols else position

blinde, opponents, obstacles, empty = "B", "P", "O", "-"
players = 3

rows, cols = list(map(int, input().split(" ")))
playground = [input().split(" ") for _ in range(rows)]

for row in range(rows):
    if blinde in playground[row]:
        position = (row, playground[row].index(blinde))

opponent_touched, steps = 0, 0

while True:
    direction = input()
    if direction == "Finish":
        break

    new_position = directions(position, direction, rows, cols)

    n_row, n_col = new_position

    if new_position != position:
        if playground[n_row][n_col] == obstacles:
            continue

        steps += 1

        if playground[n_row][n_col] == opponents:
            opponent_touched += 1
            playground[n_row][n_col] = empty
            if opponent_touched == players:
                print("Game over!")
                print(f"Touched opponents: {opponent_touched} Moves made: {steps}")
                break

        position = new_position

if opponent_touched < players:
    print("Game over!")
    print(f"Touched opponents: {opponent_touched} Moves made: {steps}")


##########: variant 2 solution CEO:##########

def find_starter_position():
    for row in range(ROWS):
        if "B" in matrix[row]:
            col = matrix[row].index("B")
            matrix[row][col] = "-"
            return row, col


def check_valid_index(row, col):
    if 0 <= row < ROWS and 0 <= col < COLS:
        return True


def check_furniture(row, col):
    if matrix[row][col] == "O":
        return True


def check_for_other_player(row, col):
    if matrix[row][col] == "P":
        matrix[row][col] = "-"
        return True


ROWS, COLS = [int(x) for x in input().split()]
matrix = [[c for c in input().split()] for r in range(ROWS)]

players_touched = 0
steps = 0

start_row, start_col = find_starter_position()

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

command = input()
while players_touched < 3 and command != "Finish":
    try_row, try_col = start_row + directions[command][0], start_col + directions[command][1]
    if check_valid_index(try_row, try_col):
        if not check_furniture(try_row, try_col):
            if check_for_other_player(try_row, try_col):
                players_touched += 1

            start_row, start_col = try_row, try_col
            steps += 1

    command = input()

print("Game over!")
print(f"Touched opponents: {players_touched} Moves made: {steps}")


##########: variant 3 solution SoftUni :##########

def find_my_cooridnates(r, c, mtrx):
    for row in range(r):
        for col in range(c):
            if mtrx[row][col] == "B":
                return [row, col]


def check_my_next_position(my_row, my_col, current_matrix):
    if 0 <= my_row < len(current_matrix) and 0 <= my_col < len(current_matrix[0]):
        next_position = current_matrix[my_row][my_col]
        if next_position == "O":
            return False
        elif next_position == "-":
            return [my_row, my_col], current_matrix, 0
        elif next_position == "P":
            current_matrix[my_row][my_col] = "-"
            return [my_row, my_col], current_matrix, 1


n, m = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append(input().split())

my_coordinates = find_my_cooridnates(n, m, matrix)
matrix[my_coordinates[0]][my_coordinates[1]] = "-"
result = False
touched_opponents = 0
moves_made = 0

while True:
    if touched_opponents == 3:
        break

    command = input()
    if command == 'Finish':
        break

    if command == 'up':
        result = check_my_next_position(my_coordinates[0] - 1, my_coordinates[1], matrix)
    elif command == 'down':
        result = check_my_next_position(my_coordinates[0] + 1, my_coordinates[1], matrix)
    elif command == 'left':
        result = check_my_next_position(my_coordinates[0], my_coordinates[1] - 1, matrix)
    elif command == 'right':
        result = check_my_next_position(my_coordinates[0], my_coordinates[1] + 1, matrix)

    if result:
        my_coordinates, matrix, touches = result
        touched_opponents += touches
        moves_made += 1

print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {moves_made}")


##########: variant 4 solution TANER:##########

def find_starter_position():
    for row in range(ROWS):
        if "B" in matrix[row]:
            col = matrix[row].index("B")
            matrix[row][col] = "-"
            return row, col


def check_valid_index(row, col):
    if 0 <= row < ROWS and 0 <= col < COLS:
        return True


def check_furniture(row, col):
    if matrix[row][col] == "O":
        return True


def check_for_other_player(row, col):
    if matrix[row][col] == "P":
        matrix[row][col] = "-"
        return True


ROWS, COLS = [int(x) for x in input().split()]
matrix = [[c for c in input().split()] for r in range(ROWS)]

players_touched = 0
steps = 0

start_row, start_col = find_starter_position()

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

command = input()
while players_touched < 3 and command != "Finish":
    try_row, try_col = start_row + directions[command][0], start_col + directions[command][1]
    if check_valid_index(try_row, try_col):
        if not check_furniture(try_row, try_col):
            if check_for_other_player(try_row, try_col):
                players_touched += 1

            start_row, start_col = try_row, try_col
            steps += 1

    command = input()

print("Game over!")
print(f"Touched opponents: {players_touched} Moves made: {steps}")

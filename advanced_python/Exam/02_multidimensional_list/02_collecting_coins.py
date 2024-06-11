# ******* Advanced Exam - 14 February 2021 ******* #

# *******  02_collecting_coins  ******* #

# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/2812#1

You are playing a game, and your goal is to collect 100 coins.
On the first line, you will be given a number representing the size of the field with a square shape.

On the following few lines, you will be given the field with:
•	One player - randomly placed in it and marked with the symbol "P"
•	Numbers for coins placed at different positions of the field
•	Walls marked with "X"

After the field state, you will be given commands for the player's movement.
Commands can be: "up", "down", "left", "right".
    If the command is invalid, you should ignore it.

The player moves in the given direction with one step for each command and collects all the coins that come across.
If he goes out of the field, he should continue to traverse the field from the opposite side in the same direction.

Note: He can go through the same path many times, but he can collect the coins just once (the first time).

There are only two possible outcomes of the game:
•	The player hits a wall, loses the game, and his coins are reduced to 50% and rounded down to the next-lowest number.
•	The player collects at least 100 coins and wins the game.

For more clarifications, see the examples below.

Input
•	A number representing the size of the field (matrix NxN)
•	A matrix representing the field (each position separated by a single space)
•	On each of the following lines, you will get a move command.


Output

•	If the player won the game, print: "You won! You've collected {total_coins} coins."
•	If the player loses the game, print: "Game over! You've collected {total_coins} coins."
•	Collected coins have to be rounded down to the next-lowest number.
•	The player's path as cooridnates in lists on separate lines:
"Your path:
[{row_position1}, {column_position1}]
[{row_position2}, {column_position2}]
…
[{row_positionN}, {column_positionN}]"
Constrains
•	There will be no case in which less than 100 coins will be in the field
•	All given numbers will be valid integers in the range [0, 100]



Examples

Input

5
1 X 7 9 11
X 14 46 62 0
15 33 21 95 X
P 14 3 4 18
9 20 33 X 0
left
right
right
up
up
right

Output

You won! You've collected 125 coins.
Your path:
[3, 0]
[3, 4]
[3, 0]
[3, 1]
[2, 1]
[1, 1]
[1, 2]


Input

8
13 18 9 7 24 41 52 11
54 21 19 X 6 4 75 6
76 5 7 1 76 27 2 37
92 3 25 37 52 X 56 72
15 X 1 45 45 X 7 63
1 63 P 2 X 43 5 1
48 19 35 20 100 27 42 80
73 88 78 33 37 52 X 22
up
down
up
left

Output

Game over! You've collected 0 coins.
Your path:
[5, 2]
[4, 2]
[5, 2]
[4, 2]
[4, 1]

"""





















##########: variant 1 :##########
from math import floor

SIZE = int(input())
row, col, coins, matrix, path = 0, 0, 0, [], []

for row_ in range(SIZE):
    matrix.append(input().split())
    if "P" in matrix[row_]:
        row, col = row_, matrix[row_].index("P")
        matrix[row][col] = "0"
        path.append([row, col])

while True:
    direction = input()

    if direction == "up":
        row -= 1
    elif direction == "down":
        row += 1
    elif direction == "left":
        col -= 1
    elif direction == "right":
        col += 1

    for c_pos, n_pos in ((-1, SIZE - 1,), (SIZE, 0)):
        if row == c_pos:
            row = n_pos
        if col == c_pos:
            col = n_pos

    step_on = matrix[row][col]
    path.append([row, col])
    if step_on.isdigit():
        coins += int(step_on)
        matrix[row][col] = "0"
        if coins >= 100:
            print(f"You won! You've collected {coins} coins.")
            break
    else:
        print(f"Game over! You've collected {floor(coins/2)} coins.")
        break

print("Your path:")
print(*path, sep="\n")























##########: variant 2 :##########

def find_player_position(size_of_matrix):
    for row in range(size_of_matrix):
        if "P" in matrix[row]:
            col = matrix[row].index("P")
            matrix[row][col] = 0
            return row, col


def check_valid_index(row, col):
    if row == matrix_size:
        row = 0
    elif row == -1:
        row = matrix_size - 1
    elif col == matrix_size:
        col = 0
    elif col == -1:
        col = matrix_size - 1
    return row, col


def collect_coins(row, col):
    if str(matrix[row][col]).isdigit():
        player_info['coins'] += matrix[row][col]
        matrix[row][col] = 0
        return
    player_info['hit wall'] = True
    player_info['coins'] //= 2


matrix_size = int(input())
matrix = [[int(col) if col.isdigit() else col for col in input().split()] for row in range(matrix_size)]


player_info = {
    'coins': 0,
    'positions': [],
    'hit wall': False
}
current_row, current_col = find_player_position(matrix_size)

player_info['positions'].append(f"[{current_row}, {current_col}]")

while player_info['coins'] < 100 and not player_info['hit wall']:
    current_direction = input()

    for where, row, col in ('up', -1, 0), ('down', 1, 0), ('left', 0, -1), ('right', 0, 1):

        if current_direction == where:
            current_row, current_col = current_row + row, current_col + col

            current_row, current_col = check_valid_index(current_row, current_col)

            player_info['positions'].append(f"[{current_row}, {current_col}]")

            collect_coins(current_row, current_col)

if not player_info['hit wall']:
    print(f"You won! You've collected {player_info['coins']} coins.")
elif player_info['hit wall']:
    print(f"Game over! You've collected {player_info['coins']} coins.")
print("Your path:")
print('\n'.join(player_info['positions']))



##########: variant 3 solution SoftUni :##########

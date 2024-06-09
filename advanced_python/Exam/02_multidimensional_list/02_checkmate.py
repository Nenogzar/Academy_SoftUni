# ******* Advanced Exam - 24 October 2020 ******* #

# *******  02_checkmate  ******* #

# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/2551#1

You will be given a chess board (8x8). On the board there will be 3 types of symbols:
•	"." – empty square
•	"Q" – a queen
•	"K" – the king
Your job is to find which queens can capture the king and print them.
The moves that the queen can do is to move diagonally,
    horizontally and vertically (basically all the moves that all the other figures can do except from the knight).
Beware that there might be queens that stand in the way of other queens and can stop them from capturing the king.
For more clarification see the examples.

Input
•	8 lines – the state of the board (each square separated by single space)
Output
•	The positions of the queens that can capture the king as lists
•	If the king cannot be captured, print: "The king is safe!"
•	The order of output does not matter
Constrains
•	There will always be exactly 8 lines
•	There will always be exactly one King
•	Only the 3 symbols described above will be present in the input


Input
. . . . . . . .
Q . . . . . . .
. K . . . Q . .
. . . Q . . . .
Q . . . Q . . .
. Q . . . . . .
. . . . . . Q .
. Q . Q . . . .

Output
[2, 5]
[5, 1]
[1, 0]

Input
. . . . . . . .
. . . Q . . . .
. . . . . . . .
. . . . . . . .
Q . . . Q . . .
. . K . . . . .
. . . . . . Q .
. . . Q . . . .



The king is safe!

"""

##########: variant 1 :##########

board = [input().split() for _ in range(8)]

capturing_queens = []

for row in range(len(board)):
    for col in range(len(board[row])):

        if board[row][col] == "Q":
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                r, c = row + dr, col + dc

                while 0 <= r < 8 and 0 <= c < 8:
                    if board[r][c] == "K":
                        capturing_queens.append([row, col])
                        break
                    elif board[r][c] == "Q":
                        break
                    r += dr
                    c += dc

if capturing_queens:
    for queen_position in capturing_queens:
        print(queen_position)
else:
    print("The king is safe!")



##########: variant solution TANER :##########

def find_queens():
    found_queens = []
    for row in range(matrix_size):
        for col in range(matrix_size):
            if matrix[row][col] == "Q":
                found_queens.append([row, col])
    return found_queens


def check_index(row, col):
    if 0 <= row < matrix_size and 0 <= col < matrix_size:
        return True


def try_to_reach_king(row, col):
    possible_directions = (
        (-1, 0),  # up
        (1, 0),  # down
        (0, -1),  # left
        (0, 1),  # right
        (-1, -1),  # up left
        (-1, 1),  # up right
        (1, 1),  # down right
        (1, -1)  # down left
    )
    look_row, look_col = row, col

    for check_row, check_col in possible_directions:
        queen_on_the_way = False
        for look in range(matrix_size):
            look_row, look_col = look_row + check_row, look_col + check_col
            if check_index(look_row, look_col):
                if matrix[look_row][look_col] == "Q":
                    queen_on_the_way = True
                if matrix[look_row][look_col] == "K" and not queen_on_the_way:
                    return True
            else:
                look_row, look_col = row, col
                break


matrix_size = 8
matrix = [[col for col in input().split()] for _ in range(matrix_size)]
all_queens = find_queens()
queens_that_can_attack = []
for queen in all_queens:
    if try_to_reach_king(queen[0], queen[1]):
        queens_that_can_attack.append(queen)
if queens_that_can_attack:
    [print(queens_that_can_attack[row]) for row in range(len(queens_that_can_attack))]
elif not queens_that_can_attack:
    print("The king is safe!")


##########: variant 3 solution CEO :##########

MATRIX_SIZE = 8

matrix, queens_pos, king_row, king_col = [], [], 0, 0

# 0 index is column 1 index is row

directions = {
    "up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0),
    "top left diagonal": (-1, -1), "bottom left diagonal": (-1, 1),
    "top right diagonal": (1, -1), "bottom right diagonal": (1, 1)}


for row in range(MATRIX_SIZE):
    matrix.append(input().split())
    if "K" in matrix[row]:
        king_row, king_col = row, matrix[row].index("K")


def check_valid_index(row, col):
    return 0 <= row < MATRIX_SIZE and 0 <= col < MATRIX_SIZE


def movement(row, col, direction):
    return row + directions[direction][0], col + directions[direction][1]


for direction in directions:
    new_row, new_col = king_row, king_col
    for step in range(MATRIX_SIZE):
        new_row, new_col = movement(new_row, new_col, direction)
        if check_valid_index(new_row, new_col):
            if matrix[new_row][new_col] == "Q":
                queens_pos.append([new_row, new_col])
                break
        else:
            break

if queens_pos:
    [print(row) for row in queens_pos]
else:
    print("The king is safe!")
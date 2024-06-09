# ******* Advanced Retake Exam - 16 December 2020 ******* #

# *******  02_game_of_words  ******* #

# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/2720#1


You will be given a string.
Then, you will be given an integer N for the size of the field with square shape.
On the next N lines, you will receive the rows of the field.

The player will be placed on a random position, marked with "P".
On random positions there will be letters.

All of the empty positions will be marked with "-".

Each turn you will be given commands for the player’s movement.
If he moves to a letter, he consumes it, concatеnates it to the initial string and the letter disappears from the field.
If he tries to move outside of the field, he is punished
    - he loses the last letter in the string, if there are any, and the player’s position is not changed.

At the end print all letters and the field.

Input
•	On the first line, you are given the initial string
•	On the second line, you are given the integer N - the size of the square matrix
•	The next N lines holds the values for every row
•	On the next line you receive a number M
•	On the next M lines you will get a move command
Output
•	On the first line the final state of the string
•	In the end print the matrix
Constraints
•	The size of the square matrix will be between [2…10]
•	The player position will be marked with "P"
•	The letters on the field will be any letter except for "P"
•	Move commands will be: "up", "down", "left", "right"

Examples

Input:

Hello
4
P---
Mark
-l-y
--e-
4
down
right
right
right

Output:

HelloMark
----
---P
-l-y
--e-

Comments
The initial string we receive is "Hello". Then we receive 4x4 field and the player is on index [0;0].
Then, we start receiving commands.
First the player moves to [1;0], where he consumes 'M', and then all letters on the right.
Оur string is "HelloMark" and the player is on index [1;3].


Input:

Initial
5
-----
t-r--
--Pa-
--S--
z--t-
4
up
left
left
left


Output:

Initialr
-----
P----
---a-
--S--
z--t-

Comments:

The initial string we receive is "Initial". Then we receive 5x5 field and the player is on index [2;2].
The player consumes 'r' and 't',
but also tries to go out of the matrix once, so he loses the last character of his string – 't'.


"""

##########: variant 1 :##########

initial_string = input()
size = int(input())

field = [list(input()) for _ in range(size)]

player_row, player_col = -1, -1
for i in range(size):
    for j in range(size):
        if field[i][j] == 'P':
            player_row, player_col = i, j
            break
    if player_row != -1:
        break

moves_count = int(input())
moves = [input().strip() for _ in range(moves_count)]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for move in moves:
    row_delta, col_delta = directions.get(move, (0, 0))

    new_player_row, new_player_col = player_row + row_delta, player_col + col_delta

    if 0 <= new_player_row < size and 0 <= new_player_col < size:
        if field[new_player_row][new_player_col] != '-':
            initial_string += field[new_player_row][new_player_col]
            field[new_player_row][new_player_col] = '-'

        field[player_row][player_col] = '-'
        field[new_player_row][new_player_col] = 'P'
        player_row, player_col = new_player_row, new_player_col
    else:
        if initial_string:
            initial_string = initial_string[:-1]

print(initial_string)

for row in field:
    print(''.join(row))

##########: variant 2  solution CEO:##########

initial_string = input()
SIZE = int(input())
matrix, row, col = [], 0, 0
for row_ in range(SIZE):
    matrix.append(list(input()))
    if "P" in matrix[row_]:
        row, col = row_, matrix[row_].index("P")
        matrix[row][col] = "-"

number_of_commands = int(input())

for com in range(number_of_commands):
    command = input()
    t_row, t_col = row, col
    if command == "up":
        t_row -= 1
    elif command == "down":
        t_row += 1
    elif command == "left":
        t_col -= 1
    elif command == "right":
        t_col += 1

    if not 0 <= t_row < SIZE or not 0 <= t_col < SIZE:
        initial_string = initial_string[:-1]
        continue
    row, col = t_row, t_col
    step_on = matrix[row][col]
    if step_on != "-":
        matrix[row][col] = "-"
        initial_string += step_on

matrix[row][col] = "P"
print(initial_string)
[print(*row, sep="") for row in matrix]


##########: variant 3 solution TANER :##########

def find_player(size_of_matrix):
    for row in range(size_of_matrix):
        if "P" in matrix[row]:
            col = matrix[row].index("P")
            matrix[row][col] = "-"
            return row, col


def check_valid_index(row, col):
    if 0 <= row < matrix_size and 0 <= col < matrix_size:
        return True


def check_for_letter(row, col, current_string):
    if matrix[row][col] != "-":
        current_string += matrix[row][col]
        matrix[row][col] = "-"
    return current_string


main_string = input()
matrix_size = int(input())
matrix = [[col for col in input()] for row in range(matrix_size)]
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}
player_row, player_col = find_player(matrix_size)
number_of_moves = int(input())
for _ in range(number_of_moves):
    command = input()
    if check_valid_index(player_row + directions[command][0],
                         player_col + directions[command][1]):
        player_row, player_col = player_row + directions[command][0], player_col + directions[command][1]
        main_string = check_for_letter(player_row, player_col, main_string)
    else:
        main_string = main_string[:-1]
matrix[player_row][player_col] = "P"
print(main_string)
[print(*matrix[row], sep='') for row in range(matrix_size)]

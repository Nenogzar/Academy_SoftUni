# ******* Advanced Retake Exam - 19 August 2020 ******* #

# *******  02_minesweeper_generator  ******* #

# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/2463#1

Everybody remembers the old mines game. Now it is time to create your own.

You will be given an integer n for the size of the mines field with square shape
    and another one for the number of bombs that you have to place in the field.
    On the next n lines, you will receive the position for each bomb.

Your task is to create the game field placing the bombs at the correct positions and mark them with "*",
and calculate the numbers in each cell of the field.

Each cell represents a number of all bombs directly near it (up, down, left, right and the 4 diagonals).

*  "2"  *           *   2   *           *   2   *
2   3   2           2  "3"  2           2   3   2
1   *   1           1   *   1           1  "*"  1

Input
•	On the first line, you are given the integer n – the size of the square matrix.
•	On the second line – the number of the bombs.
•	The next n lines holds the position of each bomb.
Output
•	Print the matrix you've created.
Constraints
•	The size of the square matrix will be between [2…15].

Examples

Input
4
4
(0, 3)
(1, 1)
(2, 2)
(3, 0)


Output
1 1 2 *
1 * 3 2
2 3 * 1
* 2 1 1

Input
5
3
(1, 1)
(2, 4)
(4, 1)


Output
1 1 1 0 0
1 * 1 1 1
1 1 1 1 *
1 1 1 1 1
1 * 1 0 0

"""

##########: variant 1 :##########

size_matrix = int(input())
number_of_bombs = int(input())

mines_matrix = [[0 for _ in range(size_matrix)] for _ in range(size_matrix)]

for _ in range(number_of_bombs):
    row, col = map(int, input()[1:-1].split(", "))
    mines_matrix[row][col] = "*"

    for dr in range(-1, 2): # Този цикъл обхожда стойности от -1 до 1 включително
        for dc in range(-1, 2): # Този цикъл обхожда стойности от -1 до 1 включително
            if dr == 0 and dc == 0:
                continue
            r, c = row + dr, col + dc

            # Проверка дали редът и колоната на съседната клетка са в границите на матрицата
            if 0 <= r < size_matrix and 0 <= c < size_matrix:
                # Проверка дали съседната клетка не е бомба
                if mines_matrix[r][c] != "*":
                    # Ако съседната клетка е валидна и не е бомба, обновяваме броя
                    mines_matrix[r][c] += 1

for row in mines_matrix:
    print(" ".join(map(lambda x: str(x) if x != "*" else x, row)))


##########: variant 2 solution CEO : ##########

MATRIX_SIZE = int(input())
bombs_number = int(input())

directions = {
    "up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0),
    "top left diagonal": (-1, -1), "bottom left diagonal": (-1, 1),
    "top right diagonal": (1, -1), "bottom right diagonal": (1, 1)}
matrix = [[x for x in "0" * MATRIX_SIZE] for _ in range(MATRIX_SIZE)]
for bomb in range(bombs_number):
    bomb_row, bomb_col = [int(x) for x in input().replace("(", "").replace(")", "").split(", ")]
    matrix[bomb_row][bomb_col] = "*"


def check_valid_index(row, col):
    return 0 <= row < MATRIX_SIZE and 0 <= col < MATRIX_SIZE


def check_for_bombs_in_range(row, col):
    current_sum = 0
    for moving_col, moving_row in directions.values():
        check_row, check_col = row + moving_row, col + moving_col
        if check_valid_index(check_row, check_col) and matrix[check_row][check_col] == "*":
            current_sum += 1
            matrix[row][col] = current_sum


for row in range(MATRIX_SIZE):
    for col in range(MATRIX_SIZE):
        if matrix[row][col] != "*":
            check_for_bombs_in_range(row, col)

[print(*matrix[row]) for row in range(MATRIX_SIZE)]

##########: variant 3 solution TANER :##########

def number_generator():
    directions = (
        (-1, 0),  # up
        (1, 0),  # down
        (0, -1),  # left
        (0, 1),  # right
        (-1, -1),  # up left
        (-1, 1),  # up right
        (1, -1),  # down left
        (1, 1)  # down right
    )
    for row in range(matrix_size):
        for col in range(matrix_size):
            bombs_hit = 0
            look_row, look_col = row, col
            if matrix[look_row][look_col] == "*":
                continue
            for check_row, check_col in directions:
                look_row, look_col = look_row + check_row, look_col + check_col
                if check_index(look_row, look_col):
                    if matrix[look_row][look_col] == "*":
                        bombs_hit += 1
                look_row, look_col = row, col
            matrix[row][col] = str(bombs_hit)


def check_index(row, col):
    if 0 <= row < matrix_size and 0 <= col < matrix_size:
        return True


matrix_size = int(input())
matrix = [["0" for col in range(matrix_size)] for row in range(matrix_size)]
bombs_count = int(input())
for _ in range(bombs_count):
    mine_position = input().split(", ")
    mine_row, mine_col = int(mine_position[0][1:]), int(mine_position[1][:-1])
    matrix[mine_row][mine_col] = "*"
number_generator()
[print(*matrix[row], sep=' ') for row in range(matrix_size)]
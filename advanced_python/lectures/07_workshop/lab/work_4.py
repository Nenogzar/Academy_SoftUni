
#***** Workshop - Python Advanced - май 2024 *****#


"""
Workshop: Console Connect Four

We will create a simple two-player "Connect Four" game in this workshop. Here is how the game is going to look in the end:

[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
1
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[1, 0, 0, 0, 0, 0, 0]
2
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[1, 2, 0, 0, 0, 0, 0]
2
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 1, 0, 0, 0, 0, 0]
[1, 2, 0, 0, 0, 0, 0]
3
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 1, 0, 0, 0, 0, 0]
[1, 2, 2, 0, 0, 0, 0]
3
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 1, 1, 0, 0, 0, 0]
[1, 2, 2, 0, 0, 0, 0]
4
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 1, 1, 0, 0, 0, 0]
[1, 2, 2, 2, 0, 0, 0]
1
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[1, 1, 1, 0, 0, 0, 0]
[1, 2, 2, 2, 0, 0, 0]
5
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0]
[1, 1, 1, 0, 0, 0, 0]
[1, 2, 2, 2, 2, 0, 0]
Играч 2 печели!


The Main Logic

· A player wins when he/she connects four slots.

· The winning connected slots must be consecutive

· A connection can be

    o Horizontal
    
    o Vertical
    
    o Diagonal

BONUS

· Try writing validation logic for:

    o More than one player
    
    o Reset logic

· Try adding error messages for invalid column

"""

"""Вариант 1  - Ines"""

ROWS = 6
COLS = 7


class FullColumnError(Exception):
    pass


def print_board(board):
    for data_row in board:
        print(data_row)


def is_valid_column_choice(col_number):
    return 1 <= col_number <= COLS


def place_player_choice(board, col_index, player_num):
    """
    Starting from the button, we are checking for empty space in
    that column for each row.
    """
    for row_index in range(len(board) - 1, -1, -1):
        if board[row_index][col_index] == 0:
            board[row_index][col_index] = player_num
            return row_index, col_index
    raise FullColumnError


board = []

for _ in range(ROWS):
    board.append([0 for el in range(COLS)])

print_board(board)

turn = 1

# TODO to change
while True:
    player_num = 1 if turn % 2 != 0 else 2
    try:
        selected_column = int(input(f"Player {player_num}, please choose a column: "))
    except ValueError:
        print("Please enter a valid digit")
        continue

    if not is_valid_column_choice(selected_column):
        print(f"Please select a number between 1 and {COLS}")
        continue

    selected_col_index = selected_column - 1
    try:
        place_player_choice(board, selected_col_index, player_num)
    except FullColumnError:
        print("This column is full, please select another one with available space")
        continue

    print_board(board)
    turn += 1

"""Вариант 2 """

ROWS = 6
COLS = 7


# Игрално поле
def print_board(board):
    for row in board:
        print(row)


# Проверявам дали избраната колона е валидна (между 1 и COLS)
def is_valid_column_choice(col_number):
    return 1 <= col_number <= COLS


def place_player_choice(board, col_index, player_num):
    for row_index in range(ROWS - 1, -1, -1):
        if board[row_index][col_index] == 0:
            board[row_index][col_index] = player_num
            return row_index, col_index
    raise Exception("Колоната е пълна")


# Проверка за границите на матрицата
def isValidPlace(row, col):
    return 0 <= row < ROWS and 0 <= col < COLS


# Проверка за победител
def check_winner(board, row, col, player_num):
    directions = [
        ((-1, 0), (1, 0)),  # вертикално
        ((0, -1), (0, 1)),  # хоризонтално
        ((-1, -1), (1, 1)),  # диагонално /
        ((-1, 1), (1, -1))  # диагонално \
    ]

    for dir1, dir2 in directions:
        count = 1
        for matrix_row, matrix_col in [dir1, dir2]:
            """
                        изчисляване на новата позиция
                        Ако текущата позиция е (3, 2) и 
                        посоката на обхождане е (-1, 0) нагоре 
                        новата позиция ще бъде:
                        r = 3 + (-1) = 2
                        c = 2 + 0 = 2
                        """
            r, c = row + matrix_row, col + matrix_col

            while isValidPlace(r, c) and board[r][c] == player_num:
                count += 1
                r += matrix_row
                c += matrix_col
        if count >= 4:
            return True
    return False


# Проверка дали дъската е пълна
def is_board_full(board):
    for col in range(COLS):
        if board[0][col] == 0:
            return False
    return True


# Празната дъска
board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
print_board(board)

turn = 1

while True:
    player_num = 1 if turn % 2 != 0 else 2
    try:
        selected_column = int(input())
    except ValueError:
        print("Моля, въведете валидна цифра")
        continue

    if not is_valid_column_choice(selected_column):
        print(f"Моля, изберете число между 1 и {COLS}")
        continue

    selected_col_index = selected_column - 1
    try:
        row, col = place_player_choice(board, selected_col_index, player_num)
    except Exception as e:
        print(e)
        continue

    print_board(board)

    if check_winner(board, row, col, player_num):
        print(f"Играч {player_num} печели!")
        break

    if is_board_full(board):
        print("Дъската е пълна! Равенство!")
        break

    turn += 1

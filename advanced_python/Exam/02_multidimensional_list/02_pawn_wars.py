# ******* Advanced Exam - 19 February 2022 ******* #

# *******  02_pawn_wars  ******* #

# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/3374#1


	A	B	C	D	E	F	G	H
8	A8	8B	C8	D8	E8	F8	G8	H8	8
7	A7	7B	C7	D7	E7	F7	G7	H7	7
6	A6	6B	C6	D6	E6	F6	G6	H6	6
5	A5	5B	C5	D5	E5	F5	G5	H5	5
4	A4	4B	C4	D4	E4	F4	G4	H4	4
3	A3	3B	C3	D3	E3	F3	G3	H3	3
2	A2	2B	C2	D2	E2	F2	G2	H2	2
1	A1	1B	C1	D1	E1	F1	G1	H1	1
	A	B	C	D	E	F	G	H


A chessboard has 8 rows and 8 columns. Rows, also called ranks, are marked from number 1 to 8,
    and columns are marked from A to H. We have a total of 64 squares.
    Each square is represented by a combination of letters and a number (a1, b1, c1, etc.).
        In this problem colors of the board will be ignored.

We will play the game with two pawns, white (w) and black (b), where they can:
•	Only move forward in a straight line:
    White (w) moves from the 1st rank to the 8th rank direction.
    Black (b) moves from 8th rank to the 1st rank direction.
•	Can move only 1 square at a time.
•	Can capture another pawn in from of them only diagonally:

When a pawn reaches the last rank (for the white one
    - this is the 8th rank, and for the black one
        - this is the 1st rank), can be promoted to a queen.

Two pawns (w and b) will be placed on two random squares of the bord.
    The first move is always made by the white pawn (w), then black moves (b), then white (w) again, and so on.


Some rules apply when moving paws:
•	If the two pawns interact diagonally, the player, in turn, must capture the opponent's pawn.
    When a pawn captures another pawn, the game is over.
•	If no capture is possible, the pawns keep on moving until one of them reaches the last rank.

Input
•	On 8 lines, you will receive each row with its 8 columns, each element separated by a single space:
    o	Empty positions are marked with "-".
    o	White pawn is marked with "w"
    o	Black pawn is marked with "b"

Output

Print either one of the following:
•	If a pawn captures the other, print:
    "Game over! {White/Black} win, capture on {square}."
•	If a pawn reaches the last rank, print:
    "Game over! {White/Black} pawn is promoted to a queen at {square}."

Constraints

•	The input will always be valid.
•	The matrix will always be 8x8.
•	There will be no case where two pawns are placed on the same square.
•	There will be no case where two pawns are placed on the same column.
•	There will be no case where black/white will be placed on the last rank.

Examples

Input
- - - - - - b -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- w - - - - - -
- - - - - - - -
- - - - - - - -


Output
Game over! White pawn is promoted to a queen at b8.


Comments
We start by pushing the white pawn to b4, next, we push the black pawn to g7:
- - - - - - - -
- - - - - - b -
- - - - - - - -
- - - - - - - -
- w - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
Then white play b5, black play g6:
- - - - - - - -
- - - - - - - -
- - - - - - b -
- w - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
…
Capturing is not possible here, so after a few more moves, the white pawn is promoted to a queen on b8.


Input
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
b - - - - - - -
- w - - - - - -
- - - - - - - -

Output
Game over! White win, capture on a3.

Comments
A white pawn always start first, so it must capture the black one on a3 in the first move:
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
w - - - - - - -
- - - - - - - -
- - - - - - - -


"""


##########: variant 1 :##########
def print_board(board):
    for row in board:
        print(" ".join(row))
    print()


board = []
white_pos = None
black_pos = None

for i in range(8):
    line = input().split()
    board.append(line)
    if "w" in line:
        white_pos = (i, line.index("w"))
    if "b" in line:
        black_pos = (i, line.index("b"))


def pos_to_chess(pos):
    row, col = pos
    return f"{chr(col + ord('a'))}{8 - row}"


game_over = False

while not game_over:
    white_row, white_col = white_pos

    if (white_row > 0 and white_col > 0 and board[white_row - 1][white_col - 1] == "b"):
        white_pos = (white_row - 1, white_col - 1)
        board[white_row][white_col] = "-"
        board[white_row - 1][white_col - 1] = "w"
        print(f"Game over! White win, capture on {pos_to_chess(white_pos)}.")
        game_over = True
    elif (white_row > 0 and white_col < 7 and board[white_row - 1][white_col + 1] == "b"):
        white_pos = (white_row - 1, white_col + 1)
        board[white_row][white_col] = "-"
        board[white_row - 1][white_col + 1] = "w"
        print(f"Game over! White win, capture on {pos_to_chess(white_pos)}.")
        game_over = True
    else:

        if white_row > 0 and board[white_row - 1][white_col] == "-":
            white_pos = (white_row - 1, white_col)
            board[white_row][white_col] = "-"
            board[white_row - 1][white_col] = "w"
        if white_row - 1 == 0:
            print(f"Game over! White pawn is promoted to a queen at {pos_to_chess(white_pos)}.")
            game_over = True

    if game_over:
        break

    black_row, black_col = black_pos

    if (black_row < 7 and black_col > 0 and board[black_row + 1][black_col - 1] == "w"):
        black_pos = (black_row + 1, black_col - 1)
        board[black_row][black_col] = "-"
        board[black_row + 1][black_col - 1] = "b"
        print(f"Game over! Black win, capture on {pos_to_chess(black_pos)}.")
        game_over = True
    elif (black_row < 7 and black_col < 7 and board[black_row + 1][black_col + 1] == "w"):
        black_pos = (black_row + 1, black_col + 1)
        board[black_row][black_col] = "-"
        board[black_row + 1][black_col + 1] = "b"
        print(f"Game over! Black win, capture on {pos_to_chess(black_pos)}.")
        game_over = True
    else:

        if black_row < 7 and board[black_row + 1][black_col] == "-":
            black_pos = (black_row + 1, black_col)
            board[black_row][black_col] = "-"
            board[black_row + 1][black_col] = "b"
        if black_row + 1 == 7:
            print(f"Game over! Black pawn is promoted to a queen at {pos_to_chess(black_pos)}.")
            game_over = True


##########: variant 2 :##########

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()


board = []
white_pos = None
black_pos = None

for i in range(8):
    line = input().split()
    board.append(line)
    if "w" in line:
        white_pos = (i, line.index("w"))
    if "b" in line:
        black_pos = (i, line.index("b"))


def pos_to_chess(pos):
    row, col = pos
    return f"{chr(col + ord('a'))}{8 - row}"  # индекси и букви -  координати


pawn_moves = {
    "w": {
        "start": white_pos,
        "direction": -1,
        "opponent": "b",
        "promote_row": 0,
        "win_message": "White win, capture on {}.",
        "promote_message": "White pawn is promoted to a queen at {}."
    },
    "b": {
        "start": black_pos,
        "direction": 1,
        "opponent": "w",
        "promote_row": 7,
        "win_message": "Black win, capture on {}.",
        "promote_message": "Black pawn is promoted to a queen at {}."
    }
}


def move_pawn(pawn, board):
    pos = pawn_moves[pawn]["start"]
    direction = pawn_moves[pawn]["direction"]
    opponent = pawn_moves[pawn]["opponent"]
    promote_row = pawn_moves[pawn]["promote_row"]
    win_message = pawn_moves[pawn]["win_message"]
    promote_message = pawn_moves[pawn]["promote_message"]

    row, col = pos

    for d_col in [-1, 1]: # улавяне на противниковата пешка диагонално
        new_row, new_col = row + direction, col + d_col
        if 0 <= new_row < 8 and 0 <= new_col < 8 and board[new_row][new_col] == opponent:
            new_pos = (new_row, new_col)
            board[row][col] = "-"
            board[new_row][new_col] = pawn
            pawn_moves[pawn]["start"] = new_pos
            print(f"Game over! " + win_message.format(pos_to_chess(new_pos)))
            return True

    new_row = row + direction
    if 0 <= new_row < 8 and board[new_row][col] == "-":
        new_pos = (new_row, col) # Проверка за нормално движение напред
        board[row][col] = "-"
        board[new_row][col] = pawn
        pawn_moves[pawn]["start"] = new_pos
        if new_row == promote_row:
            print(f"Game over! " + promote_message.format(pos_to_chess(new_pos)))
            return True

    return False


game_over = False

while not game_over:
    # Бяла пешка
    game_over = move_pawn("w", board)
    if game_over:
        break

    # Черна пешка
    game_over = move_pawn("b", board)


##########: variant 3 solution SoftUni :##########

def check_if_can_capture(coordinates_attacker, coordinates_defender):
    row_a = coordinates_attacker[0]
    col_a = coordinates_attacker[1]
    row_d = coordinates_defender[0]
    col_d = coordinates_defender[1]
    if row_a - 1 >= 0 and col_a - 1 >= 0:
        if row_a - 1 == row_d and col_a - 1 == col_d:
            return [row_a - 1, col_a - 1]
    if row_a - 1 >= 0 and col_a + 1 < 8:
        if row_a - 1 == row_d and col_a + 1 == col_d:
            return [row_a - 1, col_a + 1]
    if row_a + 1 < 8 and col - 1 >= 0:
        if row_a + 1 == row_d and col_a - 1 == col_d:
            return [row_a + 1, col_a - 1]
    if row_a + 1 < 8 and col + 1 < 8:
        if row_a + 1 == row_d and col_a + 1 == col_d:
            return [row_a + 1, col_a + 1]


matrix = []
for _ in range(8):
    matrix.append(input().split())

white_pawn_coordinates = []
black_pawn_coordinates = []

position_row = {
    0: "8",
    1: "7",
    2: "6",
    3: "5",
    4: "4",
    5: "3",
    6: "2",
    7: "1",
}
positions_col = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
}

for row in range(8):
    for col in range(8):
        if matrix[row][col] == "w":
            white_pawn_coordinates = [row, col]
        if matrix[row][col] == "b":
            black_pawn_coordinates = [row, col]

for _ in range(8):
    capture_on = check_if_can_capture(white_pawn_coordinates, black_pawn_coordinates)
    if capture_on:
        position = positions_col[capture_on[1]] + position_row[capture_on[0]]
        print(f"Game over! White win, capture on {position}.")
        break

    white_pawn_coordinates[0] -= 1

    if white_pawn_coordinates[0] == 0:
        position = positions_col[white_pawn_coordinates[1]] + position_row[white_pawn_coordinates[0]]
        print(f"Game over! White pawn is promoted to a queen at {position}.")
        break

    capture_on = check_if_can_capture(black_pawn_coordinates, white_pawn_coordinates)
    if capture_on:
        position = positions_col[capture_on[1]] + position_row[capture_on[0]]
        print(f"Game over! Black win, capture on {position}.")
        break

    black_pawn_coordinates[0] += 1

    if black_pawn_coordinates[0] == 7:
        position = positions_col[black_pawn_coordinates[1]] + position_row[black_pawn_coordinates[0]]
        print(f"Game over! Black pawn is promoted to a queen at {position}.")
        break



##########: variant 4 solution CEO :##########

matrix = []
b_row, b_col, w_col, w_row = 0, 0, 0, 0

for row in range(8):
    matrix.append(input().split())
    if "w" in matrix[row]:
        w_row, w_col = row, matrix[row].index("w")
    elif "b" in matrix[row]:
        b_row, b_col = row, matrix[row].index("b")

while True:

    if (w_row - 1, w_col - 1) == (b_row, b_col) or (w_row - 1, w_col + 1) == (b_row, b_col):
        print(f"Game over! White win, capture on {chr(97 + b_col)}{abs(b_row - 8)}.")
        break
    w_row -= 1
    if w_row == -1:
        print(f"Game over! White pawn is promoted to a queen at {chr(97 + w_col)}8.")
        break

    if (b_row + 1, b_col - 1) == (w_row, w_col) or (b_row + 1, b_col + 1) == (w_row, w_col):
        print(f"Game over! Black win, capture on {chr(97 + w_col)}{abs(w_row - 8)}.")
        break
    b_row += 1
    if b_row == 8:
        print(f"Game over! Black pawn is promoted to a queen at {chr(97 + b_col)}1.")
        break

##########: variant 5 solution CEO :##########

def draw_board_ranks():
    chess_ranks = []
    letters = "abcdefgh"
    for row in range(matrix_size, 0, -1):
        chess_ranks.append([letters[col] + str(row) for col in range(matrix_size)])
    return chess_ranks


def find_pawns():
    black = []
    white = []
    for row in range(matrix_size):
        for col in range(len(matrix[row])):
            if matrix[row][col] == "b":
                black = [row, col]
            if matrix[row][col] == "w":
                white = [row, col]
    return black, white


def white_pawn_move(row, col):
    if 0 <= row - 1 < len(matrix) and 0 <= col - 1 < len(matrix):
        if "b" == matrix[row - 1][col - 1]:
            print(f"Game over! White win, capture on {chess_board_ranks[row - 1][col - 1]}.")
            rules['white'] = True
    if 0 <= row - 1 < len(matrix) and 0 <= col + 1 < len(matrix):
        if "b" == matrix[row - 1][col + 1]:
            print(f"Game over! White win, capture on {chess_board_ranks[row - 1][col + 1]}.")
            rules['white'] = True
    if 0 <= row < len(matrix):
        if not rules['white']:
            matrix[row][col] = "-"
            row -= 1
            matrix[row][col] = "w"
        if row == 0:
            print(f"Game over! White pawn is promoted to a queen at {chess_board_ranks[row][col]}.")
            rules['white'] = True
    return [row, col]


def black_pawn_move(row, col):
    if 0 <= row + 1 < len(matrix) and 0 <= col - 1 < len(matrix):
        if "w" == matrix[row + 1][col - 1]:
            print(f"Game over! Black win, capture on {chess_board_ranks[row + 1][col - 1]}.")
            rules['black'] = True
    if 0 <= row + 1 < len(matrix) and 0 <= col + 1 < len(matrix):
        if "w" == matrix[row + 1][col + 1]:
            print(f"Game over! Black win, capture on {chess_board_ranks[row + 1][col + 1]}.")
            rules['black'] = True
    if 0 <= row < len(matrix):
        if not rules['black']:
            matrix[row][col] = "-"
            row += 1
            matrix[row][col] = "b"
        if row == 7:
            print(f"Game over! Black pawn is promoted to a queen at {chess_board_ranks[row][col]}.")
            rules['black'] = True
    return [row, col]


matrix_size = 8
chess_board_ranks = draw_board_ranks()
matrix = [[col for col in input().split()] for row in range(matrix_size)]
black_pawn, white_pawn = find_pawns()
take_turns = 1
rules = {
    'white': False,
    'black': False,
}
while not rules['white'] and not rules['black']:
    if take_turns % 2 != 0:
        white_pawn = white_pawn_move(*white_pawn)
    elif take_turns % 2 == 0:
        black_pawn = black_pawn_move(*black_pawn)
    take_turns += 1
    [print(*matrix[row]) for row in range(matrix_size)]
    print()


def print_board(board):
    for row in board:
        print(" ".join(row))
    print()



##########: variant 5 solution Bilyana Panova :##########

SIZE = 8


def find_players():
    white_p = []
    black_p = []
    for r in range(SIZE):
        for c in range(SIZE):
            if play_ground[r][c] == "w":
                white_p.extend([r, c])
            elif play_ground[r][c] == "b":
                black_p.extend([r, c])
    return white_p, black_p


def check_diagonals(args):
    directions = {"left up": [-1, -1], "left down": [1, -1], "right up": [-1, 1], "right down": [1, 1]}
    for d in directions.keys():
        r, c = [x + y for x, y in zip(args, directions[d])]
        if r in range(SIZE) and c in range(SIZE):
            if play_ground[r][c] != "-":
                return r, c
    return False


def move(playground, *args):
    winner = "White" if counter % 2 == 0 else "Black"
    m = 1 if counter % 2 == 0 else -1
    r, c = args[0] - m, args[1]
    diagonals = check_diagonals(args)

    if diagonals:
        return f"Game over! {winner} win, capture on {chr(97 + diagonals[1]) + str(SIZE - diagonals[0])}."
    if r != 0 and r != 7:
        playground[r][c] = winner[0].lower()
        playground[args[0]][args[1]] = "-"
        return playground

    return f"Game over! {winner} pawn is promoted to a queen at {chr(97 + c) + str(SIZE - r)}."


play_ground = [input().split() for _ in range(SIZE)]
counter = 0
while True:

    try:
        white_pawn, black_pawn = find_players()
    except IndexError:
        print(play_ground)
        break

    player = white_pawn if counter % 2 == 0 else black_pawn
    play_ground = move(play_ground, *player)
    counter += 1

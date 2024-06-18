# ******* Advanced Retake Exam - 13 December 2023 ******* #

# *******  02_the_gambler  ******* #

# *******  TASK CONDITION  ******* #
"""
https://judge.softuni.org/Contests/Practice/Index/4226#1

You will be given an integer n for the size of the game board (square shape).
On the next n lines, you will receive the rows of the board.
The gambler will start at a random position, marked with the letter 'G' and have an initial
    'entering the game' amount of 100$.

On each turn, until command 'end' is received, you will receive commands for the direction,
in which the gambler should move. The commands will be "up", "down", "left" and "right".

•	If a position with '-' (dash) is reached, it means that the field is empty and the gambler awaits its next direction.

•	If the position marked with the letter 'W' is reached the gambler takes it and adds 100$ to his amount
•	If the position marked with the letter 'P' (penalty) is reached decrease the gambler's total amount by 200$
•	If the position marked with the letter 'J' is reached the gambler wins the jackpot and adds 100000$ to his amount and the game ends.
•	If the gambler leaves the boundaries of the board or his total amount becomes equal to or drops below 0 (zero), he loses everything and you should stop the program.

The current gambler position should be marked with 'G'
When the gambler leaves a position marked with a letter it should be replaced by '-' (dash)

The program ends when one of these four events occurs:
•	the gambler leaves the board boundaries
•	command 'end' is received
•	the gambler's total winning amount is equal to or drops below 0(zero)
•	the position marked with 'J' is reached


Input
•	On the first line, you are given the integer n – the size of the matrix (board).
•	The next n lines hold the values for every row.
•	On each of the next lines, you will get a direction command.

Output
•	If you win the jackpot on the first and second lines print:
    "You win the Jackpot!
End of the game. Total amount: {amount}$"
•	If you do not win the jackpot print:
    "End of the game. Total amount: {amount}$"
•	If you leave the boundaries of the matrix or the gambler's amount becomes 0(zero) or below print:
    "Game over! You lost everything!"

Constraints
•	The square matrix (board) size will be between [4…10].
•	Gambler's starting position will always be marked with 'G'.
•	There will always be a field marked with 'W' and it may appear more than once.
•	There will be always one field marked with 'J'.
•	There will always be one or two fields marked with 'P'.
•	You will always receive enough commands to end the game.
•	Finally if you have any amount print the matrix.
Examples

Input
4
W-GW
W--W
--P-
----
down
down
end


Output
Game over! You lost everything!


Comment
The movement starts from position [0,2] after receiving the command "down" the gambler moves to position [1,2] where there is a '-' (dash) field - nothing is happening. The next command is "down" again, the gambler lands on a 'P' (penalty) field and since he has to pay 200$ his sum becomes negative (100 – 200 = -100) and therefore loses it. The game ends.


Input
4
G---
WWWW
P---
PJ--
right
right
right
down
left
left
end


Output
End of the game. Total amount: 400$
----
WG--
P---
PJ--


Input
4
---G
W-W-
---P
--JW
left
down
down
down
right
end


Output
You win the Jackpot!
End of the game. Total amount: 100200$
----
W---
---P
--GW



"""


##########: variant 1 :##########

def directions(position, direction, rows, matrix):
    row, col = position
    matrix[row][col] = "-"

    moves = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
    }

    d_row, d_col = moves[direction]
    row += d_row
    col += d_col
    if 0 <= row < rows and 0 <= col < rows:
        return row, col, matrix
    return None

def main():
    rows = int(input())
    game_board = []
    gambler = "G"
    amount = 0
    position = (-1, -1)

    neshto = {
        'W': 100,
        'P': -200,
        'J': 100000
    }

    for row_ in range(rows):
        line = list(input())
        if gambler in line:
            amount += 100
            position = (row_, line.index(gambler))
        game_board.append(line)

    target = input()

    while target != "end":
        result = directions(position, target, rows, game_board)
        if result is None:
            print("Game over! You lost everything!")
            return
        else:
            new_row, new_col, game_board = result
            new_position = (new_row, new_col)

            step = game_board[new_row][new_col]

            if step in neshto:
                amount += neshto[step]
                if amount <= 0:
                    print("Game over! You lost everything!")
                    return
                if step == "J":
                    game_board[new_row][new_col] = gambler
                    print("You win the Jackpot!")
                    break

            game_board[new_row][new_col] = gambler
            position = new_position

        target = input()

    print(f"End of the game. Total amount: {amount}$")
    for pr in game_board:
        print("".join(pr))

if __name__ == "__main__":
    main()

##########: variant 2 whit Functions :##########

def directions(position, direction, rows, matrix):
    row, col = position
    matrix[row][col] = "-"

    moves = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
    }

    d_row, d_col = moves[direction]
    row += d_row
    col += d_col
    if 0 <= row < rows and 0 <= col < rows:
        return row, col, matrix
    return None


def create_game_board(rows, gambler):
    game_board = []
    position = (-1, -1)
    amount = 0

    for row_ in range(rows):
        line = list(input())
        if gambler in line:
            amount += 100
            position = (row_, line.index(gambler))
        game_board.append(line)

    return game_board, position, amount


def print_game_board(game_board):
    for row in game_board:
        print("".join(row))


def get_field_rewards(symbol):
    rewards = {
        "W": 100,
        "P": -200,
        "J": 100000
    }
    return rewards.get(symbol, 0)


def main():
    rows = int(input())
    gambler = "G"

    game_board, position, amount = create_game_board(rows, gambler)

    target = input()

    while target != "end":
        result = directions(position, target, rows, game_board)
        if result is None:
            print("Game over! You lost everything!")
            return
        else:
            new_row, new_col, game_board = result
            new_position = (new_row, new_col)

            step = game_board[new_row][new_col]
            reward = get_field_rewards(step)

            amount += reward
            if amount <= 0:
                print("Game over! You lost everything!")
                return
            if step == "J":
                game_board[new_row][new_col] = gambler
                print("You win the Jackpot!")
                break

            game_board[new_row][new_col] = gambler
            position = new_position

        target = input()

    print(f"End of the game. Total amount: {amount}$")
    print_game_board(game_board)


if __name__ == "__main__":
    main()


##########: variant 3 solution CEO :##########

def create_matrix_and_find_player(field_size: int, player_symbol: str):
    player_row, player_col = 0, 0
    matrix = []
    for row in range(field_size):
        current_row = list(input())

        if player_symbol in current_row:
            player_row = row
            player_col = current_row.index(player_symbol)
            current_row[player_col] = "-"

        matrix.append(current_row)

    return matrix, player_row, player_col


def get_direction(direction: str):
    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1),
    }

    return directions[direction]


def valid_index(row: int, col: int, field_size: int):
    return 0 <= row < field_size and 0 <= col < field_size


def get_field_rewards(symbol: str):
    rewards = {
        "W": 100,
        "P": -200,
        "J": 100_000,
    }

    return rewards.get(symbol, 0)


def main():
    matrix_size = int(input())

    matrix, start_row, start_col = create_matrix_and_find_player(matrix_size, "G")
    money_left = 100

    command = input()
    while command != "end":
        next_row, next_col = get_direction(command)
        start_row += next_row
        start_col += next_col

        if not valid_index(start_row, start_col, matrix_size):
            print("Game over! You lost everything!")
            break

        money_left += get_field_rewards(matrix[start_row][start_col])
        matrix[start_row][start_col] = "-"
        if money_left > 20_001:
            print("You win the Jackpot!")
            print(f"End of the game. Total amount: {money_left}$")
            break

        if money_left <= 0:
            print("Game over! You lost everything!")
            break

        command = input()

    else:
        print(f"End of the game. Total amount: {money_left}$")

    if money_left > 0:
        matrix[start_row][start_col] = "G"
        for row in matrix:
            print("".join(row))


main()



##########: variant 3 solution SoftUni :##########

# # Function to handle the current position of the gambler
# def handle_current_position(position, board, sum_val, jackpot):
#     current_char = board[position[0]][position[1]]
#
#     if current_char == 'J':
#         sum_val += 100000
#         jackpot = True
#     elif current_char == 'W':
#         sum_val += 100
#     elif current_char == 'P':
#         sum_val -= 200
#
#     board[position[0]][position[1]] = 'G'
#
#     return sum_val, jackpot
#
#
# # Function to check if the total amount becomes zero or negative
# def zero_amount(sum_val):
#     return sum_val <= 0
#
#
# # Function to print the game over message
# def game_over():
#     print("Game over! You lost everything!")
#
#
# # Function to move the gambler on the board based on the command
# def move_gambler(command, position, board):
#     row, col = position
#     board[row][col] = '-'
#     if command == "up":
#         position[0] -= 1
#     elif command == "down":
#         position[0] += 1
#     elif command == "left":
#         position[1] -= 1
#     elif command == "right":
#         position[1] += 1
#
#     return position
#
#
# # Function to check if the gambler is out of bounds
# def is_out_of_bounds(position, size):
#     return position[0] < 0 or position[0] >= size or position[1] < 0 or position[1] >= size
#
#
# # Function to find the starting position of the gambler
# def find_start_position(size, fishing_area):
#     for i in range(size):
#         for j in range(size):
#             if fishing_area[i][j] == 'G':
#                 return [i, j]
#     return None
#
#
# # Function to fill the board with input data
# def fill_board(size):
#     board = []
#     for _ in range(size):
#         board.append(list(input()))
#     return board
#
#
# size = int(input())
# board = fill_board(size)
# current_position = find_start_position(size, board)
# sum_val = 100
# jackpot = False
#
# while True:
#     if jackpot:
#         print("You win the Jackpot!")
#         break
#     command = input()
#
#     if current_position:
#         current_position = move_gambler(command, current_position, board)
#
#     if is_out_of_bounds(current_position, size) or zero_amount(sum_val):
#         game_over()
#         break
#     else:
#         sum_val, jackpot = handle_current_position(current_position, board, sum_val, jackpot)
#
#     if command == "end":
#         break
#
# if not (is_out_of_bounds(current_position, size) or zero_amount(sum_val)):
#     print(f"End of the game. Total amount: {sum_val}$")
#     for row in board:
#         print(''.join(row))

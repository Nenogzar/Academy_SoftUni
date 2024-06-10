# ******* Advanced Retake Exam - 14 April 2021 ******* #

# *******  02_darts  ******* #

# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/2828#1

Two players bare-handedly throw small sharp-pointed missiles known as darts at a round target known as a dartboard. 
Who is going to win this game?

You will be given a matrix with 7 rows and 7 columns representing the dartboard. For example:
1	2	3	4	5	6	7
24	D	D	D	D	D	8
23	D	T	T	T	D	9
22	D	T	B	T	D	10
21	D	T	T	T	D	11
20	D	D	D	D	D	12
19	18	17	16	15	14	13

Each of the two players starts with a score of 501 and they take turns to throw a dart – one throw for each player. 
The score for each turn is deducted from the player’s total score. 

The first player who reduces their score to zero or less wins the game.

You are going to receive the information for every throw on a separate line. 
The coordinate information of a hit will be in the format: "({row}, {column})".

•	If a player hits outside the dartboard, he does not score any points.
•	If a player hits a number, it is deducted from his total.
•	If a player hits a "D" 
        the sum of the 4 corresponding numbers per column and row is doubled and then deducted from his total.
•	If a player hits a "T" 
        the sum of the 4 corresponding numbers per column and row is tripled and then deducted from his total.
•	"B" is the bullseye. 
        If a player hits it, he wins the game, and the program ends.
        
For example, if Peter hits position with coordinates (2, 1), he wins (23 + 2 + 9 + 18) * 2 = 104 points and they are deducted from his total.
Your job is to find who won the game and with how many turns.

Input

•	The name of the first player and the name of the second player, separated by ", "
•	7 lines – the dartboard (separated by single space)
•	On the next lines - the coordinates in the format: "({row}, {column})"


Output
•	You should print only one line containing the winner and his count of throws: 
"{name} won the game with {count_turns} throws!"

Constrains
•	There will always be exactly 7 lines
•	There will always be a winner
•	The points will be in range [1, 24]
•	The coordinates will be in range [0, 100]
Examples

"""

##########: variant 1 :##########
def convert_element(element):
    try:
        return int(element)
    except ValueError:
        return element


def outside_the_dartboard(row, col, rows, cols):
    return not (0 <= row < rows and 0 <= col < cols)


def calculate_points(dartboard, row, col):
    if dartboard[row][col] == 'B':
        return 'BULLSEYE'
    if isinstance(dartboard[row][col], int):
        return dartboard[row][col]

    direction_points = [dartboard[row][0], dartboard[row][6], dartboard[0][col], dartboard[6][col]]
    sum_points = sum(direction_points)

    if dartboard[row][col] == 'D':
        return sum_points * 2
    if dartboard[row][col] == 'T':
        return sum_points * 3


def play_darts():
    rows, cols = 7, 7
    player1, player2 = input().split(", ")

    dartboard = [list(map(convert_element, input().split())) for _ in range(rows)]
    # for _ in range(rows):
    #     row = input().split()
    #     dartboard.append([int(x) if x.isdigit() else x for x in row])

    player_scores = {player1: [501, 0], player2: [501, 0]}

    players = [player1, player2]
    current_player_index = 0

    while True:
        current_player = players[current_player_index]
        throw = input()
        row, col = map(int, throw.strip("()").split(", "))

        player_scores[current_player][1] += 1

        if outside_the_dartboard(row, col, rows, cols):
            current_player_index = 1 - current_player_index
            continue

        points = calculate_points(dartboard, row, col)

        if points == 'BULLSEYE':
            print(f"{current_player} won the game with {player_scores[current_player][1]} throws!")
            break

        player_scores[current_player][0] -= points

        if player_scores[current_player][0] <= 0:
            print(f"{current_player} won the game with {player_scores[current_player][1]} throws!")
            break

        current_player_index = 1 - current_player_index


# Example usage
play_darts()

##########: variant 2 :##########

player1, player2 = input().split(", ")

rows, cols = 7, 7
dartboard = []
for _ in range(rows):
    row = input().split()
    dartboard.append([int(x) if x.isdigit() else x for x in row])

player_scores = {player1: [501, 0], player2: [501, 0]}

players = [player1, player2]
current_player_index = 0


def calculate_points(dartboard, row, col):
    if dartboard[row][col] == 'B':
        return 'BULLSEYE'
    if isinstance(dartboard[row][col], int):
        return dartboard[row][col]

    direction_points = [dartboard[row][0], dartboard[row][6], dartboard[0][col], dartboard[6][col]]
    sum_points = sum(direction_points)

    if dartboard[row][col] == 'D':
        return sum_points * 2
    if dartboard[row][col] == 'T':
        return sum_points * 3


# Цикъл, който продължава, докато някой не спечели
while True:
    current_player = players[current_player_index]  # Текущия играч

    throw = input()
    row, col = map(int, throw.strip("()").split(", "))

    player_scores[current_player][1] += 1  # Увеличаване броя на хвърлянията

    if not (0 <= row < rows and 0 <= col < cols):
        current_player_index = 1 - current_player_index  # Другия играч
        continue

    points = calculate_points(dartboard, row, col)

    if points == 'BULLSEYE':
        print(f"{current_player} won the game with {player_scores[current_player][1]} throws!")
        break

    player_scores[current_player][0] -= points  # Намаляваме точките на играча

    if player_scores[current_player][0] <= 0:  # Проверяваме дали играчът е спечелил
        print(f"{current_player} won the game with {player_scores[current_player][1]} throws!")
        break

    current_player_index = 1 - current_player_index  # Превключваме към другия играч

##########: variant 3 solution TANER :##########

def check_valid_index(row, col, size_of_matrix):
    if 0 <= row < size_of_matrix and 0 <= col < size_of_matrix:
        return True


def dart_board(row, col, current_player):
    if check_valid_index(row, col, matrix_size):
        result = 0
        for check_row, check_col in (row, -1), (row, 0), (0, col), (-1, col):
            result += matrix[check_row][check_col]
        if matrix[row][col] == "B":
            both_players[current_player]['points'] = 0
        elif matrix[row][col] == "D":
            both_players[current_player]['points'] -= result * 2
        elif matrix[row][col] == "T":
            both_players[current_player]['points'] -= result * 3
        else:
            both_players[current_player]['points'] -= matrix[row][col]


matrix_size = 7
first_player, second_player = input().split(", ")
matrix = [[int(col) if col.isdigit() else col for col in input().split()] for row in range(matrix_size)]
both_players = {
    'player one': {'points': 501, 'throws': 0},
    'player two': {'points': 501, 'throws': 0}
}
take_turns = 1
while both_players['player one']['points'] > 0 and both_players['player two']['points'] > 0:
    current_position = input().split(", ")
    current_row, current_col = int(current_position[0].strip("(")), int(current_position[-1].strip(")"))
    if take_turns % 2 != 0:
        dart_board(current_row, current_col, "player one")
        both_players["player one"]["throws"] += 1
    elif take_turns % 2 == 0:
        dart_board(current_row, current_col, "player two")
        both_players["player two"]["throws"] += 1
    take_turns += 1
if both_players['player one']['points'] <= 0:
    print(f"{first_player} won the game with {both_players['player one']['throws']} throws!")
elif both_players['player two']['points'] <= 0:
    print(f"{second_player} won the game with {both_players['player two']['throws']} throws!")


##########: variant 3 solution CEO :##########

players = [{"name": x, "points": 501} for x in input().split(", ")]
matrix = [[x if x.isalpha() else int(x) for x in input().split()] for _ in range(7)]
trow, SIZE = 0, 7

while True:
    trow += 1
    p_one_row, p_one_col = [int(x) for x in input()[1:-1].split(", ")]

    if 0 <= p_one_row < SIZE and 0 <= p_one_col < SIZE:
        symbol = matrix[p_one_row][p_one_col]
        if str(symbol).isnumeric():
            players[0]["points"] -= symbol
        elif symbol == "B":
            print(f"{players[0]['name']} won the game with {trow} throws!")
            break
        elif symbol == "D":
            total_sum = (matrix[p_one_row][0] + matrix[p_one_row][6] + matrix[0][p_one_col] + matrix[6][p_one_col]) * 2
            players[0]["points"] -= total_sum
        elif symbol == "T":
            total_sum = (matrix[p_one_row][0] + matrix[p_one_row][6] + matrix[0][p_one_col] + matrix[6][p_one_col]) * 3
            players[0]["points"] -= total_sum
        if players[0]["points"] <= 0:
            print(f"{players[0]['name']} won the game with {trow} throws!")
            break

    p_two_row, p_two_col = [int(x) for x in input()[1:-1].split(", ")]

    if 0 <= p_two_row < SIZE and 0 <= p_two_col < SIZE:
        symbol = matrix[p_two_row][p_two_col]
        if str(symbol).isnumeric():
            players[1]["points"] -= symbol
        elif symbol == "B":
            print(f"{players[1]['name']} won the game with {trow} throws!")
            break
        elif symbol == "D":
            total_sum = (matrix[p_two_row][0] + matrix[p_two_row][6] + matrix[0][p_two_col] + matrix[6][p_two_col]) * 2
            players[1]["points"] -= total_sum
        elif symbol == "T":
            total_sum = (matrix[p_two_row][0] + matrix[p_two_row][6] + matrix[0][p_two_col] + matrix[6][p_two_col]) * 3
            players[1]["points"] -= total_sum
        if players[1]["points"] <= 0:
            print(f"{players[1]['name']} won the game with {trow} throws!")
            break

##########: variant 4 solution CEO :##########

player_one, player_two = input().split(", ")

MATRIX_SIZE = 7
game_info = {
            player_one: {"Score": 501, "Turn": 0},
            player_two: {"Score": 501, "Turn": 0},
            "D": 2, "T": 3}

matrix = [[int(x) if x.isdigit() else x for x in input().split()] for row in range(MATRIX_SIZE)]


def check_valid_index(row, col):
    return 0 <= row < MATRIX_SIZE and 0 <= col < MATRIX_SIZE


def get_numbers(row, col , letter):
    total_sum = 0
    for r_num in (0, 6):
        total_sum += matrix[r_num][col]
    for c_col in (0, 6):
        total_sum += matrix[row][c_col]
    return total_sum * game_info[letter]


counter = 0
while game_info[player_one]["Score"] > 0 and game_info[player_two]["Score"] > 0:
    counter += 1

    if counter % 2 != 0:
        player = player_one
        game_info[player]["Turn"] += 1
    else:
        player = player_two
        game_info[player]["Turn"] += 1

    dart_row, dart_col = [int(x) for x in input().replace("(", "").replace(")", "").split(", ")]
    if not check_valid_index(dart_row, dart_col):
        continue
    symbol = matrix[dart_row][dart_col]
    if isinstance(symbol, int):
        sum_to_extract = matrix[dart_row][dart_col]
    elif symbol in "DT":
        sum_to_extract = get_numbers(dart_row, dart_col, symbol)
    elif symbol == "B":
        sum_to_extract = game_info[player]["Score"]

    game_info[player]["Score"] -= sum_to_extract

print(f"{player} won the game with {game_info[player]['Turn']} throws!")
# ******* Advanced Exam - 25 June 2022 ******* #

# *******  02_exit_founder  ******* #

# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/3515#1

Tom and Jerry decided to play a game together.
The game is a maze of which they need to find a way out.
Monitor their moves closely and find out who the winner will be!

First, you will be given the names "Tom" and "Jerry", separated by a comma and a space ", ".
The order in which they are received determines the order in which they will take turns.
The first player starts first.

Next, you will be given a matrix with 6 rows and 6 columns representing the maze board. It consists of:

•	Only one Exit - marked with the "E" letter
•	Trap (one, many, or none) - marked with the "T" letter
•	Wall (one, many, or none) - marked with the "W" letter
•	Empty positions will be marked with "."

In the beginning,
    Tom and Jerry are outside the board.
    On each line, after the matrix is given, you will be receiving coordinates for each of the players.
    They will be taking turns and stepping on different positions
        on the board until one of them find the Exit or falls into a Trap.

Here are the rules:
•	If a player hits the letter "E", he escapes the maze and wins the game.
    Print
        "{player} found the Exit and wins the game!"
    and end the program.

•	If the letter "T" is hit, the player falls into a Trap, the game ends, and his opponent wins automatically.
    Print
        "{player} is out of the game! The winner is {winner}."
     and end the program.

•	If the letter "W" is hit, the player hits a wall, and he needs to rest. The player's next move is ignored.
    Print
        "{player} hits a wall and needs to rest."

•	If a player steps on an empty position ".", nothing happens.
•	Both players can step in the same position at the same time.

Input
•	On the first line, you will receive "Tom" and "Jerry" separated by ", ". The first player starts first.
•	On the following 6 lines, you will receive the maze board (elements will be separated by a space)
•	On the following lines, you will be receiving coordinates in the format: "({row}, {column})"

Output
•	You should print the output as described above.
•	The input coordinates will always be valid.


Еxamples
Input

Tom, Jerry
. . T . . .
. . . . . .
. . W . . .
. . W . . E
. . . . . .
. T . W . .
(3, 2)
(1, 3)
(5, 1)
(5, 1)


Output
Tom hits a wall and needs to rest.
Jerry is out of the game! The winner is Tom.

Comment
First is Tom. He moves to position (3, 2). He hits a wall and needs to rest.
Next is Jerry. He moves to position (1, 3). It is an empty position.
Tom's next move (5, 1) is ignored because he is resting.
Jerry moves to (5, 1). There is a trap, so he is out of the game. The program ends.

Input

Jerry, Tom
. T . . . W
. . . . T .
. W . . . T
. T . E . .
. . . . . T
. . T . . .
(1, 1)
(3, 0)
(3, 3)


Output
Jerry found the Exit and wins the game!


Input
Jerry, Tom
. . . W . .
. . T T . .
. . . . . .
. T . W . .
W . . . E .
. . . W . .
(0, 3)
(3, 3)
(1, 3)
(2, 2)
(3, 5)
(4, 0)
(5, 3)
(3, 1)
(4, 4)
(4, 4)


Output
Jerry hits a wall and needs to rest.
Tom hits a wall and needs to rest.
Tom hits a wall and needs to rest.
Jerry hits a wall and needs to rest.
Tom found the Exit and wins the game!



"""

##########: variant 1 :##########
size = 6

players = {x: {"rest": False} for x in input().split(", ")}
matrix = [input().split() for _ in range(size)]


def find_exit(player):
    print(f"{player[0]} found the Exit and wins the game!")
    exit()


def trap(player):
    print(f"{player[0]} is out of the game! The winner is {player[1]}.")
    exit()


def wall(player):
    players[player[0]]["rest"] = True
    print(f"{player[0]} hits a wall and needs to rest.")


commands = {"E": find_exit, "T": trap, "W": wall}

player_one, player_two = list(players.keys())
player_counter = 0

while True:
    input_row, input_col = [int(x) for x in input().strip("()").split(", ")]
    player_counter += 1
    if player_counter % 2 == 0:
        player = (player_two, player_one)
    else:
        player = (player_one, player_two)
    if players[player[0]]["rest"]:
        players[player[0]]["rest"] = False
        continue
    player_steps_on = matrix[input_row][input_col]
    if player_steps_on != ".":
        commands[player_steps_on](player)



##########: variant 2 :##########

def move(current_player, row, col):

    if matrix[row][col] == "E":
        players[current_player]['won'] = True
        print(f"{current_player} found the Exit and wins the game!")

    elif matrix[row][col] == "T":
        players[current_player]['trapped'] = True
        winner = ''.join([name for name in players if current_player != name])
        print(f"{current_player} is out of the game! The winner is {winner}.")

    elif matrix[row][col] == "W":
        players[current_player]['rest'] = True
        print(f"{current_player} hits a wall and needs to rest.")


matrix_size = 6
player_one, player_two = input().split(", ")
matrix = [[col for col in input().split()] for row in range(matrix_size)]

players = {
    player_one: {'trapped': False, 'won': False, 'rest': False},
    player_two: {'trapped': False, 'won': False, 'rest': False}
}

counter = 1

while not players[player_one]['trapped'] and not players[player_one]['won'] and not \
     players[player_two]['trapped'] and not players[player_two]['won']:

    next_position = input()

    row, col = int(next_position[1]), int(next_position[-2])

    if counter % 2 != 0:
        if not players[player_one]['rest']:
            move(player_one, row, col)
        elif players[player_one]['rest']:
            players[player_one]['rest'] = False
    else:
        if not players[player_two]['rest']:
            move(player_two, row, col)
        elif players[player_two]['rest']:
            players[player_two]['rest'] = False
    counter += 1


##########: variant 3 solution SoftUni :##########

first_player, second_player = input().split(", ")

maze_board = []

for _ in range(6):
    maze_board.append(input().split())

first_player_needs_rest = False
second_player_needs_rest = False

while True:
    first_player_coordinates = input()
    if not first_player_needs_rest:
        row, column = map(int, first_player_coordinates.strip("()").split(", "))
        position = maze_board[row][column]
        if position == 'E':
            print(f"{first_player} found the Exit and wins the game!")
            break
        if position == 'T':
            print(f"{first_player} is out of the game! The winner is {second_player}.")
            break
        if position == 'W':
            print(f"{first_player} hits a wall and needs to rest.")
            first_player_needs_rest = True
    else:
        first_player_needs_rest = False

    second_player_coordinates = input()
    if not second_player_needs_rest:
        row, column = map(int, second_player_coordinates.strip("()").split(", "))
        position = maze_board[row][column]
        if position == 'E':
            print(f"{second_player} found the Exit and wins the game!")
            break
        if position == 'T':
            print(f"{second_player} is out of the game! The winner is {first_player}.")
            break
        if position == 'W':
            print(f"{second_player} hits a wall and needs to rest.")
            second_player_needs_rest = True
    else:
        second_player_needs_rest = False


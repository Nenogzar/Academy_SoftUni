#################################### TASK CONDITION ############################
"""
                       5.	Alice in Wonderland
Alice is going to the mad tea party, to see her friends. On the way to 
the party, she needs to collect bags of tea.
You will be given an integer n for the size of the Wonderland territory 
with a square shape. On the following n lines, you will receive the rows of the territory:
•	Alice will be placed in a random position, marked with the letter "A". 
•	On the territory, there will be bags of tea, represented as numbers. 
If Alice steps on a number position, she collects the tea bags and increases 
the quantity with the corresponding number.
•	There will always be one rabbit hole on the territory marked with the letter "R".
•	All of the empty positions will be marked with ".".
After the field state, you will be given commands for Alice's movements. 
Move commands can be: "up", "down", "left" or "right".
When Alice collects at least 10 bags of tea, she is ready to go to the tea 
party, and she does not need to continue collecting. Otherwise, if she steps
on the rabbit hole or goes out of the territory, she can't return, and the program ends. 
In the end, the path she walked had to be marked with '*'.
For more clarifications, see the examples below.
Input
•	On the first line, you will be given the integer n – the size of the square matrix
•	On the following n lines - matrix representing the field (each position separated by a single space)
•	On each of the following lines, you will be given a move command
Output
•	On the first line: 
o	If Alice steps on the rabbit hole or she go out of the territory, print: 
"Alice didn't make it to the tea party."
o	If she collected at least 10 bags of tea, print: 
"She did it! She went to the party."
•	On the following lines, print the matrix.
Constraints
•	Alice will always either go outside the Wonderland or collect 10 bags of tea
•	All the commands will be valid
•	All of the given numbers will be valid integers in the range [0, 10]

____________________________________________________________________________________________
Example_01

Input
5
. A . . 1
R . 2 . .
4 7 . 1 .
. . . 2 .
. 3 . . .
down
right
left
down
up
left	

Output
Alice didn't make it to the tea party.
. * . . 1
* * * . .
4 * . 1 .
. . . 2 .
. 3 . . .

____________________________________________________________________________________________
Example_02

Input
7
. A . 1 1 . .
9 . . . 6 . 5
. 6 . R . . .
. 3 . . 1 . .
. . . 2 . . 2
. 3 . . 1 . .
. 8 3 . . . 2
left
down
down
right	

Output
She did it! She went to the party.
* * . 1 1 . .
* . . . 6 . 5
* * . R . . .
. 3 . . 1 . .
. . . 2 . . 2
. 3 . . 1 . .
. 8 3 . . . 2


"""


""" 1 """

ALICE, RABBIT_HOLE, EMPTY, VISITED = "A", "R", ".", "*"
DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}

size = int(input())

wonderland = []
row, col = None, None  # Alice position (start position)
for r in range(size):
    line = [x for x in input().split()]
    if ALICE in line:
        row, col = r, line.index(ALICE)
        line[col] = VISITED
    wonderland.append(line)

tea_collected = 0
while tea_collected < 10:
    command = input()
    r0, c0 = DIRECTIONS[command]
    next_r = row + r0
    next_c = col + c0

    if next_r < 0 or next_c < 0 or next_r >= size or next_c >= size:
        break
    elif wonderland[next_r][next_c] == RABBIT_HOLE:
        wonderland[next_r][next_c] = VISITED
        break

    if wonderland[next_r][next_c].isnumeric():
        tea_collected += int(wonderland[next_r][next_c])
    wonderland[next_r][next_c] = VISITED
    row, col = next_r, next_c

if tea_collected < 10:
    print(f"Alice didn't make it to the tea party.")
else:
    print(f"She did it! She went to the party.")
[print(*row) for row in wonderland]



""" 2 """

ALICE, RABBIT_HOLE, EMPTY, VISITED = "A", "R", ".", "*"

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}


def alice_move(mtrx, direct, pos):
    r, c = pos[0], pos[1]
    mtrx[r][c] = VISITED

    r += directions[direct][0]
    c += directions[direct][1]
    tea = 0

    if 0 <= r < len(mtrx) and 0 <= c < len(mtrx[0]):
        if mtrx[r][c].isnumeric():
            tea = int(mtrx[r][c])
        elif mtrx[r][c] == RABBIT_HOLE:
            mtrx[r][c] = VISITED
            return pos, tea

        mtrx[r][c] = VISITED
        return (r, c), tea

    return pos, tea


size = int(input())
territory = []
alice_position = None
for i in range(size):
    line = input().split()
    if ALICE in line:
        alice_position = (i, line.index(ALICE))
    territory.append(line)

collected_tea = 0
while collected_tea < 10:
    direction = input()
    new_position, current_tea = alice_move(territory, direction, alice_position)
    if new_position == alice_position:
        break
    alice_position = new_position
    collected_tea += current_tea

if collected_tea < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

[print(*territory[row], sep=" ") for row in range(size)]


""" 3 """

rows = int(input())
matrix = [[x for x in input().split()] for _ in range(rows)]
cols = len(matrix[0])

score, movement = [0], {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}


def check_movement(row, col):
    if 0 <= row < rows and 0 <= col < cols and matrix[row][col] != "R":
        return True
    print("Alice didn't make it to the tea party.")
    rabit_row, rabit_col = find_position("R", False)
    if rabit_row + rabit_col == row + col:
        matrix[row][col] = "*"
    show_result()
    exit()


def find_position(symbol, alice=True):
    for row in range(rows):
        if symbol in matrix[row]:
            col = matrix[row].index(symbol)
            if alice:
                matrix[row][col] = "*"
            return row, col


alice_row, alice_col = find_position("A")


def alice_movement(row, col, movement_pos):
    move_row, move_col = row + movement[movement_pos][0], col + movement[movement_pos][1]
    if check_movement(move_row, move_col):
        if matrix[move_row][move_col][-1].isdigit():
            score[0] += int(matrix[move_row][move_col])
        matrix[move_row][move_col] = "*"
    return move_row, move_col


def show_result():
    [print(*matrix[row]) for row in range(rows)]


while score[0] < 10:
    command = input()
    alice_row, alice_col = alice_movement(alice_row, alice_col, command)

print("She did it! She went to the party.")
show_result()


""" 4 """


from collections import deque


class AliceInWonderland:

    def __init__(self):
        self.output_message = ''
        self.size = int(input())
        self.wonderland = []
        self.alice_pos = []
        self.collected_teabags = 0
        self.finish = False
        self.moves = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }
        self.main_meth()

    def main_meth(self):
        self.create_wonderland_find_alice()
        self.alice_journey_in_wonderland()
        self.prepare_output_message()

    def create_wonderland_find_alice(self):
        for row in range(self.size):
            line = input().split()
            self.wonderland.append(line)
            if 'A' in line:
                self.alice_pos = [row, line.index('A')]
                self.wonderland[row][self.alice_pos[1]] = '*'

    def check_move_of_alice(self, row, col):
        if 0 <= row < self.size and 0 <= col < self.size:
            symbol = self.wonderland[row][col]
            if symbol == 'R':
                self.finish = True
            elif symbol.isdigit():
                self.collected_teabags += int(symbol)
            self.wonderland[row][col] = '*'
            self.alice_pos = [row, col]
        else:
            self.finish = True

    def alice_journey_in_wonderland(self):
        while True:
            direction = input()
            if not direction:
                break
            alice_row = self.alice_pos[0] + self.moves[direction][0]
            alice_col = self.alice_pos[1] + self.moves[direction][1]
            self.check_move_of_alice(alice_row, alice_col)

            if self.collected_teabags >= 10 or self.finish:
                break

    def prepare_output_message(self):
        if self.collected_teabags >= 10:
            self.output_message = 'She did it! She went to the party.'
        elif self.finish:
            self.output_message = "Alice didn't make it to the tea party."
        self.output_message += '\n' + '\n'.join(' '.join(row) for row in self.wonderland)

    def __repr__(self):
        return self.output_message


if __name__ == '__main__':
    print(AliceInWonderland())



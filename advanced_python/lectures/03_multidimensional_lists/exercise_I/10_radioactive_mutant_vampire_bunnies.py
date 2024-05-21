#################################### TASK CONDITION ############################
"""
                10.	*Radioactive Mutant Vampire Bunnies
You come across an old JS Basics teamwork game. It is about bunnies that 
multiply extremely fast. There's also a player that should escape from their 
lair. You like the game, so you decide to port it to Python because that's 
your language of choice. The last thing left is the algorithm that determines 
if the player will escape the lair or not. First, you will receive a line 
holding integers N and M, representing the  lair's rows and columns. 
Next, you receive N strings that can consist only of ".", "B", "P". They 
represent the initial state of the lair. There will be only one player. 
The bunnies are marked with "B", the player is marked with "P", and 
everything else is free space, marked with a dot ".".  Then you will receive 
a string with commands (e.g., LRRULUD) - each letter represents the next move
of the player:
•	L - the player should move one position to the left
•	R - the player should move one position to the right
•	U - the player should move one position up
•	D - the player should move one position down
After every step made, each bunny spreads one position up, down, left, and right. 
If the player moves to a bunny cell or a bunny reaches the player, the player dies. 
If the player goes out of the lair without encountering a bunny, the player wins.
When the player dies or wins, the game ends. All the activities for this turn 
continue (e.g., all the bunnies spread normally), but there are no more turns. 
There will be no cases where the moves of the player end before he dies or escapes.
In the end, print the final state of the lair with every row on a separate line. 
On the last line, print either "dead: {row} {col}" or "won: {row} {col}". 
"Row" and "col" are the cell coordinates where the player has died or the last 
cell he has been in before escaping the lair.
Input
•	On the first line of input, the numbers N and M are 
received - the number of rows and columns in the lair
•	On the following N lines, each row is received in the form of a
string. The string will contain only ".", "B", "P". All strings will 
be the same length. There will be only one "P" for all the input
•	On the last line, the directions are received in the form of a string, 
containing "R", "L", "U", "D"
Output
•	On the first N lines, print the final state of the bunny lair
•	On the last line, print:
o	If the player won - "won: {row} {col}"
o	If the player dies - "dead: {row} {col}"
Constraints
•	The dimensions of the lair are in the range [3…20]
•	The directions string length is in the range [1…20]

____________________________________________________________________________________________
Example_01

Input
5 6
.....P
......
...B..
......
......
ULDDDR

Output
......
...B..
..BBB.
...B..
......
won: 0 5	

____________________________________________________________________________________________
Example_02

Input
4 5
.....
.....
.B...
...P.
LLLLLLLL

Output
.B...
BBB..
BBBB.
BBB..
dead: 3 1

____________________________________________________________________________________________
Example_01

Input
5 8
.......B
...B....
....B..B
........
..P.....
ULLL

Output
BBBBBBBB
BBBBBBBB
BBBBBBBB
.BBBBBBB
..BBBBBB
won: 3 0



"""
""" 1 """

rows, cols = [int(num) for num in input().split()]
matrix = [[char for char in input()] for _ in range(rows)]
commands = input()

winner, movement = False, {
    "U": [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1]
}


def find_player_position():
    for row in range(rows):
        if "P" in matrix[row]:
            return row, matrix[row].index("P")


def player_alive(row, col):
    if matrix[row][col] == "B":
        show_result("dead")


def check_valid_index(row, col, player=False):
    global winner

    if 0 <= row < rows and 0 <= col < cols:
        return True

    if player:
        winner = True


def bunnies_position():
    position = []

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == "B":
                position.append(row)
                position.append(col)
    return position


def bunnies_moves(bunnies_pos):
    for i in range(0, len(bunnies_pos), 2):
        row, col = bunnies_pos[i], bunnies_pos[i + 1]
        for bunnie_move in movement:
            new_row, new_col = row + movement[bunnie_move][0], col + movement[bunnie_move][1]
            if check_valid_index(new_row, new_col):
                matrix[new_row][new_col] = "B"


def show_result(status="won"):
    [print(*matrix[row], sep="") for row in range(rows)]
    print(f"{status}: {player_row} {player_col}")
    exit()


player_row, player_col = find_player_position()
matrix[player_row][player_col] = "."

for command in commands:

    player_movement_row, player_movement_col = player_row + movement[command][0], player_col + movement[command][1]

    if check_valid_index(player_movement_row, player_movement_col, True):
        player_row, player_col = player_movement_row, player_movement_col

    bunnies_moves(bunnies_position())

    if winner:
        show_result()

    if check_valid_index(player_movement_row, player_movement_col):
        player_alive(player_movement_row, player_movement_col)



""" 2 """

def get_player_location(command, start_row, start_col):
    r, c = 0, 0
    if command == "L":
        r, c = start_row, start_col-1
    elif command == "R":
        r, c = start_row, start_col+1
    elif command == "U":
        r, c = start_row-1, start_col
    elif command == "D":
        r, c = start_row+1, start_col
    return r, c


def bunnies_after_turn(rows, cols, def_bunnies):
    temp_bunnies = set()
    for b in def_bunnies:
        r, c = b

        if 0 <= r - 1 < rows and 0 <= c < cols:
            temp_bunnies.add((r - 1, c))
        if 0 <= r + 1 < rows and 0 <= c < cols:
            temp_bunnies.add((r + 1, c))
        if 0 <= r < rows and 0 <= c - 1 < cols:
            temp_bunnies.add((r, c - 1))
        if 0 <= r < rows and 0 <= c + 1 < cols:
            temp_bunnies.add((r, c + 1))

    def_bunnies = def_bunnies.union(temp_bunnies)

    return def_bunnies


n, m = [int(x) for x in input().split()]
mm = []
bunnies = set()
player_row, player_col = 0, 0

for i in range(n):
    row = []
    line = input()
    for ch in line:
        row.append(ch)
    mm.append(row)

for i in range(n):
    for j in range(m):
        if mm[i][j] == "P":
            player_row, player_col = i, j
        if mm[i][j] == "B":
            bunnies.add((i, j))

mm[player_row][player_col] = "."
commands = input()

for com in commands:
    bunnies = bunnies_after_turn(n, m, bunnies)
    for bunny in bunnies:
        b_r, b_c = bunny
        mm[b_r][b_c] = "B"
    next_row, next_col = get_player_location(com, player_row, player_col)
    if next_row < 0 or next_row >= n or next_col < 0 or next_col >= m:
        for row in mm:
            print(*row, sep="")
        print(f"won: {player_row} {player_col}")
        break
    player_row, player_col = next_row, next_col
    if (player_row, player_col) in bunnies:
        for row in mm:
            print(*row, sep="")
        print(f"dead: {player_row} {player_col}")
        break


""" 3 """


def get_next_pos(row, col, command):
    if command == 'U':
        return row - 1, col
    if command == 'D':
        return row + 1, col
    if command == 'L':
        return row, col - 1
    if command == 'R':
        return row, col + 1


def is_outside(row, col, rows, cols):
    return row < 0 or col < 0 or row >= rows or col >= cols


def get_children(row, col, rows, cols):
    possible_children = [
        [row - 1, col],
        [row, col - 1],
        [row, col + 1],
        [row + 1, col]
    ]

    result = []
    for child_row, child_col in possible_children:
        if not is_outside(child_row, child_col, rows, cols):
            result.append([child_row, child_col])

    return result


rows, cols = [int(x) for x in input().split()]

bunnies = set()
player_row = 0
player_col = 0

matrix = []

for row in range(rows):
    # .....P
    row_elements = list(input())
    for col in range(cols):
        if row_elements[col] == 'P':
            player_row = row
            player_col = col
        elif row_elements[col] == 'B':
            bunnies.add(f'{row} {col}')
    matrix.append(row_elements)

commands = input()

won = False
dead = False

for command in commands:
    next_row, next_col = get_next_pos(player_row, player_col, command)
    matrix[player_row][player_col] = '.'

    if is_outside(next_row, next_col, rows, cols):
        won = True
    elif matrix[next_row][next_col] == 'B':
        dead = True
        player_row, player_col = next_row, next_col
    else:
        matrix[next_row][next_col] = 'P'
        player_row, player_col = next_row, next_col

    new_bunnies = set()
    for bunny in bunnies:
        bunny_row, bunny_col = [int(x) for x in bunny.split()]
        children = get_children(bunny_row, bunny_col, rows, cols)
        for child_row, child_col in children:
            new_bunnies.add(f'{child_row} {child_col}')
            matrix[child_row][child_col] = 'B'
            if child_row == player_row and child_col == player_col:
                dead = True

    bunnies = bunnies.union(new_bunnies)

    if won or dead:
        break

for row in matrix:
    print(''.join(row))

if won:
    print(f'won: {player_row} {player_col}')
else:
    print(f'dead: {player_row} {player_col}')




""" 4 """


from collections import deque


class RadioactiveBunnies:

    def __init__(self):
        self.output_message = ''
        self.rows = 0
        self.cols = 0
        self.lair = []
        self.player_pos = []
        self.bunnies_locations = deque()
        self.actions = deque()
        self.dead = False
        self.exit = False
        self.moves = {
            'U': (-1, 0),
            'D': (1, 0),
            'L': (0, -1),
            'R': (0, 1)
        }
        self.main_meth()

    def main_meth(self):
        self.define_rows_cols_for_lair()
        self.fill_lair_with_elements()
        self.define_commands_for_player()
        self.start_to_play_the_game()
        self.prepare_output_message()

    def define_rows_cols_for_lair(self):
        self.rows, self.cols = [int(x) for x in input().split()]

    def fill_lair_with_elements(self):
        for row in range(self.rows):
            line = list(input())
            self.lair.append(line)
            if 'P' in line:
                self.player_pos = [row, line.index('P')]

    def define_commands_for_player(self):
        self.actions = deque(input())

    def start_to_play_the_game(self):
        while self.actions and not self.dead and not self.exit:
            self.move_player_in_lair_field(self.actions.popleft())
            self.spread_bunnies_in_lair_field()

    def move_player_in_lair_field(self, way):
        self.lair[self.player_pos[0]][self.player_pos[1]] = '.'
        row = self.player_pos[0] + self.moves[way][0]
        col = self.player_pos[1] + self.moves[way][1]
        if 0 <= row < self.rows and 0 <= col < self.cols:
            symbol = self.lair[row][col]
            if symbol == 'B':
                self.dead = True
            else:
                self.lair[row][col] = 'P'
            self.player_pos = [row, col]
        else:
            self.exit = True

    def spread_bunnies_in_lair_field(self):
        self.find_existing_bunnies()
        while self.bunnies_locations:
            bunny = self.bunnies_locations.popleft()
            self.move_bunny_on_field(bunny)

    def find_existing_bunnies(self):
        for row in range(self.rows):
            for col in range(self.cols):
                symbol = self.lair[row][col]
                if symbol == 'B':
                    self.bunnies_locations.append([row, col])

    def move_bunny_on_field(self, bunny):
        for move in self.moves:
            row_bunny = bunny[0] + self.moves[move][0]
            col_bunny = bunny[1] + self.moves[move][1]
            if 0 <= row_bunny < self.rows and 0 <= col_bunny < self.cols:
                symbol = self.lair[row_bunny][col_bunny]
                if symbol in ['.', 'P']:
                    if symbol == 'P':
                        self.dead = True
                    self.lair[row_bunny][col_bunny] = 'B'

    def prepare_output_message(self):
        self.output_message = '\n'.join(''.join(r) for r in self.lair)
        self.output_message += f'\n{"dead:" if self.dead else "won:"} {" ".join(map(str, self.player_pos))}'

    def __repr__(self):
        return self.output_message


if __name__ == '__main__':
    print(RadioactiveBunnies())



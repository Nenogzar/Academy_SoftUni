#################################### TASK CONDITION ############################
"""
                              06. Range Day
You are participating in a Firearm course. It is a training day at 
the shooting range. You will be given a matrix with 5 rows and 5 columns. 
It is a shotgun range represented as some symbols separated by a single space:
•	Your position is marked with the symbol "A"
•	Targets marked with symbol "x"
•	All of the empty positions will be marked with "."
After the field state, you will be given an integer representing the number 
of commands you will receive. The possible commands are:
•	"move {right/left/up/down} {steps}" – you should move in the given 
direction with the given steps. You can only move if the field you want 
to step on is marked with ".".
•	"shoot {right/left/up/down}" – you should shoot in the given direction 
(from your current position without moving). Beware that there might be 
targets that stand in the way of other targets, and you cannot reach
them - you can shoot only the nearest target. When you have shot a target, 
the field becomes empty position (".").
Validate the positions since they can be outside the field.
Keep track of all the shot targets:
•	If at any point there are no targets left, end the program and print: 
"Training completed! All {count_targets} targets hit.". 
•	If, after you perform all the commands, there are some targets left print: 
"Training not completed! {count_left_targets} targets left.".
Finally, print the index positions of the targets that you hit, as shown in the examples.
Input
•	5 lines representing the field (symbols, separated by a single space)
•	N - count of commands
•	On the following N lines - the commands in the format described above
Output
•	On the first line, print one of the following:
o	If all the targets were shot
"Training completed! All {count_targets} targets hit."
o	Otherwise:
"Training not completed! {count_left_targets} targets left."
•	Finally, print the index positions "[{row}, {column}]" of the targets that you hit, 
as shown in the examples.
Constrains
•	All the commands will be valid
•	There will always be at least one target

____________________________________________________________________________________________
Example_01

Input
. . . . . 
x . . . . 
. A . . . 
. . . x . 
. x . . x 
3
shoot down
move right 4
move left 

Output
1	Training not completed! 3 targets left.
[4, 1]

____________________________________________________________________________________________
Example_02

Input
. . . . . 
. . . . . 
. A x . . 
. . . . . 
. x . . . 
2
shoot down
shoot right	

Output
Training completed! All 2 targets hit.
[4, 1]
[2, 2]

____________________________________________________________________________________________
Example_03

Input
. . . . . 
. . . . . 
. . x . . 
. . . . . 
. x . . A 
3
shoot down
move right 2
shoot left	

Output
Training not completed! 1 targets left.
[4, 1]

"""


""" 1 """

SIZE = 5
AIM, TARGET, EMPTY = "A", "x", "."
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}


def aim_move(mtrx, pos, stp, direct):
    r0, c0 = pos
    r = r0 + directions[direct][0] * stp
    c = c0 + directions[direct][1] * stp
    if 0 <= r < SIZE and 0 <= c < SIZE:
        if mtrx[r][c] == TARGET:
            return r0, c0
        mtrx[r0][c0] = EMPTY
        mtrx[r][c] = AIM
        return r, c
    return r0, c0


def shoot(mtrx, pos, direct):
    r0, c0 = pos
    while True:
        r = r0 + directions[direct][0]
        c = c0 + directions[direct][1]
        if r < 0 or c < 0 or r >= SIZE or c >= SIZE:
            break
        if mtrx[r][c] == TARGET:
            mtrx[r][c] = EMPTY
            return [r, c]
        r0, c0 = r, c


matrix, player_position = [], []
target_count = 0
for i in range(SIZE):
    line = input().split()
    if AIM in line:
        player_position = [i, line.index(AIM)]
    target_count += line.count(TARGET)
    matrix.append(line)

targets_left = target_count
targets_hit = []
for _ in range(int(input())):
    if targets_left == 0:
        break
    command = input()
    command_args = command.split()
    action, direction = command_args[0], command_args[1]

    if action == "move":
        steps = int(command_args[2])
        player_position = aim_move(matrix, player_position, steps, direction)
    elif action == "shoot":
        target = shoot(matrix, player_position, direction)
        if target:
            targets_hit.append(target)
            targets_left -= 1

if targets_left:
    print(f"Training not completed! {targets_left} targets left.")
else:
    print(f"Training completed! All {target_count} targets hit.")
print(*targets_hit, sep="\n")

""" 2 """

AIM, TARGET, EMPTY = "A", "x", "."
DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}


def validate_coordinates(row, col):
    return 0 <= row < SIZE and 0 <= col < SIZE


def move_aim(matrix, position, direction, steps):
    row, col = position
    next_row = row + DIRECTIONS[direction][0] * steps
    next_col = col + DIRECTIONS[direction][1] * steps
    if not validate_coordinates(next_row, next_col) or matrix[next_row][next_col] != EMPTY:
        return row, col
    matrix[row][col] = EMPTY
    matrix[next_row][next_col] = AIM
    return next_row, next_col


def shoot(matrix, position, direction):
    r0, c0 = DIRECTIONS[direction]
    row = position[0] + r0
    col = position[1] + c0
    while validate_coordinates(row, col):
        if matrix[row][col] == TARGET:
            matrix[row][col] = EMPTY
            return [row, col]
        row += r0
        col += c0


SIZE = 5

matrix = []
aim_position = (None, None)
targets_count = 0
for r in range(SIZE):
    line = [x for x in input().split()]
    if AIM in line:
        aim_position = r, line.index(AIM)
    if TARGET in line:
        targets_count += line.count(TARGET)
    matrix.append(line)

commands_count = int(input())
target_coordinates = []
for _ in range(commands_count):
    if len(target_coordinates) == targets_count:
        break
    command, direction, *steps = input().split()
    if command == "move":
        aim_position = move_aim(matrix, aim_position, direction, int(steps[0]))
    elif command == "shoot":
        result = shoot(matrix, aim_position, direction)
        target_coordinates.append(result) if result else None

if len(target_coordinates) == targets_count:
    print(f"Training completed! All {targets_count} targets hit.")
else:
    print(f"Training not completed! {targets_count - len(target_coordinates)} targets left.")
[print(p) for p in target_coordinates]

""" 3 """

SIZE_MATRIX = 5
matrix = [[x for x in input().split()] for _ in range(SIZE_MATRIX)]
dead_targets_pos, number_of_commands = [], int(input())
total_targets = [sum([matrix[row].count("x") for row in range(SIZE_MATRIX)])]
directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}


def check_valid_index(row, col):
    if 0 <= row < SIZE_MATRIX and 0 <= col < SIZE_MATRIX:
        return True


def find_position():
    for row in range(SIZE_MATRIX):
        if "A" in matrix[row]:
            col = matrix[row].index("A")
            matrix[row][col] = "."
            return row, col


player_row, player_col = find_position()


def shoot(row, col, direction):
    for shoot in range(SIZE_MATRIX):
        shooting_row, shooting_col = row + directions[direction][0], col + directions[direction][1]
        if check_valid_index(shooting_row, shooting_col):
            if matrix[shooting_row][shooting_col] == "x":
                total_targets[0] -= 1
                dead_targets_pos.append([shooting_row, shooting_col])
                matrix[shooting_row][shooting_col] = "."
                break
            row, col = shooting_row, shooting_col
        else:
            break


def moving(row, col, direction, steps):
    total_step = [x * steps if x != 0 else 0 for x in directions[direction]]
    moving_row, moving_col = row + total_step[0], col + total_step[1]
    if check_valid_index(moving_row, moving_col) and matrix[moving_row][moving_col] == ".":
        matrix[row][col] = "."
        matrix[moving_row][moving_col] = "A"
        return moving_row, moving_col
    return row, col


def show_result():
    [print(x) for x in dead_targets_pos]


for _ in range(number_of_commands):
    command = input().split()
    if "shoot" in command[0]:
        shoot(player_row, player_col, command[1])
    elif "move" in command[0]:
        player_row, player_col = moving(player_row, player_col, command[1], int(command[-1]))
    if total_targets[0] == 0:
        print(f"Training completed! All {len(dead_targets_pos)} targets hit.")
        show_result()
        break
else:
    print(f"Training not completed! {total_targets[0]} targets left.")
    show_result()

""" 4 """
class RangeDay:

    def __init__(self):
        self.output_message = ''
        self.size = 5
        self.field = []
        self.player_pos = []
        self.total_targets = 0
        self.hits = []
        self.directions = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }
        self.actions = {
            'move': self.moving_action,
            'shoot': self.shooting_action
        }
        self.main_meth()

    def main_meth(self):
        self.create_field_find_player_position_count_targets()
        self.start_shooting_training()
        self.prepare_output_message()

    def create_field_find_player_position_count_targets(self):
        for row in range(self.size):
            line = input().split()
            if 'A' in line:
                self.player_pos = [row, line.index('A')]
            if 'x' in line:
                self.total_targets += line.count('x')
            self.field.append(line)

    def start_shooting_training(self):
        number_of_actions = int(input())
        for _ in range(number_of_actions):
            act, *data = input().split()
            self.actions[act](data)

            if len(self.hits) == self.total_targets:
                break

    def moving_action(self, data):
        way, steps = data[0], int(data[1])
        player_row = self.player_pos[0] + (self.directions[way][0] * steps)
        player_col = self.player_pos[1] + (self.directions[way][1] * steps)
        if 0 <= player_row < self.size and 0 <= player_col < self.size:
            if self.field[player_row][player_col] != 'x':
                self.player_pos = [player_row, player_col]

    def shooting_action(self, data):
        way = data[0]
        row = self.player_pos[0]
        col = self.player_pos[1]
        while True:
            row += self.directions[way][0]
            col += self.directions[way][1]
            if 0 <= row < self.size and 0 <= col < self.size:
                symbol = self.field[row][col]
                if symbol == 'x':
                    self.hits.append([row, col])
                    self.field[row][col] = '.'
                    break
            else:
                break

    def prepare_output_message(self):
        if len(self.hits) == self.total_targets:
            self.output_message = f'Training completed! All {self.total_targets} targets hit.'
        else:
            left_targets = self.total_targets - len(self.hits)
            self.output_message = f'Training not completed! {left_targets} targets left.'
        self.output_message += '\n' + '\n'.join(f'[{x}, {y}]' for x, y in self.hits)

    def __repr__(self):
        return self.output_message


if __name__ == '__main__':
    print(RangeDay())



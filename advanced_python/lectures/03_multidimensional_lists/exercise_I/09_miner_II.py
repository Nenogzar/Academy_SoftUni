#################################### TASK CONDITION ############################
"""
https://judge.softuni.org/Contests/Compete/Index/1835#8
                                   9.	*Miner
You are going to create a game called "Miner".
First, you will receive the size of a square field in which the miner should move.
On the second line, you will receive the commands for the miner's movement,
separated by a single space. The possible commands are "left", "right", "up" and "down".
In the end, you will receive each row of the field on a separate line.
The possible characters that may appear on the screen are:
•	* - a regular position on the field
•	e - the end of the route
•	c - coal
•	s - miner
The miner starts moving from the position "s". He should perform the given commands
successively, moving with only one position in the given direction. If the miner has
reached the edge of the field and the following command indicates that he has to get
out of the area, he must remain in his current position and ignore the command.
When the miner finds coal, he collects it and replaces it with "*". Keep track of the
collected coal. In the end, you should print whether the miner has succeeded in
collecting the coal or not and his final position:
•	If the miner has collected all coal in the field, the program stops,
and you should print the message: "You collected all coal! ({row_index}, {col_index})".
•	If the miner steps at "e", the game is over (the program stops), and you
should print the message: "Game over! ({row_index}, {col_index})".
•	If there are no more commands and none of the above cases had happened,
you should print the message:
"{number_of_remaining_coal} pieces of coal left. ({row_index}, {col_index})".
Input
•	Field size - an integer number
•	Commands to move the miner - a sequence of directions,
separated by single whitespace (" ")
•	The field: some of the following characters ("*", "e", "c ", "s"),
separated by a single whitespace (" ")
Output
•	There are three types of output as mentioned above.
Constraints
•	The field size will be a 32-bit integer in the range [0 … 2 147 483 647]
•	The field will always have only one "s"

____________________________________________________________________________________________
Example_01

Input
5
up right right up right
* * * c *
* * * e *
* * c * *
s * * c *
* * c * *

Output
Game over! (1, 3)

____________________________________________________________________________________________
Example_02

Input
4
up right right right down
* * * e
* * c *
* s * c
* * * *

Output
You collected all coal! (2, 3)

____________________________________________________________________________________________
Example_03

Input
6
left left down right up left left down down down
* * * * * *
e * * * c *
* * c s * *
* * * * * *
c * * * c *
* * c * * *

Output
3 pieces of coal left. (5, 0)


"""

##########: Solutions:##########


##########: variant 1 :##########

n = int(input())
commands = input().split()

matrix = []
miner_pos = []  #[miner_row, miner_cow]
collected_coal, total_coal = 0, 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(n):
    matrix.append(input().split())

    if "s" in matrix[row]:
        miner_pos = [row, matrix[row].index("s")] # position of miner
        matrix[miner_pos[0]][miner_pos[1]] = "*"

    total_coal += matrix[row].count("c")

for command in commands:
    r, c = miner_pos[0] + directions[command][0], miner_pos[1] + directions[command][1]
        # minner row + coordinatec of command

    if not (0 <= r < n and 0 <= c < n):
        continue

    miner_pos = [r, c]

    if matrix[r][c] == "c":
        collected_coal+=1

        if collected_coal == total_coal:
            print(f"You collected all coal! ({r}, {c})")
            break
    elif matrix[r][c] == "e":
        print(f"Game over! ({r}, {c})")
        break

    matrix[r][c] = "*"
else:
    print(f"{total_coal - collected_coal} pieces of coal left. ({miner_pos[0]}, {miner_pos[1]})")


##########: variant 2 :##########

n = int(input())
commands = input().split()

matrix = []
miner_pos = []
collected_coal, total_coal = 0, 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}


for row in range(n):
    matrix.append(input().split())

    if "s" in matrix[row]:
        miner_pos = [row, matrix[row].index("s")]  # Position of miner
        matrix[miner_pos[0]][miner_pos[1]] = "*"

    total_coal += matrix[row].count("c")

# Process each command
for command in commands:
    new_row = miner_pos[0] + directions[command][0]
    new_col = miner_pos[1] + directions[command][1]

    if not (0 <= new_row < n and 0 <= new_col < n):
    # OR
    # if not (new_row in range(0, n) and new_col in range(0, n)):
        continue



    miner_pos = [new_row, new_col]

    if matrix[new_row][new_col] == "c":
        collected_coal += 1
        matrix[new_row][new_col] = "*"
        if collected_coal == total_coal:
            print(f"You collected all coal! ({new_row}, {new_col})")
            break
    elif matrix[new_row][new_col] == "e":
        print(f"Game over! ({new_row}, {new_col})")
        break
else:
    print(f"{total_coal - collected_coal} pieces of coal left. ({miner_pos[0]}, {miner_pos[1]})")

##########: variant 3 :##########


# Constants for matrix elements
EMPTY, END, COAL, MINER = "*", "e", "c", "s"

n = int(input())
commands = input().split()

matrix = []
miner_pos = []
collected_coal, total_coal = 0, 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

# Read the matrix and find initial conditions
for row in range(n):
    matrix.append(input().split())

    if MINER in matrix[row]:
        miner_pos = [row, matrix[row].index(MINER)]
        matrix[miner_pos[0]][miner_pos[1]] = EMPTY

    total_coal += matrix[row].count(COAL)

# Process each command
for command in commands:
    new_row = miner_pos[0] + directions[command][0]
    new_col = miner_pos[1] + directions[command][1]

    if not (new_row in range(0, n) and new_col in range(0, n)):
        continue

    miner_pos = [new_row, new_col]

    if matrix[new_row][new_col] == COAL:
        collected_coal += 1
        matrix[new_row][new_col] = EMPTY
        if collected_coal == total_coal:
            print(f"You collected all coal! ({new_row}, {new_col})")
            break
    elif matrix[new_row][new_col] == END:
        print(f"Game over! ({new_row}, {new_col})")
        break
else:
    print(f"{total_coal - collected_coal} pieces of coal left. ({miner_pos[0]}, {miner_pos[1]})")

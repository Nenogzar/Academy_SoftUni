# ******* Advanced Exam - 27 June 2020 ******* #

# *******  02_snake  ******* #

# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/2456#1

Everybody remembers the old snake game. Now it is time to create your own.

You will be given an integer n for the size of the snake territory with square shape. On the next n lines,
you will receive the rows of the territory. The snake will be placed on a random position, marked with the letter 'S'.

On random positions there will be food, marked with '*'. There might also be a lair on the territory.
The lair has two burrows. They are marked with the letter - 'B'. All of the empty positions will be marked with '-'.
Each turn, you will be given command for the snake’s movement. When the snake moves it leaves a trail marked with '.'
Move commands will be: "up", "down", "left", "right".
If the snake moves to a food, it eats the food and increases the food quantity with one.
If it goes inside of a burrow, it goes out on the position of the other burrow and then both burrows disappear.
If the snake goes out of its territory, it loses, can't return back and the program ends.
The snake needs at least 10 food quantity to win.
When the snake has gone outside of its territory or has eaten enough food, the game ends.
Input
•	On the first line, you are given the integer n – the size of the square matrix.
•	The next n lines holds the values for every row.
•	On each of the next lines you will get a move command.
Output
•	On the first line:
o	If the snake goes out of its territory, print: "Game over!"
o	If the snake eat enough food, print: "You won! You fed the snake."
•	On the second line print all food eaten: "Food eaten: {food quantity}"
•	In the end print the matrix.
Constraints
•	The size of the square matrix will be between [2…10].
•	There will always be 0 or 2 burrows, marked with - 'B'.
•	The snake position will be marked with 'S'.
•	The snake will always either go outside its territory or eat enough food.
•	There will be no case in which the snake will go through itself.

Examples

Input
6
-----S
----B-
------
------
--B---
--*---
left
down*-
down
down
left

Output
Game over!
Food eaten: 1
----..
----.-
------
------
--.---
--.---

Comments
1) left     2) down     3) down     5) down
   ----S.      ----..      ----..      ----..
   ----B-      ----.-      ----.-      ----.-
   ------      ------      ------      ------
   ------      ------      ------      ------
   --B---      --S---      --.---      --.---
   --*---      --*---      --S---      --.---
3) eat the food: '*' (5, 2)
5) the snake goes out from its territory and the program ends


Input
7
--***S-
--*----
--***--
---**--
---*---
---*---
---*---
left
left
left
down
down
right
right
down
left
down

Output
You won! You fed the snake.
Food eaten: 10
--....-
--.----
--...--
---..--
---S---
---*---
---*---


"""

##########: variant 1 :##########

rows = int(input())
matrix = [list(input()) for _ in range(rows)]
snake = {
    "food": 0,
    "outside": False
}

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
snake_row, snake_col, teleport = 0, 0, []
for row in range(rows):
    for col in range(rows):
        if matrix[row][col] == "S":
            snake_row, snake_col = row, col
            matrix[row][col] = "."
        elif matrix[row][col] == "B":
            teleport.append([row, col])

while snake['food'] < 10 and not snake['outside']:
    command = input()

    direction = directions[command]
    snake_row += direction[0]
    snake_col += direction[1]

    if 0 <= snake_row < rows and 0 <= snake_col < rows:
        if matrix[snake_row][snake_col] == "*":
            snake['food'] += 1
            matrix[snake_row][snake_col] = "."
        elif matrix[snake_row][snake_col] == "B":
            matrix[snake_row][snake_col] = "."
            teleport_location = [x for x in teleport if x != [snake_row, snake_col]]
            snake_row, snake_col = teleport_location[0][0], teleport_location[0][1]
            matrix[snake_row][snake_col] = "."
        elif matrix[snake_row][snake_col] == "-":
            matrix[snake_row][snake_col] = "."
    else:
        snake['outside'] = True

if snake['outside']:
    print('Game over!')
else:
    matrix[snake_row][snake_col] = "S"
    print("You won! You fed the snake.")
print(f"Food eaten: {snake['food']}")
[print(''.join(matrix[row])) for row in range(rows)]


##########: variant 2 : CEO ##########
# https://icode-example.ceo-py.eu/solution?language=Python&course=Advanced-Exams&module=Python-Advanced-Exam-27-June-2020&problem=02.-Snake&id=65a9038343b837de42b7d19c

rows = int(input())
snake_row, snake_col, lairs, matrix, food_quantity = 0, 0, [], [], [0]
directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
snake_is_alive = [True]

for row in range(rows):
    matrix.append(list(input()))
    if "S" in matrix[row]:
        snake_row, snake_col = row, matrix[row].index("S")
    elif "B" in matrix[row]:
        lairs.append([row, matrix[row].index("B")])

cols = len(matrix[0])


def check_valid_index(row, col):
    return 0 <= row < rows and 0 <= col < cols


def snake_teleport(row, col):
    lairs.remove([row, col])
    return lairs[0][0], lairs[0][1]


def movement(row, col, direction):
    return row + directions[direction][0], col + directions[direction][1]


def snake_step(row, col, direction):
    new_row, new_col = movement(row, col, direction)
    if check_valid_index(new_row, new_col):
        if matrix[new_row][new_col] == "B":
            matrix[new_row][new_col] = "."
            new_row, new_col = snake_teleport(new_row, new_col)

        elif matrix[new_row][new_col] == "*":
            food_quantity[0] += 1
        matrix[row][col] = "."
        matrix[new_row][new_col] = "S"
        return new_row, new_col
    snake_is_alive[0] = False
    matrix[row][col] = "."
    return row, col


while food_quantity[0] < 10 and snake_is_alive[0]:
    direction = input()
    if direction in directions:
        snake_row, snake_col = snake_step(snake_row, snake_col, direction)

if snake_is_alive[0]:
    print("You won! You fed the snake.")
else:
    print("Game over!")
print(f"Food eaten: {food_quantity[0]}")
[print(*matrix[row], sep="") for row in range(rows)]


##########: variant 3 solution SoftUni :##########

SNAKE, FOOD, BURROW, EMPTY, VISITED = "S", "*", "B", "-", "."
DIRECTIONS = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

size = int(input())
matrix = []
burrows = []
snake_position = None, None
for r in range(size):
    line = list(input())
    if SNAKE in line:
        snake_position = r, line.index(SNAKE)
    if BURROW in line:
        burrows.append([r, line.index(BURROW)])
    matrix.append(line)

food_collected = 0
snake_lost = False
row, col = snake_position
while food_collected < 10 and not snake_lost:
    command = input()
    if command not in DIRECTIONS:
        continue
    r, c = DIRECTIONS[command]
    matrix[row][col] = VISITED
    next_r, next_c = row + r, col + c
    if next_r < 0 or next_c < 0 or next_r >= size or next_c >= size:
        snake_lost = True
        break
    if matrix[next_r][next_c] == FOOD:
        food_collected += 1
        matrix[next_r][next_c] = SNAKE
    if [next_r, next_c] in burrows:
        for burrow in burrows:
            row_b, col_b = burrow
            if [next_r, next_c] == [row_b, col_b]:
                matrix[row_b][col_b] = VISITED
                continue
            next_r, next_c = burrow
            matrix[next_r][next_c] = SNAKE
    row, col = next_r, next_c

print("Game over!") if snake_lost else print("You won! You fed the snake.")
print(f"Food eaten: {food_collected}")
[print(*row, sep='') for row in matrix]
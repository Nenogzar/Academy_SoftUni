#################################### TASK CONDITION ############################
"""
                        7.	Snake Moves
You are tasked to visualize a snake's zigzag path in a rectangular matrix with
a size N x M.  A string represents the snake. It starts moving from the top-left
corner to the right. When the snake reaches the end of the row, it slithers its
way down to the next row and turns left. The moves are repeated to the very end.
The first cell is filled with the first symbol of the snake. The second cell is
filled with the second symbol, etc. The snake's path is as long as it takes to
fill the matrix completely - if you reach the end of the string representing the
snake, start again at the first symbol. In the end, you should print the snake's path.
Input
The input data consists of exactly two lines:
•	On the first line, you will receive the dimensions N x M of the
field in format: "{rows} {columns}".
•	On the second line, you will receive the string representing the snake
Output
•	You should print the snake's zigzag path of size N x M (rows x columns)
Constraints
•	The dimensions N and M of the matrix will be integers in the range [1 … 12]
•	The snake will be a string with length in the range [1 … 20] and
will not contain any whitespace characters

____________________________________________________________________________________________
Example_01

Input
5 6
SoftUni

Output
SoftUn
UtfoSi
niSoft
foSinU
tUniSo

____________________________________________________________________________________________
Example_02

Input
1 4
Python

Output
Pyth

"""
##########: variant 1 :##########


N, M = map(int, input().split())
# OR
# N, M = [int(num) for num in input().split()]
snake = input()

matrix = [['' for _ in range(M)] for _ in range(N)]
# OR
# matrix = [list(map(str, ['' for _ in range(M)])) for _ in range(N)]

snake_index = 0
snake_length = len(snake)

for row in range(N):

    if row % 2 == 0:
        # Ако редът е четен, попълваме от ляво на дясно
        for col in range(M):
            matrix[row][col] = snake[snake_index]
            # Увеличаваме индекса на змията и го нормализираме спрямо дължината на низа за змията
            snake_index = (snake_index + 1) % snake_length
    else:
        # Ако редът е нечетен, попълваме от дясно на ляво
        for col in range(M - 1, -1, -1):
            matrix[row][col] = snake[snake_index]
            # Увеличаваме индекса на змията и го нормализираме спрямо дължината на низа за змията
            snake_index = (snake_index + 1) % snake_length

for row in matrix:
    print(*row, sep='')

##########: variant 2 :##########


N, M = map(int, input().split())
snake = input()

matrix = [['' for _ in range(M)] for _ in range(N)]

snake_index = 0
snake_length = len(snake)

for row in range(N):
    if row % 2 == 0:
        for col in range(M):
            matrix[row][col] = snake[snake_index]
            snake_index = (snake_index + 1) % snake_length
    else:
        for col in range(M - 1, -1, -1):
            matrix[row][col] = snake[snake_index]
            snake_index = (snake_index + 1) % snake_length

for row in matrix:
    print(*row, sep='')

##########: variant 3 :##########

N, M = map(int, input().split())
snake = input()

matrix = [['' for _ in range(M)] for _ in range(N)]

snake_index = 0
snake_length = len(snake)

for row in range(N):
    for col in range(M):
        # Определяме действителния индекс на колоната в зависимост от паритета на реда
        actual_col = col if row % 2 == 0 else M - 1 - col
        matrix[row][actual_col] = snake[snake_index]
        snake_index = (snake_index + 1) % snake_length

for row in matrix:
    print(*row, sep='')



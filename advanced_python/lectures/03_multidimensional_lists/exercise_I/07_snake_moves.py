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

from collections import deque

rows, cols = [int(x) for x in input().split()]

snake = deque(input())

matrix = []

for row in range(1, rows + 1):
    snake_row = deque()
    for col in range(cols):
        symbol = snake[0]
        if row % 2 == 0:
            snake_row.appendleft(symbol)
        else:
            snake_row.append(symbol)
        snake.rotate(-1)
    matrix.append(snake_row)

for nest in matrix:
    print(*nest, sep='')

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

##########: variant 4 :##########


from collections import deque

rows, cols = map(int, input().split())
word = list(input())
word_queue = deque(word)

while len(word_queue) < rows * cols:
    word_queue.extend(word[:rows * cols - len(word_queue)])

for row in range(rows):
    if row % 2 == 0:
        print(*[word_queue.popleft() for _ in range(cols)], sep="")
    else:
        print(*[word_queue.popleft() for _ in range(cols)][::-1], sep="")

##########: variant 5 :##########

from collections import deque

rows, cols = map(int, input().split())
word = list(input())
word_queue = deque(word)

for row in range(rows):
    while len(word_queue) < cols:
        word_queue.extend(word)

    if row % 2 == 0:
        print(*[word_queue.popleft() for _ in range(cols)], sep="")
    else:
        print(*[word_queue.popleft() for _ in range(cols)][::-1], sep="")

##########: variant 6 :##########


from collections import deque


class SnakeMoves:

    def __init__(self):
        self.output_message = ''
        self.snake = deque()
        self.rows = 0
        self.cols = 0
        self.matrix = []
        self.main_meth()

    def main_meth(self):
        self.define_rows_and_cols_of_matrix()
        self.define_string_representing_snake()
        self.fill_matrix_with_elements()
        self.prepare_output_message()

    def define_rows_and_cols_of_matrix(self):
        self.rows, self.cols = [int(x) for x in input().split()]

    def define_string_representing_snake(self):
        self.snake = deque(input())

    def fill_matrix_with_elements(self):
        for row in range(1, self.rows + 1):
            current_row = self.create_snake_rows(row)
            self.matrix.append(current_row)

    def create_snake_rows(self, row):
        snake_row = deque()
        for col in range(self.cols):
            symbol = self.snake[0]
            if row % 2 == 0:
                snake_row.appendleft(symbol)
            else:
                snake_row.append(symbol)
            self.snake.rotate(-1)
        return snake_row

    def prepare_output_message(self):
        self.output_message = '\n'.join(''.join(row) for row in self.matrix)

    def __repr__(self):
        return self.output_message


if __name__ == '__main__':
    print(SnakeMoves())

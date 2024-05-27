#################################### TASK CONDITION ############################
"""
                     2.	Matrix Modification
Write a program that reads a matrix from the console and changes its 
values. On the first line, you will get the matrix's rows - N. You will 
get elements for each column on the following N lines, separated with 
a single space. You will be receiving commands in the following format:
•	"Add {row} {col} {value}" – Increase the number at the given 
coordinates with the value.
•	"Subtract {row} {col} {value}" – Decrease the number at the 
given coordinates by the value.
If the coordinate is invalid, you should print "Invalid coordinates". 
A coordinate is valid if both of the given indexes are in range [0; len() – 1].
When you receive "END", you should print the matrix and stop the program.

____________________________________________________________________________________________
Example_01

Input
3
1 2 3
4 5 6
7 8 9
Add 0 0 5
Subtract 1 1 2
END	

Output
6 2 3
4 3 6
7 8 9

____________________________________________________________________________________________
Example_02

Input
4
1 2 3 4
5 6 7 8
8 7 6 5
4 3 2 1
Add 4 4 100
Add 3 3 100
Subtract -1 -1 42
Subtract 0 0 42
END	

Output
Invalid coordinates
Invalid coordinates
-41 2 3 4
5 6 7 8
8 7 6 5
4 3 2 101

"""


##########: variant 1 :##########


row = int(input())
matrix = [list(map(int, input().split())) for _ in range(row)]

action_input = input()

while action_input != "END":
    action, start, end, value = action_input.split()
    start, end, value = int(start), int(end), int(value)

    if start not in range(row) or end not in range(len(matrix[0])):
        print("Invalid coordinates")
    else:
        if action == "Add":
            matrix[start][end] += value
        elif action == "Subtract":
            matrix[start][end] -= value
        else:
            print("Invalid action")

    action_input = input()

for r in matrix:
    print(*r)


##########: variant 2 :##########


rows = int(input())
matrix = [list(map(int, input().split(" "))) for _ in range(rows)]

command = input()
while command != "END":
    parts = command.split()
    action = parts[0]
    row, col, val = [int(x) for x in parts[1:4]]

    if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
    # OR
    # if row in range(rows) or col in range(len(matrix[0])):
      
        if action == "Add":
            matrix[row][col] += val
        elif action == "Subtract":
            matrix[row][col] -= val
    else:
        print("Invalid coordinates")


    command = input()

for nest in matrix:
    print(*nest)



##########: variant 3 :##########
n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

while True:
    command = input()
    if command == "END":
        break
    command_args = command.split()
    action = command_args[0]
    row, col, value = [int(x) for x in command_args[1:4]]
    if 0 <= row <= n and 0 <= col < n:
        if action == "Add":
            matrix[row][col] += value
        elif action == "Subtract":
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")

[print(*matrix[i], sep=" ") for i in range(n)]


##########: variant 4 - whit tri-exeption :##########

row = int(input())
matrix = [list(map(int, input().split())) for _ in range(row)]
action_input = input()

while action_input != "END":
    action, x, y, value = action_input.split()
    x, y, value = int(x), int(y), int(value)

    if x not in range(row) or y not in range(len(matrix[0])):
        print("Invalid coordinates")
    else:
        try:
            if action == "Add":
                matrix[x][y] += value
            elif action == "Subtract":
                matrix[x][y] -= value
            else:
                print("Invalid action")
        except ValueError:
            continue

    action_input = input()

for r in matrix:
    print(*r)

##########: variant 5 :##########

n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

ACTIONS = {
    "Add": lambda x: x,
    "Subtract": lambda x: - x
}

command = input()
while command != "END":
    action, *data = command.split()
    row, col, value = [int(x) for x in data]
    if row < 0 or col < 0 or row >= n or col >= n:
        print("Invalid coordinates")
    else:
        matrix[row][col] += ACTIONS[action](value)
    command = input()

[print(*row) for row in matrix]

##########: variant 5  - Whit Class :##########
 
def create_matrix(size):
    return [[int(x) for x in input().split()] for _ in range(size)]

def valid_coordinates(size, row, col):
    return 0 <= row < size and 0 <= col < size

def add_number(matrix, r, c, value):
    matrix[r][c] += value

def subtract_number(matrix, r, c, value):
    matrix[r][c] -= value

def start_modifications(matrix, size):
    actions = {
        'Add': add_number,
        'Subtract': subtract_number,
    }
    output_message = []

    while True:
        data = input().split()
        if data[0] == 'END':
            break
        act, row, col, value = data[0], int(data[1]), int(data[2]), int(data[3])

        if valid_coordinates(size, row, col):
            actions[act](matrix, row, col, value)
        else:
            output_message.append('Invalid coordinates')

    return output_message

def prepare_output_message(matrix):
    return [' '.join(str(x) for x in row) for row in matrix]

def matrix_modification():
    size = int(input())
    matrix = create_matrix(size)
    modifications_output = start_modifications(matrix, size)
    output_message = prepare_output_message(matrix)
    output_message.extend(modifications_output)
    return '\n'.join(output_message)

if __name__ == '__main__':
    print(matrix_modification())



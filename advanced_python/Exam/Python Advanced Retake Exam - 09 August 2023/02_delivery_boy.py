#################################### TASK CONDITION ############################
"""
https://judge.softuni.org/Contests/Practice/Index/4089#1

02. Delivery Boy

Today, we have an exciting programming task that will take you on a pizza delivery adventure in a neighborhood represented by a matrix. 
Get ready to navigate a delivery boy through the streets, avoid obstacles, and make timely pizza deliveries!
You are a pizza delivery boy with a motorized vehicle that delivers pizza in a neighborhood. 
The neighborhood is represented by a matrix - field. Each cell in the field represents a part of the neighborhood, and it can contain one of the following elements:
    •	'B' - Represents the starting position of the delivery boy.
    •	'A' - Represents an address where a pizza needs to be delivered.
    •	'*' - Represents an obstacle or an area where the delivery boy cannot drive.
    •	'P' - Represents the pizza restaurant.
    •	'-' – Represents the road, the delivery boy can drive over it.
In the beginning, you will be given N and M – integers, separated by a single space - " ", indicating the field’s dimensions. On the next N lines, 
you will receive strings, representing the rows of the area, with M columns.
The delivery boy must carefully navigate through the streets, following the commands that will be received on each of the following lines- "up", "down", "right", and "left", moving one position at a time.
In this pizza delivery adventure, the delivery boy starts his journey from the position marked as 'B' on the neighborhood field. 
His first task is to make his way to the pizza restaurant marked as 'P' and collect the delicious pizza. 
Once he collects the pizza, the position 'P' is marked as 'R' and a message is displayed on the Console: "Pizza is collected. 10 minutes for delivery."
However, the neighborhood is not without obstacles. 
Whenever the delivery boy encounters a cell marked with '*', it signifies an obstacle, and he cannot make a move in that direction. 
He must remain in his current position and find an alternative route. The delivery boy should wait for the next command.
If, at any point during his journey, the delivery boy steps out of the neighborhood field (matrix boundaries), it means he has ventured beyond the streets of the neighborhood. 
In such a case, the delivery boy will be considered late for the delivery, and unfortunately, the delivery will be canceled. 
The following message should be displayed on the Console: "The delivery is late. Order is canceled."
Once the delivery boy successfully reaches an address marked as 'A', he joyfully delivers the pizza, completing his mission. 
The position 'A' is marked as 'P'. A message will be displayed on the Console: "Pizza is delivered on time! Next order..."
With each step he takes, the '-'(dash) cells he passes (road) through become '.' (dot) to indicate his path.
Remember, the delivery boy must follow the commands, avoid obstacles, and ensure timely pizza deliveries to the addresses. Good luck!
In the end, print the final state of the matrix (neighborhood area) with the delivery boy in its starting position. 
If the boy has been out of the field, mark his starting position with an empty space. Each row is on a new line.

Input
  •	On the first line, you will get the number of rows and columns of the matrix, separated by a single space.
  •	On the next N lines, you will receive strings, representing each row of the matrix.
  •	On each of the following lines, you will receive the possible directions for the delivery boy to move - "up", "down", "right", and "left".
Output
  •	On the first line:
    o	When the boy collects the pizza:
      "Pizza is collected. 10 minutes for delivery."

    o	If the pizza is delivered successfully: 
      "Pizza is delivered on time! Next order..."

    o	If the boy leaves the field boundaries:
      "The delivery is late. Order is canceled."

  •	On the next lines, print the final state of the matrix with the delivery boy in its starting position. If the boy has been out of the field, mark his starting position with an empty space. Each row - on a new line.
  Constraints
  •	The commands are guaranteed to lead him either to a successful delivery or out of the field, ensuring that the commands are sufficient in all cases.
  •	Each row of the matrix will have the same length.


Input
5 6
*----A
*B***-
*-***-
*----P
******
down
down
right
right
right
right
up
up
up


Output
Pizza is collected. 10 minutes for delivery.
Pizza is delivered on time! Next order...
*----P
*B***.
*.***.
*....R
******

Input

5 6
*----A
*B***-
*-***-
*----P
******
down
down
left
right
right
right
right
right
up

Output

Pizza is collected. 10 minutes for delivery.
The delivery is late. Order is canceled.
*----A
* ***-
*.***-
*....R
******

"""
##########: variant 1 :##########


def is_valid(value, max_value):
    return 0 <= value < max_value


def next_move(command, current_row, current_col):
    if command == 'up' and is_valid(current_row-1, rows):
        return current_row-1, current_col
    if command == 'down' and is_valid(current_row+1, rows):
        return current_row+1, current_col
    if command == 'left' and is_valid(current_col-1, cols):
        return current_row, current_col-1
    if command == 'right' and is_valid(current_col+1, cols):
        return current_row, current_col+1
    return None, None


rows, cols = [int(x) for x in input().split(' ')]
field = []
start_row, start_col = None, None
boy_row, boy_col = None, None
line = ' '

for r in range(rows):
    row = list(input())
    field.append(row)
    if 'B' in row:
        boy_row = r
        boy_col = row.index('B')
        start_row = boy_row
        start_col = boy_col

while line:
    line = input()
    next_row, next_col = next_move(line, boy_row, boy_col)
    if next_row is None or next_col is None:
        print('The delivery is late. Order is canceled.')
        field[start_row][start_col] = ' '
        break
    if field[next_row][next_col] == '*':
        continue
    if field[next_row][next_col] == 'A':
        field[boy_row][boy_col] = '.'
        boy_row, boy_col = next_row, next_col
        field[boy_row][boy_col] = 'P'
        print("Pizza is delivered on time! Next order...")
        field[start_row][start_col] = 'B'
        break
    if field[next_row][next_col] == 'P':
        field[boy_row][boy_col] = '.'
        boy_row, boy_col = next_row, next_col
        field[next_row][next_col] = 'R'
        print("Pizza is collected. 10 minutes for delivery.")
        continue
    if not field[boy_row][boy_col] == 'R':
        field[boy_row][boy_col] = '.'
    boy_row, boy_col = next_row, next_col
    field[boy_row][boy_col] = '.'

for row in field:
    print(''.join(row))

##########: variant 2 :##########

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "right": [0, 1],
    "left": [0, -1]
}


def is_next_position_valid(matrix, row, col):
    if row < 0 or row >= len(matrix):
        return False
    if col < 0 or col >= len(matrix[0]):
        return False
    return True


rows, cols = [int(x) for x in input().split()]

start_position = None
field = []
for row in range(rows):
    line = input()
    if "B" in line:
        start_position = [row, line.index("B")]
    field.append(list(line))

current_position = start_position

finished = False
while not finished:
    command = input()
    if command not in directions:
        continue
    r, c = directions[command]
    next_r = current_position[0] + r
    next_c = current_position[1] + c

    if not is_next_position_valid(field, next_r, next_c):
        start_r, start_c = start_position
        field[start_r][start_c] = " "
        print("The delivery is late. Order is canceled.")
        finished = True

    elif field[next_r][next_c] == "A":
        field[next_r][next_c] = "P"
        print("Pizza is delivered on time! Next order...")
        finished = True

    elif field[next_r][next_c] == "*":
        continue

    elif field[next_r][next_c] == "P":
        field[next_r][next_c] = "R"
        print("Pizza is collected. 10 minutes for delivery.")

    if field[current_position[0]][current_position[1]] == "-":
        field[current_position[0]][current_position[1]] = "."
    current_position = [next_r, next_c]

[print(*field[row], sep="") for row in range(len(field))]

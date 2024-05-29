#################################### TASK CONDITION ############################
"""
Python Advanced Exam - 17 June 2023

https://judge.softuni.org/Contests/Practice/Index/4081#1

02. Mouse In The Kitchen

A hungry little mouse is living in an old suburbs house. It walks around the kitchen cupboard every night and eats all the cheese. 
A lazy plump cat is guarding the kitchen, so the mouse should not walk out of the cupboard area.
In the beginning, you will be given N and M – integers, separated by a comma - ",", indicating the cupboard’s area dimensions. On the next N lines, 
you will receive strings, representing the rows of the area, with M columns.
After that, on each line, until the command "danger" appears as an input string, you will receive the possible directions for the mouse to move - "up", "down", "right", and "left". 
If the mouse steps outside the cupboard area, the cat will attack, and the cheese hunt is over. 
In that case, the program ends, keep the last known position of the mouse, before it steps outside the cupboard area and the following message is printed on the Console: 
"No more cheese for tonight!"
Possible characters in the matrix are:
  •	M - represents the mouse's position.
  •	C – represents a piece of cheese. 
  •	* – represents an empty position, nothing happens if the mouse steps on it.
  •	@ – represents a wall in the cupboard, cannot step on or go through it.
  •	T – represents a trap.
The mouse starts from the M - position.
  •	If the mouse steps on C – position, it eats the cheese from the field, and the position is marked with "*". 
  o	If this is the last cheese in the cupboard area, the mouse goes to sleep. Remember that this will be the last known position of the mouse. 
The program ends and the following message is printed on the Console: "Happy mouse! All the cheese is eaten, good night!"
  •	If the mouse steps into a trap (T -position), it will be trapped. Remember that this will be the last known position of the mouse. In that case, the program ends, 
and the following message is printed on the Console: "Mouse is trapped!"
  •	If the given direction leads the mouse towards @ - position, this is a wall in the cupboard area. Do not make the move and skip the command.
  •	If the "danger" command is received before the mouse manages to eat all the cheese, the mouse disappears. 
Remember that this will be the last known position of the mouse and you will need it for the final state of the matrix. 
In that case, the program ends, and the following message is printed on the Console: "Mouse will come back later!"
In the end, print the final state of the matrix (cupboard area) with the last known position of the mouse in it. Each row on a new line. 
Input
  •	On the first line you will get the number of rows and columns of the matrix, separated by a comma.
  •	On the next N lines, you will receive strings, representing each row of the matrix.
  •	On each of the following lines, until the command "danger" appears as an input string, you will receive the possible directions for the mouse to move - "up", "down", "right", and "left".
  •	"danger" command – The mouse spots danger and disappears… for now!
Output
  •	On the first line:
    o	If the mouse steps outside the cupboard 
      "No more cheese for tonight!"

    o	If the mouse manages to eat all the cheese
      "Happy mouse! All the cheese is eaten, good night!"
    
    o	If the mouse steps into a trap (T -position)
      "Mouse is trapped!"
    
    o	If the "danger" command is received before the mouse manages to eat all the cheese – 
      "Mouse will come back later!"

  •	On the next lines, print the final state of the matrix with the last known position of the mouse in it. Each row - on a new line, each row position with NO separator.
  Constraints
  •	There will always be at least one trap in the cupboard.
  •	There will always be some cheese in the cupboard.
  •	There will always be а "danger" command in the end, but it is not necessary to reach it. The program may end earlier.
  •	Each row of the matrix will have the same length.

Examples

Input

5,5
**M**
T@@**
CC@**
**@@*
**CC*
left
down
left
down
down
down
right

Output	

danger	Mouse is trapped!
*****
M@@**
CC@**
**@@*
**CC*	


Comments
The mouse moves to the left and the position is marked with "*", so nothing happens. 
Next command is "down", but the position is marked with "@", so we skip the command.
Next command - "left", the mouse moves to the left. The position is marked with "*", so nothing happens. 
Next command is "down", the position is marked with "T", so the mouse is trapped. Remember to mark the last known position of the mouse with "M".


Input

4,8
CC@**C*M
T*@**CT*
**@@@@**
T***C***
down
right
left
down
left	

Output

danger	No more cheese for tonight!
CC@**C**
T*@**CTM
**@@@@**
T***C***	


Input

6,3
@CC
@TC
@C*
@M*
@**
@**
left
up
left
right
up
up
left
left
danger


Output

danger	Happy mouse! All the cheese is eaten, good night!
@M*
@T*
@**
@**
@**
@** 	


"""
##########: variant 1 :##########

MOUSE = "M"
CHEESE = "C"
EMPTY = "*"
WALL = "@"
TRAP = "T"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

rows, cols = [int(x) for x in input().split(",")]

field = []
pieces_of_cheese = 0
mouse_position = None
for r in range(rows):
    line = list(input())
    if MOUSE in line:
        mouse_position = [r, line.index(MOUSE)]
    if CHEESE in line:
        pieces_of_cheese += line.count(CHEESE)
    field.append(line)

result = []
command = input()
while command != "danger":

    if command not in directions:
        command = input()
        continue

    prev_r, prev_c = mouse_position
    r, c = directions[command]
    row, col = prev_r + r, prev_c + c

    if not (0 <= row < len(field)) or not (0 <= col < len(field[0])):
    # OR
    # if row not in range(len(field)) or col not in range(len(field[0]))
      
        field[prev_r][prev_c] = MOUSE
        result.append("No more cheese for tonight!")
        break

    elif field[row][col] == CHEESE:
        pieces_of_cheese -= 1
        field[prev_r][prev_c] = EMPTY
        field[row][col] = MOUSE
        mouse_position = [row, col]
        if pieces_of_cheese == 0:
            result.append("Happy mouse! All the cheese is eaten, good night!")
            break
    elif field[row][col] == TRAP:
        field[prev_r][prev_c] = EMPTY
        field[row][col] = MOUSE
        result.append("Mouse is trapped!")
        break
    elif field[row][col] == WALL:
        command = input()
        continue
    else:
        field[prev_r][prev_c] = EMPTY
        field[row][col] = MOUSE
        mouse_position = [row, col]

    command = input()

else:
    result.append("Mouse will come back later!")

[result.append(''.join(row)) for row in field]
print("\n".join(result))


##########: variant 2 :##########

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


rows, cols = [int(x) for x in input().split(',')]
field = []
mouse_row, mouse_col = None, None
cheese_cnt = 0
line = ''

for r in range(rows):
    row = list(input())
    field.append(row)
    if 'M' in row:
        mouse_row = r
        mouse_col = row.index('M')
    if 'C' in row:
        cheese_cnt += row.count('C')


while cheese_cnt != 0:
    line = input()
    if line == 'danger':
        break
    next_row, next_col = next_move(line, mouse_row, mouse_col)
    if next_row is None or next_col is None:
        print('No more cheese for tonight!')
        break
    if field[next_row][next_col] == '@':
        continue
    if field[next_row][next_col] == 'T':
        field[mouse_row][mouse_col] = '*'
        mouse_row, mouse_col = next_row, next_col
        field[mouse_row][mouse_col] = 'M'
        print("Mouse is trapped!")
        break
    if field[next_row][next_col] == '*':
        field[mouse_row][mouse_col] = '*'
        mouse_row, mouse_col = next_row, next_col
        field[mouse_row][mouse_col] = 'M'
        continue
    if field[next_row][next_col] == 'C':
        cheese_cnt -= 1
        field[mouse_row][mouse_col] = '*'
        mouse_row, mouse_col = next_row, next_col
        field[mouse_row][mouse_col] = 'M'

else:
    print("Happy mouse! All the cheese is eaten, good night!")

if cheese_cnt and line == 'danger':
    print("Mouse will come back later!")

for row in field:
    print(''.join(row))


##########: variant 3 :##########

MOUSE = "M"
CHEESE = "C"
EMPTY = "*"
WALL = "@"
TRAP = "T"

def is_valid(value, max_value):
    return 0 <= value < max_value

def next_move(command, current_row, current_col):
    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }
    if command in directions:
        dr, dc = directions[command]
        new_row, new_col = current_row + dr, current_col + dc
        if is_valid(new_row, rows) and is_valid(new_col, cols):
            return new_row, new_col
    return None, None

rows, cols = map(int, input().split(','))

field = []
mouse_row, mouse_col = None, None
cheese_cnt = 0

for r in range(rows):
    row = list(input())
    field.append(row)
    if MOUSE in row:
        mouse_row, mouse_col = r, row.index(MOUSE)
    cheese_cnt += row.count(CHEESE)

result = []

while cheese_cnt > 0:
    command = input()
    if command == 'danger':
        break

    next_row, next_col = next_move(command, mouse_row, mouse_col)
    if next_row is None or next_col is None:
        result.append("No more cheese for tonight!")
        break

    if field[next_row][next_col] == WALL:
        continue
    elif field[next_row][next_col] == TRAP:
        field[mouse_row][mouse_col] = EMPTY
        mouse_row, mouse_col = next_row, next_col
        field[mouse_row][mouse_col] = MOUSE
        result.append("Mouse is trapped!")
        break
    elif field[next_row][next_col] == CHEESE:
        cheese_cnt -= 1
        field[mouse_row][mouse_col] = EMPTY
        mouse_row, mouse_col = next_row, next_col
        field[mouse_row][mouse_col] = MOUSE
    elif field[next_row][next_col] == EMPTY:
        field[mouse_row][mouse_col] = EMPTY
        mouse_row, mouse_col = next_row, next_col
        field[mouse_row][mouse_col] = MOUSE

if cheese_cnt == 0:
    result.append("Happy mouse! All the cheese is eaten, good night!")
elif command == 'danger':
    result.append("Mouse will come back later!")

for row in field:
    result.append(''.join(row))

print("\n".join(result))

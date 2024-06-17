# ******* Advanced Exam - 22 October 2022 ******* #

# *******  02_rally_racing  ******* #

# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/3596#1

It's time for one of the biggest races in the world, Paris-Dakar.
The organizers of the event want you to do a program that helps them track
    the cars through the separate stages in the event.

On the first line,
    you will be given an integer N, which represents the size of a square matrix.

On the second line
    you will receive the racing number of the tracked race car.

On the next N lines
    you will be given the rows of  the matrix (string sequences, separated by whitespace), which will be representing the race route.
The tracked race car always starts with coordinates [0, 0].

Thеre will be a tunnel somewhere across the race route.
    If the race car runs into the tunnel , the car goes through it and exits at the other end.
    There will be always two positions marked with "T"(tunnel).

The finish line will be marked with "F".
All other positions will be marked with ".".

Keep track of the kilometers passed.
    Every time the race car receives a direction and moves to the next position of the race route,
    it covers 10 kilometers.
    If the car goes through the tunnel, it covers NOT 10, but 30 kilometers.

On each line, after the matrix is given, you will be receiving the directions for the race car.
•	left
•	right
•	up
•	down

The race car starts moving across the race route:
•	If you receive "End" command, before the race car manages to reach the finish line,
    the car is disqualified and the following output should be printed on the Console:
        "Racing car {racing number} DNF."

•	If the race car comes across a position marked with ".".
    The car passes 10 kilometers for the current move and waits for the next direction.

•	If the race car comes across a position marked with "T" this is the tunnel.
    The race car goes through it and moves to the other position marked with  "T" (the other end of the tunnel).
    The car passes 30 kilometers for the current move.
    The tunnel stays behind the car, so the race route is clear,
        and both the positions marked with "T", should be marked with ".".

•	If the car reaches the finish line - "F" position, the race is over.
    The tracked race car manages to finish the stage and the following output should be printed on the Console:
        "Racing car {racing number} finished the stage!".

    Don’t forget that the car has covered another 10 km with the last move.

Input
•	On the first line you will receive N - the size of the square matrix (race route)
•	On the second line you will receive the racing number of the tracked car
•	On the next N lines, you will receive the race route (elements will be separated by a space).
•	On the following lines, you will receive directions (left, right, up, down).
•	On the last line, you will receive the command "End".

Output
•	If the racing car has reached the finish line before the "End" command is given, print on the Console:
        "Racing car {racing number} finished the stage!"

•	If the "End"  command is given and the racing car has not reached the finish line yet,
        the race ends and the following message is printed on the Console:
            "Racing car {racing number} DNF."

•	On the second line, print the distance that the tracked race car has covered:
        "Distance covered {kilometers passed} km."

•	At the end, mark the last known position of the race car with "C" and print the final state of the matrix (race route).
    The row elements in the output matrix should NOT be separated by a whitespace.

Constraints
•	The directions will always lead to coordinates in the matrix.
•	There will always be two positions marked with "T" , representing the tunnel in the race route.
•	The size of the square matrix (race route) will be between [4…10].
Еxamples

Input

5
01
. . . . .
. . . T .
. . . . .
. T . . .
. . F . .
down
right
right
right
down
right
up
down
right
up
End


Output
Racing car 01 finished the stage!
Distance covered 80 km.
.....
.....
.....
.....
..C..


Comment
The race car starts moving from position[0,0].
The first command is down, so the moving direction is down. The race car is in position[1,0].
Next three commands are right, so the race car  comes across the tunnel – "T".
The current car position is [1,3]. Swap the "T" with "."
The race car goes through the tunnel, so its next position is [3,1]. Swap the "T" with "."
Next direction is down, so the race car position is [4,1].
Next direction is right, so the race car position is [4,2].
The race car reaches the finish line before the "End" command.
So it manages to finish the stage.
The remaining directions will be ignored and no more moves are going to be executed.


Input
10
45
. . . . . . . . . .
. . T . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . F . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . T . .
right
down
down
right
up
left
up
up
End



Output
Racing car 45 DNF.
Distance covered 100 km.
..........
..........
..........
..........
..........
..........
......F...
......C...
..........
..........

"""
##########: variant 1 :##########
def distance(position, direction, size):
    row, col = position
    if direction == "up":
        row -= 1
    elif direction == "down":
        row += 1
    elif direction == "left":
        col -= 1
    elif direction == "right":
        col += 1
    return (row, col) if 0 <= row < size and 0 <= col < size else position

size = int(input())
car_number = str(input())
race_route = [input().split() for _ in range(size)]
kilometers = 0
position = [0, 0]

finished = False

while True:
    direction = input()
    if direction == "End":
        break

    new_position = distance(position, direction, size)
    new_r, new_c = new_position

    if race_route[new_r][new_c] == "T":
        race_route[new_position[0]][new_position[1]] = "."
        for r in range(size):
            for c in range(size):
                if race_route[r][c] == "T" and (r, c) != (new_r, new_c):
                    new_r, new_c = r, c
                    race_route[new_r][new_c] = "."
                    break
        kilometers += 30
    elif race_route[new_r][new_c] == "F":
        kilometers += 10
        position = [new_r, new_c]
        print(f"Racing car {car_number} finished the stage!")
        finished = True
        break
    else:
        kilometers += 10

    position = [new_r, new_c]

if not finished:
    print(f"Racing car {car_number} DNF.")

print(f"Distance covered {kilometers} km.")

race_route[position[0]][position[1]] = "C"

for row in race_route:
    print("".join(row))




##########: variant 2 :##########
def distance(position, direction, size):
    row, col = position
    if direction == "up":
        row -= 1
    elif direction == "down":
        row += 1
    elif direction == "left":
        col -= 1
    elif direction == "right":
        col += 1
    return (row, col) if 0 <= row < size and 0 <= col < size else position

def final(position, race_route):
    row, col = position
    return race_route[row][col] == "F"

def tunnel(position, race_route, size):
    row, col = position
    if race_route[row][col] == "T":
        race_route[row][col] = "."
        for r in range(size):
            for c in range(size):
                if race_route[r][c] == "T" and (r, c) != (row, col):
                    race_route[r][c] = "."
                    return (r, c), 30
    return position, 0

size = int(input())
car_number = str(input())
race_route = [input().split() for _ in range(size)]
kilometers = 0
position = [0, 0]

finished = False

while True:
    direction = input()
    if direction == "End":
        break

    new_position = distance(position, direction, size)
    new_position, additional_km = tunnel(new_position, race_route, size)
    kilometers += additional_km

    if final(new_position, race_route):
        kilometers += 10
        position = new_position
        print(f"Racing car {car_number} finished the stage!")
        finished = True
        break
    elif additional_km == 0:
        kilometers += 10

    position = new_position

if not finished:
    print(f"Racing car {car_number} DNF.")

print(f"Distance covered {kilometers} km.")

race_route[position[0]][position[1]] = "C"

for row in race_route:
    print("".join(row))


##########: variant 3 solution CEO :##########

SIZE = int(input())
racing_number = input()
matrix, tunnel, row, col, kilometers = [], [], 0, 0, 0

for row_ in range(SIZE):
    matrix.append(input().split())

    if "T" in matrix[row_]:
        tunnel.append([row_, matrix[row_].index("T")])

command = input()

while command != "End":

    if command == "up":
        row -= 1
    elif command == "down":
        row += 1

    elif command == "left":
        col -= 1
    elif command == "right":
        col += 1

    step_on = matrix[row][col]

    if step_on == ".":
        kilometers += 10

    elif step_on == "T":
        kilometers += 30
        matrix[row][col] = "."
        tunnel.remove([row, col])
        row, col = tunnel[0]
        matrix[row][col] = "."

    elif step_on == "F":
        kilometers += 10
        print(f"Racing car {racing_number} finished the stage!")
        break

    command = input()

else:
    print(f"Racing car {racing_number} DNF.")

matrix[row][col] = "C"

print(f"Distance covered {kilometers} km.")
[print(*row, sep="") for row in matrix]


##########: variant 4 solution TANER :##########
def find_tunnels():
    tunnel_positions = []
    for row in range(matrix_size):
        for col in range(len(matrix[row])):
            if matrix[row][col] == "T":
                tunnel_positions.append([row, col])
    return tunnel_positions


def check_index(row, col):
    if 0 <= row < matrix_size and 0 <= col < matrix_size:
        return True


def move(direction, is_finished, current_kms, car_row, car_col, tunnels_pos):
    for where, row, col in ('up', -1, 0), ('down', 1, 0), ('right', 0, 1), ('left', 0, -1):
        row, col = row + car_row, col + car_col
        if where == direction and check_index(row, col):
            if matrix[row][col] != "T" and matrix[row][col] != "F":
                current_kms += 10
            elif matrix[row][col] == "T":
                teleport_location = [x for x in tunnels_pos if x != [row, col]]
                matrix[row][col] = "."
                teleport_row, teleport_col = teleport_location[0][0], teleport_location[0][1]
                matrix[teleport_row][teleport_col] = "."
                current_kms += 30
                row, col = teleport_row, teleport_col
            elif matrix[row][col] == "F":
                is_finished = True
                current_kms += 10
            return is_finished, current_kms, [row, col]
    return is_finished, current_kms, [car_row, car_col]


def show_result(is_finished, row, col):
    matrix[row][col] = "C"
    if is_finished:
        print(f"Racing car {name_of_car} finished the stage!")
    elif not is_finished:
        print(f"Racing car {name_of_car} DNF.")
    print(f"Distance covered {kilometers} km.")
    [print(''.join(matrix[row])) for row in range(matrix_size)]


matrix_size = int(input())
name_of_car = input()
matrix = [[x for x in input().split()] for _ in range(matrix_size)]
finished, kilometers = False, 0
tunnels = find_tunnels()
car_position = [0, 0]
command = input()
while command != "End" and not finished:
    finished, kilometers, car_position = move(command, finished, kilometers, *car_position, tunnels)
    command = input()
show_result(finished, *car_position)


##########: variant 5 solution YAVOR :##########

# https://github.com/yavor-gornalov/softuni_python_advanced/blob/c0c946e5d54a9baa04bd53cdb2fd7aa514246ff4/python_advanced_exams/06_python_advanced_exam_22_october_2022/02_rally_racing.py

CAR, TUNNEL, EMPTY, FINISH = "C", "T", ".", "F"

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

race_size = int(input())
car_number = input()

race_field = []
tunnel_coordinates = []
for r in range(race_size):
    line = input().split()
    if TUNNEL in line:
        tunnel_coordinates.append([r, line.index(TUNNEL)])
    race_field.append(line)

finished = False
distance = 0
current_position = [0, 0]
while not finished:
    direction = input()
    r0, c0 = current_position

    if direction == "End":
        race_field[r0][c0] = CAR
        break
    row = r0 + directions[direction][0]
    col = c0 + directions[direction][1]

    race_field[r0][c0] = EMPTY

    if race_field[row][col] == TUNNEL:
        tunnel_coordinates.pop(tunnel_coordinates.index([row, col]))
        race_field[row][col] = EMPTY
        row, col = tunnel_coordinates.pop()
        distance += 30

    elif race_field[row][col] == EMPTY:
        distance += 10

    elif race_field[row][col] == FINISH:
        distance += 10
        finished = True

    race_field[row][col] = CAR
    current_position = [row, col]

if finished:
    print(f"Racing car {car_number} finished the stage!")
else:
    print(f"Racing car {car_number} DNF.")

print(f"Distance covered {distance} km.")

[print(*race_field[row], sep="") for row in range(race_size)]



##########: variant 6 solution SoftUni :##########

size_matrix = int(input())
car_number = input()
matrix = []
total_km_passed = 0
car_coordinates = [0, 0]

for _ in range(size_matrix):
    matrix.append(input().split())

size_matrix = int(input())
car_number = input()
matrix = []
total_km_passed = 0
car_coordinates = [0, 0]

for _ in range(size_matrix):
    matrix.append(input().split())


def find_end_of_dune(mx):
    for row in range(len(mx)):
        for col in range(len(mx[row])):
            if mx[row][col] == "T":
                return row, col


while True:
    command = input()
    if command == 'End':
        matrix[car_coordinates[0]][car_coordinates[1]] = "C"
        print(f"Racing car {car_number} DNF.")
        break
    elif command == "left":
        car_coordinates[1] -= 1
    elif command == "right":
        car_coordinates[1] += 1
    elif command == "up":
        car_coordinates[0] -= 1
    elif command == "down":
        car_coordinates[0] += 1
    if matrix[car_coordinates[0]][car_coordinates[1]] == "F":
        total_km_passed += 10
        matrix[car_coordinates[0]][car_coordinates[1]] = "C"
        print(f"Racing car {car_number} finished the stage!")
        break
    elif matrix[car_coordinates[0]][car_coordinates[1]] == "T":
        total_km_passed += 30
        matrix[car_coordinates[0]][car_coordinates[1]] = "."
        car_coordinates[0], car_coordinates[1] = find_end_of_dune(matrix)
        matrix[car_coordinates[0]][car_coordinates[1]] = "."
    else:
        total_km_passed += 10

print(f"Distance covered {total_km_passed} km.")
for row in range(len(matrix)):
    print("".join(matrix[row]))

def find_end_of_dune(mx):
    for row in range(len(mx)):
        for col in range(len(mx[row])):
            if mx[row][col] == "T":
                return row, col


while True:
    command = input()
    
    if command == 'End':
        matrix[car_coordinates[0]][car_coordinates[1]] = "C"
        print(f"Racing car {car_number} DNF.")
        break
        
    elif command == "left":
        car_coordinates[1] -= 1
    elif command == "right":
        car_coordinates[1] += 1
    elif command == "up":
        car_coordinates[0] -= 1
    elif command == "down":
        car_coordinates[0] += 1
        
    if matrix[car_coordinates[0]][car_coordinates[1]] == "F":
        total_km_passed += 10
        matrix[car_coordinates[0]][car_coordinates[1]] = "C"
        print(f"Racing car {car_number} finished the stage!")
        break
        
    elif matrix[car_coordinates[0]][car_coordinates[1]] == "T":
        total_km_passed += 30
        matrix[car_coordinates[0]][car_coordinates[1]] = "."
        car_coordinates[0], car_coordinates[1] = find_end_of_dune(matrix)
        matrix[car_coordinates[0]][car_coordinates[1]] = "."
        
    else:
        total_km_passed += 10

print(f"Distance covered {total_km_passed} km.")
for row in range(len(matrix)):
    print("".join(matrix[row]))

#################################### TASK CONDITION ############################
"""
https://judge.softuni.org/Contests/Compete/Index/3194#5

                        7.	Present Delivery
The presents are ready, and Santa has to deliver them to the kids. 
You will receive an integer m for the number of presents Santa has and an 
integer n for the size of the neighborhood with a square shape. On the following 
lines, you will receive the matrix, which represents the neighborhood. Santa 
will be in a random cell, marked with the letter "S". Each cell stands for a 
house where children may live. If the cell has "X" on it, that means there 
lives a naughty kid. Otherwise, if a nice kid lives there, the cell is marked 
by "V". There can also be cells marked with "C" for cookies. All of the empty 
positions will be marked with "-". Santa can move "up", "down", "left", "right" 
with one position each time. These will be the commands that you receive. If he 
moves to a house with a nice kid, the kid receives a present, but if Santa reaches 
a house with a naughty kid, he doesn't drop a present. If the command sends Santa 
to a cell marked with "C", Santa eats cookies and becomes happy and extra generous 
to all the kids around him* (meaning all of them will receive presents - it doesn't 
matter if naughty or nice). If Santa has been to a house, the cell becomes "-".
Note: *around him means on his left, right, upwards, and downwards by one cell. In 
this case, Santa doesn't move to these cells, or if he does, he returns to the cell 
where the cookie was. If Santa runs out of presents or receives the command 
"Christmas morning", you should end the program.  Keep in mind that you should 
check whether all the nice kids received presents.
Input
•	On the first line, you are given the integer m - the count of presents
•	On the second - integer n - the size of the neighborhood
•	The following n lines hold the values for every row
•	On each of the following lines you will get a command
Output
•	On the first line:
o	If Santa runs out of presents, but there are still some nice kids 
left print: "Santa ran out of presents!"
•	Next, print the matrix.
•	In the end, print one of these messages:
o	If he manages to give all the nice kids presents, print:
"Good job, Santa! {count_nice_kids} happy nice kid/s."
o	Otherwise, print: 
"No presents for {count nice kids} nice kid/s."
Constraints
•	The size of the square matrix will be between [2…10].
•	Santa's position will be marked with 'S'.
•	There will always be at least 1 nice kid.
•	There won't be a case where the cookie is on the border of the matrix.

____________________________________________________________________________________________
Example_01

Input
5
4
- X V -
- S - V
- - - -
X - - -
up
right
down
right
Christmas morning	

Output
- - - - 
- - - S 
- - - - 
X - - - 
Good job, Santa! 2 happy nice kid/s.	

Explanation
Santa has 5 presents. The size of the matrix is 4. After we receive the matrix, 
we start reading commands. The first one is "up". The "X" means there is a naughty 
kid, so Santa moves on without dropping any presents. Next, he reaches a nice kid 
and drops a present. The "down" command moves Santa to an empty cell. The last 
command before the "Christmas morning" message is "right". Again we have a nice kid. 
The count of nice kids reached 2, and we don't have any nice kids without presents left. 
So we print the appropriate message.

____________________________________________________________________________________________
Example_02

Input
3
4
- - - -
V - X -
- V C V
- - - S
left
up	

Output
Santa ran out of presents!
- - - - 
V - - - 
- - S - 
- - - - 
No presents for 1 nice kid/s.	

Explanation
The commands send Santa to a cell with a cookie, so all of the kids around him 
receive presents. He runs out of presents because we have 3 kids there and only 
3 presents. The program ends, and we have 1 nice kid that hasn't received a present. 

"""

##########: variant 1 :##########

SANTA, NICE, NAUGHTY, COOKIE, EMPTY = "S", "V", "X", "C", "-"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "initial": (0, 0)
}


def neighbours(mtrx, pos):
    global nice_kids, presents
    for d, coordinates in directions.items():
        r, c = pos
        r += coordinates[0]
        c += coordinates[1]
        if 0 <= r < len(mtrx) and 0 <= c < len(mtrx[0]):
            if presents > 0:
                if mtrx[r][c] == NICE:
                    presents -= 1
                    nice_kids -= 1
                elif mtrx[r][c] == NAUGHTY:
                    presents -= 1
                mtrx[r][c] = EMPTY


def santa_movement(mtrx, pos, dr):
    global nice_kids, presents
    r0, c0 = pos
    r = r0 + directions[dr][0]
    c = c0 + directions[dr][1]
    if 0 <= r < len(mtrx) and 0 <= c < len(mtrx[0]):
        if mtrx[r][c] == NICE:
            presents -= 1
            nice_kids -= 1
        elif mtrx[r][c] == COOKIE:
            neighbours(mtrx, (r, c))
        mtrx[r0][c0] = EMPTY
        mtrx[r][c] = SANTA
        return r, c
    return r0, c0


presents, size = int(input()), int(input())

matrix, santa_position, total_nice_kids = [], (), 0
for i in range(size):
    line = input().split()
    if SANTA in line:
        santa_position = (i, line.index(SANTA))
    if NICE in line:
        total_nice_kids += line.count(NICE)
    matrix.append(line)

nice_kids = total_nice_kids
command = input()
while command != "Christmas morning":
    santa_position = santa_movement(matrix, santa_position, command)
    if not presents:
        break
    command = input()

if not presents and nice_kids:
    print("Santa ran out of presents!")
[print(*matrix[i], sep=" ") for i in range(size)]
if nice_kids:
    print(f"No presents for {nice_kids} nice kid/s.")
else:
    print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")

##########: variant 2 :##########

SANTA, NAUGHTY_KID, NICE_KID, COOKIE, EMPTY = "S", "X", "V", "C", "-"
DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}

presents_count = int(input())
size = int(input())
row, col = None, None  # Santa initial position
nice_kids_count = 0
matrix = []
for cookie_r in range(size):
    line = [x for x in input().split()]
    if SANTA in line:
        row, col = cookie_r, line.index(SANTA)
    if NICE_KID in line:
        nice_kids_count += line.count(NICE_KID)
    matrix.append(line)

nice_kids_left = nice_kids_count
while presents_count:
    command = input()
    if command == "Christmas morning":
        break
    next_row = row + DIRECTIONS[command][0]
    next_col = col + DIRECTIONS[command][1]

    if matrix[next_row][next_col] == NICE_KID:
        nice_kids_left -= 1
        presents_count -= 1
    elif matrix[next_row][next_col] == NAUGHTY_KID:
        pass
    elif matrix[next_row][next_col] == COOKIE:
        for r0, c0 in DIRECTIONS.values():
            if not presents_count:
                break
            cookie_r = next_row + r0
            cookie_c = next_col + c0
            if matrix[cookie_r][cookie_c] in [NAUGHTY_KID, NICE_KID]:
                if matrix[cookie_r][cookie_c] == NICE_KID:
                    nice_kids_left -= 1
                matrix[cookie_r][cookie_c] = EMPTY
                presents_count -= 1

    matrix[row][col] = EMPTY
    matrix[next_row][next_col] = SANTA
    row, col = next_row, next_col

if presents_count == 0 and nice_kids_left > 0:
    print("Santa ran out of presents!")
[print(*row) for row in matrix]
if nice_kids_left == 0:
    print(f"Good job, Santa! {nice_kids_count} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_left} nice kid/s.")



##########: variant 3 :##########


class PresentDelivery:

    def __init__(self):
        self.output_message = ''
        self.presents = int(input())
        self.size = int(input())
        self.neighborhood = []
        self.santa_pos = []
        self.total_good_kids = 0
        self.visited_good_kids = 0
        self.moves = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }
        self.actions = {
            'C': self.cookie_boost,
            'V': self.visit_nice_kid
        }
        self.main_meth()

    def main_meth(self):
        self.create_neighborhood_find_santa_count_good_kids()
        self.start_giving_presents()
        self.prepare_output_message()

    def create_neighborhood_find_santa_count_good_kids(self):
        for row in range(self.size):
            line = input().split()
            if 'S' in line:
                self.santa_pos = [row, line.index('S')]
            if 'V' in line:
                self.total_good_kids += line.count('V')
            self.neighborhood.append(line)

    def start_giving_presents(self):
        while self.presents:
            data = input()
            if data == 'Christmas morning':
                break
            self.neighborhood[self.santa_pos[0]][self.santa_pos[1]] = '-'
            self.santa_pos = [self.santa_pos[0] + self.moves[data][0],
                              self.santa_pos[1] + self.moves[data][1]]

            cell = self.neighborhood[self.santa_pos[0]][self.santa_pos[1]]
            if cell in self.actions:
                self.actions[cell]()
            self.neighborhood[self.santa_pos[0]][self.santa_pos[1]] = 'S'

            if self.total_good_kids == self.visited_good_kids:
                break

    def visit_nice_kid(self):
        self.presents -= 1
        self.visited_good_kids += 1

    def cookie_boost(self):
        for direction in self.moves:
            row = self.santa_pos[0] + self.moves[direction][0]
            col = self.santa_pos[1] + self.moves[direction][1]
            cell = self.neighborhood[row][col]
            if cell in ['X', 'V']:
                if cell == 'V':
                    self.visit_nice_kid()
                else:
                    self.presents -= 1
                self.neighborhood[row][col] = '-'

            if not self.presents:
                break

    def prepare_output_message(self):
        if not self.presents and self.total_good_kids > self.visited_good_kids:
            self.output_message += 'Santa ran out of presents!\n'
        self.output_message += '\n'.join(' '.join(row) for row in self.neighborhood)
        if self.total_good_kids > self.visited_good_kids:
            left_kid = self.total_good_kids - self.visited_good_kids
            self.output_message += f'\nNo presents for {left_kid} nice kid/s.'
        else:
            self.output_message += f'\nGood job, Santa! {self.total_good_kids} happy nice kid/s.'

    def __repr__(self):
        return self.output_message


if __name__ == '__main__':
    print(PresentDelivery())



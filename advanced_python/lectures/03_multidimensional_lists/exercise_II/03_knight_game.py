#################################### TASK CONDITION ############################
"""
https://judge.softuni.org/Contests/Compete/Index/3194#2

                             3.	Knight Game
Chess is the oldest game, but it is still popular these days.
It will be used only one chess piece for this task - the Knight.
A chess knight has 8 possible moves it can make, as illustrated.
It can move to the nearest square but not on the same row, column,
or diagonal. (e.g., it can move two squares horizontally, then one
square vertically, or it can move one square horizontally then two
squares vertically - i.e., in an "L" pattern.)
The knight game is played on a board with dimensions N x N.
You will receive a board with "K" for knights and "0" for empty cells.
Your task is to remove knights until no knights that can attack one
another with one move are left.  Always remove the knight who can attack
the greatest number of knights. If there are two or more knights with the
same number of attacks, remove the top-left one.
Input
•	On the first line, you will receive integer N - the size of the board
•	On the following N lines, you will receive strings with "K" and "0"
Output
•	Print a single integer with the number of knights that need to be removed.
Constraints
•	The size of the board will be 0 < N < 30
•	Time limit: 0.3 sec. Memory limit: 16 MB

____________________________________________________________________________________________
Example_01

Input
5
0K0K0
K000K
00K00
K000K
0K0K0

Output
1

____________________________________________________________________________________________
Example_02

Input
2
KK
KK

Output
0

____________________________________________________________________________________________
Example_03

Input
8
0K0KKK00
0K00KKKK
00K0000K
KKKKKK0K
K0K0000K
KK00000K
00K0K000
000K00KK

Output
12

"""
##########: variant 1 :##########

def main():
    rows = int(input().strip())

    pos_knights = []
    matrix = []

    for row in range(rows):
        line = list(input().strip())
        matrix.append(line)
        for col in range(len(line)):
            if line[col] == 'K':
                pos_knights.append((row, col))

    cols = len(matrix[0])

    def check_valid_index(row, col):
        return 0 <= row < rows and 0 <= col < cols

    movements = [
        (-2, -1), (-2, 1), (2, -1), (2, 1),
        (-1, -2), (-1, 2), (1, -2), (1, 2)
    ]

    def count_attacks(row, col):
        count = 0
        for m_row, m_col in movements:
            n_row, n_col = row + m_row, col + m_col
            if check_valid_index(n_row, n_col) and matrix[n_row][n_col] == 'K':
                count += 1
        return count

    total_knights_removed = 0

    while True:
        max_attacks = 0
        knight_to_remove = None

        for row, col in pos_knights:
            attacks = count_attacks(row, col)
            if attacks > max_attacks:
                max_attacks = attacks
                knight_to_remove = (row, col)

        if max_attacks == 0:
            break

        row, col = knight_to_remove
        matrix[row][col] = '0'
        pos_knights.remove((row, col))
        total_knights_removed += 1

    print(total_knights_removed)

if __name__ == "__main__":
    main()


##########: variant 2 :##########

def knights_attacked(mtrx, pos):
    row, col = pos
    count = 0
    for direction in directions:
        x, y = direction
        r, c = row + x, col + y
        if 0 <= r <= len(mtrx) - 1 and 0 <= c <= len(mtrx[0]) - 1:
            if mtrx[r][c] == KNIGHT:
                count += 1
    return count


KNIGHT, EMPTY = "K", "0"

n = int(input())
board = []
knights = []
for i in range(n):
    row, text = [], input()
    for j, ele in enumerate(text):
        if ele == KNIGHT:
            knights.append([(i, j), -1])
        row.append(ele)
    board.append(row)

directions = {
    (-2, -1),
    (-1, -2),
    (-2, 1),
    (-1, 2),
    (1, 2),
    (2, 1),
    (2, -1),
    (1, -2),
}

count_removed = 0
while True:
    if all(ele[1] == 0 for ele in knights):
        break
    max_attacker_idx = None
    max_attacker_pos = ()
    max_attacked_count = -1
    for idx, knight in enumerate(knights):
        knight[1] = knights_attacked(board, knight[0])
        if knight[1] > max_attacked_count:
            max_attacker_idx = idx
            max_attacker_pos = knight[0]
            max_attacked_count = knight[1]

    if max_attacked_count > 0:
        knights.pop(max_attacker_idx)
        row, col = max_attacker_pos
        board[row][col] = EMPTY
        count_removed += 1

print(count_removed)

##########: variant 3 :##########

KNIGHT, EMPTY = "K", "0"
POSSIBLE_MOVES = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]


def knight_attacks_counter(matrix, knight):
    counter = 0
    for move in POSSIBLE_MOVES:
        row = knight[0] + move[0]
        col = knight[1] + move[1]
        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
            continue
        if matrix[row][col] == KNIGHT:
            counter += 1
    return counter


def get_max_attacker():
    max_attacks_count = 0
    max_attacker = None
    for knight in knights:
        current_attacks_count = knight_attacks_counter(board, knight)
        if current_attacks_count > max_attacks_count:
            max_attacks_count = current_attacks_count
            max_attacker = knight
    return max_attacker


board_size = int(input())
board = []
knights = []

for r in range(board_size):
    line = list(input())
    for c in range(board_size):
        if line[c] == KNIGHT:
            knights.append((r, c))
    board.append(line)

knight_to_remove = get_max_attacker()
removed_knights_counter = 0
while True:
    knight_to_remove = get_max_attacker()
    if not knight_to_remove:
        break
    row, col = knight_to_remove
    board[row][col] = EMPTY
    removed_knights_counter += 1
    knights.remove((row, col))

print(removed_knights_counter)


##########: variant 4 :##########

rows = int(input())

pos_knights,  matrix, total_knights = [], [], [0]
for row in range(rows):
    matrix.append(list(input()))
    for col in range(len(matrix[0])):
        if matrix[row][col] == "K":
            pos_knights.append([row, col])

cols = len(matrix[0])


def check_valid_index(row, col):
    if 0 <= row < rows and 0 <= col < cols:
        return True


movement = {
    "up left": [-2, -1], "up right": [-2, 1], "down left": [2, -1], "down right": [2, 1],
    "left up": [-1, -2], "left down": [1, -2], "right up": [-1, 2], "right down": [1, 2],
}


def check_knights():
    result = {}
    for row, col in pos_knights:
        for m_row, m_col in movement.values():
            knight_row, knight_col = row + m_row, col + m_col
            if check_valid_index(knight_row, knight_col) and matrix[knight_row][knight_col] == "K":
                result[f"{row} {col}"] = result.get(f"{row} {col}", 0) + 1
    if not result:
        return
    total_knights[0] += 1
    row, col = [int(x) for x in max(result, key=result.get).split()]
    matrix[row][col] = "0"
    pos_knights.remove([row, col])
    check_knights()


check_knights()
print(total_knights[0])



##########: variant 5 :##########



class KnightGame:

    def __init__(self):
        self.output_message = ''
        self.size = int(input())
        self.chess_board = []
        self.removed_knights = 0
        self.moves = [
            (-2, -1),
            (-2, 1),
            (-1, -2),
            (-1, 2),
            (2, -1),
            (2, 1),
            (1, -2),
            (1, 2)
        ]
        self.main_meth()

    def main_meth(self):
        self.fill_chess_board_with_elements()
        self.start_attacks()

    def fill_chess_board_with_elements(self):
        self.chess_board = [list(input()) for _ in range(self.size)]

    def start_attacks(self):
        while True:
            location = self.check_for_best_attacker_knight()

            if location:
                self.chess_board[location[0]][location[1]] = '0'
                self.removed_knights += 1
            else:
                break

    def check_for_best_attacker_knight(self):
        greatest_attacker = 0
        greatest_attacker_location = []
        for row in range(self.size):
            for col in range(len(self.chess_board[row])):
                symbol = self.chess_board[row][col]
                if symbol == 'K':
                    knight_attacks = self.check_knight_attacks(row, col)
                    if knight_attacks > greatest_attacker:
                        greatest_attacker = knight_attacks
                        greatest_attacker_location = [row, col]
        return greatest_attacker_location

    def check_knight_attacks(self, row, col):
        attacks = 0
        for way in self.moves:
            knight_row = row + way[0]
            knight_col = col + way[1]
            if 0 <= knight_row < self.size and 0 <= knight_col < self.size:
                if self.chess_board[knight_row][knight_col] == 'K':
                    attacks += 1
        return attacks

    def __repr__(self):
        return str(self.removed_knights)


if __name__ == '__main__':
    print(KnightGame())

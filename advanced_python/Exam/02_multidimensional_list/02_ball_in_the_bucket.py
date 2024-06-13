# ******* Advanced Exam - 23 October 2021 ******* #

# *******  02_ball_in_the_bucket  ******* #

# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/3227#1

You are at the funfair to play different games and test your skills.
Now you are playing ball in the bucket game.

You will be given a matrix with 6 rows and 6 columns representing the board.
On the board, there will be points (integers) and buckets marked with the letter "B". Rules of the game:

•	You can throw a ball only 3 times.
•	When you hit a bucket (position marked with 'B'), you score the sum of the points in the same column.
•	You can hit a bucket only once. If you hit the same bucket again, you do not score any points.
•	If you hit outside a bucket (hit a number on the board) or outside the board, you do not score any points.

After the board state, you are going to receive the information for every throw on a separate line.
The coordinates’ information of a hit will be in the format:
"({row}, {column})".

Depending on how many points you have collected, you win one of the following:

Football	            100 to 199 points
Teddy Bear	            200 to 299 points
Lego Construction Set	300 and more points

Your job is to keep track of the scored points and to check if you won a prize.
For more clarifications, see the examples below.

Input
•	6 lines – matrix representing the board (each position separated by a single space)
•	On the next 3 lines - the coordinates of the throw in the format: "({row}, {column})"

Output
•	On the first line:
    o	If you won a prize, print:
        "Good job! You scored {points} points, and you've won {prize}."
    o	If you did not win any prize, print the points you need to get at least the first prize:
        "Sorry! You need {points} points more to win a prize."

Constraints
•	All of the given points will be integers in the range [1, 30]
•	All the given indexes will be integers in the range [0, 30]
•	There always will be exactly 6 buckets - 1 on each column


Examples

Input

10 30 B 4 20 24
7 8 27 23 11 19
13 3 14 B 17 В
12 5 21 22 9 6
B 26 1 28 29 2
25 B 16 15 B 18
(1, 1)
(20, 15)
(4, 0)

Output
Sorry! You need 33 points more to win a prize.


Input

B 30 14 23 20 24
29 8 27 18 11 19
13 3 B B 17 6
28 5 21 22 9 B
10 B 26 12 B 2
25 1 16 15 7 4
(0, 0)
(2, 2)
(2, 3)


Output

Good job! You scored 299 points, and you've won Teddy Bear.

B B B B B B
B 8 27 18 11 19
B 3 B B 17 6
B 5 21 22 9 B
B B 26 12 B 2
B 1 16 15 7 4
(0, 0)
(0, 2)
(0, 1)
Output
Good job! You scored 212 points, and you've won Teddy Bear.
"""

##########: variant 1 :##########

board, size = [], 6
coordinates_of_B = []
shots_range = 3

for r in range(size):
    line = input().split(" ")
    line = [int(el) if el.isdigit() else el for el in line]
    board.append(line)

    for c, el in enumerate(line):
        if el == "B":
            coordinates_of_B.append((r, c))

total_points = 0
hit_buckets = set()

for _ in range(shots_range):
    x, y = input().strip("()").split(", ")
    x, y = int(x), int(y)

    if (x, y) in coordinates_of_B and (x, y) not in hit_buckets:
        hit_buckets.add((x, y))
        total_points += sum(board[r][y] for r in range(size) if isinstance(board[r][y], int))

if total_points >= 300:
    prize = "Lego Construction Set"
elif 200 <= total_points < 300:
    prize = "Teddy Bear"
elif 100 <= total_points < 200:
    prize = "Football"
else:
    prize = None

if prize:
    print(f"Good job! You scored {total_points} points, and you've won {prize}.")
else:
    needed_points = 100 - total_points
    print(f"Sorry! You need {needed_points} points more to win a prize.")

##########: variant 2 :##########

board, size = [], 6
coordinates_of_B = []
shots_range = 3

for r in range(size):
    line = input().split(" ")
    line = [int(el) if el.isdigit() else el for el in line]
    board.append(line)

    for c, el in enumerate(line):
        if el == "B":
            coordinates_of_B.append((r, c))
            board[r][c] = 0

total_points = 0
hit_buckets = set()
for _ in range(shots_range):
    x, y = input().strip("()").split(", ")
    x, y = int(x), int(y)

    if (x, y) in coordinates_of_B and (x, y) not in hit_buckets:
        hit_buckets.add((x, y))
        column_sum = sum(board[r][y] for r in range(size))
        total_points += column_sum

if total_points >= 300:
    prize = "Lego Construction Set"
elif 200 <= total_points < 300:
    prize = "Teddy Bear"
elif 100 <= total_points < 200:
    prize = "Football"
else:
    prize = None


if total_points < 100:
    needed_points = 100 - total_points
    print(f"Sorry! You need {needed_points} points more to win a prize.")
else:
    print(f"Good job! You scored {total_points} points, and you've won {prize}.")


# print(*board)

##########: variant 3 solution whit Functions :##########

def read_board(size):
    board = []
    coordinates_of_B = []
    for r in range(size):
        line = input().split(" ")
        line = [int(el) if el.isdigit() else el for el in line]
        board.append(line)
        for c, el in enumerate(line):
            if el == "B":
                coordinates_of_B.append((r, c))
                board[r][c] = 0
    return board, coordinates_of_B

def read_shots(shots_range):
    shots = []
    for _ in range(shots_range):
        x, y = input().strip("()").split(", ")
        x, y = int(x), int(y)
        shots.append((x, y))
    return shots

def calculate_points(board, coordinates_of_B, shots, size):
    total_points = 0
    hit_buckets = set()
    for x, y in shots:
        if (x, y) in coordinates_of_B and (x, y) not in hit_buckets:
            hit_buckets.add((x, y))
            column_sum = sum(board[r][y] for r in range(size))
            total_points += column_sum
    return total_points

def determine_prize(total_points):
    if total_points >= 300:
        return "Lego Construction Set"
    elif 200 <= total_points < 300:
        return "Teddy Bear"
    elif 100 <= total_points < 200:
        return "Football"
    else:
        return None

def main():
    size = 6
    shots_range = 3

    board, coordinates_of_B = read_board(size)
    shots = read_shots(shots_range)
    total_points = calculate_points(board, coordinates_of_B, shots, size)
    prize = determine_prize(total_points)

    if prize:
        print(f"Good job! You scored {total_points} points, and you've won {prize}.")
    else:
        needed_points = 100 - total_points
        print(f"Sorry! You need {needed_points} points more to win a prize.")

    print(board)

if __name__ == "__main__":
    main()

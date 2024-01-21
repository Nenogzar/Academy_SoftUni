# You will receive a field of a tic-tac-toe game in three lines containing numbers, separated by a single space.
# Legend:
# •	0 - empty space
# •	1 - first player move
# •	2 - second player move
# Find out who the winner is. If the first player wins, print "First player won".
# If the second player wins, print "Second player won". Otherwise, print "Draw!".

matrix = []

for run in range(3):
    list_app = list(map(int, input().split()))
    matrix.append(list_app)
first_player = False
second_player = False

# Check for rows and columns
for i in range(3):
    # Rows
    if matrix[i][0] == matrix[i][1] == matrix[i][2] != 0:
        if matrix[i][0] == 1:
            first_player = True
        elif matrix[i][0] == 2:
            second_player = True

    # Columns
    if matrix[0][i] == matrix[1][i] == matrix[2][i] != 0:
        if matrix[0][i] == 1:
            first_player = True
        elif matrix[0][i] == 2:
            second_player = True

# Check diagonals
if matrix[0][0] == matrix[1][1] == matrix[2][2] != 0:
    if matrix[0][0] == 1:
        first_player = True
    elif matrix[0][0] == 2:
        second_player = True

if matrix[0][2] == matrix[1][1] == matrix[2][0] != 0:
    if matrix[0][2] == 1:
        first_player = True
    elif matrix[0][2] == 2:
        second_player = True

# Determine the winner or draw
if first_player:
    print("First player won")
elif second_player:
    print("Second player won")
else:
    print("Draw!")

##############################################*-*AI*-*#############################################

# lines = [input().split() for _ in range(3)]
# first_player_win = None
#
# for player in ['1', '2']:
#     if (any(all(cell == player for cell in line) for line in lines)
#             or any(all(line[i] == player for line in lines) for i in range(3))):
#         first_player_win = (player == '1')
#         break
#
# # Check diagonals for both players
# for player in ['1', '2']:
#     if (all(lines[i][i] == player for i in range(3))
#             or all(lines[i][2 - i] == player for i in range(3))):
#         first_player_win = (player == '1')
#         break
#
# if first_player_win is None:
#     print("Draw!")
# elif first_player_win:
#     print("First player won")
# else:
#     print("Second player won")


###########################################*-*FROM*CEO*-*###########################################

# first_line = input().split(" ")
# second_line = input().split(" ")
# third_line = input().split(" ")
#
# first_player_win = None
#
# if len(set(first_line)) == 1 and first_line[0] == "1":
#     first_player_win = True
#
# elif len(set(second_line)) == 1 and second_line[0] == "1":
#     first_player_win = True
#
# elif len(set(third_line)) == 1 and third_line[0] == "1":
#     first_player_win = True
#
# elif first_line[0] == second_line[1] == third_line[2] and first_line[0] == "1":
#     first_player_win = True
#
# elif first_line[1] == second_line[1] == third_line[1] and first_line[1] == "1":
#     first_player_win = True
#
# elif first_line[2] == second_line[1] == third_line[0] and first_line[2] == "1":
#     first_player_win = True
#
# elif first_line[2] == second_line[2] == third_line[2] and first_line[2] == "1":
#     first_player_win = True
#
# elif first_line[0] == second_line[0] == third_line[0] and first_line[0] == "1":
#     first_player_win = True
#
# elif len(set(first_line)) == 1 and first_line[0] == "2":
#     first_player_win = False
#
# elif len(set(second_line)) == 1 and second_line[0] == "2":
#     first_player_win = False
#
# elif len(set(third_line)) == 1 and third_line[0] == "2":
#     first_player_win = False
#
# elif first_line[0] == second_line[1] == third_line[2] and first_line[0] == "2":
#     first_player_win = False
#
# elif first_line[1] == second_line[1] == third_line[1] and first_line[1] == "2":
#     first_player_win = False
#
# elif first_line[2] == second_line[1] == third_line[0] and first_line[2] == "2":
#     first_player_win = False
#
# elif first_line[2] == second_line[2] == third_line[2] and first_line[2] == "2":
#     first_player_win = False
#
# elif first_line[0] == second_line[0] == third_line[0] and first_line[0] == "2":
#     first_player_win = False
#
#
# if first_player_win is None:
#     print("Draw!")
#
# elif first_player_win:
#     print("First player won")
#
# else:
#     print("Second player won")


###########################################*-*FROM*CEO*-*###########################################


# first_row = input().split()
# second_row = input().split()
# third_row = input().split()
#
# name_player = "First"
# found = False
#
# for player in range(1, 3):
#     player = str(player)
#     line = [player, player, player]
#     if line == first_row or second_row == line or third_row == line:  # преверка на редовете
#         found = True
#     for index in range(0, 3):
#         if first_row[index] == player and second_row[index] == player and third_row[index] == player:  # проверка на колоните
#             found = True
#     if first_row[0] == player and second_row[1] == player and third_row[2] == player:  # ляв диагонал
#         found = True
#     elif first_row[2] == player and second_row[1] == player and third_row[0] == player:  # десен диагонал
#         found = True
#     if found:
#         print(f"{name_player} player won")
#         break
#     name_player = "Second"
# else:
#     print("Draw!")
###########################################*-*FROM*CEO*-*###########################################

# field = []
#
# first_player_win = False
# second_player_win = False
# draw = False
# #  drawing the game field in separate lists
# for field_row in range(3):
#     current_row = input().split()
#     field.append(current_row)
# #  checking each row to see if there is a winner in the row
# for row in range(3):
#     if field[row][0] == field[row][1] == field[row][2] != "0":
#         if field[row][0] == field[row][1] == field[row][2] == "1":
#             first_player_win = True
#         elif field[row][0] == field[row][1] == field[row][2] == "2":
#             second_player_win = True
# #  checking each column to see if there is a winner in the column
# for col in range(3):
#     if field[0][col] == field[1][col] == field[2][col] != "0":
#         if field[0][col] == field[1][col] == field[2][col] == "1":
#             first_player_win = True
#         elif field[0][col] == field[1][col] == field[2][col] == "2":
#             second_player_win = True
# #  checking left diagonal if there is a winner
# if field[0][0] == field[1][1] == field[2][2] != "0":
#     if field[0][0] == field[1][1] == field[2][2] == "1":
#         first_player_win = True
#     elif field[0][0] == field[0][1] == field[2][2] == "2":
#         second_player_win = True
# #  checking right diagonal if there is a winner
# elif field[0][2] == field[1][1] == field[2][0] != "0":
#     if field[0][2] == field[1][1] == field[2][0] == "1":
#         first_player_win = True
#     elif field[0][2] == field[1][1] == field[2][0] == "2":
#         second_player_win = True
# # if there is no winner found the game is a draw
# if not first_player_win and not second_player_win:
#     draw = True
#
# if first_player_win:
#     print("First player won")
# elif second_player_win:
#     print("Second player won")
# elif draw:
#     print("Draw!")
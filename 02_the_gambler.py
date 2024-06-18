# ******* Advanced Retake Exam - 13 December 2023 ******* #

# *******  02_the_gambler  ******* #
 
# *******  TASK CONDITION  ******* #
"""
https://judge.softuni.org/Contests/Practice/Index/4226#1

You will be given an integer n for the size of the game board (square shape). On the next n lines, you will receive the rows of the board. The gambler will start at a random position, marked with the letter 'G' and have an initial 'entering the game' amount of 100$.
On each turn, until command 'end' is received, you will receive commands for the direction, in which the gambler should move. The commands will be "up", "down", "left" and "right".
•	If a position with '-' (dash) is reached, it means that the field is empty and the gambler awaits its next direction.
•	If the position marked with the letter 'W' is reached the gambler takes it and adds 100$ to his amount
•	If the position marked with the letter 'P' (penalty) is reached decrease the gambler's total amount by 200$
•	If the position marked with the letter 'J' is reached the gambler wins the jackpot and adds 100000$ to his amount and the game ends.
•	If the gambler leaves the boundaries of the board or his total amount becomes equal to or drops below 0 (zero), he loses everything and you should stop the program.
The current gambler position should be marked with 'G'
When the gambler leaves a position marked with a letter it should be replaced by '-' (dash)
The program ends when one of these four events occurs:
•	the gambler leaves the board boundaries
•	command 'end' is received
•	the gambler's total winning amount is equal to or drops below 0(zero)
•	the position marked with 'J' is reached
Input
•	On the first line, you are given the integer n – the size of the matrix (board).
•	The next n lines hold the values for every row.
•	On each of the next lines, you will get a direction command.
Output
•	If you win the jackpot on the first and second lines print:
o	"You win the Jackpot!
End of the game. Total amount: {amount}$"
•	If you do not win the jackpot print:
o	"End of the game. Total amount: {amount}$"
•	If you leave the boundaries of the matrix or the gambler's amount becomes 0(zero) or below print:
o	"Game over! You lost everything!"
Constraints
•	The square matrix (board) size will be between [4…10].
•	Gambler's starting position will always be marked with 'G'.
•	There will always be a field marked with 'W' and it may appear more than once.
•	There will be always one field marked with 'J'.
•	There will always be one or two fields marked with 'P'.
•	You will always receive enough commands to end the game.
•	Finally if you have any amount print the matrix.
Examples

Input
4
W-GW
W--W
--P-
----
down
down
end


Output
Game over! You lost everything!


Comment
The movement starts from position [0,2] after receiving the command "down" the gambler moves to position [1,2] where there is a '-' (dash) field - nothing is happening. The next command is "down" again, the gambler lands on a 'P' (penalty) field and since he has to pay 200$ his sum becomes negative (100 – 200 = -100) and therefore loses it. The game ends.


Input
4
G---
WWWW
P---
PJ--
right
right
right
down
left
left
end


Output
End of the game. Total amount: 400$
----
WG--
P---
PJ--


Input
4
---G
W-W-
---P
--JW
left
down
down
down
right
end


Output
You win the Jackpot!
End of the game. Total amount: 100200$
----
W---
---P
--GW



"""

##########: variant 1 :##########





##########: variant 2 :##########



##########: variant 3 solution SoftUni :##########

# # Function to handle the current position of the gambler
# def handle_current_position(position, board, sum_val, jackpot):
#     current_char = board[position[0]][position[1]]
#
#     if current_char == 'J':
#         sum_val += 100000
#         jackpot = True
#     elif current_char == 'W':
#         sum_val += 100
#     elif current_char == 'P':
#         sum_val -= 200
#
#     board[position[0]][position[1]] = 'G'
#
#     return sum_val, jackpot
#
#
# # Function to check if the total amount becomes zero or negative
# def zero_amount(sum_val):
#     return sum_val <= 0
#
#
# # Function to print the game over message
# def game_over():
#     print("Game over! You lost everything!")
#
#
# # Function to move the gambler on the board based on the command
# def move_gambler(command, position, board):
#     row, col = position
#     board[row][col] = '-'
#     if command == "up":
#         position[0] -= 1
#     elif command == "down":
#         position[0] += 1
#     elif command == "left":
#         position[1] -= 1
#     elif command == "right":
#         position[1] += 1
#
#     return position
#
#
# # Function to check if the gambler is out of bounds
# def is_out_of_bounds(position, size):
#     return position[0] < 0 or position[0] >= size or position[1] < 0 or position[1] >= size
#
#
# # Function to find the starting position of the gambler
# def find_start_position(size, fishing_area):
#     for i in range(size):
#         for j in range(size):
#             if fishing_area[i][j] == 'G':
#                 return [i, j]
#     return None
#
#
# # Function to fill the board with input data
# def fill_board(size):
#     board = []
#     for _ in range(size):
#         board.append(list(input()))
#     return board
#
#
# size = int(input())
# board = fill_board(size)
# current_position = find_start_position(size, board)
# sum_val = 100
# jackpot = False
#
# while True:
#     if jackpot:
#         print("You win the Jackpot!")
#         break
#     command = input()
#
#     if current_position:
#         current_position = move_gambler(command, current_position, board)
#
#     if is_out_of_bounds(current_position, size) or zero_amount(sum_val):
#         game_over()
#         break
#     else:
#         sum_val, jackpot = handle_current_position(current_position, board, sum_val, jackpot)
#
#     if command == "end":
#         break
#
# if not (is_out_of_bounds(current_position, size) or zero_amount(sum_val)):
#     print(f"End of the game. Total amount: {sum_val}$")
#     for row in board:
#         print(''.join(row))


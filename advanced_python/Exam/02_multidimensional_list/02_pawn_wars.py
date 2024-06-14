# ******* Advanced Exam - 19 February 2022 ******* #

# *******  02_pawn_wars  ******* #
 
# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/3374#1


	A	B	C	D	E	F	G	H
8	A8	8B	C8	D8	E8	F8	G8	H8	8
7	A7	7B	C7	D7	E7	F7	G7	H7	7
6	A6	6B	C6	D6	E6	F6	G6	H6	6
5	A5	5B	C5	D5	E5	F5	G5	H5	5
4	A4	4B	C4	D4	E4	F4	G4	H4	4
3	A3	3B	C3	D3	E3	F3	G3	H3	3
2	A2	2B	C2	D2	E2	F2	G2	H2	2
1	A1	1B	C1	D1	E1	F1	G1	H1	1
	A	B	C	D	E	F	G	H


A chessboard has 8 rows and 8 columns. Rows, also called ranks, are marked from number 1 to 8,
    and columns are marked from A to H. We have a total of 64 squares.
    Each square is represented by a combination of letters and a number (a1, b1, c1, etc.).
        In this problem colors of the board will be ignored.

We will play the game with two pawns, white (w) and black (b), where they can:
•	Only move forward in a straight line:
    White (w) moves from the 1st rank to the 8th rank direction.
    Black (b) moves from 8th rank to the 1st rank direction.
•	Can move only 1 square at a time.
•	Can capture another pawn in from of them only diagonally:

When a pawn reaches the last rank (for the white one
    - this is the 8th rank, and for the black one
        - this is the 1st rank), can be promoted to a queen.

Two pawns (w and b) will be placed on two random squares of the bord.
    The first move is always made by the white pawn (w), then black moves (b), then white (w) again, and so on.


Some rules apply when moving paws:
•	If the two pawns interact diagonally, the player, in turn, must capture the opponent's pawn.
    When a pawn captures another pawn, the game is over.
•	If no capture is possible, the pawns keep on moving until one of them reaches the last rank.

Input
•	On 8 lines, you will receive each row with its 8 columns, each element separated by a single space:
    o	Empty positions are marked with "-".
    o	White pawn is marked with "w"
    o	Black pawn is marked with "b"

Output

Print either one of the following:
•	If a pawn captures the other, print:
    "Game over! {White/Black} win, capture on {square}."
•	If a pawn reaches the last rank, print:
    "Game over! {White/Black} pawn is promoted to a queen at {square}."

Constraints

•	The input will always be valid.
•	The matrix will always be 8x8.
•	There will be no case where two pawns are placed on the same square.
•	There will be no case where two pawns are placed on the same column.
•	There will be no case where black/white will be placed on the last rank.

Examples

Input
- - - - - - b -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- w - - - - - -
- - - - - - - -
- - - - - - - -


Output
Game over! White pawn is promoted to a queen at b8.


Comments
We start by pushing the white pawn to b4, next, we push the black pawn to g7:
- - - - - - - -
- - - - - - b -
- - - - - - - -
- - - - - - - -
- w - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
Then white play b5, black play g6:
- - - - - - - -
- - - - - - - -
- - - - - - b -
- w - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
…
Capturing is not possible here, so after a few more moves, the white pawn is promoted to a queen on b8.


Input
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
b - - - - - - -
- w - - - - - -
- - - - - - - -

Output
Game over! White win, capture on a3.

Comments
A white pawn always start first, so it must capture the black one on a3 in the first move:
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
w - - - - - - -
- - - - - - - -
- - - - - - - -


"""

##########: variant 1 :##########



##########: variant 2 :##########



##########: variant 3 solution SoftUni :##########



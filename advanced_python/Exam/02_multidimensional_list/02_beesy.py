# ******* Advanced Regular Exam - 22 June 2024 ******* #

# *******  02_beesy  ******* #
 
# *******  TASK CONDITION  ******* #
"""

https://judge.softuni.org/Contests/Compete/Index/4796#1


Bees are indispensable for maintaining the health of ecosystems,
    promoting biodiversity, supporting agriculture, and ensuring food availability for human populations worldwide.
    Protecting bee populations and their habitats is crucial for the well-being of both ecosystems and humanity.

You will be given an integer n for the size of the field with a square shape.
On the next n lines, you will receive the rows of the field.

•	Your bee will be placed in a random position, marked with the letter 'B'.
•	There will be flowers with nectar which need to be pollinated on random positions, marked with a single digit.
•	There will be a hive, marked with the letter 'H'.
•	All of the empty positions will be marked with '-'.
The bee will have 15 units of energy initially.
A command is received each turn until the bee runs out of energy or reaches the hive.
The bee must collect and take at least 30 units of nectar to the hive. This would be the required quantity to make honey successfully.
Keep in mind that even if the needed amount of nectar is collected, but the hive is not reached the bee continues to move according to the commands.
You will be given commands for the bee's movement. The commands will be: "up", "down", "left", and "right". The bee moves towards the given direction. With each move, the bee's energy decreases by 1 unit.
•	If the bee leaves the field (goes out of the boundaries of the matrix) depending on the move command,
 it will be moved to the opposite side of the field.
Example: In a 3x3 matrix the bee is at position [1,2] and receives the command "right" it will be moved to position [1,0].
•	If the bee moves to a flower (a position marked with a digit), it collects the nectar (the value of the digit is added to the total amount of collected nectar) the flower disappears and should be replaced by '-'.
•	If the bee runs out of energy, and the total amount of collected nectar is less than 30 units, the program ends. The correct output should be printed on the Console.
•	If the bee runs out of energy and the total amount of collected nectar is at least 30 units, the energy will be restored with the amount of the difference between the nectar collected up to this turn and the minimum required amount for making honey (30). The value of the collected nectar is dropped to 30 units. The energy can be restored only once.
Example: Collected nectar is equal to 40 units. 40 – 30 = 10. The bee's energy is increased by 10, the nectar is decreased to 30 units.
Hint: Check for zero energy after restoration.
o	The next time the bee runs out of energy, the movement discontinues. The program ends.
The correct output should be printed on the Console.
•	If the bee reaches a position, marked with  'H', the hive is reached and the program ends.
Hint: When reaching the hive with zero energy, the success will depend on the amount of the collected nectar.
The correct output should be printed on the Console.
Input
•	On the first line, you are given the integer n – the size of the square matrix.
•	The next n lines contain the values for every matrix row.
•	After that, you will get commands to move (each one on a new line).
Output
•	On the first line:
o	If the bee reaches the hive with at least 30 units of nectar collected, print this message and stop the program:
	"Great job, Beesy! The hive is full. Energy left: {energy}"
o	If the bee reaches the hive but has not succeeded in collecting at least 30 units of nectar:
	"Beesy did not manage to collect enough nectar."
o	If the bee runs out of energy, before returning to the hive:
	"This is the end! Beesy ran out of energy."
•	On the next lines.
o	Print the final state of the matrix, with the last known position of the bee, marked with 'B'.
Constraints
•	The size of the square matrix (field) will be between [2…10].
•	Only the letters 'B' and 'H' will be present in the matrix.
•	The flowers with nectar are represented by single positive digits between [0…9].
•	There will always be enough commands to finish the program.
•	The bee will always have 15 units of energy initially.

"""
##########: variant 1 :##########









##########: variant 2 :##########



##########: variant 3 solution SoftUni :##########



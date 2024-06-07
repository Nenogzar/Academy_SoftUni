# ******* Advanced Retake Exam - 13 December 2023 ******* #

# *******  01_worms_and_holes  ******* #

# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/4226#0

The first line will give you a sequence of integers representing worms. Afterwards, you will be given another sequence of integers representing holes.
You have to start with the last worm and try to match it with the first hole.
•	If their values are equal, the worm fits the hole and can get into it. After that, you should remove both of them from their sequences. Otherwise, you should remove the hole and decrease the value of the worm by 3.
•	If the worm value becomes equal to or below 0, remove it from the sequence before trying to match it with the hole.
You need to stop matching when you have no more worms or holes.
Input / Constraints
•	On the first line, you will receive the integers, representing the worm size, separated by a single space.
•	On the second line, you will receive the integers, representing the hole size, separated by a single space.
•	All given numbers will be valid integers in the range [1, 50].
Output
•	On the first line:
	If there are matches print the following:
o	"Matches: {matchesCount}"
	If there are no matches print the following:
o	"There are no matches."
•	On the second line print:
	If there are no worms left and all of them fit a hole:
o	"Every worm found a suitable hole!"
	If there are no worms left but only some of them fit a hole:
o	"Worms left: none"
	If there are worms left:
o	"Worms left: {worm1}, {worm2}, (…),{wormn}"
•	On the third line print:
	If there are no holes left:
o	"Holes left: none"
	If there are holes left:
o	"Holes left: {hole1}, {hole2}, (…),{holen}"

Examples

Input
9 5 8 13
13 8 5 6

Output
Matches: 3
Worms left: 6
Holes left: none

Comment
The first pair is the first hole with a value of 13 and the last worm with a value of 13,
their values are equal, so the worm gets into the hole and we remove values from the sequences.
Next, there are two more matches (8 = 8) and (5 = 5)  you should remove both of them, too.
But the value of the next worm is 9 and the value of the next hole is 6, (9 > 6)
so we reduce the worm’s value by 3 and remove the hole.

Input
17 20 25 25 30
9 8 7 21 5 4 3 2 1

Output
Matches: 1
Worms left: 17, 20, 25, 10
Holes left: none

Input
9 8 7 6
6 7 8 9

Output
Matches: 4
Every worm found a suitable hole!
Holes left: none

Input
10 10 10 10
5

Output
There are no matches.
Worms left: 10, 10, 10, 7
Holes left: none

"""

##########: variant 1 :##########
from collections import deque

worms = list(map(int, input().split()))
holes = deque(map(int, input().split()))
worm_count = len(worms)
matches = 0

while worms and holes:
    worm = worms.pop()
    hole = holes.popleft()

    if worm == hole:
        matches += 1
        continue
    worm -= 3
    if worm <= 0:
        continue
    worms.append(worm)

print((f"Matches: {matches}") if matches else "There are no matches.")

if not worms and matches == worm_count:
    print("Every worm found a suitable hole!")
elif not worms and matches != worm_count:
    print("Worms left: none")
elif worms:
    print_string = [f"{atr}" for atr in worms]
    print(f"Worms left: {', '.join(print_string)}")

if holes:
    print_holes = [f'{hol}' for hol in holes]
    print(f"Holes left: {', '.join(print_holes)}")
else:
    print("Holes left: none")

##########: variant 2 :##########

from collections import deque

worms = [int(x) for x in input().split()]
holes = deque([int(x) for x in input().split()])

worms_length = len(worms)
matches = 0
while worms and holes:
    current_worm = worms.pop()
    current_hole = holes.popleft()

    if current_worm == current_hole:
        matches += 1
        continue

    current_worm -= 3
    if current_worm <= 0:
        continue

    worms.append(current_worm)


if matches:
    print(f"Matches: {matches}")
elif not matches:
    print("There are no matches.")


if not worms and matches == worms_length:
    print("Every worm found a suitable hole!")
elif not worms and matches != worms_length:
    print("Worms left: none")
elif worms:
    print(f"Worms left: {', '.join(str(x) for x in worms)}")


if not holes:
    print("Holes left: none")
elif holes:
    print(f"Holes left: {', '.join(str(x) for x in holes)}")

##########: variant 3 solution SoftUni :##########

# Read the sequences of worms and holes as lists of integers.
worms = list(map(int, input().split()))
holes = list(map(int, input().split()))

# Initialize variables to keep track of matches and the original number of worms.
matches = 0
worms_size = len(worms)

# While there are still worms and holes to process.
while worms and holes:
    # Get the current worm and hole for comparison.
    current_worm = worms[-1]
    current_hole = holes[0]

    if current_worm == current_hole:
        # A match is found, remove both the worm and the hole.
        worms.pop()
        holes.pop(0)
        matches += 1
    else:
        # Decrease the worm size by 3 and check if it becomes zero or negative.
        worms[-1] -= 3
        if worms[-1] <= 0:
            worms.pop()
        holes.pop(0)


# If there are matches, print the number of matches.
print(f"Matches: {matches}" if matches != 0 else "There are no matches.")

if matches != worms_size:
    # If not all worms found a suitable hole, print the remaining worms.
    print(f"Worms left: {', '.join(map(str, worms))}" if worms else "Worms left: none")
else:
    # If all worms found suitable holes, print a message.
    print("Every worm found a suitable hole!")

# Print the remaining holes, if any.
print(f"Holes left: {', '.join(map(str, holes))}" if holes else "Holes left: none")

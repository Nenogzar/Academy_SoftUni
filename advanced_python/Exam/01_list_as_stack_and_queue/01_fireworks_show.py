# ******* Advanced Exam - 14 February 2021 ******* #

# *******  01_fireworks_show  ******* #

# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/2812#0

Maria wants to make a firework show for the wedding of her best friend.
We should help her to make the perfect firework show.

    First, you will be given a sequence of integers representing firework effects.
Afterwards you will be given another sequence of integers representing explosive power.

You need to start from the first firework effect and try to mix it with the last explosive power.
    If the sum of their values is:
    •	divisible by 3, but it is not divisible by 5 –
        create Palm firework and remove both materials
    •	divisible by 5, but it is not divisible by 3 –
        create Willow firework and remove both materials
    •	divisible by both 3 and 5 –
        create Crossette firework and remove both materials
Otherwise, decrease the value of the firework effect by 1 and move it at the end of the sequence.
Then, try to mix the same explosive power with the next firework effect.

If any value is equal to or below 0, you should remove it from the sequence before trying to mix it with the other.
When you have successfully prepared enough fireworks for the show or
you have no more firework punches or explosive power, you need to stop mixing.

To make the perfect firework show, Maria needs 3 of each of the firework types.

Input
•	On the first line, you will receive the integers representing the firework effects, separated by ", ".
•	On the second line, you will receive the integers representing the explosive power, separated by ", ".
Output

•	On the first line, print:
    o	if Maria successfully prepared the firework show: "Congrats! You made the perfect firework show!"
    o	if Maria failed to prepare it: "Sorry. You can't make the perfect firework show."
•	On the second line, print all firework effects left if there are any:
    o	"Firework Effects left: {effect1}, {effect2}, (…)"
•	On the third line, print all explosive fillings left if there are any:
    o	" Explosive Power left: {filling1}, {filling2}, (…)"
•	Then, you need to print all fireworks and the amount you have of them:
    o	"Palm Fireworks: {count}"
    o	"Willow Fireworks: {count}"
    o	"Crossette Fireworks: {count}"

Constraints
•	All the given numbers will be integers in the range [-100, 100].
•	There will be no cases with empty sequences.

Input
5, 6, 4, 16, 11, 5, 30, 2, 3, 27
1, 13, 5, 3, -7, 32, 19, 3, 5, 7, 22

Output
Congrats! You made the perfect firework show!
Palm Fireworks: 4
Willow Fireworks: 3
Crossette Fireworks: 3


Input
-15, -8, 0, -16, 0, -22
10, 5

Output
Sorry. You can't make the perfect firework show.
Explosive Power left: 10, 5
Palm Fireworks: 0
Willow Fireworks: 0
Crossette Fireworks: 0



Input

Output
"""

##########: variant 1 :##########

from collections import deque

# Входни данни
firework_effects = deque(map(int, input().split(", ")))
explosive_power = list(map(int, input().split(", ")))

fireworks_created = {
    "Palm": 0,
    "Willow": 0,
    "Crossette": 0
}

def find_effect(result):
    if result % 3 == 0 and result % 5 == 0:
        return "Crossette"
    elif result % 3 == 0:
        return "Palm"
    elif result % 5 == 0:
        return "Willow"
    return None


while firework_effects and explosive_power:
    firework = firework_effects.popleft()
    power = explosive_power.pop()

    if firework <= 0:
        explosive_power.append(power)
        continue
    if power <= 0:
        firework_effects.appendleft(firework)
        continue

    result = firework + power
    firework_type = find_effect(result)

    if firework_type:
        fireworks_created[firework_type] += 1
    else:

        firework -= 1
        firework_effects.append(firework)
        explosive_power.append(power)

    if all(count >= 3 for count in fireworks_created.values()):
        break


if all(count >= 3 for count in fireworks_created.values()):
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print("Firework Effects left:", ", ".join(map(str, firework_effects)))

if explosive_power:
    print("Explosive Power left:", ", ".join(map(str, explosive_power)))


print(f"Palm Fireworks: {fireworks_created['Palm']}")
print(f"Willow Fireworks: {fireworks_created['Willow']}")
print(f"Crossette Fireworks: {fireworks_created['Crossette']}")

##########: variant 2 :##########


##########: variant 3 solution SoftUni :##########

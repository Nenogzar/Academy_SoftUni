# ******* Advanced Retake Exam - 09 August 2023 ******* #

# *******  01_monster_extermination  ******* #

# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/4089#0

You are tasked with simulating a battle between a brave soldier and a group of terrifying monsters.
The soldier has a striking impact, and the monsters have different levels of armor.
Your task is to write a program that takes two sequences of integers as input from the console and performs the battle simulation.
There will be given two sequences of integers.

The first sequence represents the armor of the monsters.
Each integer value represents the armor of a different monster.

The second sequence represents the soldier's striking impact.
Each integer value represents the strength of a strike performed by the soldier.

Battle Rules:
•	The monster at the front will be the first to face the soldier.
    Take the first armor value and the last strike strength value and compare the values.

•	If the soldier's striking impact is greater than or equal to the monster's armor,
    the monster is killed, and its armor is removed from the sequence.
    The soldier's strike impact is then decreased by the value of the monster's armor.
    The remaining striking impact value is added to the next strike element in the sequence (if any)
    or is considered to be the last and only element. Zero values should not be pushed back to the sequence.

•	If the soldier's striking impact is less than the monster's armor,
    the strike is performed, but the monster survives with reduced armor.
    The soldier's striking impact value is removed from the sequence,
    and the monster's armor value is decreased by the original strike value.
    The monster is then moved to the back of the sequence.
•	The battle goes on until one of the sequences becomes empty.

Your Task:
Write a console application to simulate the battle as described above.
Implement the battle logic using appropriate data structures to manage
the soldier's striking impact and the monsters' armor values.
The program should then display the appropriate outcome of the battle based on the rules.

Input
•	The first line will represent the armor values - integers, comma-separated values.
•	The second line will represent the soldier's striking impact values - integers, comma-separated values.


Output
•	If all the monsters are killed, the program should print on the Console a success message:
    "All monsters have been killed!"

•	If the soldier's striking impact stack becomes empty, the program should print on the Console a message indicating that the soldier has been defeated:
    "The soldier has been defeated."

•	The program should print on the Console the  total number of monsters killed by the soldier, on a new line:
    "Total monsters killed: {killed_monsters}"


Constraints
    •	All the given numbers will be valid integers in the range [1, 100].
    •	There will be no negative inputs.

Input
20,15,10
5,15,10,25

Output
All monsters have been killed!
Total monsters killed: 3

Comment
1)	The soldier’s first strike (last in the sequence) (25) is greater than the first monster's armor (20).
    Monster 1 is killed. Its armor value is removed from the sequence.
    The soldiers’ striking impact value is decreased by the monster’s armor value and it remains (5).
    It is added to the next element in the sequence (10)
2)	The soldier’s second strike (15 {10 + 5}) is equal to the second monster's armor (15).
    Monster 2 is killed. Its armor value is removed from the sequence.
    The soldiers’ striking impact value is decreased by the monster’s armor value and it remains (0).
    It is not necessary to be added to the next element. It just can be removed from the sequence.
3)	The soldier’s third strike (15) is greater than the third monster's armor (10).
    Monster 3 is killed. Its armor value is removed from the sequence.
    The monster’s armor sequence is empty, so the program ends, and the output is printed on the Console.
    All monsters have been killed. The soldier wins the battle, having killed 3 monsters.

Input
30,25,40,35
15,20,10,30

Output
The soldier has been defeated.
Total monsters killed: 1

Comment
1)	The soldier’s first strike (30) is equal to the first monster's armor (30).
    Monster 1 is killed. Its armor value is removed from the sequence.
    The soldiers’ striking impact value is decreased by the monster’s armor value and it remains (0).
    It is not necessary to be added to the next element. It just can be removed from the sequence.
2)	The soldier’s second strike (10) is less than the second monster's armor (25).
    Monster 2 survives with 15 armor remaining. Monster 2 moves to the back of the sequence.
3)	The soldier’s third strike (20) is less than the third monster's armor (40).
    Monster 3 survives with 20 armor remaining.
4)	The soldier’s fourth strike (15) is less than the fourth monster's armor (35).
    Monster 4 survives with 20 armor remaining.
5)	The soldier has no more strikes left, but there are still three monsters remaining.
    The soldier is defeated, having killed 1 monster.

"""

##########: variant 1 :##########
from collections import deque

monster_armor = deque(map(int, input().split(",")))
soldier_triking = list(map(int, input().split(",")))
killed_monsters = 0

while monster_armor and soldier_triking:

    armor = monster_armor.popleft()
    strength = soldier_triking.pop()

    if strength >= armor:
        strength -= armor
        killed_monsters += 1


        if soldier_triking:
            soldier_triking[-1] += strength
        elif not soldier_triking and strength != 0:
            soldier_triking.append(strength)

    elif armor > strength:
        armor -= strength
        monster_armor.append(armor)

if not monster_armor:
    print(f"All monsters have been killed!")
if not soldier_triking:
    print(f"The soldier has been defeated.")
print(f"Total monsters killed: {killed_monsters}")

##########: variant 2 :##########


##########: variant 3 solution SoftUni :##########

from collections import deque

armours_que = deque([int(x) for x in input().split(',')])
strikes_stack = [int(x) for x in input().split(',')]

monsters_defeated = 0
while armours_que and strikes_stack:
    current_armour = armours_que.popleft()
    current_strike = strikes_stack.pop()
    if current_strike >= current_armour:
        monsters_defeated += 1
        current_strike -= current_armour
        if strikes_stack:
            strikes_stack[-1] += current_strike
        elif not strikes_stack and current_strike > 0:
            strikes_stack.append(current_strike)
    else:
        current_armour -= current_strike
        armours_que.append(current_armour)

if not armours_que:
    print("All monsters have been killed!")
if not strikes_stack:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {monsters_defeated}")
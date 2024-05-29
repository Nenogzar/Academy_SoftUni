#################################### TASK CONDITION ############################
"""
Python Advanced Retake Exam - 09 August 2023

https://judge.softuni.org/Contests/Practice/Index/4089#0

01.	Monster Extermination
You are tasked with simulating a battle between a brave soldier and a group of terrifying monsters. 
The soldier has a striking impact, and the monsters have different levels of armor. 
Your task is to write a program that takes two sequences of integers as input from the console and performs the battle simulation.
There will be given two sequences of integers. 
The first sequence represents the armor of the monsters. Each integer value represents the armor of a different monster.
The second sequence represents the soldier's striking impact. Each integer value represents the strength of a strike performed by the soldier.
Battle Rules:
  •	The monster at the front will be the first to face the soldier. Take the first armor value and the last strike strength value and compare the values.
  •	If the soldier's striking impact is greater than or equal to the monster's armor, the monster is killed, and its armor is removed from the sequence. 
    The soldier's strike impact is then decreased by the value of the monster's armor. 
    The remaining striking impact value is added to the next strike element in the sequence (if any) or is considered to be the last and only element. Zero values should not be pushed back to the sequence.
  •	If the soldier's striking impact is less than the monster's armor, the strike is performed, but the monster survives with reduced armor. 
    The soldier's striking impact value is removed from the sequence, and the monster's armor value is decreased by the original strike value. The monster is then moved to the back of the sequence. 
  •	The battle goes on until one of the sequences becomes empty.

Your Task:
Write a console application to simulate the battle as described above. Implement the battle logic using appropriate data structures to manage the soldier's striking impact and the monsters' armor values. The program should then display the appropriate outcome of the battle based on the rules.

Input
  •	The first line will represent the armor values - integers, comma-separated values.
  •	The second line will represent the soldier's striking impact values - integers, comma-separated values.
Output
  •	If all the monsters are killed, the program should print on the Console a success message: 
    o	"All monsters have been killed!"
  •	If the soldier's striking impact stack becomes empty, the program should print on the Console a message indicating that the soldier has been defeated:
    o	"The soldier has been defeated."
  •	The program should print on the Console the  total number of monsters killed by the soldier, on a new line:
    o	"Total monsters killed: {killed_monsters}"
Constraints
  •	All the given numbers will be valid integers in the range [1, 100].
  •	There will be no negative inputs.

Input

20,15,10
5,15,10,25


Output
All monsters have been killed!
Total monsters killed: 3

Input
30,25,40,35
15,20,10,30

Output
The soldier has been defeated.
Total monsters killed: 1

"""

##########: variant 1 :##########

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

##########: variant 2 :##########

from collections import deque

armor_values = deque([int(x) for x in input().split(",")])
impact_values = deque([int(x) for x in input().split(",")])

killed_monsters = 0
while armor_values and impact_values:
    monster_armor = armor_values.popleft()
    solder_strike = impact_values.pop()
    if solder_strike >= monster_armor:
        killed_monsters += 1
        solder_strike -= monster_armor
        if solder_strike:
            if impact_values:
                impact_values[-1] += solder_strike
            else:
                impact_values.append(solder_strike)
    else:
        monster_armor -= solder_strike
        armor_values.append(monster_armor)

if not armor_values:
    print("All monsters have been killed!")
if not impact_values:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {killed_monsters}")


##########: variant 3 :##########

from collections import deque

monster_armors = deque(int(x) for x in input().split(","))
soldier_strikings = [int(x) for x in input().split(",")]
monsters_killed = 0

while monster_armors and soldier_strikings:
    armor = monster_armors.popleft()
    strike = soldier_strikings.pop()

    if strike >= armor:
        strike -= armor
        monsters_killed += 1

        if strike:
            if soldier_strikings:
                soldier_strikings[-1] += strike

            elif not soldier_strikings:
                soldier_strikings.append(strike)

    elif strike < armor:
        armor -= strike
        monster_armors.append(armor)


if not monster_armors:
    print("All monsters have been killed!")

if not soldier_strikings:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {monsters_killed}")

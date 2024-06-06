# ******* Advanced Exam - 27 June 2020 ******* #

# *******  01_bombs  ******* #
 
# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/2456#0

Ezio is still learning how to make bombs. With their help, he will save civilization.
We should help Ezio to make his perfect bombs.

You will be given two sequences of integers, representing bomb effects and bomb casings.
You need to start from the first bomb effect and try to mix it with the last bomb casing.
If the sum of their values is equal to any of the materials in the table below – create the bomb corresponding to the value and remove both bomb materials. Otherwise, just decrease the value of the bomb casing by 5. You need to stop combining when you have no more bomb effects or bomb casings, or you successfully filled the bombs pouch.

Bombs:
•	Datura Bombs: 40
•	Cherry Bombs: 60
•	Smoke Decoy Bombs: 120
To fill the bomb pouch, Ezio needs three of each of the bomb types.
Input
•	On the first line, you will receive the integers representing the bomb effects, separated by ", ".
•	On the second line, you will receive the integers representing the bomb casings, separated by ", ".
Output
•	On the first line, print:
o	if Ezio succeeded to fulfill the bomb pouch:
    "Bene! You have successfully filled the bomb pouch!"
o	if Ezio didn't succeed to fulfill the bomb pouch: "You don't have enough materials to fill the bomb pouch."
•	On the second line, print all bomb effects left:
o	If there are no bomb effects: "Bomb Effects: empty"
o	If there are effects: "Bomb Effects: {bombEffect1}, {bombEffect2}, (…)"
•	On the third line, print all bomb casings left:
o	If there are no bomb casings: "Bomb Casings: empty"
o	If there are casings: "Bomb Casings: {bombCasing1}, {bombCasing2}, (…)"
•	Then, you need to print all bombs and the count you have of them, ordered alphabetically:
o	"Cherry Bombs: {count}"
o	"Datura Bombs: {count}"
o	"Smoke Decoy Bombs: {count}"
Constraints
•	All of the given numbers will be valid integers in the range [0, 120].
•	There will be no cases with negative material.


Examples
Input
5, 25, 25, 115
5, 15, 25, 35

Output
You don't have enough materials to fill the bomb pouch.
Bomb Effects: empty
Bomb Casings: empty
Cherry Bombs: 0
Datura Bombs: 3
Smoke Decoy Bombs: 1

Comment
1) 5 + 35 = 40 -> Datura Bomb. Remove both.
2) 25 + 25 = 50 -> can't create bomb. Bomb casing should be decreased with 5 -> 20
3) 25 + 20 = 45 -> can't create bomb. Bomb casing should be decreased with 5 -> 15
4) 25 + 15 = 40 -> Datura Bomb. Remove both
…

Input
30, 40, 5, 55, 50, 100, 110, 35, 40, 35, 100, 80
20, 25, 20, 5, 20, 20, 70, 5, 35, 0, 10

Output
Bene! You have successfully filled the bomb pouch!
Bomb Effects: 100, 80
Bomb Casings: 20
Cherry Bombs: 3
Datura Bombs: 4
Smoke Decoy Bombs: 3

Comment
…
After creating a bomb with bomb effect 35 and bomb casing 25,
    have created 3 Cherry bombs,
    4 Datura bombs, and 3 Smoke Decoy bombs.
    From all of the bomb types we have 3 bombs, so the program ends.


"""


##########: variant 1 :##########

from collections import deque

bombs = {
    "Datura Bombs": 40,
    "Cherry Bombs": 60,
    "Smoke Decoy Bombs": 120,
}
make_bombs = {
    "Datura Bombs": 0,
    "Cherry Bombs": 0,
    "Smoke Decoy Bombs": 0,
}
bomb_effects = deque(map(int, input().split(", ")))
bomb_casings = list(map(int, input().split(", ")))

while bomb_effects and bomb_casings:
    effect = bomb_effects.popleft()
    casing = bomb_casings.pop()

    while True:
        mix = effect + casing
        if mix in bombs.values():
            bomb_name = next(key for key, value in bombs.items() if value == mix)
            make_bombs[bomb_name] += 1
            break
        else:
            casing -= 5
            if casing < 0:
                break

    if all(count >= 3 for count in make_bombs.values()):
        break

if all(count >= 3 for count in make_bombs.values()):
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join(map(str, bomb_effects))}")
else:
    print("Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join(map(str, bomb_casings))}")
else:
    print("Bomb Casings: empty")

for bomb_name in sorted(make_bombs.keys()):
    print(f"{bomb_name}: {make_bombs[bomb_name]}")


##########: variant 2 :##########

from collections import deque

bombs = {
    "Datura Bombs": [40, 0],
    "Cherry Bombs": [60, 0],
    "Smoke Decoy Bombs": [120, 0],
}

bomb_effects = deque(map(int, input().split(", ")))
bomb_casings = list(map(int, input().split(", ")))

while bomb_effects and bomb_casings:
    effect = bomb_effects.popleft()
    casing = bomb_casings.pop()

    while True:
        mix = effect + casing
        bomb_made = False
        for bomb_name, (value, count) in bombs.items():
            if mix == value:
                bombs[bomb_name][1] += 1
                bomb_made = True
                break

        if bomb_made:
            break
        else:
            casing -= 5
            if casing < 0:
                break

    if all(count >= 3 for value, count in bombs.values()):
        break


if all(count >= 3 for value, count in bombs.values()):
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join(map(str, bomb_effects))}")
else:
    print("Bomb Effects: empty")


if bomb_casings:
    print(f"Bomb Casings: {', '.join(map(str, bomb_casings))}")
else:
    print("Bomb Casings: empty")


for bomb_name in sorted(bombs.keys()):
    print(f"{bomb_name}: {bombs[bomb_name][1]}")


##########: variant 3 solution CEO :##########

from collections import deque

bomb_effects = deque(int(x) for x in input().split(", "))
bomb_casings = [int(x) for x in input().split(", ")]
full_set = False

bombs = {
    "Cherry Bombs": 0,
    "Datura Bombs": 0,
    "Smoke Decoy Bombs": 0
}

while bomb_effects and bomb_casings and not full_set:
    effect = bomb_effects.popleft()
    casing = bomb_casings.pop()
    mix_effect = effect + casing
    for bomb, quantity in (("Datura Bombs", 40), ("Cherry Bombs", 60), ("Smoke Decoy Bombs", 120)):
        if mix_effect == quantity:
            bombs[bomb] += 1
            break
    else:
        bomb_casings.append(casing - 5)
        bomb_effects.appendleft(effect)
    if all(x >= 3 for x in bombs.values()):
        full_set = True

if full_set:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effects)}")
else:
    print("Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casings)}")
else:
    print("Bomb Casings: empty")

for bomb, quantity in bombs.items():
    print(f"{bomb}: {quantity}")


##########: variant 3 solution TANER :##########

from collections import deque


def check_if_the_bombs_are_enough():
    enough_bombs = [1 for key, value in made_bombs.items() if value['count'] > 2]
    if sum(enough_bombs) == 3:
        return True


bomb_effects = deque(int(x) for x in input().split(", "))
bomb_casings = deque(int(x) for x in input().split(", "))
made_bombs = {
    40: {'name': 'Datura Bombs', 'count': 0},
    60: {'name': 'Cherry Bombs', 'count': 0},
    120: {'name': 'Smoke Decoy Bombs', 'count': 0}
}
filled_bomb_pouch = False
while bomb_effects and bomb_casings:
    current_effect = bomb_effects[0]
    current_casing = bomb_casings[-1]
    bomb_power = current_effect + current_casing
    if bomb_power in made_bombs:
        made_bombs[bomb_power]['count'] += 1
        bomb_effects.popleft()
        bomb_casings.pop()
        if check_if_the_bombs_are_enough():
            filled_bomb_pouch = True
            break
        continue
    bomb_casings[-1] -= 5
if filled_bomb_pouch:
    print("Bene! You have successfully filled the bomb pouch!")
elif not filled_bomb_pouch:
    print("You don't have enough materials to fill the bomb pouch.")
if not bomb_effects:
    print("Bomb Effects: empty")
elif bomb_effects:
    print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effects)}")
if not bomb_casings:
    print("Bomb Casings: empty")
elif bomb_casings:
    print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casings)}")
for key, value in sorted(made_bombs.items(), key=lambda item: item[1]['name']):
    print(f"{value['name']}: {value['count']}")

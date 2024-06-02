############################## 01_energy_drinks ##############################
  ############################## TASK CONDITION ##############################
"""
 https://judge.softuni.org/Contests/Practice/Index/3596#0

 Your friend Stamat is working on a new AI program. Like every irresponsible teenager,
 he programs all night and, of course, drinks a lot of energy drinks.
 Stamat's friends are concerned about him and want you
 to create a program that tells him when to stop the energy drinks and start drinking water.

On the first line,
    you will receive a sequence of numbers representing milligrams of caffeinе.

On the second line,
    you will receive another sequence of numbers representing energy drinks.

It is important to know that the maximum caffeine Stamat can have for the night is 300 milligrams, and his initial is always 0.

To calculate the caffeine in the drink take the last milligrams of caffeinе and
the first energy drink, and multiply them.
Then, compare the result with the caffeine Stamat drank:

•	If the sum of the caffeine in the drink and the caffeine that Stamat drank doesn't exceed 300 milligrams,
    remove both the milligrams of caffeinе and the drink from their sequences.
    Also, add the caffeine to Stamat's total caffeine.

•	If Stamat is about to exceed his maximum caffeine per night,
    do not add the caffeine to Stamat’s total caffeine.
    Remove the milligrams of caffeinе and move the drink to the end of the sequence.
    Also, reduce the current caffeine that Stamat has taken by 30 (Note: Stamat's caffeine cannot go below 0).

Stop calculating when you are out of drinks or milligrams of caffeine.

For more clarification, see the examples below.

Input
•	In the first line, you will be given a sequence of the milligrams of caffeinе
    - integers separated by comma and space ", " in the range [1, 50]
•	In the second line, you will be given a sequence of energy drinks
    - integers separated by comma and space ", " in the range [1, 300]

Output
•	On the first line:
    o	If Stamat hasn't drunk all the energy drinks, print the remaining ones separated by a comma and a space ", ":
    "Drinks left: { remaining drinks separated by ", " }"

    o	If Stamat has drunk all the energy drinks, print:
    "At least Stamat wasn't exceeding the maximum caffeine."

•	On the next line, print:
    "Stamat is going to sleep with { current caffeine } mg caffeine."

Constraints

•	You will always have at least one element in each sequence at the beginning.


Input

34, 2, 3
40, 100, 250

Output

Drinks left: 100, 250
Stamat is going to sleep with 60 mg caffeine.

*** Comment ***
1) Take the last milligrams of caffeine (3) and multiply them by the first energy drink (40).
    The result(120) doesn’t exceed the caffeine limit per day (300), so we can add it to Stamat's caffeine.
    Remove both items from their sequences. Stamat can accept 180 miligrams of caffeine more.
2) Take the next mg of caffeine (2) and multiply them by the next energy drink (100).
    The result is 200 and if he takes the drink, he will exceed the caffeine limit per day.
    We remove the mg of caffeine (2) and place the drink (100) at the end of the sequence ("250, 100").
    Then, decrease Stamat's caffeine by 30 (Stamat's caffeine becomes 90).
    Stamat can accept 210 miligrams of caffeine more.
3) Take the next mg of caffeine (34) and multiply them by the next energy drink (250).
    The result(8500) is above 210, so we remove the mg of caffeine (34) and place the drink (250)
    at the end of the sequence ("100, 250").
    Then, decrease Stamat's caffeine by 30 (Stamat's caffeine becomes 60).

4) Stamat slept with 60 mg of caffeine.

*** ***

Input

1, 16, 8, 14, 5
27, 23

Output

At least Stamat wasn't exceeding the maximum caffeine.
Stamat is going to sleep with 289 mg caffeine.

Input
1, 23, 2, 1, 42, 22, 7, 14
51, 100, 3, 7

Output

At least Stamat wasn't exceeding the maximum caffeine.
Stamat is going to sleep with 264 mg caffeine.


"""

##########: variant 1 :##########
from collections import deque


cofeine_mg = deque(map(int, input().split(", ")))
energy_drinks = deque(map(int, input().split(", ")))

max_caffeine = 300
total_energy = 0

while energy_drinks and cofeine_mg:

    cofeine = cofeine_mg.pop()
    energy = energy_drinks.popleft()
    current_energy = cofeine * energy

    if total_energy + current_energy > max_caffeine:
        energy_drinks.append(energy)
        total_energy -= 30
    else:
        total_energy += current_energy

if energy_drinks:
    print(f"Drinks left: {', '.join(map(str, energy_drinks))}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {total_energy} mg caffeine.")


##########: variant 2 solution SoftUni :##########
from collections import deque
milligrams_caffeine = list(map(int, input().split(", ")))
energy_drinks = deque(map(int, input().split(", ")))

stamat_caffeine = 0

while True:
    if not milligrams_caffeine:
        break
    if not energy_drinks:
        break
    current_milligrams_caffeine = milligrams_caffeine.pop()
    current_energy_drink = energy_drinks.popleft()
    caffeine = current_milligrams_caffeine * current_energy_drink
    if caffeine + stamat_caffeine <= 300:
        stamat_caffeine += caffeine
    else:
        energy_drinks.append(current_energy_drink)
        stamat_caffeine -= 30
        if stamat_caffeine < 0:
            stamat_caffeine = 0


if energy_drinks:
    print(f"Drinks left: { ', '.join(map(str, energy_drinks)) }")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {stamat_caffeine} mg caffeine.")


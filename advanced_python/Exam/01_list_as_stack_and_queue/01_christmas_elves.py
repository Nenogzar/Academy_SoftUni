# ******* Advanced Retake Exam - 15 December 2021 ******* #

# *******  01_christmas_elves  ******* #
 
# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/3306#0

Everything in the Satna Claus' workshop was going well until, on one freezing Sunday, a dangerous storm destroyed almost all toys.
Now Santa's elves fear they won't be able to meet their December deadline.

It could be a disaster, and some children around the world may not get their Christmas toys.
Luckily, you've come up with an idea, and you just need to write a program that manages your plan.

The Christmas elves have special toy-making skills - еach elf can make a toy from a given number of materials.

First, you will receive a sequence of integers representing each elf's energy.
On the following line, you will be given another sequence of integers, each representing a number of materials in a box.

Your task is to calculate the total elves' energy used for making toys and the total number of successfully made toys.
You are very clever and have immediately recognized the pros and cons of the work process
    - the first elf takes the last box of materials and tries to create the toy:

•	Usually, the elf needs energy equal to the number of materials.
    If he has enough energy, he makes the toy.
        His energy decreases by the used energy, and the toy goes straight to Santa's bag.
    Then, the elf eats a cookie reward which increases his energy by 1, and goes to the end of the line,
        preparing for the upcoming boxes.

•	Every third time one of the elves takes a box,
        he tries his best to be creative, and he will need twice as much energy as usual.
        If he has enough, he manages to create 2 toys.
        Then, his energy decreases; he eats a cookie reward and goes to the end of the line, similar to the first bullet.

•	Every fifth time one of the elves takes a box,
        he is a little clumsy and somehow manages to break the toy when he just made it (if he made it).
        The toy is thrown away, and the elf doesn't get a cookie reward.
        However, his energy is already spent, and it needs to be added to the total elves' energy.
        o	If an elf creates 2 toys, but he is clumsy, he breaks them.

•	If an elf does not have enough energy, he leaves the box of materials to the next elf. Instead of making the toy,
the elf drinks a hot chocolate which doubles his energy, and goes to the end of the line, preparing for the upcoming boxes.

Note:
    North Pole's social policy is very tolerant of the elves.
    If the current elf's energy is less than 5 units,
        he does NOT TAKE a box, but he takes a day off.
            Remove the elf from the collection.

Stop crafting toys when you are out of materials or elves.


Input
•	The first line of input will represent each elf's energy - integers, separated by a single space
•	On the second line, you will be given the number of materials in each box - integers, separated by a single space
Output

•	On the first line, print the number of created toys:
    "Toys: {total_number_of_toys}"
•	On the second line, print the total used energy:
    "Energy: {total_used_energy}"
•	On the next two lines print the elves and boxes that are left, if there are any, otherwise skip the line:
    "Elves left: {elf1}, {elf2}, … {elfN}"
    "Boxes left: {box1}, {box2}, … {boxN}"

Constraints
•	All the elves' values will be integers in the range [1, 100]
•	All the boxes' values will be integers in the range [1, 100]


Input
10 16 13 25
12 11 8

Output
Toys: 3
Energy: 31
Elves left: 3, 6, 26, 14

 *** Comment ***
1) The elf with energy 10 takes the box with 8 materials.
    He creates 1 gift and uses 8 units of energy.
        He eats a cookie and goes to the end of the line, which now looks like this: 16 13 25 3.
2) The elf with energy 16 takes the box with 11 materials.
    He creates 1 gift and uses 11 units of energy.
        Then, he eats a cookie and goes to the end of the line, which now looks like this: 13 25 3 6.
3) The elf with energy 13 takes the box with 12 materials.
    It is the third time an elf takes a box.
        The elf does not have the needed energy:
        12 * 2, so he drinks a hot chocolate and goes to the end of the line: 25 3 6 26.
4) The elf with energy 25 takes the box with 12 materials.
    It is the fourth time an elf takes a box.
        He creates 1 gift and uses 12 units of energy.
            He eats a cookie and goes to the end of the line, which now looks like this: 3 6 26 14.
No boxes are left, so the program ends. Print the desired text.


Input:
10 14 22 4 5
11 16 17 11 1 8

Output:
Toys: 7
Energy: 75
Elves left: 10, 14

Input
5 6 7
2 1 5 7 5 3

Output:
Toys: 3
Energy: 20
Boxes left: 2, 1



"""

##########: variant 1 :##########

from collections import deque

energy = deque(map(int, input().split()))
materials = deque(map(int, input().split()))

toys = 0
counter = 0
energy_spent = 0

while materials and energy:
    while energy[0] < 5:
        energy.popleft()
        if len(energy) == 0:
            break
    if len(energy) == 0:
        break
    counter += 1
    if counter % 3 != 0:
        if energy[0] >= materials[-1]:
            if counter % 5 == 0:
                energy[0] -= materials[-1]
            else:
                energy[0] -= materials[-1] - 1
                toys += 1
            energy_spent += materials[-1]
            materials.pop()
            energy.append(energy.popleft())
        else:
            energy[0] *= 2
            energy.append(energy.popleft())
    elif counter % 3 == 0:
        if energy[0] >= materials[-1] * 2:
            if counter % 5 == 0:
                energy[0] -= materials[-1] * 2
            else:
                energy[0] -= materials[-1] * 2 - 1
                toys += 2
            energy_spent += materials[-1] * 2
            materials.pop()
            energy.append(energy.popleft())
        else:
            energy[0] *= 2
            energy.append(energy.popleft())


print(f"Toys: {toys}")
print(f"Energy: {energy_spent}")
if (len(energy) > 0):
    print(f"Elves left: {', '.join([str(i) for i in energy])}")
if (len(materials) > 0):
    print(f"Boxes left: {', '.join([str(i) for i in materials])}")


##########: variant 2 whit Dictionary :##########

from collections import deque

elfs_energy = deque(int(x) for x in input().split())
materials_in_box = [int(x) for x in input().split()]

info = {
    "toys": 0,
    "energy spend": 0,
    "counter": 0
}


def make_toys(energy, box, toys):
    elfs_energy.append(energy - (box - 1))
    info["toys"] += toys
    info["energy spend"] += box


def every_third_time(energy, box):
    make_toys(energy, box, 2)


def every_fifth_time(energy, box):
    elfs_energy.append(energy - box)
    info["energy spend"] += box


def not_enough_energy(energy, box):
    elfs_energy.append(energy * 2)
    materials_in_box.append(box)


def multiply_turns(energy, box, turn_time, adding_box=False):
    multiply_box = box
    if adding_box:
        multiply_box = box * 2
    if energy >= multiply_box:
        if turn_time == 5:
            every_fifth_time(energy, multiply_box)
        elif turn_time == 3:
            every_third_time(energy, multiply_box)
    else:
        not_enough_energy(energy, box)


while elfs_energy and materials_in_box:
    energy = elfs_energy.popleft()
    if energy < 5:
        continue

    info["counter"] += 1
    box = materials_in_box.pop()
    if info["counter"] % 3 == 0 and info["counter"] % 5 == 0:
        multiply_turns(energy, box, 5, True)
    elif info["counter"] % 3 == 0:
        multiply_turns(energy, box, 3, True)
    elif info["counter"] % 5 == 0:
        multiply_turns(energy, box, 5)
    elif box > energy:
        not_enough_energy(energy, box)
    else:
        make_toys(energy, box, 1)

print(f"Toys: {info['toys']}")
print(f"Energy: {info['energy spend']}")
if elfs_energy:
    print(f"Elves left: {', '.join(str(x) for x in elfs_energy)}")
if materials_in_box:
    print(f"Boxes left: {', '.join(str(x) for x in materials_in_box)}")


##########: variant 3 :##########

from collections import deque
elf_energy = deque(int(x) for x in input().split())
materials = deque(int(x) for x in input().split())
toys_counter = 0
day_counter = 0
total_energy = 0
while elf_energy and materials:
    while elf_energy[0] < 5:
        elf_energy.popleft()
        if len(elf_energy) == 0:
            break
    if len(elf_energy) == 0:
        break
    day_counter += 1
    if day_counter % 3 != 0:
        if elf_energy[0] >= materials[-1]:
            if day_counter % 5 == 0:
                elf_energy[0] -= materials[-1]
            else:
                elf_energy[0] -= materials[-1] - 1
                toys_counter += 1
            total_energy += materials[-1]
            materials.pop()
            elf_energy.append(elf_energy.popleft())
        else:
            elf_energy[0] *= 2
            elf_energy.append(elf_energy.popleft())
    elif day_counter % 3 == 0:
        if elf_energy[0] >= materials[-1] * 2:
            if day_counter % 5 == 0:
                elf_energy[0] -= materials[-1] * 2
            else:
                elf_energy[0] -= materials[-1] * 2 - 1
                toys_counter += 2
            total_energy += materials[-1] * 2
            materials.pop()
            elf_energy.append(elf_energy.popleft())
        else:
            elf_energy[0] *= 2
            elf_energy.append(elf_energy.popleft())
print(f"Toys: {toys_counter}")
print(f"Energy: {total_energy}")
if len(elf_energy) > 0:
    print(f"Elves left: {', '.join(str(x) for x in elf_energy)}")
if len(materials) > 0:
    print(f"Boxes left: {', '.join(str(x) for x in materials)}")

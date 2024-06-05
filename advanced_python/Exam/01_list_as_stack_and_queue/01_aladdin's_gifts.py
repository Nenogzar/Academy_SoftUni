# ******* Advanced Exam - 23 October 2021 ******* #

# *******  01_aladdin's_gifts  ******* #

# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/3227#0

Aladdin, rich and powerful with the help of the Genie, is now preparing to marry the princess Jasmine.
He asks Genie for help to prepare the wedding presents.

First, you will receive a sequence of integers representing the materials for every wedding present.
After that, you will be given another sequence of integers – Genie magic level for every aim to make a gift.
Your task is to mix materials with magic levels so you can make presents, listed in the table below.

Gift	                    Magic needed
Gemstone	                100 to 199
Porcelain Sculpture	      200 to 299
Gold	                    300 to 399
Diamond Jewellery	        400 to 499

To make a present, you should take the last integer of materials and sum it with the first magic level value.
If the result is between or equal to the numbers described in the table above,
    you make the corresponding gift and remove both materials and magic value.

    Otherwise:
        •	If the product of the operation is under 100:
            o	And if it is an even number,
                double the materials, and triple the magic, then sum it again.
            o	And if it is an odd number,
                double the sum of the materials and the magic level.
                    Then, check again if it is between or equal to any of the numbers in the table above.

        •	If the product of the operation is more than 499,
                divide the sum of the material and the magic level by 2.
        Then, check again if it is between or equal to any of the numbers in the table above.

        •	If, however, the result is not between or equal to any of the numbers in the table
            above after performing the calculation, remove both the materials and the magic level.

Stop crafting gifts when you are out of materials or magic level.
You have succeeded in crafting the presents when you've crafted either one of the pairs -
    a gemstone and a sculpture or gold and jewellery.

Input
•	The first line of input will represent the values of materials - integers, separated by a single space
•	On the second line, you will be given the magic levels - integers, separated by a single space

Output

•	On the first line - print whether you have succeeded in crafting the presents:
    o	"The wedding presents are made!"
    o	"Aladdin does not have enough wedding presents."
•	On the next two lines print the materials and magic that are left, if there are any, otherwise skip the line:
    o	"Materials left: {material1}, {material2}, …"
    o	"Magic left: {magicValue1}, {magicValue2}, …
•	On the next lines, print the gifts alphabetically that the Genie has crafted at least once:
"{present1}: {amount}
{present2}: {amount}
…
{presentN}: {amount}"

Constraints
•	All the materials values will be integers in the range [1, 1000]
•	Magic level values will be integers in the range [1, 1000]

Input
105 20 30 25
120 60 11 400 10 1


Output
The wedding presents are made!
Magic left: 10, 1
Gemstone: 1
Porcelain Sculpture: 2


***** Comment *****
First, we have 25 + 120 = 145, which is the needed product for a gemstone. Remove both.
30 + 60 = 90 (under 100 and even) => 30 * 2 + 60 * 3 = 240 which is the needed product for a porcelain sculpture. Remove both.
20 + 11 = 31 (under 100 and odd) => 31 * 2 = 62 which is under 100 again so we remove both.
105 + 400 = 505 (more than 450) => 505 / 2 = 252.5 which is the needed product for a diamond porcelain sculpture. Remove both.
We do not have any material left. The program ends. Print the desired text.



Input
30 5 21 6 0 91
15 9 5 15 8


Output

Aladdin does not have enough wedding presents.
Materials left: 30
Gemstone: 1


Input
200
5 15 32 20 10 5


Output
Aladdin does not have enough wedding presents.
Magic left: 15, 32, 20, 10, 5
Porcelain Sculpture: 1

"""

##########: variant 1 :##########


from collections import deque

materials = list(map(int, input().split()))
magic_levels = deque(map(int, input().split()))

presents = {
    "Gemstone": [100, 199],
    "Porcelain Sculpture": [200, 299],
    "Gold": [300, 399],
    "Diamond Jewellery": [400, 499],
}

items = {}


def sum_item(material, magic):
    return material + magic


def check_dict(result):
    for key, value in presents.items():
        start, end = value
        if result in range(start, end + 1):

            if key not in items:
                items[key] = 1
            else:
                items[key] += 1
            return True
    return False


def under_hundred(material, magic):
    if result % 2 == 0:
        return (material * 2) + (magic * 3)
    return (material + magic) * 2


while materials and magic_levels:
    material = materials.pop()
    magic = magic_levels.popleft()
    result = sum_item(material, magic)

    if not check_dict(result):
        if result < 100:
            result = under_hundred(material, magic)
            check_dict(result)
        elif result > 499:
            result //= 2
            check_dict(result)

crafted_presents = ("Gemstone" in items and "Porcelain Sculpture" in items) or (
        "Gold" in items and "Diamond Jewellery" in items)
if crafted_presents:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(map(str, materials))}")
if magic_levels:
    print(f"Magic left: {', '.join(map(str, magic_levels))}")

for key in sorted(items):
    print(f"{key}: {items[key]}")

##########: variant 2 :##########


from collections import deque

materials = list(map(int, input().split()))
magic_levels = deque(map(int, input().split()))

presents = {
    "Gemstone": [100, 199],
    "Porcelain Sculpture": [200, 299],
    "Gold": [300, 399],
    "Diamond Jewellery": [400, 499],
}
option = list(presents.keys())

items = {}


def sum_item(material, magic):
    return material + magic


def check_dict(result):
    for key, value in presents.items():
        start, end = value
        if result in range(start, end + 1):
            if key not in items:
                items[key] = 1
            else:
                items[key] += 1
            return True
    return False


while materials and magic_levels:
    material = materials.pop()
    magic = magic_levels.popleft()
    result = sum_item(material, magic)

    if not check_dict(result):
        if result < 100:
            if result % 2 == 0:
                material *= 2
                magic *= 3
                result = sum_item(material, magic)
                check_dict(result)
            else:
                result *= 2
                check_dict(result)
        elif result > 499:
            result //= 2
            check_dict(result)

crafted_presents = all(x in items for x in option[:2]) or all(x in items for x in option[2:])

if crafted_presents:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(map(str, materials))}")
if magic_levels:
    print(f"Magic left: {', '.join(map(str, magic_levels))}")

for key in sorted(items):
    print(f"{key}: {items[key]}")

##########: variant 3 CEO :##########


from collections import deque

materials = [int(x) for x in input().split()]
magic_levels = deque(int(x) for x in input().split())

gifts = {
    'Diamond Jewellery': {"quantity": 0, "min": 400, "max ": 499},
    'Gemstone': {"quantity": 0, "min": 100, "max ": 199},
    'Gold': {"quantity": 0, "min": 300, "max ": 399},
    'Porcelain Sculpture': {"quantity": 0, "min": 200, "max ": 299}
}


def under_100(material, magic_level):
    if total_sum % 2 == 0:
        return (material * 2) + (magic_level * 3)
    return (material + magic_level) * 2


while materials and magic_levels:
    material = materials.pop()
    magic_level = magic_levels.popleft()
    total_sum = material + magic_level
    if total_sum < 100:
        total_sum = under_100(material, magic_level)
    if total_sum > 499:
        total_sum /= 2
    for key, (_, min_, max_) in gifts.items():
        if gifts[key][min_] <= total_sum <= gifts[key][max_]:
            gifts[key]['quantity'] += 1
            break

if gifts['Gemstone']['quantity'] > 0 and gifts['Porcelain Sculpture']['quantity'] > 0 or \
        gifts['Gold']['quantity'] > 0 and gifts['Diamond Jewellery']['quantity'] > 0:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")

if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

for present, (quantity, _, __) in gifts.items():
    if gifts[present][quantity]:
        print(f"{present}: {gifts[present][quantity]}")

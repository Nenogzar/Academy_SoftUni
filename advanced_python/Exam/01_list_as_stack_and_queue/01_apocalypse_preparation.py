############################## 01_apocalypse_preparation ##############################
  ############################## TASK CONDITION ##############################
"""
 https://judge.softuni.org/Contests/Practice/Index/3889#0

You are in the middle of a zombie apocalypse and you want to go out for exploration.
But before you do that, you need to prepare some healing items.

On the first line
    you will be given a sequence representing textiles.
On the second line
    you will be given another sequence, which represents medicaments.

While both collections contain any elements,
    you will have to combine elements from the collections in order to create healing items.
    You should start by getting the
        first value of textile and the last value of medicaments:

•	If their sum is equal to any of the items in the table below create that item and remove both values.

•	Otherwise, check if the sum is bigger than the value of the MedKit, create the MedKit,
    remove both values,
    and add the remaining resources(of the sum) to the next value in the medicament collection
    (Take the element from the collection, add the remaining sum to it, and put the element back to its place).
•	If you can’t create anything,
    remove the textile value,
    add 10 to the medicament value,
    and return the medicament back to its place, into its collection.

You need to stop creating healing items when either the textile or the medicaments are exhausted.

Healing item	    Resources needed
Patch	                    30
Bandage	                    40
MedKit	                    100



In the end, you should print on the console message for the sequence that has ended,
    then the created items, and in the end the remaining items (if any).

Input
•	On the first line, you will receive a sequence of integers representing the textiles,
    separated by a single space (" ").
•	On the second line, you will receive a sequence of integers representing the medicaments,
    separated by a single space (" ").

Output

•	On the first line print which one of the collections is over:
        o	If the textile is over print:
            "Textiles are empty."
        o	If the medicaments are over print:
            "Medicaments are empty."
        o	If both are empty print:
            "Textiles and medicaments are both empty."

•	On the next n lines print only the created items (if any) ordered by the amount created descending,
    then by name alphabetically:

            "{item name} - {amount created}
            {item name} - {amount created}
            …
            "

Hint: Do not print items, which are not created.

•	On the last line print the remaining items(if any):
    o	If there are any medicaments left:
        "Medicaments left: …{medicament2}, {medicament1}"
    o	If there are any textiles left:
        "Textiles left: {textile1}, {textile2}…"



Input:
20 10 40 70 20
10 50 10 30 20 80


Output:
Textiles are empty.
MedKit - 2
Bandage - 1
Patch - 1
Medicaments left: 50, 10


Input:
30 30 10 80 60
40 20 30 10 70


Output:
Textiles and medicaments are both empty.
MedKit - 3
Bandage - 2

Input:
30 30 10 80 60 20
40 20 30 10 70


Output:
Medicaments are empty.
MedKit - 3
Bandage - 2
Textiles left: 20


Input:
60 15 20 30 20
20 15 40


Output:

Medicaments are empty.
Bandage - 1
MedKit - 1
Patch - 1
Textiles left: 30, 20

"""
##########: variant 1 :##########

from collections import deque

textiles = deque(map(int, input().split()))
medicaments = deque(map(int, input().split()))

healing_items = {
    'Patch': 30,
    'Bandage': 40,
    'MedKit': 100,
}

make_items = {
    'Patch': 0,
    'Bandage': 0,
    'MedKit': 0,
}

while textiles and medicaments:
    textile = textiles.popleft()
    medicament = medicaments.pop()
    sum_medicaments = textile + medicament

    item_created = False
    for item, resource in healing_items.items():
        if sum_medicaments == resource:
            make_items[item] += 1
            item_created = True
            break

    if not item_created:
        if sum_medicaments > healing_items['MedKit']:
            make_items['MedKit'] += 1
            remaining = sum_medicaments - healing_items['MedKit']
            if medicaments:
                medicaments[-1] += remaining
            item_created = True
        else:
            medicaments.append(medicament + 10)


if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
else:
    print("Medicaments are empty.")


for item, amount in sorted(make_items.items(), key=lambda x: (-x[1], x[0])):
    if amount > 0:
        print(f"{item} - {amount}")

if medicaments:
    print(f"Medicaments left: {', '.join(map(str, reversed(medicaments)))}")
if textiles:
    print(f"Textiles left: {', '.join(map(str, textiles))}")


##########: variant 2 whit functions :##########


from collections import deque

healing_items = {
    'Patch': 30,
    'Bandage': 40,
    'MedKit': 100,
}


def read_input():
    textiles = deque(map(int, input().split()))
    medicaments = deque(map(int, input().split()))
    return textiles, medicaments


def create_healing_items(textiles, medicaments):
    make_items = {item: 0 for item in healing_items}

    while textiles and medicaments:
        textile = textiles.popleft()
        medicament = medicaments.pop()
        sum_medicaments = textile + medicament

        item_created = False
        for item, resource in healing_items.items():
            if sum_medicaments == resource:
                make_items[item] += 1
                item_created = True
                break

        if not item_created:
            if sum_medicaments > healing_items['MedKit']:
                make_items['MedKit'] += 1
                remaining = sum_medicaments - healing_items['MedKit']
                if medicaments:
                    medicaments[-1] += remaining
                item_created = True
            else:
                medicaments.append(medicament + 10)

    return make_items, textiles, medicaments


def print_output(make_items, textiles, medicaments):
    if not textiles and not medicaments:
        print("Textiles and medicaments are both empty.")
    elif not textiles:
        print("Textiles are empty.")
    else:
        print("Medicaments are empty.")

    for item, amount in sorted(make_items.items(), key=lambda x: (-x[1], x[0])):
        if amount > 0:
            print(f"{item} - {amount}")

    if medicaments:
        print(f"Medicaments left: {', '.join(map(str, reversed(medicaments)))}")
    if textiles:
        print(f"Textiles left: {', '.join(map(str, textiles))}")


def main():
    textiles, medicaments = read_input()
    make_items, textiles, medicaments = create_healing_items(textiles, medicaments)
    print_output(make_items, textiles, medicaments)


if __name__ == "__main__":
    main()

##########: variant 3 solution SoftUni :##########

from collections import deque

textiles = deque(map(int, input().split()))
medicaments = list(map(int, input().split()))

items = {"Patch": 0, "Bandage": 0, "MedKit": 0}

while True:
    if not textiles and not medicaments:
        print("Textiles and medicaments are both empty.")
        break
    if not textiles:
        print("Textiles are empty.")
        break
    if not medicaments:
        print("Medicaments are empty.")
        break
    first_textile = textiles.popleft()
    last_medicament = medicaments.pop()
    summed_items = first_textile + last_medicament
    if summed_items == 30:
        items["Patch"] += 1
    elif summed_items == 40:
        items["Bandage"] += 1
    elif summed_items == 100:
        items["MedKit"] += 1
    elif summed_items > 100:
        items["MedKit"] += 1
        summed_items -= 100
        medicaments[-1] += summed_items
    else:
        last_medicament += 10
        medicaments.append(last_medicament)

sorted_items = sorted(items.items(), key=lambda x: (-x[1], x[0]))
for item in sorted_items:
    if int(item[1]) > 0:
        print(f"{item[0]} - {item[1]}")

if medicaments:
    medicaments.reverse()
    print(f"Medicaments left: {', '.join(map(str, medicaments))}")
if textiles:
    print(f"Textiles left: {', '.join(map(str, textiles))}")

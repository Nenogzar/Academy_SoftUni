<details><summary> Mid-Exam-Preparation-1 </summary> 

####

> 1.	Computer Store

[Link to Judge](https://judge.softuni.org/Contests/Practice/Index/2517#0)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40358)

<details> <summary> Example & Code</summary>
<details> <summary>Example</summary>



| Input                                                                                                                                                                | Output                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| 1050</br>200</br>450</br>2</br>18.50</br>16.86</br>special                                                                                                           | Congratulations you've just bought a new computer!</br>Price without taxes: 1737.36$</br>Taxes: 347.47$</br>-----------</br>Total price: 1876.35$ |
| 1023 </br>15</br>-20</br>-5.50</br>450</br>20 </br>17.66 </br>19.30</br>regular                                                                                      | Invalid price!</br>Invalid price!</br>Congratulations you've just bought a new computer!</br>Price without taxes: 1544.96$</br>Taxes: 308.99$</br>-----------</br>Total price: 1853.95$ |
| regular                                                                                                                                                              | Invalid order!                                                                                                                                    |

</details>

<details> <summary>Code</summary>

```Python
total_sum = 0
data = input()
customers = list()
discount = 0.1

while data != "special" and data != "regular":
    price = float(data)
    if price < 0:
        print("Invalid price!")
        data = input()
        continue
    else:
        customers.append(data)
        data = input()

if not customers:
    print("Invalid order!")
else:
    total_sum = sum(float(n) for n in customers)
    taxes = total_sum * 0.2
    total_price = total_sum + taxes

    if data == "special":
        total_price = total_price - (total_price * discount)

    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_sum:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")
```
```Python
input_command = input()

no_tax_price = 0
special = False
while True:
    if input_command.isalpha():
        if input_command == 'special':
            special = True
            break
        elif input_command == 'regular':
            break
    else:
        price = float(input_command)
        if price >= 0:
            no_tax_price += float(input_command)
        else:
            print("Invalid price!")
    input_command=input()

if no_tax_price == 0:
    print("Invalid order!")
else:
    total_price = no_tax_price * 1.2
    taxes = total_price - no_tax_price
    if special:
        total_price *= 0.9
    print("Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {no_tax_price:.2f}$')
    print(f'Taxes: {taxes:.2f}$')
    print(f"-----------\nTotal price: {total_price:.2f}$")
```

</details>
</details>


>  2.	Shoot for the Win



[Link to Judge](https://judge.softuni.org/Contests/Practice/Index/2305#1)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40371)
<details> <summary> Example & Code</summary>
<details><summary>Example</summary>

| Input | Output |
|-------|--------|
|       |        |
|       |        |
|       |        |

</details>

<details> <summary>Code</summary>

```Python
targets = [int(x) for x in input().split()]
shoot = input()
targets_len = len(targets)


while shoot != "End":
    shoot = int(shoot)

    if 0 <= shoot < targets_len:
        target = targets[shoot]
        targets[shoot] = -1
        for i in range(targets_len):

            if targets[i] == -1:
                continue

            if targets[i] > target:
                targets[i] -= target
            else:
                targets[i] += target

    shoot = input()

print(f"Shot targets: {sum(1 for x in targets if x == -1)} ->", *targets)
```
```Python
main_target = [int(n) for n in input().split()]

made_shots = 0
command = input()
targets_number = len(main_target) - 1

while command != "End":
    command = int(command)
    if targets_number >= command >= 0 and main_target[command] != -1:
        made_shots += 1
        target_value = main_target[command]
        for index, value in enumerate(main_target):
            if value != -1:
                if value <= target_value:
                    result_between_targets = value + target_value
                    main_target[index] = result_between_targets
                else:
                    result_between_targets = value - target_value
                    main_target[index] = result_between_targets
        main_target[command] = -1

    command = input()

print(f"Shot targets: {made_shots} ->", *main_target, sep=" ")
```
</details>
</details>


> 3.	Heart Delivery


[Link to Judge](https://judge.softuni.org/Contests/Practice/Index/2031#2)</br>
[Problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40378)
<details> <summary> Example & Code</summary>
<details><summary>Example</summary>


| Input | Output |
|-------|--------|
|       |        |
|       |        |
|       |        |

</details>

<details> <summary>Code</summary>

```Python
neighborhood = [int(x) for x in input().split("@")]
jump_data = input()
neighborhood_len = len(neighborhood)
length = 0

while jump_data != "Love!":
    length += int(jump_data.split()[-1])
    if length >= neighborhood_len:
        length = 0

    if neighborhood[length] > 2:
        neighborhood[length] -= 2
    else:
        if neighborhood[length] != 0:
            neighborhood[length] -= 2
            text = "has"
        else:
            text = "already had"
        print(f"Place {length} {text} Valentine's day.")
    jump_data = input()

print(f"Cupid's last position was {length}.")

failed_houses = sum(1 for x in neighborhood if x != 0)

if failed_houses:
    print(f"Cupid has failed {failed_houses} places.")
else:
    print("Mission was successful.")
```
```Python
def jump_neighborhood(length_d):
    global jump_position
    jump_position += length_d
    if jump_position >= len(neighborhood):
        jump_position = 0
    if neighborhood[jump_position] == 0:
        print(f"Place {jump_position} already had Valentine's day.")
    else:
        neighborhood[jump_position] -= 2
        if neighborhood[jump_position] == 0:
            print(f"Place {jump_position} has Valentine's day.")


while jump_command != "Love!":
    jump_command = jump_command.split()
    jump_neighborhood(int(jump_command[1]))

    jump_command = input()

print(f"Cupid's last position was {jump_position}.")

if sum(neighborhood) == 0:
    print("Mission was successful.")
else:
    fail_count = neighborhood.count(0)
    print(f"Cupid has failed {len(neighborhood) - fail_count} places.")
```

</details>
</details>
</details>




######
<details><summary> Mid-Exam-Preparation-2 </summary>

> 1.	Counter-Strike

[judge](https://judge.softuni.org/Contests/Practice/Index/2305#0)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40370)</br>
[pastebin Ivan Shopov](https://pastebin.com/vrxNF4bB)
<details> <summary> Example & Code</summary>
^
<details><summary>Example</summary>

| Input                                                    | Output                                                       |
|----------------------------------------------------------|--------------------------------------------------------------|
| 100</br>10</br>10</br>10</br>1</br>2</br>3</br>73</br>10 | Not enough energy! Game ends with 7 won battles and 0 energy |
| 200</br>54</br>14</br>28</br>13</br>End of battle        | Won battles: 4. Energy left: 94                              |


</details>
<details> <summary>Code</summary>

```Python
energy = int(input())
distance_to_enemy = input()
win_counter = 0

while distance_to_enemy != "End of battle":

    distance_to_enemy = int(distance_to_enemy)

    if distance_to_enemy <= energy:
        energy -= distance_to_enemy
        win_counter += 1
    else:
        print(f"Not enough energy! Game ends with {win_counter} won battles and {energy} energy")
        break

    if win_counter % 3 == 0:
        energy += win_counter

    distance_to_enemy = input()

if distance_to_enemy == "End of battle":
    print(f"Won battles: {win_counter}. Energy left: {energy}")
```

```Python
def check_win_counter(energy, distance_to_enemy, win_counter):
    if distance_to_enemy <= energy:
        energy -= distance_to_enemy
        win_counter += 1
    else:
        print(f"Not enough energy! Game ends with {win_counter} won battles and {energy} energy")
        return False  # We return False to indicate that the game is over

    if win_counter % 3 == 0:
        energy += win_counter

    return win_counter, energy


energy = int(input())
distance_to_enemy = input()
win_counter = 0

while distance_to_enemy != "End of battle":
    distance_to_enemy = int(distance_to_enemy)

    result = check_win_counter(energy, distance_to_enemy, win_counter)
    if not result:
        break  # exit the loop if the game ends

    win_counter, energy = result

    distance_to_enemy = input()

if distance_to_enemy == "End of battle":
    print(f"Won battles: {win_counter}. Energy left: {energy}")
```
```Python
def check_win_counter(energy, distance_to_enemy, win_counter):
    if distance_to_enemy <= energy:
        energy -= distance_to_enemy
        win_counter += 1
    else:
        print(f"Not enough energy! Game ends with {win_counter} won battles and {energy} energy")
        exit()  #  exit from program. enegy == 0

    if win_counter % 3 == 0:
        energy += win_counter

    return win_counter, energy

energy = int(input())
distance_to_enemy = input()
win_counter = 0

while distance_to_enemy != "End of battle":
    distance_to_enemy = int(distance_to_enemy)

    win_counter, energy = check_win_counter(energy, distance_to_enemy, win_counter)

    distance_to_enemy = input()

print(f"Won battles: {win_counter}. Energy left: {energy}")
```

</details>
</details>

> 2.	Array Modifier

[judge](https://judge.softuni.org/Contests/Practice/Index/2474#1)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40365)
<details> <summary> Example & Code</summary>
<details><summary>Example</summary>

| Input                                                                                                                 | Output                              |
|-----------------------------------------------------------------------------------------------------------------------|-------------------------------------|
| 23 -2 321 87 42 90 -123</br>swap 1 3</br>swap 3 6</br>swap 1 0</br>multiply 1 2</br>multiply 2 1</br>decrease</br>end | 86, 7382, 2369942, -124, 41, 89, -3 |
| 1 2 3 4</br>swap 0 1</br>swap 1 2</br>swap 2 3</br>multiply 1 2</br>decrease</br>end                                  | 1, 11, 3, 0                         |

</details>
<details> <summary>Code</summary>

```Python
def swap_element(list_mod, index1, index2):
    list_copy = list(list_mod)
    temp = list_copy[index1]
    list_copy[index1] = list_copy[index2]
    list_copy[index2] = temp
    return list_copy


def multiply_element(list_mod, index1, index2):
    list_copy = list(list_mod)
    list_copy[index1] = list_copy[index1] * list_copy[index2]
    return list_copy


list_to_modifier = list(map(int, input().split()))
command = input()

while command != "end":

    comman_list = list(map(str, command.split(" ")))
    if len(comman_list) > 1:
        firs, second = int(comman_list[1]), int(comman_list[2])

    if comman_list[0] == "swap":
        list_to_modifier = swap_element(list_to_modifier, firs, second)
    elif comman_list[0] == "multiply":
        list_to_modifier = multiply_element(list_to_modifier, firs, second)
    elif comman_list[0] == "decrease":
        list_to_modifier = [x - 1 for x in list_to_modifier]

    command = input()

result_string = ', '.join(map(str, list_to_modifier))
print(result_string)
```
```Python
elements = [int(x) for x in input().split()]
data_info = input()
while data_info != "end":
    if "decrease" in data_info:
        elements = [x - 1 for x in elements]
        data_info = input()
        continue

    command, index_one, index_two = [x if x.isalpha() else int(x) for x in data_info.split()]

    if command == "swap":
        elements[index_one], elements[index_two] = elements[index_two], elements[index_one]

    elif command == "multiply":
        elements[index_one] *= elements[index_two]

    data_info = input()

print(*elements, sep=", ")
```
```Python
initial_array = list(map(int, input().split(' ')))

while True:
    command = input()
    if command == 'end':
        break
    order = command.split()
    if len(order) > 1:
        index_01 = int(order[1])
        index_02 = int(order[2])
    if 'swap' in order:
        initial_array[index_01], initial_array[index_02] = initial_array[index_02], initial_array[index_01]
    elif 'multiply' in order:
        initial_array[index_01] = initial_array[index_01] * initial_array[index_02]
    elif 'decrease' in order:
        initial_array = [i - 1 for i in initial_array]
print(*initial_array, sep=', ')
```

</details>
</details>

> 3.	Inventory

[judge](https://judge.softuni.org/Contests/Practice/Index/2028#2)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40384)   
<details> <summary> Example & Code</summary>
<details><summary>Example</summary>


| Input | Output |
|-------|--------|
|Iron, Wood, Sword</br>Collect - Gold</br>Drop - Wood</br>Craft!|Iron, Sword, Gold |
|Iron, Sword</br>Drop - Bronze</br>Combine Items - Sword:Bow</br>Renew - Iron</br>Craft!|Sword, Bow, Iron|


</details>
<details> <summary>Code</summary>

```Python
collected_items = input().split(', ')

input_data = input()

while input_data != 'Craft!':
    command, item = input_data.split(' - ')

    item_in_collection = item.split(':')[0] in collected_items

    if command == 'Collect' and not item_in_collection:
        collected_items.append(item)

    elif command == 'Drop' and item_in_collection:
        collected_items.remove(item)

    elif command == 'Combine Items' and item_in_collection:
        old_item, new_item = item.split(':')
        collected_items.insert(collected_items.index(old_item) + 1, new_item)

    elif command == 'Renew' and item_in_collection:
        collected_items.append(collected_items.pop(collected_items.index(item)))

    input_data = input()

print(*collected_items, sep=', ')
```
```Python
def collect_item(inventory, item):
    if item not in inventory:
        inventory.append(item)
    return inventory


def drop_item(inventory, item):
    if item in inventory:
        inventory.remove(item)
    return inventory


def combine_items(inventory, old_item, new_item):
    if old_item in inventory:
        index = inventory.index(old_item)
        inventory.insert(index + 1, new_item)
    return inventory


def renew_item(inventory, item):
    if item in inventory:
        inventory.remove(item)
        inventory.append(item)
    return inventory

journal = input().split(", ")
command = input()

while command != "Craft!":
    comman_list = list(map(str, command.split(" - ")))
    action = comman_list[0]
    args = comman_list[1:]
    item = args[0]

    if action == "Collect":
        journal = collect_item(journal, item)
    elif action == "Drop":
        journal = drop_item(journal, item)
    elif action == "Combine Items":
        old_item, new_item = args[0].split(":")
        journal = combine_items(journal, old_item, new_item)
    elif action == "Renew":
        journal = renew_item(journal, item)

    command = input()

print(", ".join(journal))
```
```Python
def collect(item):
    if item not in items:
        items.append(item)


def drop(item):
    if item in items:
        items.remove(item)


def combine_items(old_item, new_item):
    if old_item in items:
        index = items.index(old_item) + 1
        items.insert(index, new_item)


def renew(item):
    if item in items:
        items.remove(item)
        items.append(item)


items = input().split(", ")
command = input()
while command != "Craft!":
    command = command.split(" - ")
    event = command[0]
    if event == "Collect":
        collect(command[1])
    elif event == "Drop":
        drop(command[1])
    elif event == "Combine Items":
        command = command[1].split(":")
        old_item = command[0]
        new_item = command[1]
        combine_items(old_item, new_item)
    elif event == "Renew":
        renew(command[1])
    command = input()

print(*items, sep=", ")
```

</details>

</details>
</details>

######

<details><summary> Mid-Exam-Preparation-more and more </summary>

> 01. Guinea Pig

[judge](https://judge.softuni.org/Contests/Practice/Index/2031#0)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40376)

<details> <summary> Example & Code</summary>
<details><summary>Example</summary>


| Input          | Output |
|----------------|--------|
| 15</br>0 0 0 0 |The lift has empty spots!</br>4 4 4 3|
| 20</br>  0 2 0 |There isn't enough space! 10 people in a queue!</br>4 4 4|

</details>
<details> <summary>Code</summary>

Merry has a guinea pig named Puppy, that she loves very much.
Every month she goes to the nearest pet store and buys him everything he needs – food, hay, and cover.
On the first three lines, you will receive the quantity of food, hay, and cover, 
which Merry buys for a month (30 days). On the fourth line, you will receive the guinea pig's weight.
Every day Puppy eats 300 gr of food. Every second day Merry first feeds the pet, 
then gives it a certain amount of hay equal to 5% of the rest of the food. On every third day, 
Merry puts Puppy cover with a quantity of 1/3 of its weight.
Calculate whether the quantity of food, hay, and cover, will be enough for a month.
If Merry runs out of food, hay, or cover, stop the program!

Input

* •	On the first line – quantity food in kilograms - a floating-point number in the range [0.0 – 10000.0]
* •	On the second line – quantity hay in kilograms - a floating-point number in the range [0.0 – 10000.0]
* •	On the third line – quantity cover in kilograms - a floating-point number in the range [0.0 – 10000.0]
* •	On the fourth line – guinea's weight in kilograms - a floating-point number in the range [0.0 – 10000.0]

Output

* •	If the food, the hay, and the cover are enough, print:
* o	"Everything is fine! Puppy is happy! Food: {excessFood}, Hay: {excessHay}, Cover: {excessCover}."
* •	If one of the things is not enough, print:
* o	"Merry must go to the pet store!"
* The output values must be formatted to the second decimal place!

```Python

```
```Python
food, hay, cover_i, guinea_weight = float(input()), float(input()), float(input()), float(input())
food_kg = food * 1000
hay_kg = hay * 1000
cover_kg = cover_i * 1000
guinea_weight_kg = guinea_weight * 1000

cover = guinea_weight_kg / 3
feed_eaten = 0

for day in range(1, 31):
    feed_eaten += 300
    food_kg -= 300
    if day % 2 == 0:
        hay = food_kg * 0.05
        hay_kg -= hay
        feed_eaten += hay

    if day % 3 == 0:
        cover_kg -= cover

if food_kg > 0 and hay_kg > 0 and cover_kg > 0:
    print(f"Everything is fine! Puppy is happy! Food: {food_kg / 1000:.2f}, Hay: {hay_kg / 1000:.2f}, Cover: {cover_kg / 1000:.2f}.")

else:
    print("Merry must go to the pet store!")
```

</details>
</details>

>  01. SoftUni Reception

[judge](https://judge.softuni.org/Contests/Practice/Index/2474#0)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40364)

<details> <summary> Example & Code</summary>
<details><summary>Example</summary>


| Input | Output |
|-------|--------|
|       |        |
|       |        |
|       |        |

</details>
<details> <summary>Code</summary>

```Python
first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
students_number = int(input())
students_per_hour = first_employee + second_employee + third_employee

hours = 0
while students_number > 0:
    hours += 1
    if hours % 4 == 0:
        continue
    else:
        students_number-=students_per_hour
print(f"Time needed: {hours}h.")
```
</details>
</details>

> 01. Bonus Scoring System

[judge](https://judge.softuni.org/Contests/Practice/Index/2028#0)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40382)

<details> <summary> Example & Code</summary>
<details><summary>Example</summary>


| Input | Output |
|-------|--------|
|       |        |
|       |        |
|       |        |

</details>
<details> <summary>Code</summary>

```Python

```

</details>
</details>

> 02. The Lift

[judge](https://judge.softuni.org/Contests/Practice/Index/2517#1)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40359)

<details> <summary> Example & Code</summary>
<details><summary>Example</summary>

| Input           | Output                                                     |
|-----------------|------------------------------------------------------------|
| 15</br> 0 0 0 0 | The lift has empty spots!</br> 4 4 4 3                     |
| 20 </br> 0 2 0  | There isn't enough space! 10 people in a queue!</br> 4 4 4 |

</details>
<details> <summary>Code</summary>

```Python
people = int(input())
lift = list(map(int, input().split()))

for wagon, spaces in enumerate(lift):
    if spaces < 4:
        available = 4 - spaces
        if people - available >= 0:
            people -= available
            lift[wagon] += available
        else:
            lift[wagon] += people
            people -= people

not_balance = True

for count in range(len(lift)):
    if lift[count] < 4:
        not_balance = False

if not_balance and people == 0:
    print(*lift)
elif people == 0:
    print('The lift has empty spots!')
    print(*lift)
else:
    print(f"There isn't enough space! {people} people in a queue!")
    print(*lift)
```

</details>
</details>

> 02. Shopping List

[judge](https://judge.softuni.org/Contests/Practice/Index/2031#1)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40377)

<details> <summary> Example & Code</summary>
<details><summary>Example</summary>


| Input | Output |
|-------|--------|
|       |        |
|       |        |
|       |        |

</details>
<details> <summary>Code</summary>

```Python

```

</details>
</details>

> 02. MuOnline

[judge](https://judge.softuni.org/Contests/Practice/Index/2028#1)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40383)

<details> <summary> Example & Code</summary>
<details><summary>Example</summary>

Merry has a guinea pig named Puppy, that she loves very much.
Every month she goes to the nearest pet store and buys him everything he needs – food, hay, and cover.
On the first three lines, you will receive the quantity of food, hay, and cover, 
which Merry buys for a month (30 days). On the fourth line, you will receive the guinea pig's weight.
Every day Puppy eats 300 gr of food. Every second day Merry first feeds the pet, 
then gives it a certain amount of hay equal to 5% of the rest of the food. On every third day, 
Merry puts Puppy cover with a quantity of 1/3 of its weight.
Calculate whether the quantity of food, hay, and cover, will be enough for a month.
If Merry runs out of food, hay, or cover, stop the program!

Input

* On the first line – quantity food in kilograms - a floating-point number in the range [0.0 – 10000.0]
* On the second line – quantity hay in kilograms - a floating-point number in the range [0.0 – 10000.0]
* On the third line – quantity cover in kilograms - a floating-point number in the range [0.0 – 10000.0]
* On the fourth line – guinea's weight in kilograms - a floating-point number in the range [0.0 – 10000.0]

Output

* If the food, the hay, and the cover are enough, print:
  * "Everything is fine! Puppy is happy! Food: {excessFood}, Hay: {excessHay}, Cover: {excessCover}."
* If one of the things is not enough, print:
  * "Merry must go to the pet store!"

The output values must be formatted to the second decimal place!

| Input                  | Output |
|------------------------|--------|
| 10</br>5</br>5.2</br>1 |Everything is fine! Puppy is happy! Food: 1.00, Hay: 1.10, Cover: 1.87|
| 1 1.5 3 1.5            |Merry must go to the pet store!|
| 9 5 5.2 1              |Merry must go to the pet store!|

</details>
<details> <summary>Code</summary>

```Python
food_in_grams = float(input()) * 1000
hay_in_grams = float(input()) * 1000
cover_in_grams = float(input()) * 1000
weight_in_grams = float(input()) * 1000
dayly_food = 300

enough = True

for day in range(1, 30 + 1):
    if food_in_grams - dayly_food > 0:
        food_in_grams -= dayly_food
    else:
        enough = False
        break
    if day % 2 == 0:
        hay_dose = food_in_grams * 0.05
        if hay_in_grams - hay_dose > 0:
            hay_in_grams -= hay_dose
        else:
            enough = False
            break
    if day % 3 == 0:
        cover_dose = weight_in_grams / 3
        if cover_in_grams - cover_dose > 0:
            cover_in_grams -= cover_dose
        else:
            enough = False
            break

if enough:
    food_in_KG = food_in_grams / 1000
    hay_in_KG = hay_in_grams / 1000
    cover_in_KG = cover_in_grams / 1000
    print(f"Everything is fine! Puppy is happy! Food: {food_in_KG:.2f}, Hay: {hay_in_KG:.2f}, Cover: {cover_in_KG:.2f}.")
else:
    print("Merry must go to the pet store!")
```

</details>
</details>

> 03. Moving Target

[judge](https://judge.softuni.org/Contests/Practice/Index/2305#2)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40372)
<details> <summary> Example & Code</summary>
<details><summary>Example</summary>

You are at the shooting gallery again, and you need a program that helps you keep track of moving targets.
On the first line, you will receive a sequence of targets with their integer values, split by a single space. 
Then, you will start receiving commands for manipulating the targets until the "End" command. 
The commands are the following:
* "Shoot {index} {power}"
  * Shoot the target at the index if it exists by reducing its value by the given power (integer value). 
  * Remove the target if it is shot. A target is considered shot when its value reaches 0.
* "Add {index} {value}"
*	Insert a target with the received value at the received index if it exists. 
*	If not, print: "Invalid placement!"
  *	"Strike {index} {radius}"
*	Remove the target at the given index and the ones before and after it depending on the radius.
*	If any of the indices in the range is invalid, print: "Strike missed!" and skip this command.

   Example:  "Strike 2 2"
      {radius}	{radius}	{strikeIndex}	{radius}	{radius}		

* "End"
  * Print the sequence with targets in the following format and end the program:

  "{target1}|{target2}…|{targetn}"

  Input / Constraints

* On the first line, you will receive the sequence of targets – integer values [1-10000].
* On the following lines, until the "End" will be receiving the command described above – strings.
* There will never be a case when the "Strike" command would empty the whole sequence.
  Output
* Print the appropriate message in case of any command if necessary.
* In the end, print the sequence of targets in the format described above.

| Input                                                                                | Output                        |
|--------------------------------------------------------------------------------------|-------------------------------|
| 52 74 23 44 96 110</br>Shoot 5 10</br>Shoot 1 80</br>Strike 2 1</br>Add 22 3</br>End | Invalid placement!</br>52/100 |
| 1 2 3 4 5</br>Strike 0 1</br>End                                                     | Strike missed!</br>1/2/3/4/5  |


</details>
<details> <summary>Code</summary>

```Python
targets = list(map(int, input().split()))

while True:
    command = input()
    if command == 'End':
        break
    order = command.split()
    action = order[0]
    index = int(order[1])
    number = int(order[2])
    if action == 'Shoot' and 0 <= index < len(targets):
        power = number
        if targets[index] - power > 0:
            targets[index] -= power
        else:
            del targets[index]
    elif action == 'Add':
        value = number
        if index < 0 or index >= len(targets):
            print("Invalid placement!")
        else:
            targets.insert(index,value)
    elif action == 'Strike':
        radius = number
        if index - radius < 0 or index + radius >= len(targets):
            print("Strike missed!")
        else:
            del targets[index - radius:index + radius + 1:]

print(*targets, sep='|')
```

</details>
</details>

> 03. Memory Game

[judge](https://judge.softuni.org/Contests/Practice/Index/2517#2)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40360)
<details> <summary> Example & Code</summary>
<details><summary>Example</summary>

| Input                                                                    | Output                                                                                                                                                                                                                                                                                                     |
|--------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 1 2 2 3 3 4 4 5 5 </br>1 0</br>-1 0</br>1 0 </br>1 0 </br>1 0 </br>end | Congrats! You have found matching elements - 1!</br>Invalid input! Adding additional elements to the board</br>Congrats! You have found matching elements - 2!</br>Congrats! You have found matching elements - 3!</br>Congrats! You have found matching elements - -2a!</br>Sorry you lose :(</br>4 4 5 5 |
| a 2 4 a 2 4 </br>0 3 </br>0 2</br>0 1</br>0 1 </br>end                   | Congrats! You have found matching elements - a!</br>Congrats! You have found matching elements - 2!</br>Congrats! You have found matching elements - 4!</br>You have won in 3 turns!                                                                                                                       |
| a 2 4 a 2 4 </br>4 0 </br>0 2</br>0 1</br>0 1 </br>end                   | Try again!</br>Try again!</br>Try again!</br>Try again!</br>Sorry you lose :(</br>a 2 4 a 2 4                                                                                                                                                                                                              |

</details>

<details> <summary>Code</summary>

```Python
elements = input().split()

moves = 0

while True:
    input_command = input()
    if len(elements) < 1:
        print(f"You have won in {moves} turns!")
        break
    if input_command == 'end':
        print("Sorry you lose :(")
        print(*elements)
        break

    indeces = input_command.split(' ')
    moves += 1
    index_01 = int(indeces[0])
    index_02 = int(indeces[1])
    middle = int(len(elements) / 2)
    if index_02 == index_01 or index_01 < 0 or index_01 >= len(elements) or index_02 < 0 or index_02 >= len(elements):
        elements.insert(middle, f'-{moves}a')
        elements.insert(middle, f'-{moves}a')
        print("Invalid input! Adding additional elements to the board")
    elif elements[index_01] == elements[index_02]:
        element = elements[index_01]
        print(f"Congrats! You have found matching elements - {element}!")
        elements.remove(element)
        elements.remove(element)
    else:
        print('Try again!')
```

</details>
</details>

> 03. Numbers

[judge](https://judge.softuni.org/Contests/Practice/Index/2474#2)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40366)
<details> <summary> Example & Code</summary>
<details><summary>Example</summary>

| Input                               | Output         |
|-------------------------------------|----------------|
| 10 20 30 40 50                      | 50 40          |
| 5 2 3 4 -10 30 40 50 20 50 60 60 51 | 60 60 51 50 50 |
| 1                                   | No             |
| -1 -2 -3 -4 -5 -6                   | -1 -2 -3       |

</details>

<details> <summary>Code</summary>

```Python
initital_list = list(map(int, input().split()))

averrage_list = [number for number in initital_list if number > sum(initital_list) / len(initital_list)]

if len(averrage_list) < 1:
    print('No')
else:
    for index, value in enumerate(sorted(averrage_list,reverse=True)):
        if index == 5:
            break
        print(value,end=' ')
```

</details>
</details>
</details>
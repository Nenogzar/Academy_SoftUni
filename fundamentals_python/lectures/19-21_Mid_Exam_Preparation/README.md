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

Valentine's day is coming, and Cupid has minimal time to spread some love across the neighborhood. Help him with his mission!
You will receive a string with even integers, separated by a "@" - this is our neighborhood.
After that, a series of Jump commands will follow until you receive "Love!".
Every house in the neighborhood needs a certain number of hearts delivered by Cupid so it can celebrate Valentine's day.
The integers in the neighborhood indicate those needed hearts.
Cupid starts at the position of the first house (index 0) and must jump by a given length.
The jump commands will be in this format: "Jump {length}". 
Every time he jumps from one house to another, the needed hearts for the visited house are decreased by 2: 
* •	If the needed hearts for a certain house become equal to 0, print on the console "Place {house_index} has Valentine's day." 
* •	If Cupid jumps to a house where the needed hearts are already 0, print on the console "Place {house_index} already had Valentine's day."
* •	Keep in mind that Cupid can have a larger jump length than the size of the neighborhood, 
and if he does jump outside of it, he should start from the first house again (index 0)
For example, we are given this neighborhood: 6@6@6. Cupid is at the start and jumps with a length of 2.
He will end up at index 2 and decrease the needed hearts by 2: [6, 6, 4]. Next,
he jumps again with a length of 2 and goes outside the neighborhood, so he goes back to the first house (index 0)
and again decreases the needed hearts there: [4, 6, 4].
Input
* •	On the first line, you will receive a string with even integers separated by "@" – the neighborhood and the number of hearts for each house.
* •	On the next lines, until "Love!" is received, you will be getting jump commands in this format: "Jump {length}".
Output
In the end, print Cupid's last position and whether his mission was successful or not:
* •	"Cupid's last position was {last_position_index}."
* •	If each house has had Valentine's day, print: 
  * o	"Mission was successful."
* •	If not, print the count of all houses that didn't celebrate Valentine's Day:
  * o	"Cupid has failed {houseCount} places."
  Constraints
* •	The neighborhood's size will be in the range [1…20]
* •	Each house will need an even number of hearts in the range [2 … 10]
* •	Each jump length will be an integer in the range [1 … 20]

| Input                                                                  | Output                                                                                                                                                                                                          |
|------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 10@10@10@2</br>Jump 1</br>Jump 2</br>Love!                             | Place 3 has Valentine's day.</br>Cupid's last position was 3.</br>Cupid has failed 3 places.                                                                                                                    |
| 2@4@2</br>Jump 2</br>Jump 2</br>Jump 8</br>Jump 3</br>Jump 1</br>Love! | Place 2 has Valentine's day.</br>Place 0 has Valentine's day.</br>Place 0 already had Valentine's day.</br>Place 0 already had Valentine's day.</br>Cupid's last position was 1.</br>Cupid has failed 1 places. |

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
```Python
houses = list(map(int, input().split('@')))
index = 0
while True:
    command = input()
    if command == 'Love!':
        break
    jumping = command.split(' ')
    index += int(jumping[1])
    if index >= len(houses) or index < 0:
        index = 0
    if houses[index] - 2 >= 0:
        houses[index] -= 2
        if houses[index] == 0:
            print(f"Place {index} has Valentine's day.")
    elif houses[index] == 0:
        print(f"Place {index} already had Valentine's day.")
print(f"Cupid's last position was {index}.")

is_sucsessful = True
failed_houses = 0
for heart in houses:
    if heart != 0:
        failed_houses += 1
        is_sucsessful = False

if is_sucsessful:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {failed_houses} places.")
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

As a young traveler, you gather items and craft new items.
Input / Constraints
You will receive a journal with some collecting items, separated with a comma and a space (", ").
 After that, until receiving "Craft!" you will be receiving different commands split by " - ":
* •	"Collect - {item}" - you should add the given item to your inventory. 
If the item already exists, you should skip this line.
* •	"Drop - {item}" - you should remove the item from your inventory if it exists.
* •	"Combine Items - {old_item}:{new_item}" - you should check if the old item exists. 
If so, add the new item after the old one. Otherwise, ignore the command.
* •	"Renew – {item}" – if the given item exists, you should change its position and put it last in your inventory.
Output
After receiving "Craft!" print the items in your inventory, separated by ", ".
Examples

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

</details>
<details> <summary>Code</summary>

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

Create a program that calculates bonus points for each student enrolled in a course.
On the first line, you are going to receive the number of the students. On the second line,
you will receive the total number of lectures in the course. The course has an additional bonus,
which you will receive on the third line. On the following lines,
you will be receiving the count of attendances for each student.
The bonus is calculated with the following formula:
{total bonus} = {student attendances} / {course lectures} * (5 + {additional bonus})
Find the student with the maximum bonus and print them, along with his attendances,
in the following format:
"Max Bonus: {max bonus points}."
"The student has attended {student attendances} lectures."
Round the bonus points at the end to the nearest larger number.
Input / Constrains
* •	On the first line, you are going to receive the number of the students – an integer in the range [0…50]
* •	On the second line, you will receive the number of the lectures – an integer number in the range [0...50].
* •	On the third line, you will receive the additional bonus – an integer number in the range [0….100].
* •	On the following lines, you will be receiving the attendance of each student.
* •	There will never be students with equal bonuses.
Output
* •	Print the maximum bonus points and the attendances of the given student,
rounded to the nearest larger number, scored by a student in this course in the format described above.

| Input                                                                                | Output                                                    |
|--------------------------------------------------------------------------------------|-----------------------------------------------------------|
| 5</br>25</br>30</br>12</br>19</br>24</br>16</br>20                                   | Max Bonus: 34.</br> The student has attended 24 lectures. |
| 10</br>30</br>14</br>8</br>23</br>27</br>28</br>15</br>17</br>25</br>26</br>5</br>18 | Max Bonus: 18.</br>The student has attended 28 lectures.  |


</details>
<details> <summary>Code</summary>

```Python
from math import ceil

number_of_students = int(input())
lectures = int(input())
additional_bonus = int(input())

max_bonus = 0
student_attended = 0

for student in range(1, number_of_students + 1):
    attendance = int(input())
    current_bonus = attendance / lectures * (5 + additional_bonus)
    if max_bonus < current_bonus:
        max_bonus = current_bonus
        student_attended = attendance

print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {student_attended} lectures.")
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

It's the end of the week, and it is time for you to go shopping, so you need to create a shopping list first.
Input
You will receive an initial list with groceries separated by an exclamation mark "!".
After that, you will be receiving 4 types of commands until you receive "Go Shopping!".
* •	"Urgent {item}" - add the item at the start of the list. 
If the item already exists, skip this command.
* •	"Unnecessary {item}" - remove the item with the given name, only if it exists in the list.
Otherwise, skip this command.
* •	"Correct {oldItem} {newItem}" - if the item with the given old name exists,
change its name with the new one. Otherwise, skip this command.
* •	"Rearrange {item}" - if the grocery exists in the list, remove it from its current
position and add it at the end of the list. Otherwise, skip this command.
Constraints
* •	There won't be any duplicate items in the initial list
Output
* •	Print the list with all the groceries, joined by ", ":

"{firstGrocery}, {secondGrocery}, … {nthGrocery}"

| Input | Output |
|-------|--------|
|Tomatoes!Potatoes!Bread</br>Unnecessary Milk</br>Urgent Tomatoes</br>Go Shopping!|Tomatoes, Potatoes, Bread|
|Milk!Pepper!Salt!Water!Banana</br>
Urgent Salt</br>Unnecessary Grapes </br>Correct Pepper Onion</br>Rearrange Grapes</br>Correct Tomatoes Potatoes</br>Go Shopping!|Milk, Onion, Salt, Water, Banana|

</details>
<details> <summary>Code</summary>

```Python
initial_list = input().split('!')

while True:
    command = input()
    if command == "Go Shopping!":
        break
    current_input = command.split()
    order = current_input[0]
    product = current_input[1]
    if order == 'Urgent':
        if product  not in initial_list:
            initial_list.insert(0, product)
    elif order == 'Unnecessary':
        if product  in initial_list:
            initial_list.remove(product)
    elif order == 'Correct':
        if product in initial_list:
            new_product = current_input[2]
            index = initial_list.index(product)
            initial_list[index] = new_product
    elif order== 'Rearrange':
        if product  in initial_list:
            initial_list.remove(product)
            initial_list.append(product)

print(*initial_list,sep=', ')
```

</details>
</details>

> 02. MuOnline

[judge](https://judge.softuni.org/Contests/Practice/Index/2028#1)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40383)

<details> <summary> Example & Code</summary>
<details><summary>Example</summary>

You have initial health 100 and initial bitcoins 0. You will be given a string
 representing the dungeon's rooms. Each room is separated with '|' (vertical bar): "room1|room2|room3…"
Each room contains a command and a number, separated by space. The command can be:
•	"potion"
* 	You are healed with the number in the second part. But your health cannot exceed your initial health (100).
* o	First print: "You healed for {amount} hp."
* o	After that, print your current health: "Current health: {health} hp."
  * •	"chest"
* o	You've found some bitcoins, the number in the second part.
* o	Print: "You found {amount} bitcoins."
  * •	In any other case, you are facing a monster, which you will fight. 
  The second part of the room contains the attack of the monster. You should remove the monster's attack from your health. 
* o	If you are not dead (health <= 0), you've slain the monster, and you should print: "You slayed {monster}."
* o	If you've died, print "You died! Killed by {monster}." and your quest is over. 
Print the best room you've manage to reach: "Best room: {room}"
If you managed to go through all the rooms in the dungeon, print on the following three lines: 

"You've made it!"</br>
"Bitcoins: {bitcoins}"</br>
"Health: {health}"</br>

Input / Constraints

You receive a string representing the dungeon's rooms, separated with '|' (vertical bar): "room1|room2|room3…".

Output

Print the corresponding messages described above.

### Input

rat 10|bat 20|potion 10|rat 10|chest 100|boss 70|chest 1000	You slayed rat.

### Output
You slayed bat.</br>You healed for 10 hp.</br>Current health: 80 hp.</br>You slayed rat.</br>You found 100 bitcoins.</br>You died! Killed by boss.</br>Best room: 6

### Input

cat 10|potion 30|orc 10|chest 10|snake 25|chest 110	You slayed cat.

### Output

You healed for 10 hp.</br>Current health: 100 hp.</br>You slayed orc.</br>You found 10 bitcoins.</br>You slayed snake.</br>You found 110 bitcoins.</br>You've made it!</br>Bitcoins: 120</br>Health: 65


</details>
<details> <summary>Code</summary>

```Python
dungeon = input().split('|')

health = 100
bitcoin = 0
room = 0

dead = False
for command in dungeon:
    room += 1
    order, amount = command.split(' ')
    if order == 'potion':
        if health + int(amount) > 100:
            diff = 100 - health
            print(f"You healed for {diff} hp.")
            health = 100
        else:
            health += int(amount)
            print(f"You healed for {amount} hp.")
        print(f"Current health: {health} hp.")
    elif order == 'chest':
        bitcoin += int(amount)
        print(f"You found {amount} bitcoins.")
    else:
        if health - int(amount) <= 0:
            print(f"You died! Killed by {order}.")
            print(f"Best room: {room}")
            dead = True
            break
        else:
            health -= int(amount)
            print(f"You slayed {order}.")
if dead is not True:
    print(f"You've made it!\nBitcoins: {bitcoin}\nHealth: {health}")
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

######

<details><summary> Mid Exam Retake </summary> 


>  01. Black Flag

[judge](https://judge.softuni.org/Contests/Practice/Index/2474#0)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40364)

<details> <summary> Example & Code</summary>
<details><summary>Example</summary>

Pirates are invading the sea, and you're tasked to help them plunder
Create a program that checks if target plunder is reached. 
First, you will receive how many days the pirating lasts.

 Then you will receive how much the pirates plunder for a day. 
 Last you will receive the expected plunder at the end.

Calculate how much plunder the pirates manage to gather. Each day they gather the plunder. 
Keep in mind that they attack more ships every third day and 
add additional plunder to their total gain, which is 50% of the daily plunder.
 Every fifth day the pirates encounter a warship, and after the battle, they lose 30% of their total plunder.
If the gained plunder is more or equal to the target, print the following:
"Ahoy! {totalPlunder} plunder gained."
If the gained plunder is less than the target. Calculate the percentage left and print the following:
"Collected only {percentage}% of the plunder."
Both numbers should be formatted to the 2nd decimal place.
Input
* •	On the 1st line, you will receive the days of the plunder – an integer number in the range [0…100000]
* •	On the 2nd line, you will receive the daily plunder – an integer number in the range [0…50]
* •	On the 3rd line, you will receive the expected plunder – a real number in the range [0.0…10000.0]
Output
* •	 In the end, print whether the plunder was successful or not, following the format described above.

| Input     | Output |
|-----------|--------|
| 5 40 100  |Ahoy! 154.00 plunder gained.|
| 10 20 380 |Collected only 36.29% of the plunder.|
|           |        |

</details>
<details> <summary>Code</summary>

```Python
days = int(input())
daily_plunder = int(input())
expected_plunder = int(input())

gained_plunder = 0

for day in range(1, days + 1):
    if day % 3 == 0:
        gained_plunder += daily_plunder * 1.5
    else:
        gained_plunder += daily_plunder
    if day % 5 == 0:
        gained_plunder *= 0.7

if gained_plunder >= expected_plunder:
    print(f"Ahoy! {gained_plunder:.2f} plunder gained.")
else:
    percentage = gained_plunder / expected_plunder * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")
```
</details>
</details>

> 2. Treasure Hunt

[judge](https://judge.softuni.org/Contests/Practice/Index/2474#0)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40364)

<details> <summary> Example & Code</summary>
<details><summary>Example</summary>

The pirates need to carry a treasure chest safely back to the ship, looting along the way.
Create a program that manages the state of the treasure chest along the way. 
On the first line, you will receive the initial loot of the treasure chest,
 which is a string of items separated by a "|".
"{loot1}|{loot2}|{loot3} … {lootn}"
The following lines represent commands until "Yohoho!" which ends the treasure hunt:

"Loot {item1} {item2}…{itemn}":

* o	Pick up treasure loot along the way. Insert the items at the beginning of the chest. 
* o	If an item is already contained, don't insert it.

* "Drop {index}":

* o	Remove the loot at the given position and add it at the end of the treasure chest. 
* o	If the index is invalid, skip the command.

"Steal {count}":

* o	Someone steals the last count loot items. If there are fewer items than the given count, 
remove as much as there are. 
* o	Print the stolen items separated by ", ":

"{item1}, {item2}, {item3} … {itemn}"

In the end, output the average treasure gain, which is the sum of all treasure items 
length divided by the count of all items inside the chest formatted to the second decimal point:
"Average treasure gain: {averageGain} pirate credits."
If the chest is empty, print the following message:
"Failed treasure hunt."

### Input

* •	On the 1st line, you are going to receive the initial treasure chest (loot separated by "|")
* •	On the following lines, until "Yohoho!", you will be receiving commands.

### Output

* •	Print the output in the format described above.
Constraints
* •	The loot items will be strings containing any ASCII code.
* •	The indexes will be integers in the range [-200…200]
* •	The count will be an integer in the range [1….100]

### Input
Gold|Silver|Bronze|Medallion|Cup
Loot Wood Gold Coins
Loot Silver Pistol
Drop 3
Steal 3
Yohoho!

### Output
Medallion, Cup, Gold
Average treasure gain: 5.40 pirate credits.


### Input
Diamonds|Silver|Shotgun|Gold
Loot Silver Medals Coal
Drop -1
Drop 1
Steal 6
Yohoho!


### Output
Coal, Diamonds, Silver, Shotgun, Gold, Medals
Failed treasure hunt.


</details>
<details> <summary>Code</summary>

```Python
treasure = input().split('|')

empty_treasure = False

while True:
    command = input()
    if command == "Yohoho!":
        break
    input_data = command.split()
    order = input_data[0]
    if order == 'Loot':
        for item_index in range(1, len(input_data)):
            new_item = input_data[item_index]
            if new_item not in treasure:
                treasure.insert(0, new_item)
    elif order == 'Drop':
        index = int(input_data[1])
        if index < 0 or index >= len(treasure):
            continue
        item = treasure.pop(index)
        treasure.append(item)
    elif order == 'Steal':
        count = int(input_data[1])
        if count >= len(treasure):
            print(*treasure, sep=', ')
            empty_treasure = True
            break
        else:
            stolen_items = treasure[len(treasure) - count:len(treasure) + 1]
            print(*stolen_items, sep=', ')
            del treasure[len(treasure) - count:len(treasure) + 1]


if empty_treasure:
    print('Failed treasure hunt.')
else:
    lenght = 0
    for word in treasure:
        lenght += len(word)
    avverage_gain = lenght / len(treasure)

    print(f"Average treasure gain: {avverage_gain:.2f} pirate credits.")

```
</details>
</details>

> 3. Man O War

[judge](https://judge.softuni.org/Contests/Practice/Index/2474#0)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40364)

<details> <summary> Example & Code</summary>
<details><summary>Example</summary>

The pirates encounter a huge Man-O-War at sea. 
Create a program that tracks the battle and either chooses a winner or prints a stalemate.
 On the first line, you will receive the status of the pirate ship, 
 which is a string representing integer sections separated by ">".
  On the second line, you will receive the same type of status, but for the warship: 

"{section1}>{section2}>{section3}… {sectionn}"

On the third line, you will receive the maximum health capacity a section of the ship can reach. 
The following lines represent commands until "Retire":

* •	"Fire {index} {damage}" - the pirate ship attacks the warship with the given damage at that section.
 Check if the index is valid and if not, skip the command. If the section breaks (health <= 0) the warship sinks,
  print the following and stop the program: "You won! The enemy ship has sunken."
* •	"Defend {startIndex} {endIndex} {damage}" - the warship attacks the pirate ship 
with the given damage at that range (indexes are inclusive). Check if both indexes are valid and if not,
 skip the command. If the section breaks (health <= 0) the pirate ship sinks, print the following and stop the program:
"You lost! The pirate ship has sunken."
* •	"Repair {index} {health}" - the crew repairs a section of the pirate ship with the given health. 
Check if the index is valid and if not, skip the command. 
The health of the section cannot exceed the maximum health capacity.
* •	"Status" - prints the count of all sections of the pirate ship that need repair soon, 
which are all sections that are lower than 20% of the maximum health capacity. Print the following:
"{count} sections need repair."
In the end, if a stalemate occurs, print the status of both ships, which is the sum of their individual sections, 
in the following format:

"Pirate ship status: {pirateShipSum}

Warship status: {warshipSum}"

### Input
* •	On the 1st line, you are going to receive the status of the pirate ship (integers separated by '>')
* •	On the 2nd line, you are going to receive the status of the warship
* •	On the 3rd line, you will receive the maximum health a section of a ship can reach.
* •	On the following lines, until "Retire", you will be receiving commands.
### Output
* •	Print the output in the format described above.
### Constraints
* •	The section numbers will be integers in the range [1….1000]
* •	The indexes will be integers [-200….200]
* •	The damage will be an integer in the range [1….1000]
* •	The health will be an integer in the range [1….1000]

| Input | Output |
|-------|--------|
|12>13>11>20>66</br>
12>22>33>44>55>32>18</br>70</br>Fire 2 11</br>Fire 8 100</br>Defend 3 6 11</br>Defend 0 3 5</br>Repair 1 33</br>Status</br>Retire|2 sections need repair.</br>Pirate ship status: 135</br>Warship status: 205|
|2>3>4>5>2</br>6>7>8>9>10>11</br>20</br>Status</br>Fire 2 3</br>Defend 0 4 11</br>Repair 3 18</br>Retire|3 sections need repair.</br>You lost! The pirate ship has sunken.|


</details>
<details> <summary>Code</summary>

```Python
pirate_ship = list(map(int, input().split('>')))
war_ship = list(map(int, input().split('>')))
max_health = int(input())

finished_battle = False
destroyed = False

while destroyed is not True:
    input_line = input()
    if input_line == 'Retire':
        finished_battle = True
        break
    input_data = input_line.split()
    command = input_data[0]
    if command == 'Fire':
        index = int(input_data[1])  # warship index
        if index >= 0 and index < len(war_ship):
            damage = int(input_data[2])
            if war_ship[index] - damage <= 0:
                print("You won! The enemy ship has sunken.")
                break
            war_ship[index] -= damage
    elif command == 'Defend':
        start_index = int(input_data[1])  # start_index of pirate ship
        end_index = int(input_data[2])  # end_index of pirate ship
        if start_index >= 0 and start_index < len(pirate_ship):
            if end_index >= 0 and end_index < len(pirate_ship):
                damage = int(input_data[3])
                for ship_block in range(start_index, end_index + 1):
                    if pirate_ship[ship_block] - damage <= 0:
                        print(f"You lost! The pirate ship has sunken.")
                        destroyed=True
                        break
                    pirate_ship[ship_block] -= damage
    elif command == 'Repair':
        block_index = int(input_data[1])  # index of Pirate ship block for repair
        if block_index >= 0 and block_index < len(pirate_ship):
            health = int(input_data[2])
            if pirate_ship[block_index] + health > max_health:
                pirate_ship[block_index] = max_health
            else:
                pirate_ship[block_index] += health
    elif command == 'Status':
        block_for_repair = 0
        for block in pirate_ship:
            if block < (max_health * 0.2):
                block_for_repair += 1
        print(f"{block_for_repair} sections need repair.")

if finished_battle:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f'Warship status: {sum(war_ship)}')
```
</details>
</details>


</details>

<img src="https://github.com/Nenogzar/Academy_SoftUni/blob/main/fundamentals_python/image/10.jpg" alt="ME" width="400">

<details><summary> Mid-Exam-Preparation-1 </summary> 

####

> 1.	Computer Store

[Judge](https://judge.softuni.org/Contests/Practice/Index/2517#0)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40358)

<details> <summary> Example & Code</summary>

####
<details> <summary>Example</summary>


NB! Link for judge system works only if you are registered in Software University Sofia !!!!!!!!!!!!!!

Write a program that prints you a receipt for your new computer.
You will receive the parts' prices (without tax) until you receive what type of customer this is - special or regular.
Once you receive the type of customer you should print the receipt.
The taxes are 20% of each part's price you receive. 
If the customer is special, he has a 10% discount on the total price with taxes.
If a given price is not a positive number, you should print "Invalid price!" on the console and continue with the next price.
If the total price is equal tzero, you should print "Invalid order!" on the console.

Input

You will receive numbers representing prices (without tax) until command "special" or "regular":

Output

* The receipt should be in the following format: 

"Congratulations you've just bought a new computer!

Price without taxes: {total price without taxes}$

Taxes: {total amount of taxes}$

-----------

Total price: {total price with taxes}$"


Note: All prices should be displayed tthe second digit after the decimal point!
The discount is applied only on the total price. Discount is only applicable tthe final price!

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

> 02. The Lift

[judge](https://judge.softuni.org/Contests/Practice/Index/2517#1)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40359)

<details> <summary> Example & Code</summary>

####
<details><summary>Example</summary>

NB! Link for judge system works only if you are registered in Software University Sofia !!!!!!!!!!!!!!

Write a program that finds a place for the tourist on a lift. 
Every wagon should have a maximum of 4 people on it. If a wagon is full, you should direct the people tthe next one with space available.

Input

On the first line, you will receive how many people are waiting tget on the lift

On the second line, you will receive the current state of the lift separated by a single space: " ".

Output

When there is nmore available space left on the lift, or there are nmore people in the queue, 
you should print on the console the final state of the lift's wagons separated by " " and one of the following messages:

If there are nmore people and the lift have empty spots, you should print:

"The lift has empty spots!</br>{wagons separated by ' '}"

If there are still people in the queue and nmore available space, you should print:

"There isn't enough space! {people} people in a queue! </br>{wagons separated by ' '}"

If the lift is full and there are nmore people in the queue, you should print only the wagons separated by " "



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

> 03. Memory Game

[judge](https://judge.softuni.org/Contests/Practice/Index/2517#2)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40360)
<details> <summary> Example & Code</summary>

####
<details><summary>Example</summary>

Write a program that recreates the Memory game.</br>
On the first line, you will receive a sequence of elements.</br>
Each element in the sequence will have a twin. Until the player receives "end" from the console,
you will receive strings with twintegers separated by a space, representing the indexes of elements in the sequence.</br>
If the player tries tcheat and enters twequal indexes or indexes which are out of bounds of the sequence
, you should add twmatching elements at the middle of the sequence in the following format:</br>
"-{number of moves until now}a" </br>
Then print this message on the console:</br>
"Invalid input! Adding additional elements tthe board"</br>

Input

On the first line, you will receive a sequence of elements</br>
On the following lines, you will receive integers until the command "end"</br>

Output

Every time the player hit twmatching elements, you should remove them from the sequence and print on the console the following message:
"Congrats! You have found matching elements - ${element}!"</br>
If the player hit twdifferent elements, you should print on the console the following message:
"Try again!"</br>
If the player hit all matching elements before he receives "end" from the console, you should print on the console the following message: 
"You have won in {number of moves until now} turns!"</br>
If the player receives "end" before he hits all matching elements, you should print on the console the following message:
"Sorry you lose :(</br>
{the current sequence's state}"</br>

Constraints

All elements in the sequence will always have a matching element.

| Input                                                                    | Output                                                                                                                                                                                                                                                                                                     |
|--------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 1 2 2 3 3 4 4 5 5 </br>1 0</br>-1 0</br>1 0 </br>1 0 </br>1 0 </br>end | Congrats! You have found matching elements - 1!</br>Invalid input! Adding additional elements tthe board</br>Congrats! You have found matching elements - 2!</br>Congrats! You have found matching elements - 3!</br>Congrats! You have found matching elements - -2a!</br>Sorry you lose :(</br>4 4 5 5 |
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
        print("Invalid input! Adding additional elements tthe board")
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
</details>

######
<details><summary> Mid-Exam-Preparation-2 </summary>

>  01. SoftUni Reception

[judge](https://judge.softuni.org/Contests/Practice/Index/2474#0)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40364)

<details> <summary> Example & Code</summary>

####
<details><summary>Example</summary>

Every day, thousands of students pass by the reception at SoftUni with different questions task.
The employees have thelp everyone by providing all the information and answering all of the questions.
Three employees are working on the reception all day. Each of them can handle a different number of students per hour. 
Your task is tcalculate how much time it will take tanswer all the questions of a given number of students.
First, you will receive 3 lines with integers, representing the number of students that each employee can help per hour.
On the following line, you will receive students count as a single integer. 
Every fourth hour, all employees have a break, sthey don't work for an hour. It is the only break for the employees, 
because they don't need rest, nor have a personal life. Calculate the time needed tanswer all the student's
questions and print it in the following format: "Time needed: {time}h."

Input / Constraints

* On the first three lines -  each employee efficiency -  integer in the range [1 - 100]
* On the fourth line - students count – integer in the range [0 – 10000]
* Input will always be valid and in the range specified

Output

* Print a single line: "Time needed: {time}h."
* Allowed working time / memory: 100ms / 16MB

| Input                 | Output |
|-----------------------|--------|
| 5</br> 6</br>4</br>20 |Time needed: 2h.|
| 1</br>2</br>3</br>45  |       Time needed: 10h. |


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

> 2.	Array Modifier

[judge](https://judge.softuni.org/Contests/Practice/Index/2474#1)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40365)
<details> <summary> Example & Code</summary>

####
<details><summary>Example</summary>


You are given an array with integers. Write a program tmodify the elements after receiving the following commands:
* "swap {index1} {index2}" takes twelements and swap their places.
* "multiply {index1} {index2}" takes element at the 1st index and multiply 
* it with the element at 2nd index. Save the product at the 1st index.
* "decrease" decreases all elements in the array with 1.

Input

On the first input line, you will be given the initial array values separated by a single space.
On the next lines you will receive commands until you receive the command "end". The commands are as follow: 
* "swap {index1} {index2}"
* "multiply {index1} {index2}"
* "decrease"

Output

The output should be printed on the console and consist of elements of the modified array – separated by a comma and a single space ", ".
Constraints

* Elements of the array will be integer numbers in the range [-231...231]
* Count of the array elements will be in the range [2...100]
* Indexes will be always in the range of the array

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
data_inf= input()
while data_inf!= "end":
    if "decrease" in data_info:
        elements = [x - 1 for x in elements]
        data_inf= input()
        continue

    command, index_one, index_tw= [x if x.isalpha() else int(x) for x in data_info.split()]

    if command == "swap":
        elements[index_one], elements[index_two] = elements[index_two], elements[index_one]

    elif command == "multiply":
        elements[index_one] *= elements[index_two]

    data_inf= input()

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

> 03. Numbers

[judge](https://judge.softuni.org/Contests/Practice/Index/2474#2)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40366)
<details> <summary> Example & Code</summary>

####
<details><summary>Example</summary>

Write a program tread a sequence of integers and find and print the top 5 numbers
greater than the average value in the sequence, sorted in descending order.
Input
Read from the console a single line holding space-separated integers.
Output
Print the above-described numbers on a single line, space-separated. 
If less than 5 numbers hold the property mentioned above, print less than 5 numbers. 
Print "No" if nnumbers hold the above property.
Constraints
All input numbers are integers in the range [-1 000 000 … 1 000 000]. 
The count of numbers is in the range [1…10 000].

| Input                               | Output         |
|-------------------------------------|----------------|
| 10 20 30 40 50                      | 50 40          |
| 5 2 3 4 -10 30 40 50 20 50 60 60 51 | 60 60 51 50 50 |
| 1                                   | N            |
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
<details><summary> Mid-Exam-Preparation-3 </summary>

> 1.	Counter-Strike

[judge](https://judge.softuni.org/Contests/Practice/Index/2305#0)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40370)</br>
[pastebin Ivan Shopov](https://pastebin.com/vrxNF4bB)
<details> <summary> Example & Code</summary>

####
<details><summary>Example</summary>

Write a program that keeps track of every won battle against an enemy.</br>
You will receive initial energy. Afterward, you will start receiving
the distance you need treach an enemy until the "End of battle" command is given, or you run out of energy.</br>
The energy you need for reaching an enemy is equal tthe distance you receive.</br>
Each time you reach an enemy, you win a battle, and your energy is reduced. </br>
Otherwise, if you don't have enough energy treach an enemy, end the program and print:</br>
"Not enough energy! Game ends with {count} won battles and {energy} energy".</br>
Every third won battle increases your energy with the value of your current count of won battles.</br>
Upon receiving the "End of battle" command, print the count of won battles in the following format:</br>
"Won battles: {count}. Energy left: {energy}" 

Input / Constraints

On the first line, you will receive initial energy – an integer [1-10000].</br>
On the following lines, you will be receiving the distance of an enemy – an integer [1-10000]</br>

Output

The description contains the proper output messages for each case and the format they should be printed.


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
        return False  # We return False tindicate that the game is over

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


>  2.	Shoot for the Win

[Link tJudge](https://judge.softuni.org/Contests/Practice/Index/2305#1)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40371)
<details> <summary> Example & Code</summary>

####
<details><summary>Example</summary>

Write a program that helps you keep track of your shot targets. </br>
You will receive a sequence with integers, separated by a single space, 
representing targets and their value. Afterward, you will be receiving 
indices until the "End" command is given, and you need tprint the targets and the count of shot targets.</br>
Every time you receive an index, you need tshoot the target on that index, if it is possible. </br>
Every time you shoot a target, its value becomes -1, and it is considered shot. </br>

Along with that, you alsneed to:</br>
Reduce all the other targets, which have greater values than your current target, with its value.</br> 
Increase all the other targets, which have less than or equal value tthe shot target, with its value.</br>
Keep in mind that you can't shoot a target, which is already shot. You alscan't increase or reduce a target, which is considered shot.
When you receive the "End" command, print the targets in their current state and the count of shot targets in the following format:</br>
"Shot targets: {count} -> {target1} {target2}… {targetn}"

Input / Constraints

On the first line of input, you will receive a sequence of integers, separated by a single space – the targets sequence.</br>
On the following lines, until the "End" command, you be receiving integers each on a single line – the index of the target tbe shot.</br>

Output

The format of the output is described above in the problem description.



| Input                                         | Output |
|-----------------------------------------------|--------|
| 24 50 36 70<br>0 <br>4 <br>3 <br>1<br>End     |   Shot targets 3 -> -1 -1 130 -1	  |
| 30 30 12 60 54 66 <br>5<br>2<br>4<br>0<br>End |    Shot targets: 4 -> -1 120 -1 66 -1 -1    |
|                                               |        |

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

> 03. Moving Target

[judge](https://judge.softuni.org/Contests/Practice/Index/2305#2)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40372)
<details> <summary> Example & Code</summary>

####
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




</details>


######
<details><summary> Mid-Exam-Preparation-4 </summary>

> 01. Guinea Pig

[judge](https://judge.softuni.org/Contests/Practice/Index/2031#0)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40376)

<details> <summary> Example & Code</summary>

####
<details><summary>Example</summary>
Merry has a guinea pig named Puppy, that she loves very much.
Every month she goes tthe nearest pet store and buys him everything he needs – food, hay, and cover.
On the first three lines, you will receive the quantity of food, hay, and cover, 
which Merry buys for a month (30 days). On the fourth line, you will receive the guinea pig's weight.
Every day Puppy eats 300 gr of food. Every second day Merry first feeds the pet, 
then gives it a certain amount of hay equal t5% of the rest of the food. On every third day, 
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
* "Merry must gtthe pet store!"
* The output values must be formatted tthe second decimal place!

|Input|Output|
|-|-|
|10</br>5</br>5.2</br>1|Everything is fine! Puppy is happy! Food: 1.00, Hay: 1.10, Cover: 1.87.|
|1</br>1.5</br>3</br>1.5|Merry must gtthe pet store!|


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
    print("Merry must gtthe pet store!")
```
</details>
</details>

> 02. Shopping List

[judge](https://judge.softuni.org/Contests/Practice/Index/2031#1)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40377)

<details> <summary> Example & Code</summary>

####
<details><summary>Example</summary>

It's the end of the week, and it is time for you tgshopping, syou need tcreate a shopping list first.
Input
You will receive an initial list with groceries separated by an exclamation mark "!".
After that, you will be receiving 4 types of commands until you receive "GShopping!".
* "Urgent {item}" - add the item at the start of the list. 
If the item already exists, skip this command.
* "Unnecessary {item}" - remove the item with the given name, only if it exists in the list.
Otherwise, skip this command.
* "Correct {oldItem} {newItem}" - if the item with the given old name exists,
change its name with the new one. Otherwise, skip this command.
* "Rearrange {item}" - if the grocery exists in the list, remove it from its current
position and add it at the end of the list. Otherwise, skip this command.
Constraints
* There won't be any duplicate items in the initial list
Output
* Print the list with all the groceries, joined by ", ":

"{firstGrocery}, {secondGrocery}, … {nthGrocery}"

| Input | Output |
|-------|--------|
|Tomatoes!Potatoes!Bread</br>Unnecessary Milk</br>Urgent Tomatoes</br>GShopping!|Tomatoes, Potatoes, Bread|
|Milk!Pepper!Salt!Water!Banana</br>
Urgent Salt</br>Unnecessary Grapes </br>Correct Pepper Onion</br>Rearrange Grapes</br>Correct Tomatoes Potatoes</br>GShopping!|Milk, Onion, Salt, Water, Banana|

</details>
<details> <summary>Code</summary>

```Python
initial_list = input().split('!')

while True:
    command = input()
    if command == "GShopping!":
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

> 3.	Heart Delivery

[Link tJudge](https://judge.softuni.org/Contests/Practice/Index/2031#2)</br>
[Problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40378)
<details> <summary> Example & Code</summary>

####
<details><summary>Example</summary>

Valentine's day is coming, and Cupid has minimal time tspread some love across the neighborhood. Help him with his mission!
You will receive a string with even integers, separated by a "@" - this is our neighborhood.
After that, a series of Jump commands will follow until you receive "Love!".
Every house in the neighborhood needs a certain number of hearts delivered by Cupid sit can celebrate Valentine's day.
The integers in the neighborhood indicate those needed hearts.
Cupid starts at the position of the first house (index 0) and must jump by a given length.
The jump commands will be in this format: "Jump {length}". 
Every time he jumps from one house tanother, the needed hearts for the visited house are decreased by 2: 
* If the needed hearts for a certain house become equal t0, print on the console "Place {house_index} has Valentine's day." 
* If Cupid jumps ta house where the needed hearts are already 0, print on the console "Place {house_index} already had Valentine's day."
* Keep in mind that Cupid can have a larger jump length than the size of the neighborhood, 
and if he does jump outside of it, he should start from the first house again (index 0)
For example, we are given this neighborhood: 6@6@6. Cupid is at the start and jumps with a length of 2.
He will end up at index 2 and decrease the needed hearts by 2: [6, 6, 4]. Next,
he jumps again with a length of 2 and goes outside the neighborhood, she goes back tthe first house (index 0)
and again decreases the needed hearts there: [4, 6, 4].
Input
* On the first line, you will receive a string with even integers separated by "@" – the neighborhood and the number of hearts for each house.
* On the next lines, until "Love!" is received, you will be getting jump commands in this format: "Jump {length}".
Output
In the end, print Cupid's last position and whether his mission was successful or not:
* "Cupid's last position was {last_position_index}."
* If each house has had Valentine's day, print: 
  * "Mission was successful."
* If not, print the count of all houses that didn't celebrate Valentine's Day:
  * "Cupid has failed {houseCount} places."
  Constraints
* The neighborhood's size will be in the range [1…20]
* Each house will need an even number of hearts in the range [2 … 10]
* Each jump length will be an integer in the range [1 … 20]

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
<details><summary> Mid-Exam-Preparation-5 </summary>

> 01. Bonus Scoring System

[judge](https://judge.softuni.org/Contests/Practice/Index/2028#0)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40382)

<details> <summary> Example & Code</summary>

####
<details><summary>Example</summary>

Create a program that calculates bonus points for each student enrolled in a course.
On the first line, you are going treceive the number of the students. On the second line,
you will receive the total number of lectures in the course. The course has an additional bonus,
which you will receive on the third line. On the following lines,
you will be receiving the count of attendances for each student.
The bonus is calculated with the following formula:
{total bonus} = {student attendances} / {course lectures} * (5 + {additional bonus})
Find the student with the maximum bonus and print them, along with his attendances,
in the following format:
"Max Bonus: {max bonus points}."
"The student has attended {student attendances} lectures."
Round the bonus points at the end tthe nearest larger number.
Input / Constrains
* On the first line, you are going treceive the number of the students – an integer in the range [0…50]
* On the second line, you will receive the number of the lectures – an integer number in the range [0...50].
* On the third line, you will receive the additional bonus – an integer number in the range [0….100].
* On the following lines, you will be receiving the attendance of each student.
* There will never be students with equal bonuses.
Output
* Print the maximum bonus points and the attendances of the given student,
rounded tthe nearest larger number, scored by a student in this course in the format described above.

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

> 02. MuOnline

[judge](https://judge.softuni.org/Contests/Practice/Index/2028#1)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40383)

<details> <summary> Example & Code</summary>

####
<details><summary>Example</summary>

You have initial health 100 and initial bitcoins 0. You will be given a string
 representing the dungeon's rooms. Each room is separated with '|' (vertical bar): "room1|room2|room3…"
Each room contains a command and a number, separated by space. The command can be:
"potion"
* 	You are healed with the number in the second part. But your health cannot exceed your initial health (100).
* First print: "You healed for {amount} hp."
* After that, print your current health: "Current health: {health} hp."
  * "chest"
* You've found some bitcoins, the number in the second part.
* Print: "You found {amount} bitcoins."
  * In any other case, you are facing a monster, which you will fight. 
  The second part of the room contains the attack of the monster. You should remove the monster's attack from your health. 
* If you are not dead (health <= 0), you've slain the monster, and you should print: "You slayed {monster}."
* If you've died, print "You died! Killed by {monster}." and your quest is over. 
Print the best room you've manage treach: "Best room: {room}"
If you managed tgthrough all the rooms in the dungeon, print on the following three lines: 

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

> 3.	Inventory

[judge](https://judge.softuni.org/Contests/Practice/Index/2028#2)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40384)   
<details> <summary> Example & Code</summary>
<details><summary>Example</summary>

As a young traveler, you gather items and craft new items.
Input / Constraints
You will receive a journal with some collecting items, separated with a comma and a space (", ").
 After that, until receiving "Craft!" you will be receiving different commands split by " - ":
* "Collect - {item}" - you should add the given item tyour inventory. 
If the item already exists, you should skip this line.
* "Drop - {item}" - you should remove the item from your inventory if it exists.
* "Combine Items - {old_item}:{new_item}" - you should check if the old item exists. 
If so, add the new item after the old one. Otherwise, ignore the command.
* "Renew – {item}" – if the given item exists, you should change its position and put it last in your inventory.
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
<details><summary> Mid-Exam-Preparation-6 </summary>

>  01. Black Flag

[judge](https://judge.softuni.org/Contests/Practice/Index/1773#0)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40388)

<details> <summary> Example & Code</summary>
<details><summary>Example</summary>

Pirates are invading the sea, and you're tasked thelp them plunder
Create a program that checks if target plunder is reached. 
First, you will receive how many days the pirating lasts.

 Then you will receive how much the pirates plunder for a day. 
 Last you will receive the expected plunder at the end.

Calculate how much plunder the pirates manage tgather. Each day they gather the plunder. 
Keep in mind that they attack more ships every third day and 
add additional plunder ttheir total gain, which is 50% of the daily plunder.
 Every fifth day the pirates encounter a warship, and after the battle, they lose 30% of their total plunder.
If the gained plunder is more or equal tthe target, print the following:
"Ahoy! {totalPlunder} plunder gained."
If the gained plunder is less than the target. Calculate the percentage left and print the following:
"Collected only {percentage}% of the plunder."
Both numbers should be formatted tthe 2nd decimal place.
Input
* On the 1st line, you will receive the days of the plunder – an integer number in the range [0…100000]
* On the 2nd line, you will receive the daily plunder – an integer number in the range [0…50]
* On the 3rd line, you will receive the expected plunder – a real number in the range [0.0…10000.0]
Output
*  In the end, print whether the plunder was successful or not, following the format described above.

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

[judge](https://judge.softuni.org/Contests/Practice/Index/1773#1)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40389)

<details> <summary> Example & Code</summary>
<details><summary>Example</summary>

The pirates need tcarry a treasure chest safely back tthe ship, looting along the way.
Create a program that manages the state of the treasure chest along the way. 
On the first line, you will receive the initial loot of the treasure chest,
 which is a string of items separated by a "|".
"{loot1}|{loot2}|{loot3} … {lootn}"
The following lines represent commands until "Yohoho!" which ends the treasure hunt:

"Loot {item1} {item2}…{itemn}":

* Pick up treasure loot along the way. Insert the items at the beginning of the chest. 
* If an item is already contained, don't insert it.

* "Drop {index}":

* Remove the loot at the given position and add it at the end of the treasure chest. 
* If the index is invalid, skip the command.

"Steal {count}":

* Someone steals the last count loot items. If there are fewer items than the given count, 
remove as much as there are. 
* Print the stolen items separated by ", ":

"{item1}, {item2}, {item3} … {itemn}"

In the end, output the average treasure gain, which is the sum of all treasure items 
length divided by the count of all items inside the chest formatted tthe second decimal point:
"Average treasure gain: {averageGain} pirate credits."
If the chest is empty, print the following message:
"Failed treasure hunt."

### Input

* On the 1st line, you are going treceive the initial treasure chest (loot separated by "|")
* On the following lines, until "Yohoho!", you will be receiving commands.

### Output

* Print the output in the format described above.
Constraints
* The loot items will be strings containing any ASCII code.
* The indexes will be integers in the range [-200…200]
* The count will be an integer in the range [1….100]

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

> 3. Man War

[judge](https://judge.softuni.org/Contests/Practice/Index/1773#2)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40390)

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

* "Fire {index} {damage}" - the pirate ship attacks the warship with the given damage at that section.
 Check if the index is valid and if not, skip the command. If the section breaks (health <= 0) the warship sinks,
  print the following and stop the program: "You won! The enemy ship has sunken."
* "Defend {startIndex} {endIndex} {damage}" - the warship attacks the pirate ship 
with the given damage at that range (indexes are inclusive). Check if both indexes are valid and if not,
 skip the command. If the section breaks (health <= 0) the pirate ship sinks, print the following and stop the program:
"You lost! The pirate ship has sunken."
* "Repair {index} {health}" - the crew repairs a section of the pirate ship with the given health. 
Check if the index is valid and if not, skip the command. 
The health of the section cannot exceed the maximum health capacity.
* "Status" - prints the count of all sections of the pirate ship that need repair soon, 
which are all sections that are lower than 20% of the maximum health capacity. Print the following:
"{count} sections need repair."
In the end, if a stalemate occurs, print the status of both ships, which is the sum of their individual sections, 
in the following format:

"Pirate ship status: {pirateShipSum}

Warship status: {warshipSum}"

### Input
* On the 1st line, you are going treceive the status of the pirate ship (integers separated by '>')
* On the 2nd line, you are going treceive the status of the warship
* On the 3rd line, you will receive the maximum health a section of a ship can reach.
* On the following lines, until "Retire", you will be receiving commands.
### Output
* Print the output in the format described above.
### Constraints
* The section numbers will be integers in the range [1….1000]
* The indexes will be integers [-200….200]
* The damage will be an integer in the range [1….1000]
* The health will be an integer in the range [1….1000]

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

######

<details><summary> Mid-Exam-1   - Missing Condition 2,3 </summary>

> 01. The Biscuit Factory - to solve the task

[judge]()</br>
[problem](https://github.com/Nenogzar/Academy_SoftUni/blob/main/fundamentals_python/lectures/19-21_Mid_Exam_Preparation/my_mid_exam/01_The_Biscuit_Factory.pdf)

<details> <summary> Example & Code</summary>

####

<details><summary>Example</summary>

Create a program that will help Anna calculate how many biscuits her factory can make in a month (**30 days**) and the percentage of production compared tanother factory's production.</br>
First, you will receive the biscuits produced **per day** (per worker). After that, you will receive the count of workers in your factory. Last, you will receive the number of biscuits that the **competing factory produces for 30 days**.</br>
You need tcalculate the production of your factory within **30 days**. Then you should calculate how much more or less biscuits you produce compared tthe other factory (**in percentage**). There will be ncase where the factories will produce the same number of biscuits.</br>
Every **third day** the workers produce **only 75%** of the usual production. Keep in mind that there can be only a whole biscuit after making calculations for each day – format them tthe lower number.</br>
In the end, **print the number** of biscuits produced for **30 days** in the following format:</br>
**"You have produced {countBiscuits} biscuits for the past month.**"</br>
Then print the **percentage of the difference**, formatted tthe 2nd decimal place, in the following format:</br>
If your production is **bigger** than the other factory:</br>
**"You produce {percentage} percent more biscuits."**</br>
If not:</br>
**"You produce {percentage} percent less biscuits."**

#### Input

* On the first line, you will receive the number of biscuits a worker produces per day – an integer number in the range [1…200].
* On the second line, you will receive the count of the workers in your factory – an integer number in the range [1…1000].
* On the third line, you will receive the number of biscuits that the competing factory produces for 30 days – an integer number in the range [1…264].
NOTE: The input will always be in the correct format.

#### Output

* Print the number of biscuits produced for 30 days in the format described above.
* Print the percentage of the difference formatted tthe 2nd decimal place in the format described above.

#### Constraints
* The percentage can be over 100%.
* There will be ncase where the factories will produce the same number of biscuits.

| Input                | Output                                                                                            |
|----------------------|---------------------------------------------------------------------------------------------------|
| 78</br>8</br>16000   | You have produced 17160 biscuits for the past month.</br>You produce 7.25 percent more biscuits.  |
| 65</br>12</br>26000  | You have produced 21450 biscuits for the past month.</br>You produce 17.50 percent less biscuits. |
| 163</br>16</br>67020 | You have produced 71720 biscuits for the past month.</br>You produce 7.01 percent more biscuits.  |

</details>
<details> <summary>Code</summary>

```Python

```

</details>
</details>

> 2. Coffee Lover  - Missing Condition

[judge]()</br>
[problem]()

<details> <summary> Example & Code</summary>

####

<details><summary>Example</summary>

| Input | Output |
|-------|--------|
|       |        |
|       |        |

</details>
<details> <summary>Code</summary>

```Python


```

</details>
</details>

> 3. The Angry Cat  - Missing Condition

[judge]()</br>
[problem]()

<details> <summary> Example & Code</summary>

####

<details><summary>Example</summary>

| Input | Output |
|-------|--------|
|       |        |
|       |        |

</details>

<details> <summary>Code</summary>

Bilyana Panova
```Python
price_rating = [int(x) for x in input().split(", ")]
entry_point = int(input())
type_of_items = input()
 
 
def cheep_summing(side):
    return sum([x for x in side if x < entry_point])
 
 
def expensive_summing(side):
    return sum([x for x in side if x >= entry_point])
 
 
left_side = price_rating[:entry_point]
right_side = price_rating[entry_point+1:]
entry_point = price_rating.pop(entry_point)
 
if type_of_items == "cheap":
    if cheep_summing(left_side) >= cheep_summing(right_side):
        print(f"Left - {cheep_summing(left_side)}")
    else:
        print(f"Right - {cheep_summing(right_side)}")
if type_of_items == "expensive":
    if expensive_summing(left_side) >= expensive_summing(right_side):
        print(f"Left - {expensive_summing(left_side)}")
    else:
        print(f"Right - {expensive_summing(right_side)}")
```

</details>
</details>
</details>

######

<details><summary> Mid-Exam-2 - 1 and 3 to solve the task </summary>

> 01. Burger Bus - to solve the task

[judge]()</br>
[problem](https://github.com/Nenogzar/Academy_SoftUni/blob/main/fundamentals_python/lectures/19-21_Mid_Exam_Preparation/my_mid_exam/01_Burger_Bus.pdf)

<details> <summary> Example & Code</summary>

####

<details><summary>Example</summary>

_The Burger Bus travels around the country and serves delicious burgers. You need thelp the owner keep track of his
income and expenses along the way._</br>
First, you will receive the number of cities the bus has visited. Then for every city, you will receive:
* the name of the city
* how much money the owner earned
* owner's expenses

Every 3rd (third) city the bus visits, the owner organizes a special event tensure a true "Burger Bus" experience, spending an additional 50% over costs.</br>
In every 5th (fifth) city, it is raining, and the owner losses 10% of the money he earned. In a rainy city, there is npossibility torganize a special event.</br>
You have tcalculate the owner's profit for each city and his total profit from the tour. Profit is calculated by deducting the expenses from the income.</br>
#### Input
The input will consist of:
* Number of cities – integer in the range [1…15]
* For each city, you will receive the following information:
  * name of the city - string
  * owner's income - a real number in the range [0.0…10 000.0]
  * owner's expenses - a real number in the range [0.0…10 000.0]
* The input will always be in the correct format.
#### Output
* For every city, you need tprint the following message: </br>
**"In {cityName} Burger Bus earned {profit} leva."**
* At the end of the tour, print:</br>
**"Burger Bus total profit: {totalProfit} leva."**
NOTE: The profit and the total profit should be formatted tthe 2nd decimal place

| Input                                                                                                                                                                             | Output                                                                                                                                                                                                                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 3</br>Sofia</br>895.67</br>213.50</br>Plovdiv</br>2563.20</br>890.26</br>Burgas</br>2360.55</br>600.00</br>                                                                       | In Sofia Burger Bus earned 682.17 leva.</br>In Plovdiv Burger Bus earned 1672.94 leva.</br>In Burgas Burger Bus earned 1460.55 leva.</br>Burger Bus total profit: 3815.66 leva.                                                                                                |
| 5</br>Lille</br>2226.00</br>1200.60</br>Rennes</br>6320.60</br>5460.20</br>Reims</br>600.20</br>452.32</br>Bordeaux</br>6925.30</br>2650.40</br>Montpellier</br>680.50</br>290.20 | In Lille Burger Bus earned 1025.40 leva.</br>In Rennes Burger Bus earned 860.40 leva.</br>In Reims Burger Bus earned -78.28 leva.</br>In Bordeaux Burger Bus earned 4274.90 leva.</br>In Montpellier Burger Bus earned 322.25 leva.</br>Burger Bus total profit: 6404.67 leva. |

</details>
<details> <summary>Code</summary>

```Python

```

</details>
</details>

> 2. Numbers

[judge]()</br>
[problem](https://github.com/Nenogzar/Academy_SoftUni/blob/main/fundamentals_python/lectures/19-21_Mid_Exam_Preparation/my_mid_exam/02_Numbers.pdf)

<details> <summary> Example & Code</summary>

####

<details><summary>Example</summary>

You are given numbers in a sequence on a single line, separated by a space. After that, you will receive commands that modify the sequence differently:

* **"Add {value}"** - you should add the given value tthe end of the sequence.
* **"Remove {value}"** - you should remove the first occurrence of the given value if there is such.
* **"Replace {value} {replacement}"** - you should replace the first occurrence of the given value with the replacement if there is such occurrence.
* **"Collapse {value}"** you must remove each number with a value less than the given one.

When you receive the command "Finish", you should print the modified sequence and end the program.

Input:
* On the first line, you will receive a sequence with numbers, separated by spaces - integers in the range [-1000…1000].
* On the following lines, you will receive commands until the "Finish" command is received.
* The commands will always be valid.

Output
* Print a single line the array of numbers separated by a space, with the modified values.

| Input                                                   | Output        |
|---------------------------------------------------------|---------------|
| 1 4 5 19</br>Add 1</br>Remove 4</br>Finish              | 1 5 19 1      |
| 1 20 -1 10</br>Collapse 8</br>Finish</br>               | 20 10         |
| 5 9 70 -56 9 9</br>Replace 9 10</br>Remove 9</br>Finish | 5 10 70 -56 9 |


</details>
<details> <summary>Code</summary>

```Python
def add_num(list_num, num):
    list_num.append(num)
    return list_num


def rem_num(list_num, num):
    if num in list_num:
        list_num.remove(num)
    return list_num


def rep_num(list_num, num, r_num):
    if num in list_num:
        index = list_num.index(num)
        list_num[index] = r_num
    return list_num


def colaps_num(list_num, upper_limit):
    filtered_list = [num for num in list_num if num >= upper_limit]
    return filtered_list


input_numbers = list(map(int, input().split(" ")))
command = input()
while command != "Finish":

    command_list = list(map(str, command.split(" ")))
    if len(command_list) == 2:
        first = int(command_list[1])
    elif len(command_list) == 3:
        first, second = int(command_list[1]), int(command_list[2])

    if command_list[0] == "Add":
        input_numbers = add_num(input_numbers, first)
    elif command_list[0] == "Remove":
        input_numbers = rem_num(input_numbers, first)
    elif command_list[0] == "Replace":
        input_numbers = rep_num(input_numbers, first, second)
    elif command_list[0] == "Collapse":
        input_numbers = colaps_num(input_numbers, first)

    command = input()

result_string = ' '.join(map(str, input_numbers))
print(result_string)
```
```Python
def add_num(list_num, num):
    list_num.append(num)
    return list_num


def rem_num(list_num, num):
    if num in list_num:
        list_num.remove(num)
    return list_num


def rep_num(list_num, num, r_num):
    if num in list_num:
        index = list_num.index(num)
        list_num[index] = r_num
    return list_num


def collapse_num(list_num, upper_limit):
    list_num = [num for num in list_num if num >= upper_limit]
    return list_num


def execute_command(command_list, input_numbers):
    if len(command_list) == 2:
        first = int(command_list[1])
    elif len(command_list) == 3:
        first, second = int(command_list[1]), int(command_list[2])

    if command_list[0] == "Add":
        return add_num(input_numbers, first)
    elif command_list[0] == "Remove":
        return rem_num(input_numbers, first)
    elif command_list[0] == "Replace":
        return rep_num(input_numbers, first, second)
    elif command_list[0] == "Collapse":
        return collapse_num(input_numbers, first)


input_numbers = list(map(int, input().split(" ")))
command = input()

while command != "Finish":
    command_list = list(map(str, command.split(" ")))
    input_numbers = execute_command(command_list, input_numbers)
    command = input()

result_string = ' '.join(map(str, input_numbers))
print(result_string)
```
```Python
sequence_of_numbers = [int(x) for x in input().split()]
 
while True:
    commands = input()
 
    if commands == "Finish":
        print(*sequence_of_numbers)
        break
 
    commands = commands.split()
    action = commands[0]
    value = int(commands[1])
    if action == "Add":
        sequence_of_numbers.append(value)
 
    elif action == "Remove":
        sequence_of_numbers.remove(value)
 
    elif action == "Replace":
        replace_value = int(commands[2])
        find_index = sequence_of_numbers.index(value)
        sequence_of_numbers.remove(value)
        sequence_of_numbers.insert(find_index, replace_value)
 
    elif action == "Collapse":
        sequence_of_numbers = [x for x in sequence_of_numbers if x >= value]
```

</details>
</details>

> 3. Deck of Cards - to solve the task

[judge]()</br>
[problem](https://github.com/Nenogzar/Academy_SoftUni/blob/main/fundamentals_python/lectures/19-21_Mid_Exam_Preparation/my_mid_exam/03_Deck_of_Cards.pdf)

<details> <summary> Example & Code</summary>

####

<details><summary>Example</summary>

You will **receive a list** of Cards on a single line **separated by ", "**. On the **next line**, you will receive a number **n**. On the next **n** lines, you will receive commands that could be:

* **"Add, {CardName}"**: 
  * Add the given card tthe card deck and print: **"Card successfully added"**
  * If it is already in the deck, print:  **"Card is already in the deck"**
* **"Remove, {CardName}"**:
  * Remove the given card from the card deck and print:  **"Card successfully removed"**
  * If it is not in the deck, print: **"Card not found"**
* **"Remove At, {index}"**:
  * Remove the card at the given index and print: **"Card successfully removed"**
  * If the index is not in the range of the list, print: **"Index out of range"**
* **"Insert, {index}, {CardName}"**:
  * Add the card at the given index and print: **"Card successfully added"**
  * If the index is out of range, print: **"Index out of range"**
  * If the index is in range, but the card is already in the deck, print: **"Card is already added"**

#### Input

* The first input line will contain the list of cards.
* The second input will be the number of commands – an integer number in the range [0…50].
* On the following input lines, you will be receiving commands.

#### Output

* After going through all the commands, you need tprint all cards on a single line separated by ", ".

| Input                                                                                                                                     | Output                                                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ace of Diamonds, Queen of Hearts, King of Clubs</br>3</br>Add, King of Diamonds</br>Insert, 2, Jack of Spades</br>Remove, Ace of Diamonds | Card successfully added</br>Card successfully added</br>Card successfully removed</br>Queen of Hearts, Jack of Spades, King of Clubs, King of Diamonds |
| Twof Clubs, King of Spades, Five of Spades, Jack of Hearts</br>2</br>Add, Twof Clubs</br>Remove, Five of Hearts                       | Card is already in the deck</br>Card not found</br>Twof Clubs, King of Spades, Five of Spades, Jack of Hearts                                        |
| Jack of Spades, Ace of Clubs, Jack of Clubs</br>2</br>Insert, -1, Queen of Spades</br>Remove At, 1                                        | Index out of range</br>Card successfully removed</br>Jack of Spades, Jack of Clubs                                                                     |
</details>

<details> <summary>Code</summary>

```Python

```

</details>
</details>
</details>

######

<details><summary> Mid-Exam-3  - Missing 2 Condition</summary>

> 01. Cooking Masterclass	

[judge]()</br>
[problem](https://github.com/Nenogzar/Academy_SoftUni/blob/main/fundamentals_python/lectures/19-21_Mid_Exam_Preparation/my_mid_exam/01_Cooking_Masterclass.pdf)

<details> <summary> Example & Code</summary>

####

<details><summary>Example</summary>

_George is starting his own course, a Cooking Masterclass. So, he asked you tbuy the needed items._</br>
The number of items depends on how many students will sign up for the course. The educational set for one student consists of 1 package of flour, 10 eggs, and an apron.</br> 
You will be given George's budget, the number of students signed, and each item's price. You should help George calculate if the budget is enough tbuy all the items or how much more money he needs.</br> 
You should know that the aprons get dirty often, sGeorge should buy 20% more, rounded up tthe next integer. Also, every fifth package of flour is free. </br>

* Input / Constraints

#### The input data will consist of:

* budget - a floating-point number in the range [0.00…1000.00]
* students - an integer in the range [0…100]
* price for a package of flour - a floating-point number in the range [0.00…100.00]
* price for a single egg - a floating-point number in the range [0.00…100.00]
* price for a single apron - a floating-point number in the range [0.00…100.00]
The input data will always be valid. There is nneed tcheck it explicitly.
#### Output
The output should be printed on the console.
* If the calculated price of the items is less or equal tthe budget:
  * "Items purchased for {the cost of the items}$."
* If the calculated price is more than the budget:
  * "{neededMoney}$ more needed."
* All prices must be formatted ttwdigits after the decimal point.

| Input                                   | Output                      |
|-----------------------------------------|-----------------------------|
| 50</br>2</br>1.0</br>0.10</br>10.0      | Items purchased for 34.00$. |
| 100</br>25</br>4.0</br>1.0</br>6.0      | 410.00$ more needed.        |
| 946</br>20</br>12.05</br>0.42</br>27.89 | 0.16$ more needed.          |

</details>
<details> <summary>Code</summary>

```Python
import math

budget = float(input())
students = int(input())
price_flour = float(input())
price_one_egg = float(input()) * 10
price_apron = float(input())

po_malk= 0
for n in range(1, students + 1):
    if n % 5 == 0:
        po_malk+= 1


total_price_flour = price_flour * (students - po_malko)
total_price_egg = price_one_egg * students
total_price_apron = price_apron * (math.ceil(students*1.2))

razhod = (total_price_flour + total_price_egg + total_price_apron)

if razhod <= budget:
    print(f"Items purchased for {razhod:.2f}$.")
else:
    print(f"{abs(budget - razhod):.2f}$ more needed.")
```

</details>
</details>

> 2. Friend List Maintenance  - Missing Condition

[judge]()</br>
[problem]()

<details> <summary> Example & Code</summary>

####

<details><summary>Example</summary>

| Input | Output |
|-------|--------|
|       |        |
|       |        |

</details>
<details> <summary>Code</summary>

```Python


```

</details>
</details>

> 3. Chat Logger  - Missing Condition

[judge]()</br>
[problem]()

<details> <summary> Example & Code</summary>

####

<details><summary>Example</summary>

| Input | Output |
|-------|--------|
|       |        |
|       |        |

</details>

<details> <summary>Code</summary>

```Python

```

</details>
</details>
</details>

####
<details><summary> Mid-Exam-4  - Missing 2 Condition </summary>

> 01. Cooking Masterclass  - Missing Condition

[judge]()</br>
[problem]()

<details> <summary> Example & Code</summary>

####

<details><summary>Example</summary>

| Input | Output |
|-------|--------|
|       |        |
|       |        |

</details>
<details> <summary>Code</summary>

```Python

```

</details>
</details>

> 2. Friend List Maintenance  - Missing Condition

[judge]()</br>
[problem]()

<details> <summary> Example & Code</summary>

####

<details><summary>Example</summary>

| Input | Output |
|-------|--------|
|       |        |
|       |        |

</details>
<details> <summary>Code</summary>

```Python


```

</details>
</details>

> 3. Chat Logger  - Missing Condition

[judge]()</br>
[problem]()

<details> <summary> Example & Code</summary>

####

<details><summary>Example</summary>

| Input | Output |
|-------|--------|
|       |        |
|       |        |

</details>

<details> <summary>Code</summary>

```Python

```

</details>
</details>
</details>

####
<details><summary> Mid-Exam-5  - Missing Condition </summary>

> 01. Experience Gaining  - Missing Condition

[judge]()</br>
[problem]()

<details> <summary> Example & Code</summary>

####

<details><summary>Example</summary>

| Input | Output |
|-------|--------|
|       |        |
|       |        |

</details>
<details> <summary>Code</summary>

```Python

```

</details>
</details>

> 2. Tax Calculator - to solve the task

[judge]()</br>
[problem](https://github.com/Nenogzar/Academy_SoftUni/blob/main/fundamentals_python/lectures/19-21_Mid_Exam_Preparation/my_mid_exam/02_Tax_Calculator.pdf)

<details> <summary> Example & Code</summary>

####

<details><summary>Example</summary>

_The National Revenue Agency hired you tcreate software, which will help them tcalculate the vehicle taxes.</br>_
You will be given a string representing vehicles that will be taxed. Each vehicle is separated by ">>", where the first element is a string representing the car type, the second element is an integer representing the years the tax should be paid, and the third element is an integer representing the kilometers traveled.</br>
There are three valid types of vehicles:</br>
* "**family**" – the initial tax for a family car is 50 euros</br>
* " **heavyDuty**" – the initial tax for a heavy-duty is 80 euros</br>
* "**sports**" – the initial tax for a sports car is 100 euros</br>
If the car is not valid print **"Invalid car type."** and continue tthe next vehicle.</br>
When calculating tax keep in mind the following rules:</br> 
* For a **family** car, the tax declines by 5 euros for every year in use. Also, the tax increases by **12 euros** for every **3000 km**. traveled. 
* For a **heavyDuty** car, the tax declines by 8 euros for every year in use. Also, the tax increases by **14 euros** for every **9000 km**. traveled.
* For a **sports** car, the tax declines by 9 euros for every year in use. Also, the tax increase by **18 euros** for every **2000 km**. Traveled.</br>

#### Input</br>
You receive a string representing the vehicles, separated with ">>": **"vehicle1>>vehicle2>>vehicle3…"**.
#### Output</br>
* Upon every successful taxed car print: "**A {car type} car will pay {total tax tpay} euros in taxes.**" Format the total tax tpay tthe second digit after the decimal point.
* On the last line, print how much the National Revenue Agency will collect: **"The National Revenue Agency will collect {total tax collected} euros in taxes."** Formatted tthe second digit after the decimal point.

| Input                                                                                   | Output                                                                                                                                                                                                                                                                                    |
|-----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| family 3 7210>>van 4</br> 2345>>heavyDuty 9 31000>>sports 4</br> 7410                   | A family car will pay 59.00 euros in taxes.</br>Invalid car type.</br>A heavyDuty car will pay 50.00 euros in taxes.</br>A sports car will pay 118.00 euros in taxes.                                                                                                                     |
| family 5 3210>>pickUp 1</br> 1345>>heavyDuty 7 21000>>sports 5 </br>9410>>family 3 9012 | A family car will pay 37.00 euros in taxes.</br>Invalid car type.</br>A heavyDuty car will pay 52.00 euros in taxes.</br>A sports car will pay 127.00 euros in taxes.</br>A family car will pay 71.00 euros in taxes.</br>The National Revenue Agency will collect 287.00 euros in taxes. |

</details>
<details> <summary>Code</summary>

```Python


```

</details>
</details>

> 3. Phone Shop  - to solve the task

[judge]()</br>
[problem](https://github.com/Nenogzar/Academy_SoftUni/blob/main/fundamentals_python/lectures/19-21_Mid_Exam_Preparation/my_mid_exam/03_Phone_Shop.pdf)

<details> <summary> Example & Code</summary>

####

<details><summary>Example</summary>

_Kevin has a phone shop. He has torder new models, but his storage is slarge that he doesn't know which phone models he has._

Write a program that will help Kevin not tbuy unnecessary phones. You will receive a list of phones separated by "**,** " (comma and space). After that, until you receive **"End"**, you will receive different commands, each on a new line. The commands are:</br>
* **"Add - {phone}"**:
  * Add the given phone tthe storage.
  * If the phone already **exists**, you should **skip** this line.
* **"Remove - {phone}"**:
  * Remove the phone from the storage **if it exists**.
  * Otherwise, ignore the command.
* **"Bonus phone - {oldPhone}:{newPhone}"**:
  * If the old phone exists, add the new phone **after** the **old one**.
  * Otherwise, ignore the command.
* **"Last - {phone}"**:
  * If the given **phone exists**, you should change its position and **put it last** in your storage.
  * Otherwise, **ignore** the command.

#### Input</br>
On the first line - list of phones separated by ", " (comma and space)</br>
On the next lines - commands until you receive "End"</br>
#### Output</br>
After receiving the "End" command, print the phones in your storage, separated by ", " (comma and space)

| Input                                                                                   | Output                            |
|-----------------------------------------------------------------------------------------|-----------------------------------|
| SamsungA50, MotorolaG5, IphoneSE</br>Add - Iphone10</br>Remove - IphoneSE</br>End       | SamsungA50, MotorolaG5, Iphone10  |
| HuaweiP20, XiaomiNote</br>Remove - Samsung</br>Bonus phone - XiaomiNote:Iphone5</br>End | HuaweiP20, XiaomiNote, Iphone5    |
| SamsungA50, MotorolaG5, HuaweiP10</br>Last - SamsungA50</br>Add - MotorolaG5</br>End    | MotorolaG5, HuaweiP10, SamsungA50 |

</details>

<details> <summary>Code</summary>

```Python

```

</details>
</details>
</details>


####
<details><summary> Mid-Exam-6  - Missing 2 Condition</summary>

> 01. The Hunting Games - Missing Condition

[judge]()</br>
[problem]()

<details> <summary> Example & Code</summary>

####

<details><summary>Example</summary>

| Input | Output |
|-------|--------|
|       |        |
|       |        |

</details>
<details> <summary>Code</summary>

```Python
days_of_the_adventure = int(input())
number_of_players = int(input())
groups_energy = float(input())
water_per_day_per_person = float(input())
food_per_day_per_person = float(input())
 
current_water = number_of_players * water_per_day_per_person * days_of_the_adventure
all_food = number_of_players * food_per_day_per_person * days_of_the_adventure
days_count_for_water = 0
days_count_for_food = 0
 
for day in range(1, days_of_the_adventure + 1):
    chopping_wood = float(input())
    groups_energy -= chopping_wood
    days_count_for_water += 1
    
    if groups_energy <= 0:
        break
 
    if days_count_for_water >= 2:
        groups_energy = (groups_energy * 0.05) + groups_energy
        current_water = current_water - (current_water * 0.3)
        days_count_for_water = 0
 
    days_count_for_food += 1
    if days_count_for_food >= 3:
        groups_energy = (groups_energy * 0.1) + groups_energy
        all_food = all_food - (all_food / number_of_players)
        days_count_for_food = 0
 
if groups_energy > 1:
    print(f"You are ready for the quest. You will be left with - {groups_energy :.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {all_food :.2f} food and {current_water :.2f} water.")
```

</details>
</details>

> 2. Space Travel	 - Missing Condition

[judge]()</br>
[problem]()

<details> <summary> Example & Code</summary>

####

<details><summary>Example</summary>

| Input | Output |
|-------|--------|
|       |        |
|       |        |

</details>
<details> <summary>Code</summary>

```Python


```

</details>
</details>

> 3. School Library	

[judge]()</br>
[problem](https://github.com/Nenogzar/Academy_SoftUni/blob/main/fundamentals_python/lectures/19-21_Mid_Exam_Preparation/my_mid_exam/03.%20School_Library.pdf)

<details> <summary> Example & Code</summary>

####

<details><summary>Example</summary>

Your task is tdan online book library.
On the first line, you will receive a string representing a shelf with books in the library. Every book is separated with "&".

On the next lines until the "Done" command, you will be receiving the commands separated with " | ":

* "Add Book | {book name}":
  * Add the book in the first place on the shelf.
  * If the book is already present on the shelf, ignore the command.
* "Take Book | {book name}":
  * Remove the book with the given name only if the book is on the shelf.
  * Otherwise, ignore this command.
* "Swap Books | {book1} | {book2}":
  * If both books are on the shelf, swap their places.
  * If at least one is missing, ignore the command.
* "Insert Book | {book name}":
  * Add the given book at the end of the shelf.
  * If the book is already present on the shelf, ignore the command.
* "Check Book | {index}":
  * Print the name of the book, which is at the given index.
  * If the index is invalid, ignore the command.

#### Input
* On the 1st line, you will receive a string representing a shelf with books in the library, separated by "&".
* On the following lines, until you receive "Done", you will be receiving commands in the format described above.
#### Output
* Print the collection of books joined by ", ":
"{firstBook}, {secondBook}, … {lastBook}"
#### Constraints
* You won't receive duplicate book names in the initial list of books.

#### Input

Don Quixote&The Great Gatsby&Moby Dick</br>
Add Book | Ulysses</br>
Take Book | Don Quixote</br>
Insert Book | Alice's Adventures in Wonderland</br>
Done

#### Output


Ulysses, The Great Gatsby, Moby Dick, Alice's Adventures in Wonderland

#### Input
Anna Karenina&Heart of Darkness&Catch-22&The Stranger</br>
Add Book | Catch-22</br>
Swap Books | Anna Karenina | Catch-22</br>
Take Book | David Copperfield</br>
Done

#### Output
Catch-22, Heart of Darkness, Anna Karenina, The Stranger

#### Input
War and Peace&Hamlet&Ulysses&Madame Bovary</br>
Check Book | 2</br>
Swap Books | Don Quixote | Ulysses</br>
Done</br>

#### Output
Ulysses</br>
War and Peace, Hamlet, Ulysses, Madame Bovary


</details>

<details> <summary>Code</summary>

```Python
shelf = input().split("&")

while True:
    command = input().split(" | ")
    action = command[0]

    if action == "Done":
        break

    elif action == "Add Book":
        book_name = command[1]
        if book_name not in shelf:
            shelf.insert(0, book_name)

    elif action == "Take Book":
        book_name = command[1]
        if book_name in shelf:
            shelf.remove(book_name)

    elif action == "Swap Books":
        book1 = command[1]
        book2 = command[2]
        if book1 in shelf and book2 in shelf:
            index1, index2 = shelf.index(book1), shelf.index(book2)
            shelf[index1], shelf[index2] = shelf[index2], shelf[index1]

    elif action == "Insert Book":
        book_name = command[1]
        if book_name not in shelf:
            shelf.append(book_name)

    elif action == "Check Book":
        index = int(command[1])
        if 0 <= index < len(shelf):
            print(shelf[index])

print(", ".join(shelf))
```
```Python
def add_book(shelf, book_name):
    if book_name not in shelf:
        shelf.insert(0, book_name)

def take_book(shelf, book_name):
    if book_name in shelf:
        shelf.remove(book_name)

def swap_books(shelf, book1, book2):
    if book1 in shelf and book2 in shelf:
        index1, index2 = shelf.index(book1), shelf.index(book2)
        shelf[index1], shelf[index2] = shelf[index2], shelf[index1]

def insert_book(shelf, book_name):
    if book_name not in shelf:
        shelf.append(book_name)

def check_book(shelf, index):
    if 0 <= index < len(shelf):
        print(shelf[index])

shelf = input().split("&")

while True:
    command = input().split(" | ")
    action = command[0]

    if action == "Done":
        break

    elif action == "Add Book":
        add_book(shelf, command[1])

    elif action == "Take Book":
        take_book(shelf, command[1])

    elif action == "Swap Books":
        swap_books(shelf, command[1], command[2])

    elif action == "Insert Book":
        insert_book(shelf, command[1])

    elif action == "Check Book":
        check_book(shelf, int(command[1]))

print(", ".join(shelf))
```


</details>
</details>
</details>

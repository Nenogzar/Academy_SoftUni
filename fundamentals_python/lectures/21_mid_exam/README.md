
<img src="https://github.com/Nenogzar/Academy_SoftUni/blob/main/fundamentals_python/image/10_1.jpg" alt="ME" width="400">


<details><summary>👈Mid-Exam-1 </summary>

> 01. The Biscuit Factory - to solve the task | [judge]() | [problem](https://github.com/Nenogzar/Academy_SoftUni/blob/main/fundamentals_python/lectures/19-21_Mid_Exam_Preparation/my_mid_exam/01_The_Biscuit_Factory.pdf)

<details> <summary>🛠️🐍 Example & Code</summary>

####

<details><summary>🛠️Example</summary>

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
 <details> <summary>🐍Code</summary>

```Python

```

</details>
</details>

> 2. Coffee Lover | [judge]()  | [problem]() |

<details> <summary>🛠️🐍 Example & Code</summary>

_John is a lover of expensive and luxurious coffees._

Create a program that helps John keep track of the coffee he has. You will receive a list of the coffees that John has in stock, on a single line separated by a single space in the following format:</br>
**"{coffee1} {coffee2} {coffee3} ... {coffeeNn}"**.
Then you will receive a number – n - a count of commands you need to execute over your list. There are four possible commands:

* **"Include {coffee}"**:
  * Add the coffee at the end of your list.
* **"Remove {first/last} {numberOfCoffees}"**:
  * Depending on the input, remove either the "**first**" or the "**last**" number of coffees from your list.
  * If you have fewer coffees in your list than the given number, skip this command.
* **"Prefer {coffeeIndex1} {coffeeIndex2}"**:
  * If both coffee indexes exist in your list, take the two coffees and change their places.
  * Otherwise, skip the command.
* **"Reverse"**:
  * Reverse the order of the coffees.

In the end, print the manipulated list in the following format:
"Coffees:
{coffee1} {coffee2} … {coffeeNn}"


#### Input / Constraints

* On the 1st line, you will receive the **starting** list with the names of the coffees separated by a " " (empty space).
* On the 2nd line, you will receive the **number** of commands - n – an integer in the range [1…100].
* On the following n lines, you will be receiving **commands** in the format described above.
#### Output
* Print the list after the manipulations in the format described above.

####

<details><summary>🛠️Example</summary>

| Input                                                                                                                                                                         | Output                                                                    |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| Arabica Liberica Charrieriana Magnistipula Robusta BulkCoffee StrongCoffee </br> 5 </br>Include TurkishCoffee</br>Remove first 2</br>Remove last 1</br>Prefer 3 1</br>Reverse | Coffees:</br>StrongCoffee Magnistipula Robusta BulkCoffe Charrieriana     |
| Arabica Robusta BulkCoffee StrongCoffee TurkishCoffee</br>5</br>Include OrdinaryCoffee</br>Remove first 1</br>Prefer 0 1</br>Prefer 3 1</br>Reverse                           | Coffees:</br>OrdinaryCoffee Robusta StrongCoffee TurkishCoffee BulkCoffee |
| Robusta StrongCoffee BulkCoffee TurkishCoffee Arabica</br>3</br>Include OrdinaryCoffee</br>Remove first 1</br>Prefer 4 1                                                      | Coffees:</br>StrongCoffee OrdinaryCoffee TurkishCoffee Arabica BulkCoffee |

</details>
 <details> <summary>🐍Code</summary>

```Python
coffee = input().split()
number_of_commands = int(input())
 
for i in range(number_of_commands):
    command = input().split()
    if command[0] == "Include":
        new_coffee = command[1]
        if new_coffee not in coffee:
            coffee.append(new_coffee)
    elif command[0] == "Remove":
        if command[1] == "first":
            command[2] = int(command[2])
            coffee = coffee[command[2]:]
        elif command[1] == "last":
            command[2] = int(command[2])
            coffee = coffee[:- command[2]]
    elif command[0] == "Prefer":
        index1 = int(command[1])
        index2 = int(command[2])
        if 0 <= index1 < len(coffee) and 0 <= index2 < len(coffee):
            coffee[index1], coffee[index2] = coffee[index2], coffee[index1]
    elif command[0] == "Reverse":
        coffee.reverse()
 
print(f"Coffees:")
print(f"{coffee}")

```

</details>
</details>

> 3. The Angry Cat  | [judge]()  | [problem]() |



<details> <summary>🛠️🐍 Example & Code</summary>

####

<details><summary>🛠️Example</summary>

_John is very angry with his owner because he left him alone during the teamwork defenses for the Programming Fundamentals Course at SoftUni. It's time for John to get his payback, and he will do it by breaking various household items._

Each item has a **price rating**, a number that describes how valuable that item is for John's owner. You will be **given an entry point** from which John will **break** the **items to his left** and **then** to **his right**. John **will never** break the item at his **entry point**.</br>
You must calculate the damage to **both** his **left** and **right**, then print **only the higher (bigger)** damage to the household. If both **sums** are **equal**, print the **left** one.</br>
#### Input / Constrains
* On the first line, you will receive the price ratings, separated by (", "). Each element will be an integer in the range [-231… 231].
* On the second line, you will receive the entry point, which will always be between the second and the penultimate element in the array.
* On the third line, you will receive the type of items John wants to break, which will be one of the following:
  * "cheap" – items that have a lower price rating than the entry point item
  * "expensive" – items that have the same price rating, or higher price rating than the entry point item
#### Output
* A single line containing the sum of price ratings and their position based on the entry point in the following format:
  * "{position} - {sum of price ratings}"
  * Positions can be "Right" or "Left"

| Input                                                      | Output    |
|------------------------------------------------------------|-----------|
| 1, 5, 1</br>1</br>cheap                                    | Left - 1  |
| 5, 10, 12, 5, 4, 20</br>3</br>cheap                        | Right - 4 |
| -2, 2, 1, 5, 9, 3, 2, -2, 1, -1, -3, 3</br>7</br>expensive | Left - 20 |

</details>

 <details> <summary>🐍Code</summary>

Bilyana Panova
```Python
def cheap_summing(side, entry_point):
    return sum([x for x in side if x < entry_point])

def expensive_summing(side, entry_point):
    return sum([x for x in side if x >= entry_point])

def main():
    price_rating = [int(x) for x in input().split(", ")]
    entry_point = int(input())
    type_of_items = input()

    left_side = price_rating[:entry_point]
    right_side = price_rating[entry_point + 1:]
    entry_point_value = price_rating[entry_point]

    if type_of_items == "cheap":
        if cheap_summing(left_side, entry_point_value) >= cheap_summing(right_side, entry_point_value):
            print(f"Left - {cheap_summing(left_side, entry_point_value)}")
        else:
            print(f"Right - {cheap_summing(right_side, entry_point_value)}")
    elif type_of_items == "expensive":
        if expensive_summing(left_side, entry_point_value) >= expensive_summing(right_side, entry_point_value):
            print(f"Left - {expensive_summing(left_side, entry_point_value)}")
        else:
            print(f"Right - {expensive_summing(right_side, entry_point_value)}")

if __name__ == "__main__":
    main()
```
Dobromir Dimitrov
```Python
def calculate_low_cost(aList, points):
    cost = 0
    for item in aList:
        if item < points:
            cost += item
    return cost

def calculate_high_cost(aList, points):
    cost = 0
    for item in aList:
        if item >= points:
            cost += item
    return cost

def main():
    priceRatings = list(map(int, input().split(", ")))
    entryPoint = int(input())
    targetType = input()
    costTarget = priceRatings[entryPoint]
    rightList = priceRatings[entryPoint + 1:]
    leftList = priceRatings[:entryPoint]
    if targetType == "cheap":
        leftDamage = calculate_low_cost(leftList, costTarget)
        rightDamage = calculate_low_cost(rightList, costTarget)
    elif targetType == "expensive":
        leftDamage = calculate_high_cost(leftList, costTarget)
        rightDamage = calculate_high_cost(rightList, costTarget)
    if leftDamage >= rightDamage:
        print(f"Left - {leftDamage}")
    else:
        print(f"Right - {rightDamage}")

if __name__ == "__main__":
    main()
```

</details>
</details>
</details>

######

<details><summary>👈Mid-Exam-2 </summary>

> 01. Burger Bus   | [judge]()  | [problem]() |- to solve the task 

<details> <summary>🛠️🐍 Example & Code</summary>

####

<details><summary>🛠️Example</summary>

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
 <details> <summary>🐍Code</summary>

```Python
def profit(earned, expense):
    return earned - expense


def special_event(expense):
    return expense * 1.5


def loss(expense):
    return expense * 0.9


city_num = int(input())
report = {}
total_profit = 0

for position in range(1, city_num + 1):
    city = input()
    owner_earned = float(input())
    owner_expense = float(input())

    if position % 3 == 0:
        current_profit = profit(owner_earned, special_event(owner_expense))
    elif position % 5 == 0:
        current_profit = profit(owner_earned, loss(owner_expense))
    else:
        current_profit = profit(owner_earned, owner_expense)

    total_profit += current_profit
    report[city] = {'earned': owner_earned, 'expense': owner_expense, 'profit': current_profit}

    # Print individual city message
    print(f"In {city} Burger Bus earned {current_profit:.2f} leva.")

# Print total profit message at the end
print(f"Burger Bus total profit: {total_profit:.2f} leva.")
```

</details>
</details>

> 2. Numbers  | [judge]()  | [problem]() |

<details> <summary>🛠️🐍 Example & Code</summary>

####

<details><summary>🛠️Example</summary>

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
 <details> <summary>🐍Code</summary>

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

> 3. Deck of Cards  | [judge]()  | [problem]() |

<details> <summary>🛠️🐍 Example & Code</summary>

####

<details><summary>🛠️Example</summary>

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

 <details> <summary>🐍Code</summary>

```Python
def add_card(list_card, card_name):
    if card_name not in list_card:
        list_card.append(card_name)
        print("Card successfully added")
    else:
        print("Card is already in the deck")


def remove_card(list_card, card_name):
    if card_name in list_card:
        list_card.remove(card_name)
        print("Card successfully removed")
    else:
        print("Card not found")


def remove_index_card(list_card, index):
    if 0 <= index < len(list_card):
        list_card.pop(index)
        print("Card successfully removed")
    else:
        print("Index out of range")


def insert_card(list_card, index, card_name):
    if abs(index) <= len(list_card):
        if card_name not in list_card:
            list_card.insert(index, card_name)
            print("Card successfully added")
        else:
            print("Card is already added")
    else:
        print("Index out of range")


cards_list = list(map(str, input().split(", ")))
manipulation_range = int(input())

for _ in range(manipulation_range):
    command = list(map(str, input().split(", ")))

    manipulation = command[0]

    if len(command) == 3:
        card_name = command[2]
        position = int(command[1])
        if manipulation == "Insert":
            insert_card(cards_list, position, card_name)
        else:
            print("Invalid command format")
    elif len(command) == 2:
        if manipulation == "Add":
            add_card(cards_list, command[1])
        elif manipulation == "Remove":
            remove_card(cards_list, command[1])
        elif manipulation == "Remove At":
            position = int(command[1])
            remove_index_card(cards_list, position)

# print(cards_list)
print(",".join(cards_list))
```

</details>
</details>
</details>

######

<details><summary>👈Mid-Exam-3  - Missing - 2. Friend List Maintenance</summary>

> 01. Cooking Masterclass	  | [judge]()  | [problem]() |

<details> <summary>🛠️🐍 Example & Code</summary>

####

<details><summary>🛠️Example</summary>

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
 <details> <summary>🐍Code</summary>

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

> 2. Friend List Maintenance   | [judge]()  | [problem]() | - Missing Condition


<details> <summary>🛠️🐍 Example & Code</summary>

####

<details><summary>🛠️Example</summary>

| Input | Output |
|-------|--------|
|       |        |
|       |        |

</details>
 <details> <summary>🐍Code</summary>

```Python


```

</details>
</details>

> 3. Chat Logger  | [judge]()  | [problem]() |


<details> <summary>🛠️🐍 Example & Code</summary>

A company hires you to create a program that implements a chat logger which works with commands. You may receive the following commands:

* **"Chat {message}"**:
  * Add the message at the last position in the chat.
* **"Delete {message}"**:
  * Delete the message if it exists.
  * Otherwise, ignore the command.
* **"Edit {message} {editedVersion}"**:
  * Update the message with the edited version.
  * If it does not exist, ignore the command.
* **"Pin {message}"**:
  * Find the given message and move it to the last index.
  * If it does not exist, ignore the command.
* **"Spam {message1} {message2} {messageN}"**:
  * Add all messages at the end of the chat.
* **"end"**:
  * Stop receiving commands.

After the "end" command, you should print the chat history starting from the first message.

#### Input

* Until you receive "end", you will be receiving commands.
* 
#### Output

* As output, you must print the chat starting from the first message. Every message must be in a new line.
* Constraints
* The command will always be valid.


####

<details><summary>🛠️Example</summary>

| Input                                                                                                | Output                                                      |
|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| Chat Hello</br>Chat darling</br>Edit darling Darling</br>Spam how are you</br>Delete Darling</br>end | Hello</br>how</br>are</br>you                               |
| Chat Hello</br>Delete John</br>Pin Hi</br>end                                                        | Hello                                                       |
| Chat John</br>Spam Let's go to the zoo</br>Edit zoo cinema</br>Chat tonight</br>Pin John</br>end     | Let's</br>go</br>to</br>the</br>cinema</br>tonight</br>John |

</details>

 <details> <summary>🐍Code</summary>

```Python
command = input().split()
 
chat = []
 
while command[0] != "end":
    word = command[1]
 
    if command[0] == "Chat":
        chat.append(word)
 
    elif command[0] == "Delete":
        if word in chat:
            chat.remove(word)
 
    elif command[0] == "Edit":
        if word in chat:
            chat.remove(word)
            command[1] = command[2]
            chat.append(command[1])
 
    elif command[0] == "Pin":
        if word in chat:
            chat.remove(word)
            chat.append(word)
            # word = chat[-1]
 
    elif command[0] == "Spam":
        chat.extend(command[1::])
 
    command = input().split()
 
print("\n".join(chat))
```

</details>
</details>
</details>



####
<details><summary>👈Mid-Exam-4  - Missing  - 01. Experience Gaining and 3. Phone Shop </summary>

> 01. Experience Gaining   | [judge]()  | [problem]() |- Missing Condition


<details> <summary>🛠️🐍 Example & Code</summary>

####

<details><summary>🛠️Example</summary>

| Input | Output |
|-------|--------|
|       |        |
|       |        |

</details>
 <details> <summary>🐍Code</summary>

```Python

```

</details>
</details>

> 2. Tax Calculator  | [judge]()  | [problem]() | - to solve the task

<details> <summary>🛠️🐍 Example & Code</summary>

####

<details><summary>🛠️Example</summary>

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
 <details> <summary>🐍Code</summary>

```Python


```

</details>
</details>

> 3. Phone Shop   | [judge]()  | [problem]() |- to solve the task

<details> <summary>🛠️🐍 Example & Code</summary>

####

<details><summary>🛠️Example</summary>

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

 <details> <summary>🐍Code</summary>

```Python

```

</details>
</details>
</details>


####
<details><summary>👈Mid-Exam-5  - Missing - 2. Space Travel</summary>

> 01. The Hunting Games  | [judge]()  | [problem]() |


<details> <summary>🛠️🐍 Example & Code</summary>

####

_A group of friends has decided to participate in a game. The first stage of the game is to gather some supplies. They have a list, and your job is to help them follow it and make the needed calculations._

Write a program that calculates the needed provisions for a quest in the woods.</br>
First, you will receive the days of the adventure, the count of the players, and the group's energy. Afterward, you will receive provisions for a day for one person:

* Water
* Food
* 
The group calculates how many supplies they'd need for the adventure and takes that much water and food.
Every day they chop wood and lose a certain amount of energy. For each of the days, you are going to receive the amount of energy lost from chopping wood. The program should end if the energy reaches 0 or less.</br>
Every second day they drink water, which boosts their energy with 5% of their current energy and at the same time drops their water supplies by 30% of their current water.</br>
Every third day they eat, which reduces their food supplies (all food they have) by the following amount:</br>
**{currentFood} / {countOfPeople}** and at the same time raises their group's energy by 10%.</br>
The chopping of wood, the drinking of water, and the eating happen in the order above.</br>
If they have enough energy to finish the quest, print the following message:</br>
**"You are ready for the quest. You will be left with - {energyLevel} energy!"**</br>
If they run out of energy, print the following message and the food and water they were left with before they ran out of energy:</br>
**"You will run out of energy. You will be left with {food} food and {water} water."**</br>

### Input / Constraints

* On the 1st line, you will receive a number N - the days of the adventure – an integer in the range [1…100].
* On the 2nd line – the number of players – an integer in the range [1 – 1000].
* On the 3rd line - the group's energy – a real number in the range [1 - 50000].
* On the 4th line – water per day for one person – a real number [0.00 – 1000.00].
* On the 5th line – food per day for one person – a real number [0.00 – 1000.00].
* On the next N lines – one for each of the days – the amount of energy loss– a real number in the range [0.00 - 1000.00].
* You will always have enough food and water.

### Output
* The final numbers should be formatted to the second digit after the decimal separator.

<details><summary>🛠️Example</summary>

| Input                                                                                                                                        | Output |
|----------------------------------------------------------------------------------------------------------------------------------------------|--------|
| 10</br>7</br>5035.5</br>11.3</br>7.2</br>942.3</br>500.57</br>520.68</br>540.87</br>505.99</br>630.3</br>784.20</br>321.21</br>456.8</br>330 |You are ready for the quest. You will be left with - 658.72 energy!|
|12</br>6</br>4430</br>9.8</br>5.5</br>620.3</br>840.2</br>960.1</br>220</br>340</br>674</br>365</br>345.5v</br>212</br>412.12</br>258 496|You will run out of energy. You will be left with 229.17 food and 118.59 water.|

</details>
 <details> <summary>🐍Code</summary>

#### Konstantin Aleksiev
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

# print(f"{int(current_water)}")
# print(f"{int(all_food)}")
```


</details>
</details>

> 2. Space Travel	  | [judge]()  | [problem]() | - Missing Condition


<details> <summary>🛠️🐍 Example & Code</summary>

####

<details><summary>🛠️Example</summary>

| Input | Output |
|-------|--------|
|       |        |
|       |        |

</details>
 <details> <summary>🐍Code</summary>

```Python


```

</details>
</details>

> 3. School Library	  | [judge]()  | [problem]() |

<details> <summary>🛠️🐍 Example & Code</summary>

####

<details><summary>🛠️Example</summary>

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

 <details> <summary>🐍Code</summary>

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

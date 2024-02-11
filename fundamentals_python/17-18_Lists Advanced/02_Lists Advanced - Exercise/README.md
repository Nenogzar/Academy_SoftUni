# Exercise: Lists Advanced

[judge](https://judge.softuni.org/Contests/1731/Lists-Advanced-Exercise) </br>
[icode-example](https://icode-example.ceo-py.eu/menu?language=Python&course=Fundamentals&module=Lists%20Advanced%20-%20Exercise) </br>
[pastebin Ivan Shopov](https://pastebin.com/4TgF7d7s) </br>

## 1. Which Are In?


<details><summary>Condition</summary>

You will be given two sequences of strings, separated by ", ". 
**Print a new list** containing only the strings from the **first input line**, 
which are **substrings** of **any string** in the **second input line**.

Example

| Input                                                       | Output                   |
|-------------------------------------------------------------|--------------------------|
| arp, live, strong</br>lively, alive, harp, sharp, armstrong | ['arp', 'live', 'strong' |
| tarp, mice, bull</br>lively, alive, harp, sharp, armstron   | [ ]                      |
   

</details>

<details> <summary>Code</summary>

```Python
list_one = input().split(", ")
list_two = input().split(", ")

result_list = list()

for n in list_one:
    for i in list_two:
        if n in i:
            result_list.append(n)
result_list = list(dict.fromkeys(result_list))
print(result_list)
```
whit function
```Python
words = input().split(", ")
check_if_words_are_in = input().split(", ")
list_with_checked_words = []


def which_are_in(string, check_strings):
    for word in string:
        for check_word in check_strings:
            if word in check_word:
                list_with_checked_words.append(word)
                break
    return list_with_checked_words


print(which_are_in(words, check_if_words_are_in))
```
solution of the task by Ivan Shopov
```Python
list_one, list_two = input().split(", "), input().split(", ")

result_list = list()
[result_list.append(n) for n in list_one for i in list_two if n in i]
result_list = list(dict.fromkeys(result_list))
print(result_list)
```

</details>

## 2. Next Version


<details><summary>Condition</summary>

You are fed up with changing the version of your software manually. Instead, you will create a little script that will make it for you.
You will be given a string representing the version of your software in the format: "{n1}.{n2}.{n3}". Your task is to print the next version. For example, if the current version is "1.3.4", the next version will be "1.3.5". 
The only rule is that the numbers cannot be greater than 9. If it happens, set the current number to 0 and increase the previous number. For more clarification, see the examples below. 
Note: there will be no case in which the first number will become greater than 9.

Example

| Input | Output |
|-------|--------|
| 1.2.3 | 1.2.4  |
| 1.3.9 | 1.4.0  |
| 3.9.9 | 4.0.0  |

</details>

<details> <summary>Code</summary>

The idea here is to turn it into an integer, add one, and turn it back into a list
```Python
version = int(input().replace('.', ''))
new_version = ".".join(str(version+1))
print(new_version)
```
The idea here is to loop by index, check for >9, add one, 
and carry the difference forward because the check starts from back to front
```Python
version = [int(digit) for digit in input().split(".")]
version[-1] += 1
for index in range(len(version) -1, 0, -1):
    if version[index] > 9:
        version[index] = 0
        version[index -1] += 1
print(".".join(str(digit) for digit in version))
```

```Python
program_version = [int(n) for n in input().split(".")]

new_version = program_version.copy()

if new_version[-1] + 1 > 9:
    new_version[1] = new_version[1] + 1
    new_version[2] = 0

else:
    new_version[2] = new_version[2] + 1

if new_version[1] + 1 > 10:
    new_version[0] = new_version[0] + 1
    new_version[1] = 0

print(f"{new_version[0]}.{new_version[1]}.{new_version[2]}")
```
</details>

## 3. Word Filter

<details><summary>Condition</summary>

Using **comprehension**, write a program that receives some **text**, separated by **space**, 
and takes only those words whose length is **even**. Print each word on a new line.

Example

| Input                    | Output                     |
|--------------------------|----------------------------|
| kiwi orange banana apple | kiwi</br>orange</br>banana |
| pizza cake pasta chips   | cake                       |

</details>

<details> <summary>Code</summary>

```Python
word_input = input().split(" ")
word_filter = [word for word in word_input if len(word) % 2 == 0]
""" print to new line whit for loop"""
# for w in word_filter:
#     print(w)
""" print to new line whit join method"""
print("\n".join(word_filter))
```
solution of the task by kumchovylcho
```Python
words = input().split()


def even_length(text):
    for word in text:
        if len(word) % 2 == 0:
            print(word)


even_length(words)
```
solution of the task by Ceo
```Python
[print(text) for text in input().split() if len(text) % 2 == 0]
```
</details>

## 4. Number Classification

<details><summary>Condition</summary>

Using a **list comprehension**, write a program that receives **numbers**, separated by comma and space **", "**, and prints all the **positive**, **negative**, **even**, and **odd** numbers on separate lines as shown below.

_Note: Zero is counted as a positive number_


Example

| Input                                     | Output                                                                                                                       |
|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| 1, -2, 0, 5, 3, 4, -100, -20, 12, 19, -33 | Positive: 1, 0, 5, 3, 4, 12, 19</br>Negative: -2, -100, -20, -33</br>Even: -2, 0, 4, -100, -20, 12</br>Odd: 1, 5, 3, 19, -33 |
| 1, 2, 53, 2, 21	                          | Positive: 1, 2, 53, 2, 21</br>Negative:</br>Even: 2, 2</br>Odd: 1, 53, 21                                                    | 
    

</details>

<details> <summary>Code</summary>

```Python
def positive_numbers(positive):
    positive_num = [pos for pos in positive if pos >= 0]
    return positive_num


def negative_numbers(negative):
    negativ_num = [neg for neg in negative if neg < 0]
    return negativ_num


def even_numbers(even):
    even_num = [ev for ev in even if ev % 2 == 0]
    return even_num


def odd_numbers(odd):
    odd_list = [od for od in odd if od % 2 != 0]
    return odd_list


def number_classification(check_list):

    print(f"Positive: {', '.join(map(str, positive_numbers(check_list)))}")
    print(f"Negative: {', '.join(map(str, negative_numbers(check_list)))}")
    print(f"Even: {', '.join(map(str, even_numbers(check_list)))}")
    print(f"Odd: {', '.join(map(str, odd_numbers(check_list)))}")


check_list = list(map(int, input().split(", ")))
number_classification(check_list)
```
```Python
def positive_numbers(list_of_numbers):
    return ", ".join([number for number in list_of_numbers if int(number) >= 0])
 
 
def negative_numbers(list_of_numbers):
    return ", ".join([number for number in list_of_numbers if int(number) < 0])
 
 
def even_numbers(list_of_numbers):
    return ", ".join([number for number in list_of_numbers if int(number) % 2 == 0])
 
 
def odd_numbers(list_of_numbers):
    return ", ".join([number for number in list_of_numbers if int(number) % 2 != 0])
 
 
numbers = input().split(", ")
print(f"Positive: {positive_numbers(numbers)}")
print(f"Negative: {negative_numbers(numbers)}")
print(f"Even: {even_numbers(numbers)}")
print(f"Odd: {odd_numbers(numbers)}")
```
```Python
number_list = [int(n) for n in input().split(", ")]

negative = [number for number in number_list if number < 0]
positive = [number for number in number_list if number >= 0]

odd = [number for number in number_list if number % 2 != 0]
even = [number for number in number_list if number % 2 == 0]

print("Positive:", end=" ")
print(*positive, sep = ", ")
print("Negative:", end=" ")
print(*negative, sep = ", ")
print("Even:", end=" ")
print(*even, sep = ", ")
print("Odd:", end=" ")
print(*odd, sep = ", ")
```

</details>

## 5. Office Chairs


<details><summary>Condition</summary>

_You are a facility manager at a large business center. One of your responsibilities is to check 
if each conference room in the center has enough chairs for the visitors._

On the first line, you will be given an integer n representing **the number of rooms** in the business center. 
On the following **n lines** for each room, you will receive information about the chairs in the room and 
the number of **visitors**. Each **chair** will be presented with the char **"X"**. 
Next, there will be a **single space** and the number of visitors at the end. 
For example: **"XXXXX 4"** (**5 chairs** and **4 visitors**). 
Keep track of the free chairs:
* If there are not enough chairs in a specific room, print the following message: "{needed_chairs_in_room} more chairs needed in room {number_of_room}". The rooms start from 1.
* Otherwise, print: "Game On, {total_free_chairs} free chairs left".


Example

| Input                                        | Output                                                             |
|----------------------------------------------|--------------------------------------------------------------------|
| 4</br>XXXX 4</br>XX 1</br>XXXXXX 3</br>XXX 3 | Game On, 4 free chairs left                                        |
| 3</br>XXXXXXX 5</br>XXXX 5</br>XXXXXX 8</br> | 1 more chairs needed in room 2</br> 2 more chairs needed in room 3 |

</details>

<details> <summary>Code</summary>

```Python
rooms_number = int(input())
free_chairs = 0

for room in range(1, rooms_number + 1):
    chairs, visitors = input().split()
    chairs = len(chairs)  # брой на столовете
    visitors = int(visitors)  # брой на посетителите
    if chairs >= visitors:
        free_chairs += (chairs - visitors)
    else:
        need_chairs = visitors - chairs
        print(f"{need_chairs} more chairs needed in room {room}")
        free_chairs += (chairs - visitors)

if free_chairs >= 0:
    print(f"Game On, {free_chairs} free chairs left")
```

```Python
number_rooms = int(input())

enough_chairs = True
chairs_left = 0


def check_chairs(chairs, people, room_floor):
    if chairs < people:
        result = people - chairs
        global enough_chairs
        enough_chairs = False
        return print(f"{result} more chairs needed in room {room_floor}")
    else:
        global chairs_left
        chairs_left += chairs - people


for room in range(1, number_rooms + 1):
    room_input, chairs = input().split()
    check_chairs(len(room_input), int(chairs), room)

if enough_chairs:
    print(f"Game On, {chairs_left} free chairs left")
```

</details>

## 6. Electron Distribution


<details><summary>Condition</summary>

_You are a mad scientist, and you have decided to play with electron distribution among atom shells. 
The basic idea of electron distribution is that electrons should fill a shell until it holds the maximum number of electrons._

You will receive a single integer - the **number of electrons**. 
our task is to **fill shells until there are no more electrons left**. 
The rules for electron distribution are as follows:

* The maximum number of electrons in a shell can be 2n**2, where n is the **position** of a shell (starting from 1). 
For example, the maximum number of electrons in the 3rd shield can be 2\*3\**2 = 18.
* You should start **filling** the shells from the **first one** at the first position.
* If the electrons are enough to **fill** the first shell, the left **unoccupied electrons** should fill the following shell and so on.

In the end, **print a list with the filled shells.**

Example

| Input | Output         |
|-------|----------------|
| 10    | [2, 8]         |
| 44    | [2, 8, 18, 16] |

</details>

<details> <summary>Code</summary>

```Python
num = int(input())
shells = []
count = 1

while num > 0:
    fill_shells = min(2 * count ** 2, num) # uses the min() function to select the smaller value between 2 * count ** 2 and num.
    shells.append(fill_shells)
    num -= fill_shells
    count += 1

print(shells)
```
solution of the task by Ivan Shopov
```Python
number_of_electrons = int(input())
shells = []
for shell in range(1, number_of_electrons + 1):
    max_electrons_in_current_shell = 2 * shell ** 2
    if number_of_electrons >= max_electrons_in_current_shell:
        shells.append(max_electrons_in_current_shell)
        number_of_electrons -= max_electrons_in_current_shell
        if number_of_electrons == 0 :
            break
    else:
        shells.append(number_of_electrons)
        break
print(shells)
```
solution of the task by Ceo
```Python
number = int(input())
new_list = []
i = 0

while 0 < number:

    i += 1
    shell = 2 * i ** 2

    if number >= shell:
        new_list.append(shell)
        number -= shell
    else:
        new_list.append(number)
        number = 0

print(new_list)
```
solution of the task by Kumchovalcho
```Python
number = int(input())
n = 1
lst = []
while number > 0:
    electron = 2*n**2
    lst.append(min(number, electron))
    number -= lst[-1]
    n += 1
```
</details>

## 7. Group of 10's


<details><summary>Condition</summary>

Write a program that receives a sequence of numbers (a string containing integers separated by ", ") 
and prints the numbers sorted into lists of 10's in the format</br> **"Group of {group}'s: {list_of_numbers}**".
Examples:</br>
* The numbers 2, 8, 4, and 10 fall into the group of 10's.</br>
* The numbers 13, 19, 14, and 15 fall into the group of 20's.</br>
For more clarification, see the examples below.

Example

| Input                            | Output                                                                                                                                   |
|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| 8, 12, 38, 3, 17, 19, 25, 35, 50 | 	Group of 10's: [8, 3]</br>Group of 20's: [12, 17, 19]</br>Group of 30's: [25]</br>Group of 40's: [38, 35]</br>Group of 50's: [50] 1.2.4 |
| 1, 3, 3, 4, 34, 35, 25, 21, 33   | Group of 10's: [1, 3, 3, 4]</br>Group of 20's: []</br>Group of 30's: [25, 21]</br>Group of 40's: [34, 35, 33]                            |

</details>

<details> <summary>Code</summary>

```Python
sequence = list(map(int, input().split(", ")))

max_sequence = max(sequence)

for group_start in range(1, max_sequence + 1, 10):
    group_end = group_start + 9
    group_numbers = [num for num in sequence if group_start <= num <= group_end]
    print(f"Group of {group_end}'s: {group_numbers}")
```
solution of the task by Ivan Shopov
```Python
numbers = [int(number) for number in input().split(", ")]
current_group = 10
while numbers:
    filtered_numbers_for_current_group = [number for number in numbers if number <= current_group]
    print(f"Group of {current_group}'s: {filtered_numbers_for_current_group}")
    current_group += 10
    numbers = [number for number in numbers if number not in filtered_numbers_for_current_group]
```
solution of the task by Ceo
```Python
number_list = [int(n) for n in input().split(", ")]

for n in range(1, 11):
    check_list = list()
    if len(number_list) != 0:
        [check_list.append(i) for i in number_list if i <= (n * 10)]
        [number_list.remove(o) for o in check_list]
        print(f"Group of {n * 10}'s: {check_list}")

```
solution of the task by Taner
```Python
numbers = [int(n) for n in input().split(", ")]
check_numbers = list()

for number in range(1, 10 + 1):
    check_numbers.clear()
    if len(numbers) != 0:
        for num in numbers:
            if int(num) <= number * 10:
                check_numbers.append(num)
        for d in check_numbers:
            numbers.remove(d)

        print(f"Group of {number * 10}'s: {check_numbers}")
```

</details>

## 8. Decipher This!


<details><summary>Condition</summary>

You are given a **secret message** you should **decipher**. 
To do that, you need to know that **in each word**:
* the second and the **last letter** are **switched** (e.g., Holle means Hello)
* the first letter is **replaced** by its **character code** (e.g., 72 means H)

Example

| Input               | Output         |
|---------------------|----------------|
| 72olle 103doo 100ya | Hello good day |
| 82yade 115te 103o   | Ready set go   |

    

</details>

<details> <summary>Code</summary>

```Python
message = input().split()
words, numbers = [], []

# Обхождаме всяка дума във входните данни
for word in message:
    # Инициализираме празни низове за числата и буквите
    num, let = "", ""

    for symbol in word:
        # Проверяваме дали символът е цифра или буква
        if symbol.isdigit():
            # Ако е цифра, добавяме я към низа за числата
            num += symbol
        else:
            # Ако е буква, добавяме я към низа за буквите
            let += symbol

    # Конвертираме числата в цяло число и ги добавяме към списъка с числата
    numbers.append(int(num))

    # Проверяваме дължината на низа за буквите и го променяме, ако не е с дължина 1
    if len(let) != 1:
        let = f"{let[-1]}{let[1:-1]}{let[0]}"

    # Добавяме променения низ за буквите към списъка с думите
    words.append(let)

# Обхождаме списъците с числа и думи паралелно и генерираме изхода
for numer, word in zip(numbers, words):
    print(f"{chr(numer)}{word}", end=" ")
```
solution of the task by Ceo
```Python
message = input().split()

words = []
for word in message:
    num, let = "", ""
    for symbol in word:
        if symbol.isdigit():
            num += symbol
        else:
            let += symbol
    if len(let) != 1:
        let = f"{let[-1]}{let[1:-1]}{let[0]}"
    words.append(f"{chr(int(num))}{let}")

print(*words, end=' ')
```
solution of the task by kumchovalcho
```Python
words = input().split()
result = []

for word in words:
    cur_word = list(word)

    char_code = []
    while cur_word[0].isdigit():
        char_code.append(cur_word.pop(0))

    cur_word.insert(0, chr(int("".join(char_code))))
    cur_word[1], cur_word[-1] = cur_word[-1], cur_word[1]

    result.append("".join(cur_word))

print(" ".join(result))
```

</details>


## 8. ** Feed the Animals


<details><summary>Condition</summary>



The sanctuary needs to provide food for the animals and feed them, so your task is to help with the process

Create a program that organizes the daily feeding of animals. You need to keep information about animals, their daily food limit and the areas of the Wildlife Refuge they live in. You will be receiving lines with commands until you receive the "Last Info" message. There are two possible commands:

* "Add:{animalName}:{dailyFoodLimit}:{area}":

  * Add the animal and its daily food limit to your records. It is guaranteed that the names of the animals are unique and there will never be animals with the same name. If it already exists, just increase the value of the daily food limit with the current one that is given.

* "Feed:{animalName}:{food}:{area}":

  * Check if the animal exists and if it does, reduce its daily food limit with the given food for feeding. If its limit reaches 0 or less, the animal is considered successfully fed and you need to remove it from your records and print the following message:

    * **"{animalName} was successfully fed"**

You need to know the count of hungry animals there are left in each area in the end. If an animal has daily food limit above 0, it is considered hungry.
In the end, you have to print each animal with its daily food limit sorted in descending order by the daily food limit and then by its name in ascending order in the following format:

**Animals:**</br>
**{animalName} -> {dailyFoodLimit}g**</br>
**{animalName} -> {dailyFoodLimit}g**

Afterwards, print the areas with the count of animals, which are not fed in descending order by the count of animals. If an area has 0 hungry animals in it, don't print it. The output must be in the following format:

**Areas with hungry animals:**</br>
**{areaName} : {countOfUnfedAnimals}**</br>

**{areaName} : {countOfUnfedAnimals}**</br>

### Input / Constraints

* You will be receiving lines until you receive the "Last Info" command.
* The food comes in grams and is an integer number in the range [1...100000].
* The input will always be valid.
* There will never be a case, in which an animal is in two or more areas at the same time.

### Output

* Print the appropriate message after the "Feed" command, if an animal is fed.
* Print the animals with their daily food limit in the format described above.
* Print the areas with the count of unfed animals in them in the format described above.

Example

| Input | Output |
|-------|--------|
|  Add:Maya:7600:WaterfallArea</br>Add:Bobbie:6570:DeepWoodsArea</br>Add:Adam:4500:ByTheCreek</br>Add:Jamie:1290:RiverArea</br>Add:Gem:8730:WaterfallArea</br>Add:Maya:1230:WaterfallArea</br>Add:Jamie:560:RiverArea</br>Feed:Bobbie:6300:DeepWoodsArea</br>Feed:Adam:4650:ByTheCreek</br>Feed:Jamie:2000:RiverArea</br>Last Info|Adam was successfully fed</br>Jamie was successfully fed</br>Animals:</br>Maya -> 8830g</br>Gem -> 8730g</br>Bobbie -> 270g</br>Areas with hungry animals:</br>WaterfallArea : 2</br>DeepWoodsArea : 1|
|Add:Bonie:3490:RiverArea</br>Add:Sam:5430:DeepWoodsArea</br>Add:Bonie:200:RiverArea</br>Add:Maya:4560:ByTheCreek</br>Feed:Maya:2390:ByTheCreek</br>Feed:Bonie:3500:RiverArea</br>Feed:Johny:3400:WaterFall</br>Feed:Sam:5500:DeepWoodsArea</br>Last Info|Sam was succesfully fed</br>Animals:</br>Maya -> 2170g</br>Bonie -> 190g</br>Areas with hungry animals:</br>RiverArea : 1</br>ByTheCreek : 1|


</details>

<details> <summary>Code</summary>

```Python
command_names_food_area = input().split(":")
animals = []
daily_feed = []
area = []
while command_names_food_area[0] != "Last Info":
    if command_names_food_area[0] == "Add":
        if command_names_food_area[1] in animals:
            index = animals.index(command_names_food_area[1])
            daily_feed[index] += int(command_names_food_area[2])
        else:
            animals.append(command_names_food_area[1])
            daily_feed.append(int(command_names_food_area[2]))
            area.append(command_names_food_area[3])
    elif command_names_food_area[0] == "Feed":
        animal_index = animals.index(command_names_food_area[1])
        feed = int(command_names_food_area[2])
        daily_feed[animal_index] -= feed
        if daily_feed[animal_index] <= 0:
            print(f'{animals[animal_index]} was successfully fed')
            animals.pop(animal_index)
            daily_feed.pop(animal_index)
            area.pop(animal_index)
    command_names_food_area = input().split(":")
print("Animals:")
food_need_sorted = {}
for index, value in enumerate(daily_feed):
    if value in food_need_sorted:
        food_need_sorted[value] += [animals[index]]
    else:
        food_need_sorted[value] = [animals[index]]
if len(food_need_sorted) != 0:
    for index in sorted(food_need_sorted.keys(), reverse=True):
        for i in sorted(food_need_sorted[index]):
            print(f'{i} -> {index}g')
still_hungry_area = {}
for value in area:
    if value in still_hungry_area:
        still_hungry_area[value] += 1
    else:
        still_hungry_area[value] = 1
still_hungry_area = sorted(still_hungry_area.items(), key=lambda x: x[1], reverse=True)
print('Areas with hungry animals:')
if len(still_hungry_area) != 0:
    for value in still_hungry_area:
        print(f'{value[0]} : {value[1]}')
```

```Python
def add_animal(command, animals, daily_feed, area):
    if command[1] in animals:
        index = animals.index(command[1])
        daily_feed[index] += int(command[2])
    else:
        animals.append(command[1])
        daily_feed.append(int(command[2]))
        area.append(command[3])

def feed_animal(command, animals, daily_feed, area):
    animal_index = animals.index(command[1])
    feed = int(command[2])
    daily_feed[animal_index] -= feed
    if daily_feed[animal_index] <= 0:
        print(f'{animals[animal_index]} was successfully fed')
        animals.pop(animal_index)
        daily_feed.pop(animal_index)
        area.pop(animal_index)

def print_animals(animals, daily_feed):
    print("Animals:")
    food_need_sorted = {}
    for index, value in enumerate(daily_feed):
        if value in food_need_sorted:
            food_need_sorted[value] += [animals[index]]
        else:
            food_need_sorted[value] = [animals[index]]
    if len(food_need_sorted) != 0:
        for index in sorted(food_need_sorted.keys(), reverse=True):
            for i in sorted(food_need_sorted[index]):
                print(f'{i} -> {index}g')

def print_hungry_areas(area):
    still_hungry_area = {}
    for value in area:
        if value in still_hungry_area:
            still_hungry_area[value] += 1
        else:
            still_hungry_area[value] = 1
    still_hungry_area = sorted(still_hungry_area.items(), key=lambda x: x[1], reverse=True)
    print('Areas with hungry animals:')
    if len(still_hungry_area) != 0:
        for value in still_hungry_area:
            print(f'{value[0]} : {value[1]}')

def main():
    animals = []
    daily_feed = []
    area = []
    
    command_names_food_area = input().split(":")
    while command_names_food_area[0] != "Last Info":
        if command_names_food_area[0] == "Add":
            add_animal(command_names_food_area, animals, daily_feed, area)
        elif command_names_food_area[0] == "Feed":
            feed_animal(command_names_food_area, animals, daily_feed, area)
        command_names_food_area = input().split(":")
    
    print_animals(animals, daily_feed)
    print_hungry_areas(area)

if __name__ == "__main__":
    main()

```

```Python
```

</details>



## 9. *Anonymous Threat


<details><summary>Condition</summary>

Anonymous has created a hyper cyber virus, which steals data from the CIA. The virus is known for its innovative and unbelievably clever merging and dividing data into partitions. As the lead security developer in the CIA, you have been tasked to analyze the software of the virus and observe its actions on the data. 
You will receive a single input line containing strings, separated by spaces. The strings may contain any ASCII character except whitespace. Then you will begin receiving commands in one of the following formats:

* merge {startIndex} {endIndex}
* divide {index} {partitions}

Every time you receive the merge command, you must merge all elements from the startIndex to the endIndex. In other words, you should concatenate them. 

**Example: {abc, def, ghi} -> merge 0 1 -> {abcdef, ghi}**

If any of the given indexes is out of the array, you must take only the range that is inside the array and merge it.
Every time you receive the divide command, you must divide the element at the given index into several small substrings with equal length. The count of the substrings should be equal to the given partitions. 

**Example: {abcdef, ghi, jkl} -> divide 0 3 -> {ab, cd, ef, ghi, jkl}**

If the string cannot be exactly divided into the given partitions, make all partitions except the last with equal lengths and make the last one - the longest. 

**Example: {abcd, efgh, ijkl} -> divide 0 3 -> {a, b, cd, efgh, ijkl}**

The input ends when you receive the command "3:1". At that point, you must print the resulting elements, joined by a space.

Input

* The first input line will contain the array of data.
* On the next several input lines, you will receive commands in the format specified above.
* The input ends when you receive the command "3:1".

Output

* As output, you must print a single line containing the elements of the array, joined by a space.



Example

| Input                                                                       | Output                             |
|-----------------------------------------------------------------------------|------------------------------------|
| Ivo Johny Tony Bony Mony</br>merge 0 3</br>merge 3 4</br>merge 0 3</br>3:1  | IvoJohnyTonyBonyMony               |
| abcd efgh ijkl mnop qrst uvwx yz</br>merge 4 10</br>divide 4 5</br>3:1</br> | abcd efgh ijkl mnop qr st uv wx yz |

    

</details>

<details> <summary>Code</summary>

```Python
main_string = input().split()
commands = input()

while commands != "3:1":
    command, start_index, end_index = [int(x) if x[-1].isdigit() else x for x in commands.split()]
    
    if command == "merge":
        if start_index < 0:
            start_index = 0
        if start_index < end_index:
            how_long = len(main_string)
            if end_index >= how_long:
                end_index = how_long - 1
            for num in range(start_index, end_index):
                main_string[start_index] += f"{main_string.pop(start_index + 1)}"
    
    elif command == "divide":
        index_ = start_index
        partitions = end_index
        if 0 <= index_ < len(main_string):
            how_long = len(main_string[index_])
            space_between = how_long // partitions
            string_to_change = main_string.pop(index_)
            result_ = []
            for x in range(partitions - 1):
                result_.append(string_to_change[:space_between])
                string_to_change = string_to_change[space_between:]
            result_.append(string_to_change)
            for x in result_[::-1]:
                main_string.insert(index_, x)
    
    commands = input()

print(" ".join(main_string))
```
solution of the task by Ceo
```Python
words = input().split()


def merge(start_index, end_index, words):
    current_merge = []
    all_in_one_string = ""
    if start_index < 0:
        start_index = 0
    elif start_index > len(words):
        start_index = len(words) - 2
    if end_index > len(words):
        end_index = len(words) - 1
    current_merge += words[start_index:end_index + 1]
    for word in current_merge:
        all_in_one_string += word
    del words[start_index:end_index + 1]
    words.insert(start_index, all_in_one_string)


def divide(divide_index, how_many_pieces, words):
    how_long = len(words[divide_index])
    space_between = how_long // how_many_pieces
    string_to_change = words.pop(divide_index)
    result_ = []
    for x in range(how_many_pieces - 1):
        result_.append(string_to_change[:space_between])
        string_to_change = string_to_change[space_between:]
    result_.append(string_to_change)
    for x in result_[::-1]:
        words.insert(divide_index, x)


command = input()
while command != "3:1":
    command = command.split()
    operation = command[0]
    if operation == "merge":
        merge(int(command[1]), int(command[2]), words)
    elif operation == "divide":
        divide(int(command[1]), int(command[2]), words)
    command = input()

print(*words)
```
solution of the task by Bilyana Panova 
```Python
def valid_index(start, end):
    if start < 0:
        start = 0
    if end >= len(strings):
        end = len(strings) - 1
    return start, end


strings = input().split()
commands = input()
while commands != "3:1":
    command = commands.split()
    if command[0] == "merge":
        start_index, end_index = valid_index(int(command[1]), int(command[2]))
        strings[start_index:end_index + 1] = ["".join(strings[start_index:end_index + 1])]
    elif command[0] == "divide":
        index, partitions = int(command[1]), int(command[2])
        cut_part = len(strings[index]) // partitions
        text = strings.pop(index)
        counter = 1
        while True:
            if counter < partitions:
                strings.insert(index, text[:cut_part])
                text = (text[cut_part:])

            else:
                strings.insert(index, text)
                break
            index += 1
            counter += 1
    commands = input()
else:
    print(" ".join(strings))
```

</details>


## 10. *Pokemon Don't Go


<details><summary>Condition</summary>

_Ely likes to play Pokemon Go a lot. But Pokemon Go bankrupted… So the developers made Pokemon Don't Go out of depression. 
And so Ely now plays Pokemon Don't Go. In Pokemon Don't Go, when you walk to a certain pokemon, 
those closest to you naturally get further, and those further from you, get closer._

You will receive a **sequence of integers**, separated by **spaces** - the distances to the pokemon. 
Then you will begin **receiving integers**, which will **correspond** to **indexes** in **that sequence**.

When you **receive** an **index**, you must **remove** the **element** at that index from the **sequence** (as if you've captured the pokemon).
* You must **increase** the **value of all elements** in the sequence that are **less** or **equal** to the removed element with the value of the removed element.
* You must **decrease** the **value of all elements** in the sequence that are **greater** than the removed element with the value of the removed element.
If the **given index is less than 0, remove the first element of the sequence**, and **copy** the last element to its place.
If the **given index is greater than the last index of the sequence**, _remove the last element from the sequence,_ and **copy the first element to its place**.

The **increasing** and **decreasing** elements should also be done in these cases. The **element** whose value you should use is the removed element.
The program ends when the sequence has no elements (there are no pokemon left for Ely to catch).

Input
* On the **first line** of input, you will receive a **sequence of integers, separated by spaces**.
* On the **next several** lines, you will receive **integers** - the **indexes**.

Output
* When the program ends, you must print the **summed value** of **all removed elements**.

Constraints
* •	The input data will consist **only** of **valid integers** in **the range [-2.147.483.648…2.147.483.647]**.


Example

| Input                                                | Output |
|------------------------------------------------------|--------|
| 4 5 3</br>1</br>1</br>0                              | 14     |
| 5 10 6 3 5</br>2</br>4</br>1</br>1</br>3</br>0</br>0 | 51     |
    

</details>

<details> <summary>Code</summary>

```Python
pokemons = [int(n) for n in input().split()]
sum_of_captures_pokemons = []


def capture_pokemons(index, pokemons):
    first_element = int(pokemons[0])
    last_element = int(pokemons[-1])
    if index < 0:
        sum_of_captures_pokemons.append(first_element)  # appends the first element
        del pokemons[0]                     # deletes element at current_index 0
        pokemons.insert(0, last_element)    # puts last element to current_index 0

    elif index > len(pokemons) - 1:
        sum_of_captures_pokemons.append(last_element)  # appends the last element
        del pokemons[-1]                    # deletes element at current_index -1
        pokemons.insert(len(pokemons), first_element)  # puts first element at current_index -1

    if 0 <= index < len(pokemons):
        if index == len(pokemons):
            sum_of_captures_pokemons.append(pokemons[index - 1])
            del pokemons[index - 1]
        else:
            sum_of_captures_pokemons.append(pokemons[index])
            del pokemons[index]

    for counter, number in enumerate(pokemons):
        if number <= sum_of_captures_pokemons[-1]:
            pokemons[counter] = number + sum_of_captures_pokemons[-1]
        elif number > sum_of_captures_pokemons[-1]:
            pokemons[counter] = number - sum_of_captures_pokemons[-1]


while len(pokemons) > 0:
    current_position = int(input())
    capture_pokemons(current_position, pokemons)

print(sum(sum_of_captures_pokemons))
```
solution of the task by Ivan Shopov
```Python
distance = [int(number) for number in input().split()]
sum_of_removed_elements = 0
while distance: # while len(distance) > 0
    index = int(input())
    removed_element = 0
    if index < 0:
        removed_element = distance[0]
        distance[0] = distance[-1]
    elif index >= len(distance):
        removed_element = distance[-1]
        distance[-1] = distance[0]
    else:  # Index is valid
        removed_element = distance.pop(index)
    sum_of_removed_elements += removed_element
    for manipulating_index in range(len(distance)):
        if distance[manipulating_index] <= removed_element:
            distance[manipulating_index] += removed_element
        else:  # distance_list[manipulating_index] > removed_element
            distance[manipulating_index] -= removed_element
print(sum_of_removed_elements)
```
solution of the task by Ceo
```Python
distance_to_pokemon = [int(x) for x in input().split()]

result_ = []


while distance_to_pokemon:
    index_ = int(input())
    captured_pokemon = ""
    if index_ < 0:
        captured_pokemon = distance_to_pokemon.pop(0)
        distance_to_pokemon.insert(0, distance_to_pokemon[-1])
    elif index_ >= len(distance_to_pokemon):
        captured_pokemon = distance_to_pokemon.pop(-1)
        distance_to_pokemon.append(distance_to_pokemon[0])
    if not captured_pokemon:
        captured_pokemon = distance_to_pokemon.pop(index_)
    result_.append(captured_pokemon)
    for pos, pokemon in enumerate(distance_to_pokemon):
        if pokemon <= captured_pokemon:
            distance_to_pokemon[pos] += captured_pokemon
        else:
            distance_to_pokemon[pos] -= captured_pokemon

print(sum(result_))
```
</details>

##  11. *SoftUni Course Planning


<details><summary>Condition</summary>

Help plan the next Programming Fundamentals course by keeping track of the lessons that will be included in the course and all the exercises for the lessons. 
Before the course starts, there are some changes to be made. 
On the first input line, you will receive the initial schedule of lessons and exercises that will be part of the next course, separated by a comma and a space ", ". 
Until you receive the "course start" command, you will be given some commands to modify the course schedule. 

The possible commands are:
* "**Add:{lessonTitle}" - add the lesson to the end** of the schedule if it does not exist.
* "**Insert:{lessonTitle}:{index}" - insert the lesson to the given inde**x, if it does not exist.
* "**Remove:{lessonTitle}" - remove the lesson**, if it exists.
* "**Swap:{lessonTitle}:{lessonTitle}" - swap the position** of the two lessons if they exist.
* "**Exercise:{lessonTitle}" - add Exercise in the schedule right after the lesson index**, if the lesson exists and there is no exercise already, in the following format "{lessonTitle}-Exercise". 
 
If the lesson doesn't exist, add the lesson at the end of the course schedule, followed by the Exercise.
 
**Note: Each time you Swap or Remove a lesson, you should do the same with the Exercises, if there are any following the lessons.**


Example

| Input | Output |
|-------|--------|
| Data Types, Objects, Lists</br>Add:Databases</br>Insert:Arrays:0</br>Remove:Lists</br>course start | 1.Arrays</br>2.Data Types</br>3.Objects</br>4.Databases</br>|
| Arrays, Lists, Methods</br>Swap:Arrays:Methods</br>Exercise:Databases</br>Swap:Lists:Databases</br>Insert:Arrays:0</br>course start</br>|1.Methods</br>2.Databases</br>3.Databases-Exercise</br>4.Arrays</br>5.Lists|
    

</details>

<details> <summary>Code</summary>

```Python
input_schedule = input().split(", ")
new_schedule = input_schedule.copy()

command = input()
while command != "course start":
    command = command.split(":")
    operation = command[0]
    lesson_title = command[1]
    
    if operation == "Add":
        if lesson_title not in new_schedule:
            new_schedule.append(lesson_title)
    elif operation == "Insert":
        index = int(command[2])
        if lesson_title not in new_schedule:
            new_schedule.insert(index, lesson_title)
    elif operation == "Remove":
        if lesson_title in new_schedule:
            new_schedule.remove(lesson_title)
            if f"{lesson_title}-Exercise" in new_schedule:
                new_schedule.remove(f"{lesson_title}-Exercise")
    elif operation == "Swap":
        lesson_title_2 = command[2]
        if lesson_title in new_schedule and lesson_title_2 in new_schedule:
            first_lesson = new_schedule.index(lesson_title)
            second_lesson = new_schedule.index(lesson_title_2)
            new_schedule[first_lesson], new_schedule[second_lesson] = new_schedule[second_lesson], new_schedule[first_lesson]
            
            if f"{lesson_title_2}-Exercise" in new_schedule:
                index_of_lesson_2 = new_schedule.index(lesson_title_2) + 1
                new_schedule.insert(index_of_lesson_2, f"{lesson_title_2}-Exercise")
                new_schedule.pop(new_schedule.index(f"{lesson_title_2}-Exercise", new_schedule.index(f"{lesson_title_2}-Exercise") + 1))
            
            if f"{lesson_title}-Exercise" in new_schedule:
                index_of_lesson_1 = new_schedule.index(lesson_title) + 1
                new_schedule.insert(index_of_lesson_1, f"{lesson_title}-Exercise")
                new_schedule.pop(new_schedule.index(f"{lesson_title}-Exercise", new_schedule.index(f"{lesson_title}-Exercise") + 1))
    elif operation == "Exercise":
        if lesson_title in new_schedule:
            if f"{lesson_title}-Exercise" not in new_schedule:
                current_lesson_index = new_schedule.index(lesson_title) + 1
                new_schedule.insert(current_lesson_index, f"{lesson_title}-Exercise")
        elif lesson_title not in new_schedule:
            new_schedule.append(lesson_title)
            new_schedule.append(f"{lesson_title}-Exercise")
    
    command = input()

for count, lesson in enumerate(new_schedule, 1):
    print(f"{count}.{lesson}")
```
same with Function
```Python
input_schedule = input().split(", ")
new_schedule = input_schedule.copy()


def add(lesson_tittle):
    if lesson_tittle not in new_schedule:
        new_schedule.append(lesson_tittle)


def insert(lesson_tittle, index_to_position):
    if lesson_tittle not in new_schedule:
        new_schedule.insert(index_to_position, lesson_tittle)


def remove(lesson_tittle):
    if lesson_tittle in new_schedule:
        new_schedule.remove(lesson_tittle)
    if f"{lesson_tittle}-Exercise" in new_schedule:
        new_schedule.remove(f"{lesson_tittle}-Exercise")


def swap(lesson_1, lesson_2):
    if lesson_1 in new_schedule and lesson_2 in new_schedule:
        first_lesson = new_schedule.index(lesson_1)
        second_lesson = new_schedule.index(lesson_2)
        new_schedule[first_lesson], new_schedule[second_lesson] = new_schedule[second_lesson], new_schedule[
            first_lesson]
        if lesson_2 and f"{lesson_2}-Exercise" in new_schedule:
            index_of_lesson_2 = new_schedule.index(lesson_2) + 1
            new_schedule.insert(index_of_lesson_2, f"{lesson_2}-Exercise")
            new_schedule.pop(new_schedule.index(f"{lesson_2}-Exercise", new_schedule.index(f"{lesson_2}-Exercise") + 1))
        if lesson_1 and f"{lesson_1}-Exercise" in new_schedule:
            index_of_lesson_1 = new_schedule.index(lesson_1) + 1
            new_schedule.insert(index_of_lesson_1, f"{lesson_1}-Exercise")
            new_schedule.pop(new_schedule.index(f"{lesson_1}-Exercise", new_schedule.index(f"{lesson_1}-Exercise") + 1))


def exercise(lesson_title):
    if lesson_title in new_schedule:
        if f"{lesson_title}-Exercise" not in new_schedule:
            current_lesson_index = new_schedule.index(lesson_title) + 1
            new_schedule.insert(current_lesson_index, f"{lesson_title}-Exercise")
    elif lesson_title not in new_schedule:
        new_schedule.append(lesson_title)
        new_schedule.append(f"{lesson_title}-Exercise")


command = input()
while command != "course start":
    command = command.split(":")
    operation = command[0]
    lesson_title = command[1]
    if operation == "Add":
        add(lesson_title)
    elif operation == "Insert":
        index = int(command[2])
        insert(lesson_title, index)
    elif operation == "Remove":
        remove(lesson_title)
    elif operation == "Swap":
        lesson_title_1 = command[1]
        lesson_title_2 = command[2]
        swap(lesson_title_1, lesson_title_2)
    elif operation == "Exercise":
        exercise(lesson_title)
    command = input()

for count, lesson in enumerate(new_schedule, 1):
    print(f"{count}.{lesson}")
```
solution of the task by Ceo
```Python
schedule_of_lessons = input().split(", ")


def check_for_exercise(find_index: int) -> bool:
    try:
        return "Exercise" in schedule_of_lessons[find_index + 1]
    except IndexError:
        return


def add_lesson(lesson_title: str) -> None:
    if lesson_title not in schedule_of_lessons:
        schedule_of_lessons.append(lesson_title)


def insert_lesson(lesson_title: str, index: int) -> None:
    if lesson_title not in schedule_of_lessons:
        schedule_of_lessons.insert(index, lesson_title)


def remove_lesson(lesson_title: str) -> None:
    if lesson_title in schedule_of_lessons:
        find_index = schedule_of_lessons.index(lesson_title)
        if check_for_exercise(find_index):
            del schedule_of_lessons[find_index]
        del schedule_of_lessons[find_index]


def swap_lesson(lesson_title: str, lesson_title_swap: str) -> None:
    if lesson_title in schedule_of_lessons and lesson_title_swap in schedule_of_lessons:
        index_lesson_one = schedule_of_lessons.index(lesson_title)
        index_lesson_two = schedule_of_lessons.index(lesson_title_swap)
        schedule_of_lessons[index_lesson_one], schedule_of_lessons[index_lesson_two] = \
            schedule_of_lessons[index_lesson_two], schedule_of_lessons[index_lesson_one]
        if check_for_exercise(index_lesson_one):
            schedule_of_lessons.insert(index_lesson_two + 1, schedule_of_lessons.pop(index_lesson_one + 1))
        if check_for_exercise(index_lesson_two):
            schedule_of_lessons.insert(index_lesson_one + 1, schedule_of_lessons.pop(index_lesson_two + 1))


def exercise_lesson(lesson_title: str) -> bool:
    if lesson_title in schedule_of_lessons:
        find_index = schedule_of_lessons.index(lesson_title)
        if not check_for_exercise(find_index):
            schedule_of_lessons.insert(find_index + 1, f"{lesson_title}-Exercise")
    elif lesson_title not in schedule_of_lessons:
        schedule_of_lessons.append(lesson_title)
        schedule_of_lessons.append(f"{lesson_title}-Exercise")


commands = {
    "Add": add_lesson,
    "Insert": insert_lesson,
    "Remove": remove_lesson,
    "Swap": swap_lesson,
    "Exercise": exercise_lesson
}

command = input()

while command != "course start":
    command_type, *info = [int(x) if x.isdigit() else x for x in command.split(":")]
    commands[command_type](*info)
    command = input()

for pos, lesson in enumerate(schedule_of_lessons, 1):
    print(f"{pos}.{lesson}")
```



</details>
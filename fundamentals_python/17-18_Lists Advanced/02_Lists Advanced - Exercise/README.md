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
</details>


## 10. *Pokemon Don't Go


<details><summary>Condition</summary>

Example

| Input | Output |
|-------|--------|
| 1.2.3 | 1.2.4  |
| 1.3.9 | 1.4.0  |
| 3.9.9 | 4.0.0  |
    

</details>

<details> <summary>Code</summary>

```Python
 

```
</details>

##  11. *SoftUni Course Planning


<details><summary>Condition</summary>

Example

| Input | Output |
|-------|--------|
| 1.2.3 | 1.2.4  |
| 1.3.9 | 1.4.0  |
| 3.9.9 | 4.0.0  |
    

</details>

<details> <summary>Code</summary>

```Python
 

```
</details>
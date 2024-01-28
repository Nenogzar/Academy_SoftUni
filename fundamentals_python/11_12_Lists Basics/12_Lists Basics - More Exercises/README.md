# List Basic - More Exercise

[judge](https://judge.softuni.org/Contests/1726)</br>

[Code from kumchovylcho](https://github.com/kumchovylcho/softuni/tree/master/Fundamentals%20-%20Python/Lists_Basics%20-%20more%20exercises)</br>

[Code from CEO](https://icode-example.ceo-py.eu/menu?language=Python&course=Fundamentals&module=Lists%20Basics%20-%20More%20Exercises)</br>


## 1.	Zeros to Back</br>
Write a program that receives a **single string (integers separated by a comma and space ", ")**, **finds all the zeros**, 
and **moves them to the back** without messing up the other elements. **Print** the resulting **integer list**.

### Example

| Input | Output |
|-------|--------|
|1, 0, 1, 2, 0, 1, 3|[1, 1, 2, 1, 3, 0, 0]|
|0, 5, 0, 4, 0, 0, 5|[5, 4, 5, 0, 0, 0, 0]|

### Code
```Python
list_input = input().split(", ")
new_list = []

for num in list_input:
    num_int = int(num)
    if num_int == 0:
        new_list.append(num_int)

list_input = [int(num) for num in list_input if int(num) != 0]
list_input.extend(new_list)

print(list_input)
```
#### or 
```Python
number_list, zero_list, event_list = [], [], input()

for num in event_list.split(", "):
    number = int(num)
    if number == 0:
        zero_list.append(number)
    else:
        number_list.append(number)
output_list = number_list + zero_list
print(output_list)
```
#### or  From CEO
```Python
numbers = list(map(int, input().strip().split(", ")))

for _ in numbers:
    numbers.append(numbers.pop(numbers.index(0)))
print(numbers)
```
#### or  from Taner
```Python
numbers_with_zeros = [int(number) for number in input().split(", ")]

finding_the_zeros = [number for number in numbers_with_zeros if number == 0]
numbers_without_zeros = [number for number in numbers_with_zeros if number > 0]
list_with_zeros_at_the_back = numbers_without_zeros + finding_the_zeros

print(list_with_zeros_at_the_back)
```

## 2.	Messaging</br>
On the **first line**, you will receive a sequence of numbers **separated by a single space**. 
On the **second line**, you will receive a **string**.</br>
Your task is to write a program that sends a message **only using chars** from the given string. 
**Each char** the program adds to the message should be found by **its index**. </br>
The index you are looking for is the **sum of a number's digits** from the first sequence. 
**If the index is greater** than the length of the text, **continue counting** from the beginning 
so that you always have a valid index). </br>
**When you find a char**, you should add it to the **message and remove it from the string**. 
It means that for the following index, the text will contain one character less.</br>
**Print the final message.**
### Example
| Input                                         | Output |
|-----------------------------------------------|-------|
| 9992 562 8933</br>This is some message for you |hey|
| 2 122 1123 1321 9 17211</br>87j973u59dg37e725!|judge!|

### Code
```Python
numbers_input = input()
text_input = input()

message = ""
text_list = list(text_input)

for num in map(int, numbers_input.split()):
    digit_sum = sum(int(digit) for digit in str(num))

    list_index = digit_sum % len(text_list)

    message += text_list[list_index]
    text_list.pop(list_index)

    if len(text_list) == 0:
        break

print(message)
```
### or
```Python
code_number = [int(num) for num in input().split(" ")]
code_string = input()
cod_list = []

for code in code_number:
    sum_digits = 0
    for digit in str(code):
        sum_digits += int(digit)
    cod_list.append(sum_digits)

decoded_message = ""
for index in cod_list:
    if len(code_string) == 0:
        break
    current_char = code_string[index % len(code_string)]
    decoded_message += current_char
    code_string = code_string.replace(current_char, "", 1)

print(decoded_message)
```
### or from CEO
```Python
numbers_input = input()
text_input = input()

message = ""
text_list = list(text_input)

for num in map(int, numbers_input.split()):
    digit_sum = sum(int(digit) for digit in str(num))

    list_index = digit_sum % len(text_list)

    message += text_list[list_index]
    text_list.pop(list_index)

    if len(text_list) == 0:
        break
```
### or from CEO
```Python
numbers = input().split()
string_text = input()
msg_show = ""

for num in numbers:
    find_index = sum([int(s_num) for s_num in num])
    if find_index >= len(string_text):
        find_index = find_index - len(string_text)
    msg_show += string_text[find_index]
    string_text = string_text[:find_index] + string_text[find_index + 1:]

print(msg_show)
```
### or from CEO
```Python
numbers = input().split()
string_text = input()

msg_show = ""

for num in numbers:
    find_index = 0
    for s_num in num:
        find_index += int(s_num)
    if find_index > len(string_text):
        find_index = find_index - len(string_text)
    msg_show += string_text[find_index]
    string_text = string_text[:find_index] + string_text[find_index + 1:]

print(msg_show)
```
### or from kumchovylcho
```Python
numbers = [number for number in input().split()]
text = list(input())
index = 0
final_string = ""


def check_text(letter_position):
    global text
    global final_string
    if 0 <= letter_position < len(text):
        final_string += text[letter_position]
        text.pop(letter_position)
    elif letter_position >= len(text):
        index_to_remove = index - len(text)
        final_string += text[index_to_remove]
        text.pop(index_to_remove)


for number in numbers:
    index = 0
    for digit in number:
        index += int(digit)
    check_text(index)

print(final_string)
```

## 3.	Car Race</br>
Write a program that announces the winner of a car race. </br>
You will **receive a sequence of numbers**. 
**Each number** represents the time the car needs to pass through that **step (the index)**. 
**There will be two cars**.</br>
**The first** one starts from the **left side**, and the **other** one starts from the **right side**.
**The middle index** of the sequence is the **finish line**. 
**Calculate** the **total time** each racer needs to reach the finish line and **print the winner** with his total time (**the racer with less time**). 
**If you have a zero** in the list, you should **reduce the racer's time** that reached it by **20%** (**from his current time**).
**The number of elements** in the sequence will **always be odd**.</br>
Print the result in the following format **"The winner is {left/right} with total time: {total_time}"**.
The time should be **formatted** to the **first decimal point**.</br>

#### Example
| Input | Output |Comment|
|-------|--------|-|
|29 13 9 0 13 0 21 0 14 82 12|The winner is left with total time: 53.8|The time of the left racer is (29 + 13 + 9) * 0.8 (because of the zero) + 13 = 53.8.</br>The time of the right racer is (82 + 12 + 14) * 0.8 + 21 = 107.4.</br>The winner is the left racer, so we print it.|
|123 20 4 0 13 0 0 5 5 14 0|The winner is right with total time: 19.2||

### Code
```Python
time_index = [int(num) for num in input().split(" ")]
left_car = 0
right_car = 0

middle_index = len(time_index) // 2
middle_element = time_index[middle_index]

for l_time in time_index[0:middle_index]:
    if l_time == 0:
        left_car *= 0.8
    else:
        left_car += l_time

for r_time in time_index[-1:middle_index:-1]:
    if r_time == 0:
        right_car *= 0.8
    else:
        right_car += r_time

if left_car < right_car:
    print(f"The winner is left with total time: {left_car:.1f}")
else:
    print(f"The winner is right with total time: {right_car:.1f}")
```
### or 
```Python
numbers_input = input()
numbers_list = list(map(int, numbers_input.split()))
    # Изчисляване на сумата на индексите
sum_of_indexes = sum(range(len(numbers_list)))
    # Изчисляване на броя на елементите в списъка
num_elements = len(numbers_list)
    # Изчисляване на средния индекс - FINAL
finish_index = int(sum_of_indexes / num_elements)
left_list = numbers_list[:finish_index]
right_list = numbers_list[finish_index+1:][::-1]
# print("left_list", left_list)
# print("right_list", right_list)
left_sum, right_sum = 0, 0
for l in left_list:
    if l == 0:
        left_sum *= 0.8
    else:
        left_sum += l
for r in right_list:
    if r == 0:
        right_sum *= 0.8
    else:
        right_sum += r

if left_sum < right_sum:
    winer = "left"
    winer_time = left_sum
else:
    winer = "right"
    winer_time = right_sum

print(f"The winner is {winer} with total time: {winer_time:.1f}")
```
### or 
```Python
numbers_list = list(map(int, input().split()))
finish = len(numbers_list) // 2
left_list = numbers_list[:finish]
right_list = numbers_list[finish+1:][::-1]
left_sum, right_sum = 0, 0
for l, r in zip(left_list, right_list):
    left_sum += l
    if l == 0:
        left_sum *= 0.8
    right_sum += r
    if r == 0:
        right_sum *= 0.8

print(f"The winner is left with total time: {left_sum:.1f}" if left_sum < right_sum
      else f"The winner is right with total time: {right_sum:.1f}")
```
### or 
```Python
sequence_of_numbers = [int(num) for num in input().split()]

first_car = len(sequence_of_numbers) // 2

first_car_score = sum([num if num != 0 else -sum(sequence_of_numbers[:first_car][:pos]) * 0.2 for pos, num in
                       enumerate(sequence_of_numbers[:first_car])])
second_car_score = sum([num if num != 0 else -sum(sequence_of_numbers[::-1][:first_car][:pos]) * 0.2 for pos, num in
                    enumerate(sequence_of_numbers[::-1][:first_car])])

if first_car_score < second_car_score:
    print(f"The winner is left with total time: {first_car_score:.1f}")
else:
    print(f"The winner is right with total time: {second_car_score:.1f}")
```
### or 
```Python
sequence_of_numbers = input().split(" ")

car_one_total = 0
car_two_total = 0
s_car = sequence_of_numbers
where_is_split = len(sequence_of_numbers) // 2


for car_one, car_two in zip(sequence_of_numbers[:where_is_split], s_car[::-1]):
    car_one = int(car_one)
    car_two = int(car_two)
    if car_one == 0:
        car_one_total = car_one_total * 0.8
    else:
        car_one_total += car_one

    if car_two == 0:
        car_two_total = car_two_total * 0.8
    else:
        car_two_total += car_two

if car_one_total < car_two_total:
    print(f"The winner is left with total time: {car_one_total:.1f}")

else:
    print(f"The winner is right with total time: {car_two_total:.1f}")
```
## 4.	Josephus Permutation</br>
This problem takes its name from arguably the most important event in the life of the ancient historian Josephus. </br>
According to his tale, he and his 40 soldiers were trapped in a cave by the Romans during a siege. 
Refusing to surrender to the enemy, they instead opted for mass suicide, with a twist:</br> 
    they formed a circle and proceeded to kill one man of every three until one last man was left (and that it was supposed to kill himself to end the act). 
    Well, Josephus and another man were the last, and, as we now know every detail of the story, you may have correctly guessed that they did not precisely follow through with the original idea.</br></br>
You are now to create a program that prints a Josephus permutation, receiving two lines of code:</br> 
    * the list itself - numbers separated by a single space representing the people in the circle</br> 
    * a number k</br> 
People are standing in a circle waiting to be executed.</br>
Counting begins from the first one in the circle and proceeds from left to right.</br>  
After a specified number of people are skipped, the k person is executed.</br>
The procedure is repeated with the remaining people, starting with the next person, </br> 
    going in the same direction, and skipping the same number of people until no one remains.</br> 
Print the people by order of executions in the format: **"[{executed1},{executed2}, … {executedN}]"**
### Example
| Input                   | Output |
|-------------------------|--------|
| 1 2 3 4 5 6 7</br>3     |[3,6,2,7,5,1,4]|
| 10 5 65 104 1 0 2</br>8 |[10,65,0,1,5,2,104]|

### Code
```Python
input_numbers = list(map(int, input().split()))
dead = len(input_numbers)
output_r = []
kill_step = int(input()) - 1
result, index = [], 0

while dead > 0:
    index = (index + kill_step) % dead
    eliminated_number = input_numbers.pop(index)
    result.append(str(eliminated_number))
    dead -= 1

output_r = '[' + ','.join(result) + ']'  # Convert list to a string without spaces
print(output_r)
```
### whit FOR LOOP  
```Python
input_numbers = list(map(int, input().split()))
dead = len(input_numbers)
kill_step = int(input())
kill_step -= 1
result, index = [], 0

for _ in range(dead):
    index = (index + kill_step) % dead
    eliminated_number = input_numbers.pop(index)
    result.append(str(eliminated_number))
    dead -= 1

output = "[" + ",".join(result) + "]" # Convert list to a string without spaces
print(output)
```
### or:  from [SimeonChifligarov](https://github.com/SimeonChifligarov/SoftUni_Judge_Python_Problems/blob/main/Python_Fundamentals_Course/03_List_Basics_More_Exercises/04_Josephus_Permutation.py)
```Python
the_list_itself = [int(el) for el in input().split()]
number_k = int(input())
result = []
current_list = the_list_itself.copy()

for _ in range(len(the_list_itself)):
    new_number_k = number_k
    while new_number_k > len(current_list):
        new_number_k -= len(current_list)
    else:
        result.append(current_list[new_number_k - 1])
        current_list.pop(new_number_k - 1)
        current_left = current_list[:new_number_k - 1]
        current_right = current_list[new_number_k - 1:]
        current_list = current_right + current_left

result = [str(el) for el in result]
print(f"[{','.join(result)}]")
```
### or
```Python
people = input().split(' ')
k = int(input())

counter = 0
i = 0
executed = list()
while len(people) > 0:
    counter += 1

    if counter % k == 0:
        # print(people[i], end=' ')
        executed.append(people[i])
        people.pop(i)
    else:

        i += 1

    if i >= len(people):
        i = 0

prt_str = ','.join([str(x) for x in executed.copy()])
print(f'[{prt_str}]')
```



## 5.	Tic-Tac-Toe
You will receive a field of a tic-tac-toe game in three lines containing numbers, separated by a single space.</br>
Legend:</br>
* 0 - empty space</br>
* 1 - first player move</br>
* 2 - second player move</br>
Find out who the winner is.</br> **If the first player wins**, print **"First player won"**.</br>
If the **second player** wins, print **"Second player won"**. **Otherwise**, print **"Draw!"**.

### Example
| Input                     | Output |
|---------------------------|--------|
| 2 0 1</br>0 1 0</br>1 0 2 |First player won|
| 0 1 0</br>2 2 2</br>1 0 0 |Second player won|
| 1 0 2</br>0 1 2</br>1 2 0 |Draw!|

### Code
```Python
lines = [input().split() for _ in range(3)]
first_player_win = None

for player in ['1', '2']:
    if (any(all(cell == player for cell in line) for line in lines)
            or any(all(line[i] == player for line in lines) for i in range(3))):
        first_player_win = (player == '1')
        break

# Check diagonals for both players
for player in ['1', '2']:
    if (all(lines[i][i] == player for i in range(3))
            or all(lines[i][2 - i] == player for i in range(3))):
        first_player_win = (player == '1')
        break

if first_player_win is None:
    print("Draw!")
elif first_player_win:
    print("First player won")
else:
    print("Second player won")
```
### from CEO
```Python
first_line = input().split(" ")
second_line = input().split(" ")
third_line = input().split(" ")

first_player_win = None

if len(set(first_line)) == 1 and first_line[0] == "1":
    first_player_win = True

elif len(set(second_line)) == 1 and second_line[0] == "1":
    first_player_win = True

elif len(set(third_line)) == 1 and third_line[0] == "1":
    first_player_win = True

elif first_line[0] == second_line[1] == third_line[2] and first_line[0] == "1":
    first_player_win = True

elif first_line[1] == second_line[1] == third_line[1] and first_line[1] == "1":
    first_player_win = True

elif first_line[2] == second_line[1] == third_line[0] and first_line[2] == "1":
    first_player_win = True

elif first_line[2] == second_line[2] == third_line[2] and first_line[2] == "1":
    first_player_win = True

elif first_line[0] == second_line[0] == third_line[0] and first_line[0] == "1":
    first_player_win = True

elif len(set(first_line)) == 1 and first_line[0] == "2":
    first_player_win = False

elif len(set(second_line)) == 1 and second_line[0] == "2":
    first_player_win = False

elif len(set(third_line)) == 1 and third_line[0] == "2":
    first_player_win = False

elif first_line[0] == second_line[1] == third_line[2] and first_line[0] == "2":
    first_player_win = False

elif first_line[1] == second_line[1] == third_line[1] and first_line[1] == "2":
    first_player_win = False

elif first_line[2] == second_line[1] == third_line[0] and first_line[2] == "2":
    first_player_win = False

elif first_line[2] == second_line[2] == third_line[2] and first_line[2] == "2":
    first_player_win = False

elif first_line[0] == second_line[0] == third_line[0] and first_line[0] == "2":
    first_player_win = False


if first_player_win is None:
    print("Draw!")

elif first_player_win:
    print("First player won")

else:
    print("Second player won")
```
### whit MATRIX 
```Python
matrix = []

for run in range(3):
    list_app = list(map(int, input().split()))
    matrix.append(list_app)
first_player = False
second_player = False

# Check for rows and columns
for i in range(3):
    # Rows
    if matrix[i][0] == matrix[i][1] == matrix[i][2] != 0:
        if matrix[i][0] == 1:
            first_player = True
        elif matrix[i][0] == 2:
            second_player = True

    # Columns
    if matrix[0][i] == matrix[1][i] == matrix[2][i] != 0:
        if matrix[0][i] == 1:
            first_player = True
        elif matrix[0][i] == 2:
            second_player = True

# Check diagonals
if matrix[0][0] == matrix[1][1] == matrix[2][2] != 0:
    if matrix[0][0] == 1:
        first_player = True
    elif matrix[0][0] == 2:
        second_player = True

if matrix[0][2] == matrix[1][1] == matrix[2][0] != 0:
    if matrix[0][2] == 1:
        first_player = True
    elif matrix[0][2] == 2:
        second_player = True

# Determine the winner or draw
if first_player:
    print("First player won")
elif second_player:
    print("Second player won")
else:
```

## 6.	List Manipulator
Trifon has finally become a junior developer and has received his first task. It is about manipulating a list of integers. He is not quite happy about it since he hates manipulating lists. They will pay him a lot of money, though, and he is willing to give somebody half of it if to help him do his job. On the other hand, you love lists (and money), so you decide to try your luck.
The list may be manipulated by one of the following commands:</br>
* "exchange {index}" – splits the list after the given index and exchanges the places of the two resulting sub-lists. E.g., [1, 2, 3, 4, 5] -> "exchange 2" -> result: [4, 5, 1, 2, 3]
  * If the index is outside the boundaries of the list, print "Invalid index"
  * A negative index is considered invalid
* "max even/odd"– returns the INDEX of the max even/odd element. E.g., [1, 4, 8, 2, 3] -> "max odd" -> print: 4
* "min even/odd" – returns the INDEX of the min even/odd element. E.g. [1, 4, 8, 2, 3] -> "min even" -> print: 3
  * If there are two or more equal min/max elements, return the index of the rightmost one
  * If a min/max even/odd element cannot be found, print "No matches"
* "first {count} even/odd" – returns the first count even/odd elements. E.g. [1, 8, 2, 3] -> "first 2 even" -> print [8, 2]
* "last {count} even/odd" – returns the last count even/odd elements. E.g. [1, 8, 2, 3] -> "last 2 odd" -> print [1, 3]
  * If the count is greater than the list length, print "Invalid count"
  * If there are not enough elements to satisfy the count, print as many as you can. If there are zero even/odd elements, print an empty list "[]"
* "end" - stop taking input and print the final state of the list
### Input
* The input data should be read from the console.
* On the first line, the initial list is received as a line of integers, separated by a single space.
* On the following lines, until the command "end" is received, you will receive the list manipulation commands.
* The input data will always be valid and in the format described. There is no need to check it explicitly.
### Output
* The output should be printed on the console.
* On a separate line, print the output of the corresponding command.
* On the last line, print the final list in square brackets with its elements separated by a comma and a space.
* See the examples below to get a better understanding of your task.
### Constraints
* The number of input lines will be in the range [2 … 50].
* The list elements will be integers in the range [0 … 1000].
* The number of elements will be in the range [1 .. 50].
* The split index will be an integer in the range [-231 … 231 – 1].
* The first/last count will be an integer in the range [1 … 231 – 1].
* There will not be redundant whitespace anywhere in the input.
* Allowed working time for your program: 0.1 seconds. Allowed memory: 16 MB.
### Examples

| Input | Output |
|-------|--------|
|1 3 5 7 9</br>exchange 1</br>max odd</br>min even</br>first 2 odd</br>last 2 even</br>exchange 3</br>end|2</br>No matches</br>[5, 7]</br>[]</br>[3, 5, 7, 9, 1]|
|1 10 100 1000</br>max even</br>first 5 even</br>exchange 10</br>min odd</br>exchange 0</br>max even</br>min even</br>end|3</br>Invalid count</br>Invalid index</br>0</br>2</br>0</br>[10, 100, 1000, 1]|
|1 10 100 1000</br>exchange 3</br>first 2 odd</br>last 4 odd</br>end|[1]</br>[1]</br>[1, 10, 100, 1000]|
### Code
```Python
numbers = [int(i) for i in input().split()]
command = input().split()

while command[0] != "end":
    even = [i for i in numbers if i % 2 == 0]
    odd = [i for i in numbers if i % 2 != 0]

    if command[0] == "exchange":
        if 0 <= int(command[1]) < len(numbers):
            numbers = numbers[int(command[1]) + 1:] + numbers[:int(command[1]) + 1]
        else:
            print(f'Invalid index')

    elif command[0] == "max":
        if command[1] == "even" and even:
            print((len(numbers) - numbers[::-1].index(max(even)) - 1))
        elif command[1] == "odd" and odd:
            print((len(numbers) - numbers[::-1].index(max(odd)) - 1))
        else:
            print('No matches')

    elif command[0] == "min":
        if command[1] == "even" and even:
            print((len(numbers) - numbers[::-1].index(min(even)) - 1))
        elif command[1] == "odd" and odd:
            print((len(numbers) - numbers[::-1].index(min(odd)) - 1))
        else:
            print('No matches')

    elif command[0] == "first":
        if 0 < int(command[1]) <= len(numbers):
            if command[2] == "even":
                print(even[0:int(command[1])])
            else:
                print(odd[0:int(command[1])])
        else:
            print(f"Invalid count")

    elif command[0] == "last":
        if 0 < int(command[1]) <= len(numbers):
            if command[2] == "even":
                print(even[-int(command[1]):])
            else:
                print(odd[-int(command[1]):])
        else:
            print(f"Invalid count")
    command = input().split()

print(numbers)
```
### whit dictionary from CEO
```Python
main_list = [int(x) for x in input().split()]


def check_valid_index(index):
    if 0 <= index < len(main_list):
        return True
    print("Invalid index")


def exchange(_, info):
    index = info[0]
    global main_list
    if check_valid_index(index):
        part_one = main_list[:index + 1]
        part_two = main_list[index + 1:]
        main_list = part_two + part_one


def max_min_even_odd(max_or_min, info):
    operation ={ "max":max, "min": min}
    type_number = info[0]
    if type_number == "even":
        result = [x for x in main_list if x % 2 == 0]
    else:
        result = [x for x in main_list if x % 2 != 0]
    if result:
        ind = operation[max_or_min](result)
        print(len(main_list) - main_list[::-1].index(ind) - 1)
    else:
        print("No matches")


def first_numbers(starting_from, info):
    number, number_type = info
    if number > len(main_list):
        print("Invalid count")
        return
    odd, even = [], []
    for num in main_list:
        if num % 2 != 0:
            odd.append(num)
        else:
            even.append(num)
    if starting_from == "first":
        if number_type == "even":
            print(even[:number])
        elif number_type == "odd":
            print(odd[:number])
    elif starting_from == "last":
        if number_type == "even":
            print(even[-number:])
        else:
            print(odd[-number:])


commands = {
    "max": max_min_even_odd,
    "min": max_min_even_odd,
    "first": first_numbers,
    "last": first_numbers,
    "exchange": exchange

}

command = input()

while command != "end":
    command_type, *info = [x if x.isalpha() else int(x) for x in command.split()]
    commands[command_type](command_type, info)
    command = input()

print(main_list)
```
### whit dictionary from kumchovalcho
```Python
numbers = [int(number) for number in input().split()]


def exchange(index):
    global numbers
    if 0 <= index < len(numbers):
        numbers = numbers[index + 1:] + numbers[:index + 1]
    else:
        print("Invalid index")


def min_max(min_max, even_odd):
    global even, odd
    if min_max == "max":
        if even_odd == "even" and even:
            print((len(numbers) - numbers[::-1].index(max(even)) - 1))
        elif even_odd == "odd" and odd:
            print((len(numbers) - numbers[::-1].index(max(odd)) - 1))
        else:
            print("No matches")
    elif min_max == "min":
        if even_odd == "even" and even:
            print((len(numbers) - numbers[::-1].index(min(even)) - 1))
        elif even_odd == "odd" and odd:
            print((len(numbers) - numbers[::-1].index(min(odd)) - 1))
        else:
            print("No matches")


def first_last_numbers(first_last, count_of_numbers, even_odd):
    global even, odd
    if 0 <= count_of_numbers <= len(numbers):
        if first_last == "first" and even_odd == "even":
            print(even[:count_of_numbers])
        elif first_last == "first" and even_odd == "odd":
            print(odd[:count_of_numbers])
        elif first_last == "last" and even_odd == "even":
            print(even[-count_of_numbers:])
        elif first_last == "last" and even_odd == "odd":
            print(odd[-count_of_numbers:])
    else:
        print("Invalid count")


command = input()
while command != "end":
    even = [number for number in numbers if number % 2 == 0]
    odd = [number for number in numbers if number % 2 != 0]
    command = command.split()
    command_type = command[0]
    if command_type == "exchange":
        index = int(command[1])
        exchange(index)
    elif command_type == "max" or command_type == "min":
        min_max(command[0], command[1])
    elif command_type == "first" or command_type == "last":
        first_last_numbers(command[0], int(command[1]), command[2])
    command = input()

print(numbers)
```










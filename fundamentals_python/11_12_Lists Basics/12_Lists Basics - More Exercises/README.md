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


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

## 4. Number Classification


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

## 5. Office Chairs


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

## 6. Electron Distribution


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
```Python

```
</details>

## 9. *Anonymous Threat


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
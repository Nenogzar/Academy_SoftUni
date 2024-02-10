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

| Input                                                        | Output                   |
|--------------------------------------------------------------|--------------------------|
| arp, live, strong</br>>lively, alive, harp, sharp, armstrong | ['arp', 'live', 'strong' |
| tarp, mice, bull</br>lively, alive, harp, sharp, armstron    | [ ]                      |

|
    

</details>

<details> <summary>Code</summary>

```Python
 

```
</details>

## 2. Next Version


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
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>

<body style="background-color: #0d1117; color: white; align-items: center; height: 100vh; margin: 0;">


<table>
  <tr>
    <th><a href="https://github.com/Nenogzar/Academy_SoftUni/tree/main/fundamentals_python/lectures/25-26_Dictionaries"><img src="https://github.com/Nenogzar/Academy_SoftUni/blob/main/fundamentals_python/image/13.jpg" alt="Dictionary" width="300"></a>
</th>
    <th>Legend:<br>Under each task name, you have two choices:<br>🛠️Condition - task conditions<br>🐍Code - solution of tasks</th>
  </tr>
  <tr>
    <td>
    <a href="https://github.com/Nenogzar/Academy_SoftUni/tree/main/fundamentals_python/lectures/25-26_Dictionaries/01_Dictionaries%20-%20Lab">Lab</a>
  |  
    <a href="https://github.com/Nenogzar/Academy_SoftUni/tree/main/fundamentals_python/lectures/25-26_Dictionaries/02_Dictionaries%20-%20Exercise">Exercise</a>
  |  
    <a href="https://github.com/Nenogzar/Academy_SoftUni/tree/main/fundamentals_python/lectures/25-26_Dictionaries/03_Dictionaries%20-%20More%20Exercises">More</a>
    </td>
    <th><a href="https://github.com/Nenogzar/Academy_SoftUni/tree/main/fundamentals_python/lectures/25-26_Dictionaries/02_Dictionaries%20-%20Exercise/Exercise">problem solving python files</a></th>
  </tr>

</table>


[judge](https://judge.softuni.org/Contests/Practice/Index/1737)

> ## Dictionaries - Exercise

<details><summary> TASK CONDITIONS 🛠️ AND SOLUTION OF TASKS 🐍</summary>

> ### 1. Count Chars in a String

<details><summary>🛠️Condition</summary>

Write a program that counts all characters in a string except for space **(" ")**.

Print all the occurrences in the following format:

**"{char} -> {occurrences}"**

Example

| Input	| Output  	                  |
|-------|----------------------------|
|text| t -> 2<br>e -> 1<br>x -> 1 |
|text text text| t -> 6<br>e -> 3<br>x -> 3 |

</details>

<details> <summary>🐍Code</summary>

```Python
text = input()
letters = {}
for char in text:
    if char != " ":
        if char not in letters.keys():
            letters[char] = 1
        else:
            letters[char] += 1
for key, value in letters.items():
    print(f"{key} -> {value}")
```
```Python
characters = input().replace(" ", "")

character_count = {}

for character in characters:
    character_count[character] = character_count.get(character, 0) + 1
    
# for key, value in character_count.items():
#     print(f"{key} -> {value}")
#  OR
[print(f"{keys} -> {value}") for keys, value in character_count.items()]
```
```Python
def count_letter(current_text):
    char_dict = {}

    for word in current_text:
        for letter in word:
            if letter not in char_dict:
                char_dict[letter] = 1
            else:
                char_dict[letter] += 1
    return char_dict

input_str = input().split(" ")
char_dict = count_letter(input_str)

for k, v, in char_dict.items():
    print(f"{sorted({k})} -> {v}")
```


</details>

> ### 2. A Miner Task

<details><summary>🛠️Condition</summary>

You will be given a sequence of strings, each on a **new line** until you receive the **"stop"** command. 
Every **odd line** on the console represents a resource (e.g., Gold, Silver, Copper, and so on) and **every even - quantity**. 
Your task is to collect the resources and print them each on a new line.<br>
Print the resources and their quantities in the following format:<br>
"{resource} -> {quantity}"<br>
The quantities will be in the range [1 … 2 000 000 000].<br>

Example

| Input	| Output  	|
|-------|-----------|
|Gold<br>155<br>Silver<br>10<br>Copper<br>17<br>stop|Gold -> 155<br>Silver -> 10<br>Copper -> 17|
|gold<br>155<br>silver<br>10<br>copper<br>17<br>gold<br>15<br>stop|gold -> 170<br>silver -> 10<br>copper -> 17|

</details>
<details> <summary>🐍Code</summary>

```Python
""" whit list """
command = input()
res_list = []
resourse_dict = {}
while command != "stop":
    res_list.append(command)
    command = input()

for i in range(0, len(res_list), 2):
    resourse = res_list[i]

    if resourse in resourse_dict:
        resourse_dict[resourse] += int(res_list[i + 1])
    else:
        resourse_dict[resourse] = int(res_list[i + 1])

for resource, quantity in resourse_dict.items():
    print(f"{resource} -> {quantity}")

```
```Python
""" whit dicrionary """

mined_materials = dict()

material = input()
while material != "stop":
    quantity = int(input())

    if material not in mined_materials:
        mined_materials[material] = quantity

    elif material in mined_materials:
        mined_materials[material] += quantity

    material = input()

for resource, quantity in mined_materials.items():
    print(f"{key} -> {quantity}")
```
```Python
"""whit get() """

resource = input()

total_resource = {}
while resource != "stop":
    quantity = int(input())
    total_resource[resource] = total_resource.get(resource, 0) + quantity
    resource = input()

for resource, quantity in total_resource.items():
    print(f"{key} -> {quantity}")
```

</details>

> ### 3. Capitals

<details><summary>🛠️Condition</summary>




Example

| Input	| Output  	|
|-------|-----------|
|       |     		|
|  		|    		|

</details>
<details> <summary>🐍Code</summary>


```Python
 

```
</details>


</details>END

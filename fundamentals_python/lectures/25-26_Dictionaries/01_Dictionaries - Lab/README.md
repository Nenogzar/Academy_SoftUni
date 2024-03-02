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
    <th><a href="https://github.com/Nenogzar/Academy_SoftUni/tree/main/fundamentals_python/lectures/25-26_Dictionaries/01_Dictionaries%20-%20Lab/Exercise">problem solving python files</a></th>
  </tr>

</table>


[judge](https://judge.softuni.org/Contests/Practice/Index/1736)

> ## Dictionaries Lab

<details><summary> TASK CONDITIONS 🛠️ AND SOLUTION OF TASKS 🐍</summary>

> ### 01. Bakery

<details><summary>🛠️Condition</summary>

Your first task at your new job is to create a table of the stock in a bakery, and you really don't want to fail on your first day at work.
You will receive a single line containing some food (**keys**) and quantities (**values**). 
They will be separated by a **single space** (the first element is the key, the second – is the value, and so on). 
**Create a dictionary with all the keys and values and print it on the console.**

Example

| Input	                           | Output  	                                         |
|----------------------------------|---------------------------------------------------|
| bread 10 butter 4 sugar 9 jam 12 | {'bread': 10, 'butter': 4, 'sugar': 9, 'jam': 12} |
| eggs 3 sugar 7 salt 1 butter 3   | {'eggs': 3, 'sugar': 7, 'salt': 1, 'butter': 3}   |

</details>

<details> <summary>🐍Code</summary>

```Python
input_text = input().split(" ")
new_dict = {}

for i in range(0, len(input_text), 2):
    keys, values = input_text[i], input_text[i + 1]
    new_dict[keys] = int(values)

print(new_dict)

```
```Python
initial_list = input().split()
food_type = {initial_list[i]: int(initial_list[i + 1]) for i in range(0, len(initial_list), 2)}
print(food_type)
```

</details>


> ### 02. Stock


<details><summary>🛠️Condition</summary>

_After you have completed your first task, your boss decides to give you another one right away._ 
_Now, not only do you have to keep track of the stock, but you also need to answer customers about product availability._
You will be given **key-value** pairs of products and quantities (on a single line separated by space). 
On the following line, you will be given products to search for. Check for each product. You have **2 possibilities:**

* If you have the product, print **"We have {quantity} of {product} left"**.
* Otherwise, print **"Sorry, we don't have {product}"**.

#### Example

| Input	                                                           | Output  	                                                                                                           |
|------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| cheese 10 bread 5 ham 10 chocolate 3</br>jam cheese ham tomatoes | Sorry, we don't have jam</br>We have 10 of cheese left</br>We have 10 of ham left</br>Sorry, we don't have tomatoes |
| eggs 5 bread 10</br>bread eggs                                   | We have 10 of bread left</br>We have 5 of eggs left                                                                 |

</details>

<details> <summary>🐍Code</summary>


```Python
input_products = input().split(" ")
products = {}

for n in range(0, len(input_products), 2):
    # key, value = input_products[n], input_products[n + 1]
    # products[key] = int(value)
    products = {input_products[i]: int(input_products[i + 1]) for i in range(0, len(input_products), 2)}


def check_products(product_dict):
    results = []
    for product in product_dict:
        if product not in products:
            results.append(f"Sorry, we don't have {product}")
        else:
            results.append(f"We have {products[product]} of {product} left")
    return results


new_check = input().split(" ")
check_results = check_products(new_check)
for result in check_results:
    print(result)


```

</details>


> ### 3. Statistics

<details><summary>🛠️Condition</summary>

_You seem to be doing great at your first job, so your boss decides to give you as your next task something more challenging. 
You have to accept all the new products coming into the bakery and finally gather some statistics._

You will be receiving **key-value** pairs on separate lines separated by ": " until you receive the command **"statistics"**. 
Sometimes you may receive a product **more than once**. In that case, you have to **add** the **new** quantity to the existing one. 
When you receive the **"statistics"** command, print the following:

**"Products in stock:**</br>
**- {product1}: {quantity1}**</br>
**- {product2}: {quantity2}**</br>
**…**</br>
**- {productN}: {quantityN}**</br>
**Total Products: {count_all_products}**</br>
**Total Quantity: {sum_all_quantities}"**</br>

Example

| Input	                                                         | Output  	                                                                                                                   |
|----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| bread: 4</br>cheese: 2</br>ham: 1</br>bread: 1</br>statistics  | Products in stock:</br>- bread: 5</br>- cheese: 2</br>- ham: 1</br>Total Products: 3</br>Total Quantity: 8                  |
| eggs: 10</br>bread: 6</br>cheese: 8</br>milk: 7</br>statistics | Products in stock:</br>- eggs: 10</br>- bread: 6</br>- cheese: 8</br>- milk: 7</br>Total Products: 4</br>Total Quantity: 31 |

</details>

<details> <summary>🐍Code</summary>

```Python
def product_func(dict_product, product_dict):
    key, value = dict_product[0], int(dict_product[1])

    if key not in product_dict:
        product_dict[key] = value
    else:
        product_dict[key] += value
    return product_dict


command = input()
product_dict = {}
while command != "statistics":
    product_info = command.split(": ")
    product_dict = product_func(product_info, product_dict)

    command = input()

print("Products in stock:")
for k, v in product_dict.items():
    print(f"- {k}: {v}")
print(f"Total Products: {len(product_dict)}")
print(f"Total Quantity: {sum(product_dict.values())}")
# or 
# print(f"Products in stock:")
# [print(f"- {item}: {quantity}") for item, quantity in product_dict.items()]
# print(f"Total Products: {len(product_dict)}\nTotal Quantity: {sum(product_dict.values())}")
```
```Python
product_input = input()

products_in_stock = {}

while product_input != 'statistics':
    product, quantity = product_input.split(': ')
    products_in_stock[product] = products_in_stock.get(product, 0) + int(quantity)
    product_input = input()

print('Products in stock:')
for product, quantity in products_in_stock.items():
    print(f'- {product}: {quantity}')
print(f'Total Products: {len(products_in_stock)}')
print(f'Total Quantity: {sum(products_in_stock.values())}')
```

</details>


> ### 4. Students


<details><summary>🛠️Condition</summary>

You will be receiving names of students, their ID, and a course of programming they have taken in the format
#### "{name}:{ID}:{course}"
On the last line, you will receive the **name** of a course in snake case lowercase letters. 
You should **print only the information** of the students who have taken the corresponding course in the format:
#### "{name} - {ID}"
on separate lines.
#### Note: **each student's ID will always be unique**

Example

| Input	                                                                                                                       | Output  	                               |
|------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| Peter:123:programming basics<br>John:5622:fundamentals<br>Maya:89:fundamentals<br>Lilly:633:fundamentals<br>fundamentals     | John - 5622<br>Maya - 89<br>Lilly - 633 |
| Alex:6:programming basics<br>Maria:7:programming basics<br>Kaloyan:9:advanced<br>Todor:10:fundamentals<br>programming_basics | Alex - 6<br>Maria - 7                   |

</details>

<details> <summary>🐍Code</summary>


```Python
"""Building a dictionary by student -> {'student': ('ID', 'course')}"""
command = input().split(":")
student_dict = {}

while len(command) > 1:

    studen, id_student, course  = command
    student_dict[studen] = (id_student, course)
    command = input().split(":")
#print(student_dict)
# {'Peter': ('123', 'programming basics'), 'John': ('5622', 'fundamentals'), 'Maya': ('89', 'fundamentals'), 'Lilly': ('633', 'fundamentals')}
value = command[0]
formatted_value = value.replace('_', ' ')

for name, (id, courses) in student_dict.items():
    if formatted_value == courses:
        print(f"{name} - {id}")

```
kumchovylcho solution

```Python
""" Building a dictionary by course - student  - ID - > {'course': {'student': 'ID'}"""
student_information = input()
student_dic = {}

while not student_dic.get(student_information):
    student_information = student_information.split(":")
    name_student, id_student, couse_student = student_information

    if couse_student not in student_dic:
        student_dic[couse_student] = {}
    student_dic[couse_student][name_student] = id_student
#   {'programming basics': {'Peter': '123'}, 'fundamentals': {'John': '5622', 'Maya': '89', 'Lilly': '633'}}
    student_information = input()

    student_information = student_information.replace("_", " ")

for key, value in student_dic[student_information].items():
    print(f"{key} - {value}")
```


</details>



> ### 5. ASCII Values


<details><summary>🛠️Condition</summary>

Write a program that receives a list of characters separated by **", "**. 

It should create a dictionary with each character as a key and its ASCII value as a value. 
Try solving that problem using comprehension.

Example


| Input	| Output  	|
|-------|-----------|
|a, b, c, a|{'a': 97, 'b': 98, 'c': 99}|
|d, c, m, h|{'d': 100, 'c': 99, 'm': 109, 'h': 104}|
|s, t, o, y, a, n|{'s': 115, 't': 116, 'o': 111, 'y': 121, 'a': 97, 'n': 110}|


</details>

<details> <summary>🐍Code</summary>

```Python
input_string = input().split(", ")
ascii_dict = {}

for char in input_string:
    ascii_dict[char] = ord(char)

print(ascii_dict)
```

```Python
"""using comprehension """
input_characters = list(map(str, input().split(", ")))

ascii_dict = {char: ord(char) for char in input_characters}

print(ascii_dict)

```

```Python
def create_ascii_dict(characters):
    ascii_dict = {char: ord(char) for char in characters}
    return ascii_dict

input_characters = input().split(", ")
result_dict = create_ascii_dict(input_characters)

print(result_dict)
```

</details>

> ### 6. Odd Occurrences

<details><summary>🛠️Condition</summary>

Write a program that prints all elements from a given sequence of words that occur an odd number of times (case-insensitive) in it.
• Words are given on a single line, space-separated.



Example


| Input	                         | Output  	  |
|--------------------------------|------------|
| Java C# PHP PHP JAVA C java    | java c# c  |
| 3 5 5 hi pi HO Hi 5 ho 3 hi pi | 5 hi       |
| a a A SQL xx a xx a A a XX c   | a sql xx c |


</details>

<details> <summary>🐍Code</summary>


```Python
words = input().split()
odd_occurrences = {}

for word in words:
    word = word.lower()
    if word not in odd_occurrences.keys():
        odd_occurrences[word] = 1
    else:
        odd_occurrences[word] += 1
for key, value in odd_occurrences.items():
    if value % 2 != 0:
        print(f"{key} ", end="")

```

</details>

> ### 7. Word Synonyms

<details><summary>🛠️Condition</summary>

Write a program, which keeps a dictionary with **synonyms**.<br> The key of the dictionary will be the word. 
The value **will be a list** of all the synonyms of that word. <br>
You will be given a **number n – the count of the words**. 
After each term, you will be **given a synonym**, so the count of lines you should read from the console is **2 * n**. 
You will be receiving a word and a synonym each on a **separate line like this**:
* **{word}**<br>
* **{synonym}**<br>
If you get the same word twice, just add the new synonym to the list.<br>
Print the words in the following format:<br>
**{word} - {synonym1, synonym2 … synonymN}**

Example

| Input	                                                       | Output  	                                   |
|--------------------------------------------------------------|---------------------------------------------|
| 3<br>cute<br>adorable<br>cute<br>charming<br>smart<br>clever | cute - adorable, charming<br>smart - clever |
| 2<br>task<br>problem<br>task<br>assignment                   | task – problem, assignment                  |



</details>

<details> <summary>🐍Code</summary>


```Python
number_synonyms = int(input())
synonyms_dict = {}

for _ in range(number_synonyms):
    word = input()
    synonym = input()

    if word in synonyms_dict:
        synonyms_dict[word].append(synonym)
    else:
        synonyms_dict[word] = [synonym]
# print(synonyms_dict)
for word, synonyms in synonyms_dict.items():
    print(f"{word} - {', '.join(synonyms)}")
```
```Python
count_of_synonyms = int(input())
synonyms = dict()

for item in range(count_of_synonyms):
    word, synonym = input(), input()

    synonyms[word] = synonyms.get(word, [])
    synonyms[word].append(synonym)

[print(f"{word} - {', '.join(synonyms[word])}") for word in synonyms]
```

</details>

</details>





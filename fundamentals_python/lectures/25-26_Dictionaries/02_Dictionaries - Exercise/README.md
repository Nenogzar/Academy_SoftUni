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

Using **dictionary comprehension**, write a program that receives **country** names on the first line, 
separated by comma and space **", "**, and their corresponding **capital** cities on the second line 
(again separated by **comma and space ", "**). 
Print each country with its capital on a separate line in the following format: **"{country} -> {capital}"**.

**Hints**

* You could use the zip() method.

Example

| Input	                                                                  | Output  	                                                                           |
|-------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| Bulgaria, Romania, Germany, England<br>Sofia, Bucharest, Berlin, London | Bulgaria -> Sofia<br>Romania -> Bucharest<br>Germany -> Berlin<br>England -> London |
| Bulgaria, Germany, France<br>Varna, Frankfurt, Paris                    | Bulgaria -> Varna<br>Germany -> Frankfurt<br>France -> Paris                        |

</details>
<details> <summary>🐍Code</summary>


```Python
country_names = input().split(", ")
capytal_name = input().split(", ")
country_dict = dict(zip(country_names, capytal_name))

[print(f"{country} -> {capital}") for country, capital in country_dict.items()]

```
</details>

> ### 4. Phonebook

<details><summary>🛠️Condition</summary>

Write a program that receives info from the console about people and their phone numbers.
Each entry should have a **name and a number (both strings) separated by a "-"**.

If you receive a **name that already exists** in the phonebook, **update its number**.
After filling out the phonebook, you will receive a number – N.
Your program should be able to perform a search of contact by name and print its details in the format:

**"{name} -> {number}"**. 

In case the contact isn't found, print: **"Contact {name} does not exist."**

Example

| Input	                                                                                                                    | Output  	                                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Adam-0888080808<br>2<br>Mery<br>Adam                                                                                      | Contact Mery does not exist.<br>Adam -> 0888080808                                                            |
| Adam-+359888001122<br>Ralf-666<br>George-5559393<br>Silvester-02/987665544<br>4<br>Silvester<br>silvester<br>Rolf<br>Ralf | Silvester -> 02/987665544<br>Contact silvester does not exist.<br>Contact Rolf does not exist.<br>Ralf -> 666 |

</details>
<details> <summary>🐍Code</summary>

```Python
phone_book = {}

input_data = input()

while not input_data.isdigit():
    parts = input_data.split("-")
    if len(parts) == 2:
        name = parts[0].strip()
        phone = parts[1].strip()
        phone_book[name] = phone
    input_data = input()

num = int(input_data)

for _ in range(num):
    check_name = input()
    if check_name in phone_book:
        print(f"{check_name} -> {phone_book[check_name]}")
    else:
        print(f"Contact {check_name} does not exist.")
```
```Python
phone_book = {}
phone_number = input()
while not phone_number.isdigit():
    name, number = phone_number.split("-")
    phone_book[name] = phone_book.get(name, number)
    phone_number = input()

for _ in range(int(phone_number)):
    name_check = input()
    if name_check in phone_book:
        print(f"{name_check} -> {phone_book[name_check]}")
    else:
        print(f"Contact {name_check} does not exist.")
```
</details>

> ### 5. Legendary Farming

<details><summary>🛠️Condition</summary>

You are playing a game, and your goal is to win a **legendary item** - any legendary item will be good enough. 
However, it's a tedious process, and it requires quite a bit of farming. **The possible items are**:
* "**Shadowmourne**" - requires 250 Shards
* "**Valanyr**" - requires 250 Fragments
* "**Dragonwrath**" - requires 250 Motes

"**Shards**", "**Fragments**", and "**Motes**" are the key materials (**case-insensitive**), and everything else is junk.<br>
You will be given lines of input in the format:<br>
**"{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"**<br>

**Keep track** of the key materials - the **first one that reaches 250**, wins the race. 
At that **point**, you have to **print** that the **corresponding legendary item is obtained.**
**In the end**, **print** the remaining **shards, fragments,** and **motes** in the format:<br>

**"shards: {number_of_shards}"**<br>
**"fragments: {number_of_fragments}"**<br>
**"motes: {number_of_motes}"**<br>

Finally, **print** the collected junk items in the order of appearance.
#### Input
* Each line comes in the following format:

**"{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"**
#### Output
* On the **first line**, print the obtained item in the format: **"{Legendary item} obtained!"**<br>
* On the **next three lines**, print the remaining key **materials**<br>
* On the **several final lines**, print the junk **items**<br>
* **All materials** should be printed in the format: **"{material}: {quantity}"**<br>
* The **output** should be lowercase, except for the **first letter of the legendary**<br>



Example

| Input	                                                                                                     | Output  	                                                                                   |
|------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| 3 Motes 5 stones 5 Shards<br>6 leathers 255 fragments 7 Shards                                             | Valanyr obtained!<br>shards: 5<br>fragments: 5<br>motes: 3<br>stones: 5<br>leathers: 6      |
| 123 silver 6 shards 8 shards 5 motes<br>9 fangs 75 motes 103 MOTES 8 Shards<br>86 Motes 7 stones 19 silver | Dragonwrath obtained!<br>shards: 22<br>fragments: 0<br>motes: 19<br>silver: 123<br>fangs: 9 |

</details>
<details> <summary>🐍Code</summary>

```Python 
input_items = input().split()
item_useful = {"shards": 0, "fragments": 0, "motes": 0}
item_useless = {}

obtained = False

while True:
    for i in range(0, len(input_items), 2):
        quantity = int(input_items[i])
        material = input_items[i + 1].lower()
        if material == "shards" or material == "fragments" or material == "motes":
            item_useful[material] += quantity
        else:
            if material not in item_useless:
                item_useless[material] = quantity
            else:
                item_useless[material] += quantity
        if item_useful["motes"] >= 250:
            print("Dragonwrath obtained!")
            item_useful["motes"] -= 250
            obtained = True
            break
        elif item_useful["fragments"] >= 250:
            print("Valanyr obtained!")
            item_useful["fragments"] -= 250
            obtained = True
            break
        elif item_useful["shards"] >= 250:
            print("Shadowmourne obtained!")
            item_useful["shards"] -= 250
            obtained = True
            break
    if obtained:
        break
    input_items = input().split()


for keys, value in item_useful.items():
    print(f"{keys}: {value}")
for keys, value in item_useless.items():
    print(f"{keys}: {value}")
```
```Python 
def print_func(legendary_items_dict, junk_items_dict, special_item):
    print(f'{special_item} obtained!')
    print(f"shards: {legendary_items_dict['shards']}")
    print(f"fragments: {legendary_items_dict['fragments']}")
    print(f"motes: {legendary_items_dict['motes']}")

    for key, value in junk_items_dict.items():
        print(f'{key}: {value}')


def legendary_farming():
    legendary_items_dict = {'shards': 0, 'fragments': 0, 'motes': 0}
    junk_items_dict = {}
    while_condition = False

    while True:
        items = input().lower()
        items = items.split(' ')

        for value, material in zip(items[0::2], items[1::2]):
            material = material.lower()
            value = int(value)

            if material in ['shards', 'fragments', 'motes']:
                if material not in legendary_items_dict:
                    legendary_items_dict[material] = value
                else:
                    legendary_items_dict[material] += value

                if legendary_items_dict[material] >= 250:
                    legendary_items_dict[material] -= 250
                    special_item = ''
                    if material == 'shards':
                        special_item = 'Shadowmourne'
                    elif material == 'fragments':
                        special_item = 'Valanyr'
                    elif material == 'motes':
                        special_item = 'Dragonwrath'

                    print_func(legendary_items_dict, junk_items_dict, special_item)
                    while_condition = True

            else:
                if material not in junk_items_dict:
                    junk_items_dict[material] = value
                else:
                    junk_items_dict[material] += value

            if while_condition:
                break
        if while_condition:
            break

legendary_farming()
```
</details>

> ### 6. Orders

<details><summary>🛠️Condition</summary>

Write a program that **keeps the information** about **products** and their **prices**. 
Each product has a name, a price, and a quantity:
* **If the product doesn't exist** yet, **add** it with its starting quantity.
*  **If you receive a product**, that **already exists**, increase its quantity by the **input quantity** and if its price is **different**, **replace** the price as well.
You will receive products' names, prices, and quantities on new lines. Until you receive the command "buy", keep adding items. 
* Finally, **print** all items with their **names** and the **total price of each product**.
#### Input
*  Until you receive "**buy**", the products will be coming in the format: **"{name} {price} {quantity}"**.
* The product data is always delimited by a **single space**.
#### Output
* Print information about each product in the following format: **"{product_name} -> {total_price}"**
* **Format** the total price to the **2nd digit** after the decimal separator.

Example

| Input	                                                                                        | Output  	                                                                            |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| Beer 2.20 100<br>IceTea 1.50 50<br>NukaCola 3.30 80<br>Water 1.00 500<br>buy                  | Beer -> 220.00<br>IceTea -> 75.00<br>NukaCola -> 264.00<br>Water -> 500.00           |
| Beer 2.40 350<br>Water 1.25 200<br>IceTea 5.20 100<br>Beer 1.20 200<br>IceTea 0.50 120<br>buy | Beer -> 660.00<br>Water -> 250.00<br>IceTea -> 110.00                                |
| CesarSalad 10.20 25<br>SuperEnergy 0.80 400<br>Beer 1.35 350<br>IceCream 1.50 25<br>buy       | CesarSalad -> 255.00<br>SuperEnergy -> 320.00<br>Beer -> 472.50<br>IceCream -> 37.50 |

</details>

<details> <summary>🐍Code</summary>

```Python 
dict_products = {}

input_info = input()

while input_info != "buy":
    input_info = input_info.split(" ")
    names, prices, quantities = input_info[0], float(input_info[1]), int(input_info[2])

    if names in dict_products:
        existing_prices, existing_quantities = dict_products[names]
        dict_products[names] = (prices, existing_quantities + quantities)
    else:
        dict_products[names] = (prices, quantities)

    input_info = input()

for names, (prices, quantities) in dict_products.items():
    total_price = prices * quantities
    print(f"{names} -> {total_price:.2f}")
```
```Python
def orders_func(dict_products, input_info):
    names = input_info[0]
    price = float(input_info[1])
    quantity = int(input_info[2])

    if names in dict_products:
        dict_products[names] = [price, (quantity + dict_products[names][1])]
    else:
        dict_products[names] = [price, quantity]

    return dict_products

def orders():

    dict_products = {}
    input_info = input()
    while  input_info != 'buy':

        input_info = input_info.split(' ')
        dict_products = orders_func(dict_products, input_info)
        input_info = input()
        
    for k in dict_products:
        total_sum = dict_products[k][0] * dict_products[k][1]
        print(f'{k} -> {total_sum:.2f}')

orders()
```
```Python
dict_products = {}

input_info = input()
while input_info != "buy":
    names, price, quantity = [item for item in input_info.split()]

    dict_products[names] = dict_products.get(names, {"price": 0, "quantity": 0})
    dict_products[names]['price'] = float(price)
    dict_products[names]['quantity'] += int(quantity)


    input_info = input()

for key, value in dict_products.items():
    print(f"{key} -> {value['price'] * value['quantity']:.2f}")
```
</details>

> ### 7. SoftUni Parking

<details><summary>🛠️Condition</summary>

SoftUni just got a new fancy **parking lot**. It even has online **parking validation**, except the online service doesn't work. It can only receive users' data, but it doesn't know what to do with it. Good thing you're on the dev team and know how to fix it, right?
Write a program, which validates a parking place - users can register to enter the park and unregister to leave.
The program receives 2 types of commands:

* **"register {username} {license_plate_number}"**:
  *The system only supports one car per user at the moment, so if a user tries to register another license plate using the same username, the system should print: "ERROR: already registered with plate number {license_plate_number}"
  * If the check above passes successfully, the user should be registered, so the system should print: "{username} registered {license_plate_number} successfully"
* **"unregister {username}"**:
  * If the user is not present in the database, the system should print: "ERROR: user {username} not found"
  * If the check above passes successfully, the system should print: "{username} unregistered successfully"

After you execute all of the commands, print all the currently registered users and their license plates in the format:
  * • **"{username} => {license_plate_number}"**
### Input
  * • First line: n - number of commands - **integer**
  * • Next n lines: commands in one of the two possible formats:
    * o Register: **"register {username} {license_plate_number}"**
    * o Unregister: **"unregister {username}"**
    
The input will always be valid, and you do not need to check it explicitly.

Example

| Input	                                                                                                                                                     | Output  	                                                                                                                                                                                                                                                                                                        |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 5<br>register John CS1234JS<br>register George JAVA123S<br>register Andy AB4142CD<br>register Jesica VR1223EE<br>unregister Andy                           | John registered CS1234JS successfully<br>George registered JAVA123S successfully<br>Andy registered AB4142CD successfully<br>Jesica registered VR1223EE successfully<br>Andy unregistered successfully<br>John => CS1234JS<br>George => JAVA123S<br>Jesica => VR1223EE                                           |
| 4<br>register Jony AA4132BB<br>register Jony AA4132BB<br>register Linda AA9999BB<br>unregister Jony                                                        | Jony registered AA4132BB successfully<br>ERROR: already registered with plate number AA4132BB<br>Linda registered AA9999BB successfully<br>Jony unregistered successfully<br>Linda => AA9999BB                                                                                                                   |
| 6<br>register Jacob MM1111XX<br>register Anthony AB1111XX<br>unregister Jacob<br>register Joshua DD1111XX<br>unregister Lily<br>register Samantha AA9999BB | Jacob registered MM1111XX successfully<br>Anthony registered AB1111XX successfully<br>Jacob unregistered successfully<br>Joshua registered DD1111XX successfully<br>ERROR: user Lily not found<br>Samantha registered AA9999BB successfully<br>Anthony => AB1111XX<br>Joshua => DD1111XX<br>Samantha => AA9999BB |

</details>

<details> <summary>🐍Code</summary>


```Python
dict_registered = {}

reg_num = int(input())

for _ in range(reg_num):
    info_string = input().split(" ")

    if len(info_string) == 3:
        type_register, name, reg_num = [item for item in info_string]

        if type_register == "register":
            if name not in dict_registered:
                dict_registered[name] = reg_num
                print(f"{name} registered {reg_num} successfully")
            else:
                print(f"ERROR: already registered with plate number {dict_registered[name]}")

    elif len(info_string) == 2:
        type_register, name = [item for item in info_string]
        if type_register == "unregister":
            if name in dict_registered:
                del dict_registered[name]
                print(f"{name} unregistered successfully")
            else:
                print(f"ERROR: user {name} not found")

for name, license in dict_registered.items():
    print(f"{name} => {license}")

```
```Python
""" Ivan Shopov solution"""
parking = {}
n = int(input())
for i in range(n):
    command = input().split()
    action = command[0]

    if action == "register":
        key = command[1]
        value = command[2]
        if key in parking.keys():
            print(f"ERROR: already registered with plate number {parking[key]}")
        else:
            parking[key] = value
            print(f"{key} registered {value} successfully")
    elif action == "unregister":
        key = command[1]
        if key in parking.keys():
            del parking[key]
            print(f"{key} unregistered successfully")
        else:
            print(f"ERROR: user {key} not found")
for key in parking.keys():
    print(f"{key} => {parking[key]}")
```
```Python
""" kumchovalcho solution """
def register(username: str, car_plate: str):
    if username in parking:
        return f"ERROR: already registered with plate number {car_plate}"

    parking[username] = car_plate
    return f"{username} registered {car_plate} successfully"


def unregister(username: str):
    if username not in parking:
        return f"ERROR: user {username} not found"

    parking.pop(username)
    return f"{username} unregistered successfully"


parking = {}

commands = {
    'register': register,
    'unregister': unregister,
    }

number_of_operations = int(input())
for _ in range(number_of_operations):
    command, name, *license_plate = input().split()

    print(commands[command](name, *license_plate))

for name, plate in parking.items():
    print(f"{name} => {plate}")
```
</details>

> ### 8. Courses
<details><summary>🛠️Condition</summary>

Write a program that **keeps the information about courses**. Each **course** has a name and registered **students**.
You will be **receiving** a **course name** and a **student name** until you receive the command **"end"**.
You should register each user into the corresponding course. **If** the given course **does not** exist, **add it**.
When you **receive** the command **"end"**, print the courses with their **names** and **total registered users**. 
For each course, print the registered users.
### Input
* Until the "end" command is received, you will be receiving input lines in the format:

**"{course_name} : {student_name}"**
 * The product data is always delimited by **" : "**
### Output
* Print the information about each **course** in the following **format**: 
 **"{course_name}: {registered_students}"**
* Print the information about each **student** in the following **format**: 
**"-- {student_name}"**

Example

| Input                                                                                                                                                                                                                | Output                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Programming Fundamentals : John Smith<br>Programming Fundamentals : Linda Johnson<br>JS Core : Will Wilson<br>Java Advanced : Harrison White<br>end                                                                  | Programming Fundamentals: 2<br>-- John Smith<br>-- Linda Johnson<br>JS Core: 1<br>-- Will Wilson<br>Java Advanced: 1<br>-- Harrison White                                          |
| Algorithms : Jay Moore<br>Programming Basics : Martin Taylor<br>Python Fundamentals : John Anderson<br>Python Fundamentals : Andrew Robinson<br>Algorithms : Bob Jackson<br>Python Fundamentals : Clark Lewis<br>end | Algorithms: 2<br>-- Jay Moore<br>-- Bob Jackson<br>Programming Basics: 1<br>-- Martin Taylor<br>Python Fundamentals: 3<br>-- John Anderson<br>-- Andrew Robinson<br>-- Clark Lewis |


</details>

<details> <summary>🐍Code</summary>


```Python
dict_courses = {}

courses_info = input()
while courses_info != "end":
    info = courses_info.split(" : ")
    if len(info) > 1:

        course_name, student_name = [item for item in info]
        if course_name not in dict_courses:
            dict_courses[course_name] = [student_name]
        else:
            if student_name not in dict_courses[course_name]:
                dict_courses[course_name].append(student_name)

    courses_info = input()

for course_name, registered_students in dict_courses.items():
    print(f"{course_name}: {len(registered_students)}")
    for student_name in registered_students:
        print(f"-- {student_name}")
```
```Python
dict_courses = {}

courses_info = input()
while courses_info != "end":
    courses = courses_info.split(" : ")
    course_name, student_name = courses[0], courses[1]

    dict_courses[course_name] = dict_courses.get(course_name,  {})
    dict_courses[course_name][student_name] = student_name

    courses_info = input()

for key, value in dict_courses.items():
    print(f"{key}: {len(dict_courses[key])}")
    for name in dict_courses[key]:
        print(f"-- {dict_courses[key][name]}")  
```
</details>

> ### 9. Student Academy
<details><summary>🛠️Condition</summary>

Write a program that **keeps** the information about **students and their grades**.<br>
On the **first line**, you will receive an **integer number** representing the next pair of rows. <br>
On the **next lines**, you will be receiving each **student's name and their grade**.****
**Keep** track of **all grades for each student** and **keep only** the students with an average grade **higher** than or **equal to 4.50**.

**Print** the final dictionary with students and their average grade in the following format:

**"{name} -> {averageGrade}"**

**Format** the average grade to the **2nd decimal place**.

Example

| Input                                                                            | Output                                             |
|----------------------------------------------------------------------------------|----------------------------------------------------|
| 5<br>John<br>5.5<br>John<br>4.5<br>Alice<br>6<br>Alice<br>3<br>George<br>5       | John -> 5.00<br>Alice -> 4.50<br>George -> 5.00    |
| 5<br>Amanda<br>3.5<br>Amanda<br>4<br>Rob<br>5.5<br>Christian<br>5<br>Robert<br>6 | Rob -> 5.50<br>Christian -> 5.00<br>Robert -> 6.00 |

</details>

<details> <summary>🐍Code</summary>

```Python
""" whit list for grades"""
students = {}
student_number = int(input())

for _ in range(student_number):
    name, grade = input(), float(input())
    if name not in students:
        students[name] = [grade]
    else:
        students[name].append(grade)

for name, grades in students.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.5:
        # students[name] = {"grades": grades, "average_grade": average_grade}
        print(f"{name} -> {average_grade:.2f}")
# print(students)
```
```Python
""" whit nested dict for grades"""

number_students = int(input())

students_grades = {}

for _ in range(number_students):
    name = input()
    grade = float(input())
    if name not in students_grades:
        students_grades[name] = {}
        students_grades[name][name + str(grade)] = 0
    if name in students_grades:
        students_grades[name][name + str(grade)] = 0
    students_grades[name][name + str(grade)] += grade

for name_student in students_grades:
    score = 0
    for key, value in students_grades[name_student].items():
        score += value
    average_score = score / len(students_grades[name_student])
    if average_score >= 4.50:
        print(f"{name_student} -> {average_score:.2f}")
print(students_grades)
```
```Python
""" whit Function and  list for grades"""

students_with_grades = dict()


def main():
    pair_of_rows = int(input())
    for pair in range(pair_of_rows):
        student_name = input()
        student_grade = float(input())

        if student_name not in students_with_grades:
            students_with_grades[student_name] = []

        students_with_grades[student_name].append(student_grade)

    average_grade_checker()


def average_grade_checker():
    for student in students_with_grades:
        average_grade = sum(students_with_grades[student]) / len(students_with_grades[student])
        if average_grade >= 4.50:
            print(f"{student} -> {average_grade:.2f}")
    print(students_with_grades)
main()
```
</details>


> 10. Company Users

<details><summary>🛠️Condition</summary>

Write a program that **keeps the information about companies and their employees**.<br>
You will be receiving **company names** and an **employees**' id until you receive the **command "End"** command.<br> 
Add each employee to the given company. **Keep** in mind that a company cannot have two employees with the same id.<br>
Print the company name and each employee's id in the following format:

**{company_name}**
**-- {id1}**
**-- {id2}**
**…**
**-- {idN}"**
#### Input / Constraints

* Until you receive the **"End"** command, you will be receiving input in the format:<br>
**"{company_name} -> {employee_id}"**
* The input always will be valid.

Example

| Input                                                                                                             | Output                                                                                |
|-------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| SoftUni -> AA12345<br>SoftUni -> BB12345<br>Microsoft -> CC12345<br>HP -> BB12345<br>End                          | SoftUni<br>-- AA12345<br>-- BB12345<br>Microsoft<br>-- CC12345<br>HP<br>-- BB12345    |
| SoftUni -> AA12345<br>SoftUni -> CC12344<br>Lenovo -> XX23456<br>SoftUni -> AA12345<br>Movement -> DD11111<br>End | SoftUni<br>-- AA12345<br>-- CC12344<br>Lenovo<br>-- XX23456<br>Movement<br>-- DD11111 |

</details>

<details> <summary>🐍Code</summary>

```Python
"""  dictionary whit value[list]"""

companies_info = input()
dict_compani = {}

while companies_info != "End":
    compani, reg_num = companies_info.split(" -> ")

    if compani not in dict_compani:
        dict_compani[compani] = [reg_num]
    else:
        if reg_num not in dict_compani[compani]:
            dict_compani[compani].append(reg_num)

    companies_info = input()

for compani, register_list in dict_compani.items():
    print(compani)
#     for reg_number in register_list:
#         print(f"-- {reg_number}")
    [print(f"-- {reg_num}") for reg_num in register_list]
```
```Python
""" Ivan Shopov  whit sorted dictionary"""

companies = {}
command = input().split(" -> ")
while command[0] != "End":
    company = command[0]
    id = command[1]
    if company in companies.keys():
        if id not in companies[company]:
            companies[company].append(id)
    else:
        companies[company] = []
        companies[company].append(id)
    command = input().split(" -> ")
companies = dict(sorted(companies.items(), key=lambda x: (x[0])))
for value in companies.values():
    value = sorted(value, key=lambda x: (value))
for key in companies.keys():
    print(f"{key}")
    for value in companies[key]:
        print(f"-- {value}")
```
```Python
""" CEO - whit Function and whit value{dictionary} """

command = input()

company_info = {}


def employee_id_search(id):
    for value in company_info[id].values():
        if id == value:
            return True
    return False

while command != "End":
    company_name, employee_id = command.split(" -> ")
    company_info[company_name] = company_info.get(company_name, {})
    if not employee_id_search(company_name):
        company_info[company_name][employee_id] = employee_id
    command = input()

for name_uni in company_info:
    print(name_uni)
    for key, value in company_info[name_uni].items():
        print(f"-- {value}")
```
</details>

> 11. *Force Book

<details><summary>🛠️Condition</summary>

The force users struggle to remember which side is the different force users from because they switch them too often. So you are tasked to create a web application to manage their profiles. You should store information for every unique force user registered in the application.
You will receive several input lines in one of the following formats:

**"{force_side} | {force_user}"**<br>
**"{force_user} -> {force_side}"**

The **"force_user"** and **"force_side"** are **strings**, containing any character.

If you **receive "force_side | force_user":**

* If there is **no such force user and no such force side** -> **create** a **new force** side and add the force user to the corresponding side.
* **Only** if there **is no such force user in any force side** -> **add** the **force user** to the corresponding side.
* **If there is such** force user **already** -> **skip** the **command** and **continue** to the next operation.

If you receive a **"force_user -> force_side":**

* If there is **such force user already** -> **change** their side.
* If there is **no such force user** in any force side -> **add** the force user to the corresponding force side.
* If there is **no such force user** and **no such force side** -> **create new force** side and add the force user to the corresponding side.

* Then you should print on the console: **"{force_user} joins the {force_side} side!"**.

You should end your program when you **receive** the command **"Lumpawaroo"**. 
At that **point**, you should print each force side. **For each side, print the force users.**
In case there are no forced users on a side, **you shouldn't print the side information**.
#### Input / Constraints
* The input comes in the form of commands in one of the formats specified above.
* The input ends when you receive the command **"Lumpawaroo"**.
#### Output
* As output for each force side, you must print all the force users.
* The output format is:

**Side: {force_side}, Members: {force_users_count}**
**! {force_user1}**
**! {force_user2}**
**…**
**! {force_userN}"**

* In case there are **NO** force users on a side, **don't print this side**.

Example

| Input                                                                                       | Output                                                                                                                                |
|---------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Light ! Peter<br>Dark ! Kim<br>Light ! Kim<br>Lumpawaroo                                    | Side: Light, Members: 1<br>! Peter<br>Side: Dark, Members: 1<br>! Kim                                                                  |
| Lighter ! Royal<br>Darker ! DCay<br>Ivan Ivanov -> Lighter<br>DCay -> Lighter<br>Lumpawaroo | Ivan Ivanov joins the Lighter side!<br>DCay joins the Lighter side!<br>Side: Lighter, Members: 3<br>! Royal<br>! Ivan Ivanov<br>! DCay |

</details>

<details> <summary>🐍Code</summary>


```Python
force_book = {}
input_info = input()

while input_info != "Lumpawaroo":
    if "|" in input_info:
        side, user = input_info.split(" | ")
        # Инициализация на страната в речника, ако тя все още не съществува
        force_book[side] = force_book.get(side, [])
        # Проверка за потребителя в други страни
        no_user = True
        for key in force_book:
            if user in force_book[key]:
                no_user = False
                break
        # Ако потребителят не съществува в други страни, се добавя към текущата
        if no_user:
            force_book[side].append(user)

    elif "->" in input_info:
        user, side = input_info.split(" -> ")
        # Проверка за съществуване на потребителя в други страни и премахване от тях
        for key in force_book:
            if user in force_book[key]:
                force_book[key].remove(user)
        # Инициализация на новата страна в речника, ако тя все още не съществува
        force_book[side] = force_book.get(side, [])
        # Добавяне на потребителя към новата страна
        force_book[side].append(user)

        print(f"{user} joins the {side} side!")
        
    input_info = input()


for side in force_book:
    if force_book[side]:
        print(f"Side: {side}, Members: {len(force_book[side])}")
        for names in range(len(force_book[side])):
            print(f"! {force_book[side][names]}")

```
```Python
force_side_dict = {}
while True:
    command = input()
    if command == 'Lumpawaroo':
        break
    if ' | ' in command:
        force_side, force_user = command.split(' | ')
        present = 0
        for k, v in force_side_dict.items():
            if force_user in v:
                present = 1
        if present == 0:
            if force_side not in force_side_dict:
                force_side_dict[force_side] = [force_user]
            else:
                if force_user not in force_side_dict[force_side]:
                    force_side_dict[force_side].append(force_user)
    else:
        force_side, force_user = command.split(' -> ')
        present = 0
        for k, v in force_side_dict.items():
            if force_user in v:
                force_side_dict[k].pop(v.index(force_user))
                present = 1
        if present == 1:
            if force_side not in force_side_dict:
                force_side_dict[force_side] = [force_user]
            else:
                force_side_dict[force_side] += [force_user]
        else:
            if force_side not in force_side_dict:
                force_side_dict[force_side] = [force_user]
            else:
                force_side_dict[force_side] += [force_user]
        print(f"{force_user} joins the {force_side} side!")

for i in force_side_dict:
    if len(force_side_dict[i]) > 0:
        print(f"Side: {i}, Members: {len(force_side_dict[i])}")
        [print(f"! {i}") for i in (force_side_dict[i])]
```

</details>

> 12. *SoftUni Exam Results


<details><summary>🛠️Condition</summary>

Judge statistics on the last Programming Fundamentals exam were not working correctly, 
so you have the task of taking all the submissions and analyzing them properly. 
You should collect all the submissions and print the final results and 
statistics about each language in which the participants submitted their solutions.

You will be receiving lines in the following format: **"{username}-{language}-{points}"** until you receive **"exam finished"**. 
You should store each username and their submissions and points. 
If a student has two or more submissions for the **same language**, save only his **maximum points**.
You can receive a command to ban a user for cheating in the following format: **"{username}-banned"**. 
In that case, you should remove the user from the contest but **preserve his submissions in the total count of submissions for each language**.
After receiving the "exam finished", print each of the participants in the following format:

Results:
**{username1} | {points}<br>
{username2} | {points}<br>
…<br>
{usernameN} | {points}**


After that, print each language used in the exam in the following format:


Submissions:

**{language1} - {submissions_count}<br>
{language2} - {submissions_count}<br>
…<br>
{language3} - {submissions_count}<br>**


#### Input / Constraints
Until you receive "exam finished" you will be receiving participant submissions in the following format: **"{username}-{language}-{points}"**
You can receive a ban command -> **"{username}-banned"**
The points of the participant will always be a **valid integer in the range** [0-100];
#### Output
* Print the **exam results for each participant**
* After that, print **each language in the format shown above**
* Allowed working time **/ memory: 100ms / 16MB**

Example

| Input                                                                                       | Output                                                                                  |
|---------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| Peter-Java-84<br>George-C#-84<br>George-C#-70<br>Katy-C#-94<br>exam finished                | Results:<br>Peter \ 84<br>George\ 84<br>Katy \ 94<br>Submissions:<br>Java - 1<br>C# - 3 |
| Peter-Java-91<br>George-C#-84<br>Katy-Java-90<br>Katy-C#-50<br>Katy-banned<br>exam finished | Results:<br>Peter \ 91<br>George \ 84<br>Submissions:<br>Java - 2<br>C# - 2             |


</details>

<details> <summary>🐍Code</summary>


```Python
university = {}
language_counts = {}
collect = input()

while collect != "exam finished":
    if "banned" in collect.split("-"):
        username = collect.split("-")[0]
        del university[username]
    else:
        username, language, points = collect.split("-")
        language_counts[language] = language_counts.get(language, 0) + 1
        points = int(points)
        if username not in university:
            university[username] = {language: points}
        else:
            if language not in university[username]:
                university[username][language] = points
            else:
                if points > university[username][language]:
                    university[username][language] = points

    collect = input()
# print(university)
# print(language_counts)
print("Results:")
for user, scores in university.items():
    for language, points in scores.items():
        print(f"{user} | {points}")

print("Submissions:")
for language, count in language_counts.items():
    print(f"{language} - {count}")

```
```Python
university = {}

collect = input()
while collect != "exam finished":
    if "banned" in collect.split("-"):
        username = collect.split("-")[0]
        del university[language]["users"][username]
    else:
        username, language, points = collect.split("-")
        points = int(points)
        if language not in university:
            university[language] = {"count": 1, "users": {username: points}}
        else:
            university[language]["count"] += 1
            if username not in university[language]["users"]:
                university[language]["users"][username] = points
            else:
                if points > university[language]["users"][username]:
                    university[language]["users"][username] = points

    collect = input()

print("Results:")
for language, data in university.items():
    for user, points in data["users"].items():
        print(f"{user} | {points}")

print("Submissions:")
for language, data in university.items():
    print(f"{language} - {data['count']}")
```
</details>



</details>END

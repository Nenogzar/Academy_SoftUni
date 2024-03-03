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
</details>END

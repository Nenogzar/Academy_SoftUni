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
  </tr>
  <tr>
    <td>
    <a href="https://github.com/Nenogzar/Academy_SoftUni/tree/main/fundamentals_python/lectures/25-26_Dictionaries/01_Dictionaries%20-%20Lab">Lab</a>
  |  
    <a href="https://github.com/Nenogzar/Academy_SoftUni/tree/main/fundamentals_python/lectures/25-26_Dictionaries/02_Dictionaries%20-%20Exercise/Exercise">Exercise</a>
  |  
    <a href="https://github.com/Nenogzar/Academy_SoftUni/tree/main/fundamentals_python/lectures/25-26_Dictionaries/03_Dictionaries%20-%20More%20Exercises/Exercise">More</a>
    </td>
  </tr>
</table>


[judge](https://judge.softuni.org/Contests/Practice/Index/1736)

><details><summary>01. Bakery</summary>

<details><summary>🛠️Condition</summary>

Your first task at your new job is to create a table of the stock in a bakery, and you really don't want to fail on your first day at work.
You will receive a single line containing some food (**keys**) and quantities (**values**). 
They will be separated by a **single space** (the first element is the key, the second – is the value, and so on). 
**Create a dictionary with all the keys and values and print it on the console.**

Example

| Input	| Output  	|
|-------|-----------|
|bread 10 butter 4 sugar 9 jam 12|{'bread': 10, 'butter': 4, 'sugar': 9, 'jam': 12}|
|eggs 3 sugar 7 salt 1 butter 3|{'eggs': 3, 'sugar': 7, 'salt': 1, 'butter': 3}|

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
</details>

><details><summary>02. Stock</summary>


<details><summary>🛠️Condition</summary>

_After you have completed your first task, your boss decides to give you another one right away._ 
_Now, not only do you have to keep track of the stock, but you also need to answer customers about product availability._
You will be given **key-value** pairs of products and quantities (on a single line separated by space). 
On the following line, you will be given products to search for. Check for each product. You have **2 possibilities:**

* If you have the product, print **"We have {quantity} of {product} left"**.
* Otherwise, print **"Sorry, we don't have {product}"**.

#### Example

| Input	| Output  	|
|-------|-----------|
|cheese 10 bread 5 ham 10 chocolate 3</br>jam cheese ham tomatoes|Sorry, we don't have jam</br>We have 10 of cheese left</br>We have 10 of ham left</br>Sorry, we don't have tomatoes|
|eggs 5 bread 10</br>bread eggs|We have 10 of bread left</br>We have 5 of eggs left|

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
</details>

><details><summary>3. Statistics</summary>

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

| Input	| Output  	|
|-------|-----------|
|bread: 4</br>cheese: 2</br>ham: 1</br>bread: 1</br>statistics|Products in stock:</br>- bread: 5</br>- cheese: 2</br>- ham: 1</br>Total Products: 3</br>Total Quantity: 8|
|eggs: 10</br>bread: 6</br>cheese: 8</br>milk: 7</br>statistics|Products in stock:</br>- eggs: 10</br>- bread: 6</br>- cheese: 8</br>- milk: 7</br>Total Products: 4</br>Total Quantity: 31|


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
</details>

><details><summary>EXAMP</summary>


<details><summary>🛠️Condition</summary>




Example


| Input	| Output  	|
|-------|-----------|
|       |     		|
|  		|    		|
|  		|  			|


</details>

<details> <summary>🐍Code</summary>


```Python
 

```

</details>
</details>
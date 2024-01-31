# Functions - lab
[judge](https://judge.softuni.org/Contests/1727/Functions-Lab)
* Functions Overview;
* Declaring and Invoking Functions;
* Return Values;
* Lambda Functions;
* Parameters vs Arguments.


## 1.	Absolute Values 
<details><summary>Condition</summary>

Write a program that receives a sequence of numbers, separated by a single space, and prints their absolute value as a list. Use abs().


Example

| Input         | Output                 |
|---------------|------------------------|
| 1 2.5 -3 -4.5 | [1.0, 2.5, 3.0, 4.5]   |
| -0 1 10 -6.66 | [0.0, 1.0, 10.0, 6.66] |

</details>
<details> <summary>Code</summary>

```Python
main_list = [float(num) for num in input().split()]

def abs_value(main_list):
    result = [abs(lement) for lement in main_list]
    return print(result)

abs_value(main_list)
```
</details>

## 2. Grades 
<details> <summary>Condition</summary>
Write a function that receives a grade between 2.00 and 6.00 and print the corresponding grade in words.

* 2.00 – 2.99 - "**Fail**"
* 3.00 – 3.49 - "**Poor**"
* 3.50 – 4.49 - "**Good**"
* 4.50 – 5.49 - "**Very Good**"
* 5.50 – 6.00 - "**Excellent**"

Examples

| Input | Output |
|-------|--------|
|3.33|Poor|
|4.50|Very Good|
|2.99|Fail|

</details>
<details> <summary>Code</summary>

```Python
grades = float(input())

def grade_check(grade):
    if 2.00 <= grade <= 2.99:
        return print("Fail")
    elif 3.00 <= grade <= 3.49:
        return print("Poor")
    elif 3.50 <= grade <= 4.49:
        return print("Good")
    elif 4.50 <= grade <= 5.49:
        return print("Very Good")
    elif 5.50 <= grade <= 6:
        return print("Excellent")

grade_check(grades)
```
</details>

## 3. Calculations

<details> <summary>Condition</summary>

Create a function that receives three parameters, **calculates** a result depending on the given operator, and **returns** it. Print the result of the function.
The input comes as three parameters – an operator as a string and two integer numbers. The operator can be one of the following:  **"multiply", "divide", "add",** and **"subtract"**.

Example

| Input                | Output |
|----------------------|--------|
| subtract</br>5</br>4 | 1      |
| divide</br>8</br>4   | 2      |




</details>
<details> <summary>Code</summary>

```Python
def operation_multiply(num1, num2):
    operation = num1 * num2
    return operation

def operation_divide(num1, num2):
    if num2 == 0:
        print("Cannot divide by zero!")
    else:
        operation = num1 / num2
        return operation

def operation_add(num1, num2):
    operation = num1 + num2
    return operation

def operation_subtract(num1, num2):
    operation = num1 - num2
    return operation

def calculation(operator, num1, num2):  
    if operator.lower() == "multiply":
        print(f"{operation_multiply(num1, num2):.0f}")
    elif operator.lower() == "divide":
        print(f"{operation_divide(num1, num2):.0f}")
    elif operator.lower() == "add":
        print(f"{operation_add(num1, num2):.0f}")
    elif operator.lower() == "subtract":
        print(f"{operation_subtract(num1, num2):.0f}")
    else:
        print("Wrong command!")

def main():
    operator = input()
    num1 = int(input())
    num2 = int(input())
    calculation(operator, num1, num2)

if __name__ == "__main__":
    main()

```

</details>

    
## 4. Repeat String

<details> <summary>Condition</summary>

Write a function that receives a string and a counter **n**. 
The function should **return** a new **string** – the result of repeating the old string n times. 
**Print the result of the function**. Try using **lambda**.
Examples

| Input        | Output       |
|--------------|--------------|
| abc</br>3    | abcabcabc    |
| String</br>2 | StringString |


</details>
<details> <summary>Code</summary>
whit string

```Python
def repeat_string(input_string, repeat_range):
    result_string = ''

    for _ in range(repeat_range):
        result_string += input_string

    return result_string


string_input = input()
repeat_range = int(input())

result = repeat_string(string_input, repeat_range)
print(result)
```
whit list

```Python
string_input = input()
repeat_range = int(input())
new_string = []

for _ in range(repeat_range):
    new_string.append(string_input)

result_string = ''.join(new_string)
print(result_string)
```
whit list in Function
```Python
def repeat_string(input_string, repeat_range):
    new_string = []

    for _ in range(repeat_range):
        new_string.append(input_string)

    result_string = ''.join(new_string)
    return result_string


string_input = input()
repeat_range = int(input())

result = repeat_string(string_input, repeat_range)
print(result)
```
solution of the task by CIO
```Python
string_to_show = input()
number_to_multi_string = int(input())

def multi_strint(string_show, number):
    result = string_show * number
    return result

print(multi_strint(string_to_show, number_to_multi_string))
```
</details>

## 5. Orders

<details> <summary>Condition</summary>
Write a function that calculates the total price of an order and returns it. 
The function should receive one of the following products: **"coffee", "coke", "water"**, or **"snacks"**, 
and a quantity of the product. The prices for a single **piece** of each product are:

* coffee - 1.50</br>
* water - 1.00</br>
* coke - 1.40</br>
* snacks - 2.00</br>

Print the result **formatted** to the **second decimal place**.

### Example

| Inout        | Output |
|--------------|--------|
| water</br>5  | 5.00   |
| coffee</br>2 | 3.00   |


</details>
<details> <summary>Code</summary>

```Python
def order(products, quantity_products):
    price = 0.00
    if products == "coffee":
        price = 1.50
    elif products == "coke":
        price = 1.40
    elif products == "water":
        price = 1.00
    elif products == "snacks":
        price = 2.00
    else:
        print("Wrong order product")

    total_order = price * quantity_products
    print(f"{total_order:.2f}")

products = input()
quantity_products = int(input())

order(products, quantity_products)
```
whit dictionary
```Python
def order(products, quantity_products):
    price = product_prices.get(products)

    if price is None:
        print("Wrong order product")
        return

    total_order = price * quantity_products
    print(total_order)


products_input = input()
quantity_input = int(input())

order(products_input, quantity_input)
```
</details>

## 6. Calculate Rectangle Area
<details> <summary>Condition</summary>

Create a function that **calculates** and **returns** the **area** of a **rectangle** by a given **width** and **height**. 
**Print the resul**t on the console.
### Example

| Input   | Output |
|---------|--------|
| 3</br>4 | 12     |
| 6</br>2 | 12     |

</details>
<details> <summary>Code</summary>

```Python
width  = int(input())
height = int(input())
def rectangle_area(a, b):
    area = a * b
    return area

print(rectangle_area(width, height))
```
### whit lambda function
```Python
a, b = int(input()), int(input())
area_calculation = lambda side_a, side_b: side_a * side_b
print(area_calculation(a, b))
```
</details>

## 7. Rounding

<details> <summary>Condition</summary>

Write a program that rounds all the given numbers, separated by a single space, and prints the result as a list. Use round().
### Example

| Input             | Output        |
|-------------------|---------------|
| 1.0 2.5 3.0 4.5   | [1, 2, 3, 4]  |
| 2.56 1.9 -3.4 8.1 | [3, 2, -3, 8] |
</details>
<details> <summary>Code</summary>

```Python
```

</details>
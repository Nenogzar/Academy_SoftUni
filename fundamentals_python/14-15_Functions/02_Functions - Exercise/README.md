# Functions - Exercise

[judge](https://judge.softuni.org/Contests/1728/Functions-Exercise)</br>
[link problems](https://judge.softuni.org/Contests/Compete/DownloadResource/40497)


## 1. Smallest of Three Numbers

<details><summary>Condition</summary>

Write a function that receives **three intege**r numbers and returns the **smallest**.
Print the result on the console. Use an appropriate name for the function.

Example

| Input               | Output |
|---------------------|--------|
| 2</br>5</br>3       | 2      |
| 600</br>342</br>123 | 123    |
| 25</br>21</br>4     | 4      |

</details>
<details> <summary>Code</summary>

```Python
n1, n2, n3 = int(input()), int(input()), int(input())
min_num = min(n1, n2, n3)
print(min_num)
```

whit function

```Python
def find_smallest(num1, num2, num3):
    return min(num1, num2, num3)


num1, num2, num3 = int(input()), int(input()), int(input())

print(find_smallest(num1, num2, num3))
```

```Python
print(min(int(input()), int(input()), int(input())))
```

</details>

## 2. Add and Subtract

<details><summary>Condition</summary>

You will receive **three integer numbers**.</br>
Write functions named:</br>

* **sum_numbers()** that returns the sum of the **first two** integers</br>
* **subtract()** that returns the **difference** between the **returned result** of the first function and the third
  integer</br>

Wrap the two functions in a function named **add_and_subtract()** which will receive the three numbers as parameters.
Print the result of the **subtract()** function on the console.</br>

Example

| Input             | Output |
|-------------------|--------|
| 23</br>6</br>10   | 19     |
| 1</br>17</br>30   | -12    |
| 42</br>58</br>100 | 0      |

</details>
<details> <summary>Code</summary>
basic

```Python
sum_numbers = int(input()) + int(input())
subtract = sum_numbers - int(input())
print(subtract)
```

```Python
print((int(input()) + int(input())) - int(input()))
```

whit function

```Python
def substract_number(num1, num2, num3):
    sub = (num1 + num2) - num3
    return sub


a, b, c = int(input()), int(input()), int(input())
print(substract_number(a, b, c))
```

task solution by mario zahariev whit lambda()

```Python
sum_numbers = lambda num1, num2: num1 + num2
subtract = lambda result, num3: result - num3
add_and_subtract = lambda num1, num2, num3: subtract(sum_numbers(num1, num2), num3)
num1, num2, num3 = int(input()), int(input()), int(input())
print(add_and_subtract(num1, num2, num3))
```

</details>

## 3.Characters in Range

<details><summary>Condition</summary>

Write a function that receives **two characters** and returns a **single string with all the characters**
**in between them** (according to the ASCII code), separated by a **single space**. Print the result on the console.

Example

| Input   | Output                                                        |
|---------|---------------------------------------------------------------|
| a</br>d | b c                                                           |
| #</br>: | $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9                   |
| #</br>C | $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B |

</details>
<details> <summary>Code</summary>

```Python
start_char = ord(input())
end_char = ord(input())
char_string = [chr(ch) for ch in range(start_char + 1, end_char)]
# print(char_string)
new_chars = ' '.join(char_string)
print(new_chars)
```

whit function

```Python
def characters_in_between(char1, char2):
    start = ord(char1)
    end = ord(char2)
    char_list = [chr(i) for i in range(start + 1, end)]
    return ' '.join(char_list)


char1, char2 = input(), input()

result = characters_in_between(char1, char2)
print(result)
```

task solution by mario zahariev whit lambda()

```Python
chars_range = lambda first_char, second_char: ' '.join(map(chr, range(ord(first_char) + 1, ord(second_char))))
char1 = input()
char2 = input()
print(chars_range(char1, char2))
```

</details>

## 4. Odd and Even Sum

<details><summary>Condition</summary>

You will receive a **single number**.
You should write a function that returns the sum of all even and all odd digits in a given number. The result should be
returned as a single string in the format:
**"Odd sum = {sum_of_odd_digits}**, **Even sum = {sum_of_even_digits}"**
Print the result of the function on the console.

Example

| Input            | Output                      |
|------------------|-----------------------------|
| 1000435          | Odd sum = 9, Even sum = 4   |
| 3495892137259234 | Odd sum = 54, Even sum = 22 |

</details>
<details> <summary>Code</summary>

```Python
number = int(input())
even_sum = 0
odd_sum = 0

# Convert the number to a string to iterate through each character
for digit in str(number):
    num = int(digit)
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")
```

whit function

```Python
def odd_even_sum(number):
    odd_sum = 0
    even_sum = 0

    for digit in str(number):

        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number = int(input())
print(odd_even_sum(number))
```

```Python
number = int(input())
odd_sum = sum(int(digit) for digit in str(number) if int(digit) % 2 != 0)
even_sum = sum(int(digit) for digit in str(number) if int(digit) % 2 == 0)
```

</details>

## 5. Even Numbers

<details><summary>Condition</summary>

Write a program that receives a sequence of numbers (integers) separated by a single space.
It should print a list of only the even numbers. Use filter().

Example

| Input          | Output  |
|----------------|---------|
| 1 2 3 4        | [2, 4]  |
| 1 2 3 -1 -2 -3 | [2, -2] |

</details>
<details> <summary>Code</summary>

```Python
num_string = input().split()
even_list_str = []

for num in num_string:
    if num.lstrip('-').isdigit() and int(num) % 2 == 0:
        even_list_str.append(int(num))

print(even_list_str)
```

whit function

```Python
def extract_even_numbers(input_string):
    even_list = []

    for num in input_string.split():
        if num.lstrip('-').isdigit() and int(num) % 2 == 0:
            even_list.append(int(num))

    return even_list


# Taking input from the user
input_numbers = input()
result = extract_even_numbers(input_numbers)
print(result)
```

```Python
num_string = input()
even_list = [int(num) for num in num_string.split() if num.lstrip('-').isdigit() and int(num) % 2 == 0]
print(even_list)
```

</details>

## 6. Sort

<details><summary>Condition</summary>

Write a program that receives a sequence of numbers (integers) separated by a single space.
It should print a sorted list of numbers in ascending order. Use sorted().

Example

| Input              | Output                     |
|--------------------|----------------------------|
| 6 2 4              | [2, 4, 6]                  |
| 12 52 11 53 2 8 45 | [2, 8, 11, 12, 45, 52, 53] |

</details>
<details> <summary>Code</summary>

```Python
input_str = input()
new_list = list(map(int, input_str.split()))
sorted_list = sorted(new_list)
print(sorted_list)
```

whit function

```Python
def convert_to_int_list(input_string):
    return sorted(list(map(int, input_string.split())))


# Example usage:
input_numbers = input()
result_list = convert_to_int_list(input_numbers)
print(result_list)
```

```Python
print(sorted(list(map(int, input().split()))))
```

</details>

## 7. Min Max and Sum

<details><summary>Condition</summary>

Write a program that receives a sequence of numbers (integers) separated by a single space. It should print the min and
max values of the given numbers and the sum of all the numbers in the list. Use min(), max() and sum().
The output should be as follows:

* On the first line: **"The minimum number is {minimum number}"**
* On the second line: **"The maximum number is {maximum number}"**
* On the third line: **"The sum number is: {sum of all numbers}"**

Example

| Input              | Output                                                                          |
|--------------------|---------------------------------------------------------------------------------|
| 2 4 6              | The minimum number is 2</br>The maximum number is 6</br>The sum number is: 12   |
| 12 52 11 53 2 8 45 | The minimum number is 2</br>The maximum number is 53</br>The sum number is: 183 |

</details>
<details> <summary>Code</summary>

```Python
list_number = list(map(int, input().split(" ")))
minimum_number = min(list_number)
maximum_number = max(list_number)
sum_of_all_numbers = sum(list_number)

print(f"The minimum number is {minimum_number}")
print(f"The maximum number is {maximum_number}")
print(f"The sum number is: {sum_of_all_numbers}")
```

whit function

```Python
def analyze_numbers(numbers):
    minimum_number = min(numbers)
    maximum_number = max(numbers)
    sum_of_all_numbers = sum(numbers)

    print(f"The minimum number is {minimum_number}")
    print(f"The maximum number is {maximum_number}")
    print(f"The sum number is: {sum_of_all_numbers}")


# Example usage:
list_number = list(map(int, input().split()))
analyze_numbers(list_number)
```

```Python
numbers = list(map(int, input().split()))
print(f"The minimum number is {min(numbers)}")
print(f"The maximum number is {max(numbers)}")
print(f"The sum of all numbers is: {sum(numbers)}")
```

</details>

## 8. Palindrome integers

<details><summary>Condition</summary>

A palindrome is a number that reads the same **backward as forward**, such as 323 or 1001.
Write a function that receives a list of positive integers, separated by comma and space ", ".
The function should check if each integer is a **palindrome** - **True** or **False**. Print the result.

Example

| Input              | Output                            |
|--------------------|-----------------------------------|
| 123, 323, 421, 121 | False</br>True</br>False</br>True |
| 32, 2, 232, 1010   | False</br>True</br>True</br>False |

</details>
<details> <summary>Code</summary>

```Python
input_string = list(map(int, input().split(", ")))

for num in input_string:
    num_str = str(num)
    if num_str == num_str[::-1]:
        command = "True"
    else:
        command = "False"

    print(command)
```

function whit list

```Python
def palindrom_func(input):
    results = []
    for num in input:
        num_str = str(num)
        if num_str == num_str[::-1]:
            results.append("True")
        else:
            results.append("False")
    return results


inp_string = list(map(int, input().split(", ")))
palindrom = palindrom_func(inp_string)
print("\n".join(palindrom))
```

task solution by mario zahariev

```Python
def is_palindrome(num):
    return str(num) == str(num)[::-1]


def palindrome_function(lst):
    return '\n'.join(['True' if is_palindrome(num) else 'False' for num in lst])


list_of_palindromes = list(map(int, input().split(', ')))
print(palindrome_function(list_of_palindromes))
```

task solution by Ceo

```Python
def check_palindrome(numbers):
    [print(n == n[::-1]) for n in numbers]


check_palindrome(input().split(", "))
```

```Python
input_string = list(map(int, input().split(", ")))
result = ["True" if str(num) == str(num)[::-1] else "False" for num in input_string]
print("\n".join(result))
```

</details>

## 9. Password Validator

<details><summary>Condition</summary>

Write a function that checks if a given password is valid.
Password validations are:

* It should be **6 - 10** (inclusive) characters long
* It should consist **only of letters and digits**
* It should have **at least** 2 digits
  If a password is **valid**, print **"Password is valid".**

Otherwise, for every unfulfilled rule, print a message:

* **"Password must be between 6 and 10 characters"**
* **"Password must consist only of letters and digits"**
* **"Password must have at least 2 digits"!**

Example

| Input     | Output                                                                                    |
|-----------|-------------------------------------------------------------------------------------------|
| logIn     | Password must be between 6 and 10 characters</br>Password must have at least 2 digits     |
| MyPass123 | Password is valid                                                                         |
| Pa$s$s    | Password must consist only of letters and digits</br>Password must have at least 2 digits |

</details>
<details> <summary>Code</summary>

```Python
password = input()
error_messages = []

if not 6 <= len(password) <= 10:
    error_messages.append("Password must be between 6 and 10 characters")
if not password.isalnum():
    error_messages.append("Password must consist only of letters and digits")
if sum(1 for x in password if x.isdigit()) < 2:
    error_messages.append("Password must have at least 2 digits")

if error_messages:
    print(*error_messages, sep='\n')
else:
    print("Password is valid")
```

```Python
def is_valid_password(password):
    if not 6 <= len(password) <= 10:
        return "Password must be between 6 and 10 characters"
    if not password.isalnum():
        return "Password must consist only of letters and digits"
    if sum(1 for c in password if c.isdigit()) < 2:
        return "Password must have at least 2 digits"

    return "Password is valid"


user_password = input()
result = is_valid_password(user_password)
print(result)
```

task solution by mario zahariev

```Python
def password_validator(password):
    errors = []

    if not 6 <= len(password) <= 10:
        errors.append("Password must be between 6 and 10 characters")

    if not password.isalnum():
        errors.append("Password must consist only of letters and digits")

    if sum(char.isdigit() for char in password) < 2:
        errors.append("Password must have at least 2 digits")

    if errors:
        for error in errors:
            print(error)
    else:
        print("Password is valid")


user_password = input()
password_validator(user_password)
```

password_validator_oop From Mario Zahariev

```Python
import re


class PasswordValidator:
    def __init__(self, password):
        self.password = password
        self.errors = []

    def is_valid(self):
        self._check_length()
        self._check_alphanumeric()
        self._check_digit_count()

        if self.errors:
            return False
        return True

    def _check_length(self):
        if not 6 <= len(self.password) <= 10:
            self.errors.append("Password must be between 6 and 10 characters")

    def _check_alphanumeric(self):
        if not re.match("^[a-zA-Z0-9]+$", self.password):
            self.errors.append("Password must consist only of letters and digits")

    def _check_digit_count(self):
        if sum(char.isdigit() for char in self.password) < 2:
            self.errors.append("Password must have at least 2 digits")

    def get_errors(self):
        return self.errors


user_password = input()
validator = PasswordValidator(user_password)

if validator.is_valid():
    print("Password is valid")
else:
    for error in validator.get_errors():
        print(error)
```

</details>

## 10. Perfect Number

<details><summary>Condition</summary>

A perfect number is a positive integer that is equal to the sum of its proper positive divisors. That is the sum of its
positive divisors, excluding the number itself (also known as its aliquot sum).
Write a function that receives an integer number and returns one of the following messages:

* **"We have a perfect number!"** - if the number is perfect.
* **"It's not so perfect."** - if the number is NOT perfect.
  Print the result on the console.

Example

| Input   | Output                    | Comments           |
|---------|---------------------------|--------------------|
| 6       | We have a perfect number! | 1 + 2 + 3          |
| 28      | We have a perfect number! | 1 + 2 + 4 + 7 + 14 |
| 1236498 | We have a perfect number! |                    |

</details>
<details> <summary>Code</summary>

```Python
number = int(input())
perfect_num = 0

for n in range(1, number):
    if n != 0 and number % n == 0:
        perfect_num += n

if perfect_num == number:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
```

whit Function

```Python
def perfectNumber(number):
    sum = 0
    for x in range(1, number):
        if number % x == 0:
            sum += x
    return "We have a perfect number!" if sum == number else "It's not so perfect."


result = perfectNumber(int(input()))
print(result)
```

task solution by mario zahariev

```Python
def is_perfect_number(number):
    divisors_sum = 0

    for divisior in range(1, number):
        if number % divisior == 0:
            divisors_sum += divisior

    if divisors_sum == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


num = int(input())
print(is_perfect_number(num))
```

</details>

## 11. Loading Bar

<details><summary>Condition</summary>

You will receive a single integer number between 0 and 100 (inclusive)
divisible by 10 without remainder (0, 10, 20, 30...).
Your task is to create a function that returns a loading bar depending on the number you have received in the input.
Print the result on the console. For more clarification, see the examples below.

Example

| Input | Output                                |
|-------|---------------------------------------|
| 30    | 30% [%%%.......]</br>Still loading... |
| 50    | 50% [%%%%%.....]</br>Still loading... |
| 100   | 100% Complete!</br>[%%%%%%%%%%]       |

</details>
<details> <summary>Code</summary>

```Python
def create_bar(percentage_fill: int):
    percentage_fill //= 10

    perc_symbols = "%" * percentage_fill
    dot_symbols = "." * (10 - len(perc_symbols))

    return f"[{perc_symbols}{dot_symbols}]"


def display_result(percentage_fill: int):
    result = []
    bar = create_bar(percentage_fill)

    if percentage_fill == 100:
        result.append("100% Complete!")
        result.append(bar)

    elif percentage_fill != 100:
        result.append(f"{percentage_fill}% {bar}")
        result.append("Still loading...")

    return "\n".join(result)


percentage = int(input())
print(display_result(percentage))
```

```Python
number = int(input())


def loading_bar(num):
    num_range = int(num / 10)
    target = 10
    if target == num_range:
        return "100% Complete!\n" + "[" + target * "%" + "]"
    else:
        return f"{num}% " + "[" + num_range * "%" + (target - num_range) * "." + "]\n" + "Still loading..."


print(loading_bar(number))
```

</details>

## 12. Factorial Division

<details><summary>Condition</summary>

Write a function that receives two integer numbers. Calculate the factorial of each number.
Divide the first result by the second and print the division formatted to the second decimal point.

Example

| Input   | Output |
|---------|--------|
| 5</br>2 | 60.00  |
| 6</br>2 | 360.00 |

</details>
<details> <summary>Code</summary>

```Python
def factorial_numbers(first, second):
    result_first_number, result_second_number = 1, 1
    for first_digit in range(1, first + 1):
        result_first_number *= first_digit
    for second_digit in range(1, second + 1):
        result_second_number *= second_digit
    return result_first_number / result_second_number


num1 = int(input())
num2 = int(input())
result = factorial_numbers(num1, num2)
print(f"{result:.2f}")
```
```Python
def get_factorial(number: int):
    output = 1
    for i in range(1, number + 1):
        output *= i

    return output


first_number = int(input())
second_number = int(input())
result = get_factorial(first_number) / get_factorial(second_number)
print(f"{result:.2f}")
```
### factorial_recursive
```Python
def factorial_recursive(x):
    if x == 0:
        return 1
    else:
        return x * factorial_recursive(x - 1)


n1 = int(input())
n2 = int(input())

factorial_n1 = factorial_recursive(n1)
factorial_n2 = factorial_recursive(n2)

result = factorial_n1 / factorial_n2
print(f"{result:.2f}")
```

```Python
def factorial_recursive(x):
    return 1 if x == 0 else x * factorial_recursive(x - 1)


n1 = int(input())
n2 = int(input())

factorial_n1 = factorial_recursive(n1)
factorial_n2 = factorial_recursive(n2)

result = factorial_n1 / factorial_n2
print(f"{result:.2f}") 
```

</details>
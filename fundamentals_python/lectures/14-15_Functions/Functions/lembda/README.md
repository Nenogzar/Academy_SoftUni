### Lambdas, also known as anonymous functions or function literals, are a concise way to define small and simple functions in many programming languages. I'll explain various aspects of lambdas in Python, as it's a commonly used language for beginners.
____________________
## Basic Lambda Syntax:

A lambda function is defined using the lambda keyword, followed by parameters and an expression.
```Python
lambda x: x * 2         # This creates a function that takes one argument x and returns x * 2.
add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y

print(add(3, 5))        # Output: 8</br>
print(subtract(8, 3))    # Output: 5</br>
print(multiply(4, 6))    # Output: 24</br>
print(divide(10, 2))     # Output: 5.0</br>
```
____________________
## Sorting a List of Tuples :
```Python
pairs = [(1, 5), (2, 3), (4, 1), (3, 8)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  # Output: [(4, 1), (2, 3), (1, 5), (3, 8)]
```

## Assigning Lambdas to Variables:
You can assign a lambda function to a variable for later use.
```Python
double = lambda x: x * 2
```
Now, double(5) will return 10.
____________________
## Using Lambdas as Arguments:
Lambdas are often used as arguments for functions that accept functions, like map(), filter(), and sorted().
```Python
numbers = [1, 4, 2, 7]
sorted(numbers, key=lambda x: x)
sorted_numbers = sorted(numbers, key=lambda x: x)
```
This sorts the list in ascending order.

____________________
## Filtering with Lambdas:
filter() can be used with a lambda to selectively include elements in a collection.
```Python
even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) 
# This filters out only the even numbers from the list.
```
```Python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8]
```
____________________
## Mapping with Lambdas:
map() applies a function to all items in an input list.

```Python
squared_numbers = list(map(lambda x: x*2, numbers))
# This squares each number in the list
```
```Python
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
```
____________________
## Using Lambda with map and filter:
```Python
# Doubling each element in a list using map

numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(doubled_numbers)  # Output: [2, 4, 6, 8, 10]

# Filtering odd numbers using filter
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)  # Output: [1, 3, 5]
```
#### len list whit lambda and map
```Python
len_list = list(maps(lambda x: 1, numbers))
print(len_list)     #: [5]
```
____________________
## Lambda with Multiple Parameters:
Lambdas can take multiple parameters separated by commas.
```Python
add = lambda x, y: x + y
Now, add(3, 4) returns 7.
```
____________________
## Using Lambdas in Key Functions:
Lambdas are handy for defining key functions in sorting.
```Python
# Sorting a list of strings based on the length of each string
words = ['apple', 'banana', 'kiwi', 'orange']
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)  # Output: ['kiwi', 'apple', 'banana', 'orange']
```
____________________
## Creating Functions on the Fly:
```Python
# Creating a simple calculator with lambda functions
calculator = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y,
    'multiply': lambda x, y: x * y,
    'divide': lambda x, y: x / y,
}

result = calculator['multiply'](4, 5)
print(result)  # Output: 20
```
____________________
## Conditional Lambda:
You can use conditional expressions in lambdas for more complex logic.
```Python
is_even = lambda x: True if x % 2 == 0 else False
```
This lambda checks if a number is even.
____________________
## Using Lambda in List Comprehensions:
```Python
# Squaring each element in a list using list comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = [(lambda x: x**2)(x) for x in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
```
____________________
## Lambdas in GUI Programming:
Lambdas are often used in GUI programming for event handlers.
```Python
button = Button(text="Click me", command=lambda: print("Button clicked"))
```
____________________
## Using Lambdas with reduce():
reduce() from the functools module can be used with lambdas to accumulate values.

```Python
from functools import reduce
sum_all = reduce(lambda x, y: x + y, numbers)
```
This computes the sum of all elements in the list.
____________________
## @ Higher-Order Functions:
Lambdas are commonly used with higher-order functions that accept functions as arguments or return functions.

```Python
def multiplier(n):
    return lambda x: x n
```
```Python
# A higher-order function that takes a function as an argument
def operate_on_numbers(x, y, operation):
    return operation(x, y)

# Using a lambda function as an argument
result = operate_on_numbers(10, 5, lambda x, y: x / y)
print(result)  # Output: 2.0
```
____________________
## Closures:
Lambdas can capture variables from their surrounding scope, creating closures.

```Python
def outer_func(x):
    return lambda y: x + y
```
____________________
## Recursion with Named Lambdas:
Although less common, you can define recursive functions using named lambdas.

```Python
factorial = (lambda f: lambda x: x * f(f, x - 1) if x > 0 else 1)(lambda f, x: x * f(f, x - 1) if x > 0 else 1)

if you want recursion with a named lambda you just, use the name of the function right in it:
```Python
f=lambda x:x*f(x-1) if x>0 else 1
```


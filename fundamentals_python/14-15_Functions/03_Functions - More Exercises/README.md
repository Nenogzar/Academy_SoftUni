# Functions - More Exercise

[judge](https://judge.softuni.org/Contests/1729/Functions-More-Exercises)

## 1. Data Types

<details><summary>Condition</summary>

Write a function that, depending on the **first line of the input**,
reads one of the following strings: **"int"**, **"real"**, or **"string"**.

* If the data type is an int, multiply the number by 2.
* If the data type is real, multiply the number by 1.5 and format the result to the second decimal point.
* If the data type is a string, surround the input with "$".
  Print the result on the console.

Example

| Input            | Output  |
|------------------|---------|
| int</br>5        | 10      |
| real</br>2       | 3.00    |
| string</br>hello | $hello$ |

</details>
<details> <summary>Code</summary>

```Python
command = input()
num = input()

if command == "int":
    result = int(num) * 2
elif command == "real":
    result = f"{float(num) * 1.5:.2f}"
elif command == "string":
    result = f"${num}$"

print(result)
```

task solution by kumchovalcho

```Python
command = input()
to_process = input()


def calculate(command, calculation):
    result = ""
    if command == "int":
        result = f"{int(calculation) * 2:.0f}"
    elif command == "real":
        result = f"{float(calculation) * 1.5:.2f}"
    elif command == "string":
        result = "$" + calculation + "$"
    return result


print(calculate(command, to_process))
```

task solution by Ceo

```Python
def calc(arg1, arg2):
    if arg1 == "int":
        result = float(arg2) * 2
        return f"{result:.0f}"

    elif arg1 == "real":
        result = float(arg2) * 1.5
        return f"{result:.2f}"

    elif arg1 == "string":
        return f"${arg2}$"


print(calc(command, number))
```

</details>

## 2. Center Point

<details><summary>Condition</summary>

You will be given the coordinates of two points on a Cartesian coordinate system - X1, Y1, X2, and Y2 on separate lines.
Write a **function** that prints the point which is closest to the center
of the coordinate system (0, 0) in the format: **"({X}, {Y})"**</br>
If the points are at the same distance from the center, print only the first one.
The resulting coordinates must be **formatted** to the **lower integer.**

Example

| Input                        | Output   |
|------------------------------|----------|
| 2</br>4</br>-1</br>2         | (-1, 2)  |
| 10</br>14.5</br>-17.2</br>16 | (10, 14) |

</details>
<details> <summary>Code</summary>

```Python
import math

x1 = math.floor(float(input()))
x2 = math.floor(float(input()))
y1 = math.floor(float(input()))
y2 = math.floor(float(input()))

sum_x = math.floor(abs(x1) + abs(x2))
sum_y = math.floor(abs(y1) + abs(y2))


def whats_closer(arg1, arg2):
    if arg1 <= arg2:
        return f"({x1}, {x2})"

    elif arg2 <= arg1:
        return f"({y1}, {y2})"


print(whats_closer(sum_x, sum_y))
```

```Python
import math


# Function to get coordinates from the user
def get_coordinates():
    x = math.floor(float(input()))
    y = math.floor(float(input()))
    return x, y


# Function to calculate the distance from the center
def calculate_distance(coord):
    return math.floor(abs(coord[0]) + abs(coord[1]))


# Function to determine which of two points is closer to the center
def whats_closer(coord1, coord2):
    distance1 = calculate_distance(coord1)
    distance2 = calculate_distance(coord2)

    if distance1 <= distance2:
        return coord1
    else:
        return coord2


# Get coordinates for points A and B
point_a = get_coordinates()
point_b = get_coordinates()

# Determine which point is closer
closer_point = whats_closer(point_a, point_b)

print(f"{closer_point}")
```

</details>

## 3. Longer Line

<details><summary>Condition</summary>

You will be given the coordinates of four points.
The first and the second pair of points form two different lines.
Create a function that prints the **longer line** in the format:
**"({X1}, {Y1})({X2}, {Y2})"** starting from the point which is closer to the center of the coordinate system (0, 0).
You can reuse the method that you wrote for the previous problem.
If the lines are of equal length, print only the first one.
The resulting coordinates must be **formatted** to the **lower integer.**

Example

| Input                                           | Output          |
|-------------------------------------------------|-----------------|
| 2</br>4</br>-1</br>2</br>-5</br>-5</br>4</br>-3 | (4, -3)(-5, -5) |
| 1</br>2</br>3</br>4</br>9</br>7</br>5</br>6     | (5, 6)(9, 7)    |
|                                                 |                 |

</details>
<details> <summary>Code</summary>

```Python
x1, x2, y1, y2 = math.floor(float(input())), math.floor(float(input())), math.floor(float(input())), math.floor(
    float(input()))
z1, z2, v1, v2 = math.floor(float(input())), math.floor(float(input())), math.floor(float(input())), math.floor(
    float(input()))

sum_x = math.floor(abs(x1) + abs(x2))
sum_y = math.floor(abs(y1) + abs(y2))
sum_z = math.floor(abs(z1) + abs(z2))
sum_v = math.floor(abs(v1) + abs(v2))


def whats_closer(arg1, arg2, arg3, arg4):
    one = arg1 + arg2
    two = arg3 + arg4
    if one > two:
        if abs(x1) + abs(x2) > abs(y1) + abs(y2):
            return f"({y1}, {y2})({x1}, {x2})"
        else:
            return f"({x1}, {x2})({y1}, {y2})"
    elif one < two:
        if abs(z1) + abs(z2) > abs(v1) + abs(v2):
            return f"({v1}, {v2})({z1}, {z2})"
        else:
            return f"({z1}, {z2})({v1}, {v2})"
    else:
        if abs(z1) + abs(z2) > abs(v1) + abs(v2):
            return f"({v1}, {v2})({z1}, {z2})"
        else:
            return f"({z1}, {z2})({v1}, {v2})"


print(whats_closer(sum_x, sum_y, sum_z, sum_v))
```

```Python
import math


def get_input_values():
    x1, x2, y1, y2 = map(lambda x: math.floor(float(input())), range(4))
    z1, z2, v1, v2 = map(lambda x: math.floor(float(input())), range(4))
    return x1, x2, y1, y2, z1, z2, v1, v2


def calculate_sums(x1, x2, y1, y2, z1, z2, v1, v2):
    sum_x = math.floor(abs(x1) + abs(x2))
    sum_y = math.floor(abs(y1) + abs(y2))
    sum_z = math.floor(abs(z1) + abs(z2))
    sum_v = math.floor(abs(v1) + abs(v2))
    return sum_x, sum_y, sum_z, sum_v


def whats_closer(x1, x2, y1, y2, z1, z2, v1, v2):
    sum_x, sum_y, sum_z, sum_v = calculate_sums(x1, x2, y1, y2, z1, z2, v1, v2)

    one = sum_x + sum_y
    two = sum_z + sum_v

    if one > two:
        if abs(x1) + abs(x2) > abs(y1) + abs(y2):
            return f"({y1}, {y2})({x1}, {x2})"
        else:
            return f"({x1}, {x2})({y1}, {y2})"
    elif one < two:
        if abs(z1) + abs(z2) > abs(v1) + abs(v2):
            return f"({v1}, {v2})({z1}, {z2})"
        else:
            return f"({z1}, {z2})({v1}, {v2})"
    else:
        if abs(z1) + abs(z2) > abs(v1) + abs(v2):
            return f"({v1}, {v2})({z1}, {z2})"
        else:
            return f"({z1}, {z2})({v1}, {v2})"


def main():
    x1, x2, y1, y2, z1, z2, v1, v2 = get_input_values()
    result = whats_closer(x1, x2, y1, y2, z1, z2, v1, v2)
    print(result)


if __name__ == "__main__":
    main()
```

</details>

## 4. Tribonacci Sequence

<details><summary>Condition</summary>

In the Tribonacci sequence, every number is formed by the **sum of the previous 3**.
Write a function that prints numbers from the Tribonacci
sequence on **one line** separated by a single space, starting from 1.
You will receive a positive integer number as input.

Example

| Input | Output             |
|-------|--------------------|
| 4     | 1 1 2 4            |
| 8     | 1 1 2 4 7 13 24 44 |

</details>
<details> <summary>Code</summary>

```Python
a, b, c = 1, 1, 2
upper_limit = int(input())

sequence = []

while len(sequence) + 1 <= upper_limit:
    sequence.append(a)
    a, b, c = b, c, a + b + c

print(' '.join(map(str, sequence)))
```

task solution by kumchovalcho

```Python
def tribonacci_sequence(number: int):
    sequence = [1, 1, 2]

    if 1 <= number <= 3:
        return sequence[:number]

    rotations = number - len(sequence)
    for _ in range(rotations):
        current_numbers = sequence[-3:]
        sequence.append(sum(current_numbers))

    return sequence


tribonacci_number = int(input())
result = tribonacci_sequence(tribonacci_number)
print(*result, sep=" ")
```

task solution by Ceo

```Python
starting_number = int(input())

last_three = [1, 1]


def show_tribonacci(num):
    for number in range(1, num + 1):
        if number == 1 or number == 2:
            print(last_three[number - 1], end=" ")
            continue
        else:
            add_last_number = 0
            if len(last_three) > 2:
                add_last_number = last_three.pop(0)
        print(sum(last_three) + add_last_number, end=" ")
        last_three.append(sum(last_three) + add_last_number)


show_tribonacci(starting_number)
```

task solution by Ceo

```Python
n = int(input())


def tribonacci(n):
    list = [1, 0, 0]
    for i in range(n):
        next_num = sum(list)
        print(next_num, end=" ")
        list.append(next_num)
        list.pop(0)


tribonacci(n)
```

</details>

## 5. Multiplication Sign

<details><summary>Condition</summary>

You will receive three integer numbers.
Write a program that finds if their multiplication (the result) is **negative, positive, or zero**.
Try to do this **WITHOUT** multiplying the 3 numbers.

Example

| Input          | Output   |
|----------------|----------|
| 2</br>3</br>-1 | negative |
| 2</br>3</br>1  | positive |

</details>
<details> <summary>Code</summary>

with multiplication

```Python
import math

x, y, z = map(lambda r: math.floor(int(input())), range(3))
sign = ''
result = x * y * z

if result < 0:
    sign = 'negative'
elif result > 0:
    sign = 'positive'
else:
    sign = 'zero'

print(sign)
```

without multiplication

```Python
import math

# Въвеждане на три числа и закръгляне надолу до най-близкото цяло
x, y, z = map(lambda r: math.floor(int(input())), range(3))

def check_numbers(one, two, three):
    if (three > 0 and one < 0 and two < 0) or \
            (two > 0 and one < 0 and three < 0) or \
            (one > 0 and two < 0 and three < 0) or \
            (one > 0 and two > 0 and three > 0):
        return "positive"
    elif one == 0 or two == 0 or three == 0:
        return "zero"
    elif one < 0 or two < 0 or three < 0:
        return "negative"

print(check_numbers(x, y, z))
```

task solution by kumchovalcho

```Python
def check_numbers(first, second, third):
    if any(x == 0 for x in (first, second, third)):
        return "zero"

    if all(x > 0 for x in (first, second, third)) or \
            sum(1 for x in (first, second, third) if x < 0) == 2:
        return "positive"

    return "negative"


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(check_numbers(first_number,
                    second_number,
                    third_number
                    )
      )
      )
```

```Python
```

</details>
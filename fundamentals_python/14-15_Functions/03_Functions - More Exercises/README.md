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
```

print(calc(command, number))

</details>

## 2. Data Types

<details><summary>Condition</summary>


Example

| Input | Output |
|-------|--------|
|       |        |
|       |        |
|       |        |

</details>
<details> <summary>Code</summary>

```Python

```

</details>

## 3. Data Types

<details><summary>Condition</summary>


Example

| Input | Output |
|-------|--------|
|       |        |
|       |        |
|       |        |

</details>
<details> <summary>Code</summary>

```Python

```

</details>

## 4. Data Types

<details><summary>Condition</summary>


Example

| Input | Output |
|-------|--------|
|       |        |
|       |        |
|       |        |

</details>
<details> <summary>Code</summary>

```Python

```

</details>

## 5. Data Types

<details><summary>Condition</summary>


Example

| Input | Output |
|-------|--------|
|       |        |
|       |        |
|       |        |

</details>
<details> <summary>Code</summary>

```Python

```

</details>
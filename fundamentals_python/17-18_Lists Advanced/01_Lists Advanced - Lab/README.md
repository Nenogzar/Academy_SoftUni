# Exercise: Lists Advanced

[judge](https://judge.softuni.org/Contests/1730/Lists-Advanced-Lab) and
[icode-example](https://icode-example.ceo-py.eu/menu?language=Python&course=Fundamentals&module=Lists%20Advanced%20-%20Lab)

## 1.	No Vowels

<details><summary>Condition</summary>

Example

| Input       | Output  |
|-------------|---------|
| Python      | Pythn   |
| ILovePython | LvPythn |
        

</details>

<details> <summary>Code</summary>

```Python
original_text = input()

skip_letters = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']


def change_text(arg1):
    result = ""
    for letter in arg1:
        if letter not in skip_letters:
            result += letter
    return result


print(change_text(original_text))
```
comprehension
```Python
def remove_vowels(text):
    # Create a list of vowels to be removed
    vowels = ['a', 'o', 'u', 'e', 'i']

    new_text = [char for char in text if char.lower() not in vowels]

    return ''.join(new_text)


input_string = input()

print(remove_vowels(input_string))
```
</details>

## 2.	Trains


<details><summary>Condition</summary>

Example

| Input                                                                                                                                    | Output                |
|------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| 3</br>add 20</br>insert 0 15</br>leave 0 5</br>End                                                                                       | [10, 0, 20]           
| 5</br>add 10</br>add 20</br>insert 0 16</br>insert 1 44</br>leave 1 12</br>insert 2 100</br>insert 4 61</br>leave 4 1</br>add 15</br>End | [16, 32, 100, 0, 105] |



    

</details>

<details> <summary>Code</summary>

```Python
wagon_number = int(input())
train_wagon_index = []

for _ in range(wagon_number):
    train_wagon_index.append(0)
# print(train_wagon_index)

command_list = input().split()

while command_list[0] != "End":

    if "add" in command_list:
        train_wagon_index[-1] += int(command_list[1])
    elif "insert" in command_list:
        train_wagon_index[int(command_list[1])] += int(command_list[2])
    elif "leave" in command_list:
        train_wagon_index[int(command_list[1])] -= int(command_list[2])
    command_list = input().split()

print(train_wagon_index)
```
whit function
```Python
train_wagons = int(input())
train = []
command = input()

for n in range(train_wagons):
    train.append(0)


def add_people(umber_people):
    train[-1] += umber_people


def insert_people(wagon, number_people):
    train[wagon] += number_people


def leave_people(wagon, number_people):
    train[wagon] -= number_people


while command != "End":

    command = command.split()

    if "add" in command:
        add_people(int(command[-1]))

    elif "insert" in command:
        insert_people((int(command[1])), int(command[-1]))

    elif "leave" in command:
        leave_people(int(command[1]), int(command[-1]))

    command = input()

print(train)

```


</details>

## 3.	To-do List


<details><summary>Condition</summary>

Example

| Input                                                        | Output                                             |
|--------------------------------------------------------------|----------------------------------------------------|
| 2-Walk the dog</br>1-Drink coffee</br>6-Dinner</br>5-WorkEnd | ['Drink coffee', 'Walk the dog', 'Work', 'Dinner'] |
| 3-C</br>2-A</br>1-B</br>6-V</br>End                          | ['B', 'A', 'C', 'V']                               |

    

</details>

<details> <summary>Code</summary>

whit nested list
```Python
num_list = list()
export_list = list()
while True:
    to_do_list = input()
    if to_do_list == "End":
        break

    tasks = to_do_list.split("-")
    nested_list = [task.strip() for task in tasks]
    num_list.append(nested_list)

num_list.sort(key=lambda x: int(x[0]))

# print(num_list)

for nested_list in num_list:
    export_list.append(nested_list[1])
print(export_list)
```
whit tuple
```Python

to_do_list = input()

num_list = list()

while to_do_list != "End":
    importance, note = map(str.strip, to_do_list.split("-"))
    num_list.append((int(importance), note))

    to_do_list = input()

num_list.sort(key=lambda x: x[0])

export_list = [note for _, note in num_list]
print(export_list)
```

</details>

## 4.	Palindrome Strings


<details><summary>Condition</summary>

Example

| Input                                  | Output                                                      |
|----------------------------------------|-------------------------------------------------------------|
| wow father mom wow shirt stats</br>wow | ['wow', 'mom', 'wow', 'stats']</br>Found palindrome 2 times |
| hey how you doin? lol</br>mom          | ['lol']</br>Found palindrome 0 times                        |

    

</details>

<details> <summary>Code</summary>

```Python
input_text = input().split()
wanted_palindrome = input()
palindromes = []

for string in input_text:
    if string == string[::-1]:
        palindromes.append(string)
counter_palindrom = palindromes.count(wanted_palindrome)

print("Palindromes:", palindromes)
print(f"Found palindrome {counter_palindrom} times")
```
```Python
input_text = input().split()
wanted_palindrome = input()
palindromes = [string for string in input_text if string == string[::-1]]
counter_palindrom = palindromes.count(wanted_palindrome)

print("Palindromes:", palindromes)
print(f"Found palindrome {counter_palindrom} times")
```
```Python
input_text = input().split(" ")
wanted_palindrome = input()
palindromes = []

[palindromes.append(string) for string in input_text if string == "".join(reversed(string))]
counter_palindrom = palindromes.count(wanted_palindrome)
print(palindromes)
print(f"Found palindrome {counter_palindrom} times")
```

</details>

## 5.	Sorting Names


<details><summary>Condition</summary>

Example

| Input                                | Output                                             |
|--------------------------------------|----------------------------------------------------|
| Ali, Marry, Kim, Teddy, Monika, John | ["Monika", "Marry", "Teddy", "John", "Ali", "Kim"] |
| Lilly, Tim, Kate, Tom, Alex          | ['Lilly', 'Alex', 'Kate', 'Tim', 'Tom']            |
    

</details>

<details> <summary>Code</summary>

```Python
 

```
</details>

## 6.	Even Numbers


<details><summary>Condition</summary>

Example

| Input | Output |
|-------|--------|
| 3, 2, 1, 5, 8 | [1, 4]  |
| 2, 4, 6, 9, 10| [0, 1, 2, 4] |
    

</details>

<details> <summary>Code</summary>

```Python
 

```
</details>

## 7.	The Office


<details><summary>Condition</summary>

Example

| Input             | Output                               |
|-------------------|--------------------------------------|
| 1 2 3 4 2 1</br>3 | Score: 2/6. Employees are not happy! |
| 2 3 2 1 3 3</br>4 | Score: 3/6. Employees are happy!     |

    

</details>

<details> <summary>Code</summary>



```Python
```
</details>
<details><summary> Mid-Exam-Preparation-1 </summary>

## 1.	Computer Store

[Link to Judge](https://judge.softuni.org/Contests/Practice/Index/2517#0)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40358)

<details><summary>Condition</summary>

_Write a program that prints you a receipt for your new computer. You will receive the parts' prices (without tax) until you receive what type of customer this is - special or regular. Once you receive the type of customer you should print the receipt._

**The taxes are 20%** of each part's price you receive.

If the customer is **special**, he has a 10% discount on the total price with taxes.
If a given price is not a positive number, you should print **"Invalid price!"** on the console and continue with the next price.
If the total price is equal to zero, you should print **"Invalid order!"** on the console.

### Input

•	You will receive numbers representing prices (without tax) until the command **"special"** or "regular":

### Output

•	The receipt should be in the following format: 

"Congratulations you've just bought a new computer!</br>
Price without taxes: {total price without taxes}$</br>
Taxes: {total amount of taxes}$</br>
-----------</br>
Total price: {total price with taxes}$"

Note: All prices should be displayed to the second digit after the decimal point! The discount is applied only on the total price. Discount is only applicable to the final price!


Example

| Input                                                                                                                                                                | Output                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| 1050</br>200</br>450</br>2</br>18.50</br>16.86</br>special                                                                                                           | Congratulations you've just bought a new computer!</br>Price without taxes: 1737.36$</br>Taxes: 347.47$</br>-----------</br>Total price: 1876.35$ |
| 1023 </br>15</br>-20</br>-5.50</br>450</br>20 </br>17.66 </br>19.30</br>regular                                                                                      | Invalid price!</br>Invalid price!</br>Congratulations you've just bought a new computer!</br>Price without taxes: 1544.96$</br>Taxes: 308.99$</br>-----------</br>Total price: 1853.95$ |
| regular                                                                                                                                                              | Invalid order!                                                                                                                                    |

</details>
<details> <summary>Code</summary>

```Python
total_sum = 0
data = input()
customers = list()
discount = 0.1

while data != "special" and data != "regular":
    price = float(data)
    if price < 0:
        print("Invalid price!")
        data = input()
        continue
    else:
        customers.append(data)
        data = input()

if not customers:
    print("Invalid order!")
else:
    total_sum = sum(float(n) for n in customers)
    taxes = total_sum * 0.2
    total_price = total_sum + taxes

    if data == "special":
        total_price = total_price - (total_price * discount)

    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_sum:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")
```

</details>

## 2.	Shoot for the Win

[Link to Judge](https://judge.softuni.org/Contests/Practice/Index/2305#1)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40371)

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
targets = [int(x) for x in input().split()]
shoot = input()
targets_len = len(targets)


while shoot != "End":
    shoot = int(shoot)

    if 0 <= shoot < targets_len:
        target = targets[shoot]
        targets[shoot] = -1
        for i in range(targets_len):

            if targets[i] == -1:
                continue

            if targets[i] > target:
                targets[i] -= target
            else:
                targets[i] += target

    shoot = input()

print(f"Shot targets: {sum(1 for x in targets if x == -1)} ->", *targets)
```
```Python
main_target = [int(n) for n in input().split()]

made_shots = 0
command = input()
targets_number = len(main_target) - 1

while command != "End":
    command = int(command)
    if targets_number >= command >= 0 and main_target[command] != -1:
        made_shots += 1
        target_value = main_target[command]
        for index, value in enumerate(main_target):
            if value != -1:
                if value <= target_value:
                    result_between_targets = value + target_value
                    main_target[index] = result_between_targets
                else:
                    result_between_targets = value - target_value
                    main_target[index] = result_between_targets
        main_target[command] = -1

    command = input()

print(f"Shot targets: {made_shots} ->", *main_target, sep=" ")
```
</details>

## 3.	Heart Delivery

[Link to Judge](https://judge.softuni.org/Contests/Practice/Index/2031#2)</br>
[Problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40378)

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
neighborhood = [int(x) for x in input().split("@")]
jump_data = input()
neighborhood_len = len(neighborhood)
length = 0

while jump_data != "Love!":
    length += int(jump_data.split()[-1])
    if length >= neighborhood_len:
        length = 0

    if neighborhood[length] > 2:
        neighborhood[length] -= 2
    else:
        if neighborhood[length] != 0:
            neighborhood[length] -= 2
            text = "has"
        else:
            text = "already had"
        print(f"Place {length} {text} Valentine's day.")
    jump_data = input()

print(f"Cupid's last position was {length}.")

failed_houses = sum(1 for x in neighborhood if x != 0)

if failed_houses:
    print(f"Cupid has failed {failed_houses} places.")
else:
    print("Mission was successful.")
```
```Python
def jump_neighborhood(length_d):
    global jump_position
    jump_position += length_d
    if jump_position >= len(neighborhood):
        jump_position = 0
    if neighborhood[jump_position] == 0:
        print(f"Place {jump_position} already had Valentine's day.")
    else:
        neighborhood[jump_position] -= 2
        if neighborhood[jump_position] == 0:
            print(f"Place {jump_position} has Valentine's day.")


while jump_command != "Love!":
    jump_command = jump_command.split()
    jump_neighborhood(int(jump_command[1]))

    jump_command = input()

print(f"Cupid's last position was {jump_position}.")

if sum(neighborhood) == 0:
    print("Mission was successful.")
else:
    fail_count = neighborhood.count(0)
    print(f"Cupid has failed {len(neighborhood) - fail_count} places.")
```

</details>

</details>

######
<details><summary> Mid-Exam-Preparation-2 </summary>

## 1.	Counter-Strike

[judge](https://judge.softuni.org/Contests/Practice/Index/2305#0)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40370)
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

## 2.	Array Modifier

[judge](https://judge.softuni.org/Contests/Practice/Index/2474#1)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40365)

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

## 3.	Inventory

[judge](https://judge.softuni.org/Contests/Practice/Index/2028#2)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40384)   

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

</details>


######

<details><summary> Mid-Exam-Preparation-more and more </summary>

## 01. Guinea Pig

[judge](https://judge.softuni.org/Contests/Practice/Index/2031#0)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40376)


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

## 01. SoftUni Reception

[judge](https://judge.softuni.org/Contests/Practice/Index/2474#0)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40364)


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

## 01. Bonus Scoring System

[judge](https://judge.softuni.org/Contests/Practice/Index/2028#0)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40382)


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


## 02. The Lift

[judge](https://judge.softuni.org/Contests/Practice/Index/2517#1)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40359)


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

## 02. Shopping List

[judge](https://judge.softuni.org/Contests/Practice/Index/2031#1)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40377)


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

## 02. MuOnline

[judge](https://judge.softuni.org/Contests/Practice/Index/2028#1)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40383)


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




## 03. Moving Target

[judge](https://judge.softuni.org/Contests/Practice/Index/2305#2)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40372)

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



## 03. Memory Game

[judge](https://judge.softuni.org/Contests/Practice/Index/2517#2)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40360)

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

## 03. Numbers

[judge](https://judge.softuni.org/Contests/Practice/Index/2474#2)</br>
[problem](https://judge.softuni.org/Contests/Practice/DownloadResource/40366)

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

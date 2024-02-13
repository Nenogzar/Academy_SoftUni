# Exercise: Lists Advanced - More Exercises

[judge](https://judge.softuni.org/Contests/1732/Lists-Advanced-More-Exercises) </br>
[link problems](https://judge.softuni.org/Contests/Practice/DownloadResource/40501)</br>
[icode-example](https://icode-example.ceo-py.eu/menu?language=Python&course=Fundamentals&module=Lists%20Advanced%20-%20More%20Exercises) </br>

## 1.Social Distribution


<details><summary>Condition</summary>

A core idea of several left-wing ideologies is that the wealthiest should support the poorest, no matter what, and that is exactly what you are called to do for this problem.
On the first line, you will be given the population (numbers separated by comma and space ", "). On the second line, you will be given the minimum wealth. You should distribute the wealth so that no part of the population has less than the minimum wealth. To do that, you should always take wealth from the wealthiest part of the population. 
There will be cases where the distribution will not be possible. In that case, print: "No equal distribution possible". 

Example

| Input                  | Output                         |
|------------------------|--------------------------------|
| 2, 3, 5, 15, 75</br>5  | [5, 5, 5, 15, 70]              |
| 2, 3, 5, 15, 75</br>20 | [20, 20, 20, 20, 20]           |
| 2, 3, 5, 45, 45</br>30 | No equal distribution possible |
   

</details>

<details> <summary>Code</summary>

```Python
wealth_numbers = list(map(int, input().split(", ")))
minimum_wealth = int(input())

for i in range(len(wealth_numbers)):
    wealthiest = wealth_numbers.index(max(wealth_numbers))

    number = wealth_numbers[i]
    if number < minimum_wealth:
        wealth_difference = minimum_wealth - number
        wealth_numbers[i] += wealth_difference

        wealth_numbers[wealthiest] -= wealth_difference
        if wealth_numbers[wealthiest] < minimum_wealth:
            print('No equal distribution possible')
            break

else:
    print(wealth_numbers)
```
solution of the task by CEO
```Python
population = [int(x) for x in input().split(", ")]
minimum_wealth = int(input())

if minimum_wealth > sum(population) / len(population):
    print("No equal distribution possible")
    exit()

while any(x < minimum_wealth for x in population):
    max_number, number_to_change = max(population), min(population)
    index_max, index_min = population.index(max_number), population.index(number_to_change)
    added_value = minimum_wealth - number_to_change
    population[index_max] -= added_value
    population[index_min] += added_value

print(population)
```

```Python
wealth = list(map(int, input().split(", ")))
min_wealth = int(input())

if min_wealth > sum(wealth) / len(wealth):
    print("No equal distribution possible")
    exit()
else:
    for i in range(len(wealth)):
        num = wealth[i]
        if num < min_wealth:
            result = min_wealth - num
            max_waelt = max(wealth)
            index_max_num = wealth.index(max_waelt)
            check_num = max_waelt - result
            wealth[i] = min_wealth
            wealth[index_max_num] = check_num

print(wealth)
```

</details>

## 2.


<details><summary>Condition</summary>




Example

| Input | Output |
|-------|--------|
|       |        |
|       |        |


</details>

<details> <summary>Code</summary>

```Python
```

```Python
```

```Python
```

</details>

## 3.


<details><summary>Condition</summary>

Kate is stuck in a maze. You should help her to find her way out.
On the **first line**, you will be given how many rows there are in the maze. 
On the following **n lines**, you will be given the maze itself. 

Here is a legend for the maze:
* **"#" - means a wall**; Kate cannot go through there
* **" " - means empty space**; Kate can go through there
* **"k" - the initial position of Kate**; start looking for a way out from there
There are **two options**: Kate either gets out or not:
* If Kate can get out, print the following: 
**"Kate got out in {number_of_moves} moves"**. 
* Note: If there are **two or more ways out**, she always chooses the **longest one**.
Otherwise, print: **"Kate cannot get out".**



Example

| Input                                                    | Output                  |
|----------------------------------------------------------|-------------------------|
| 4</br>######</br>##  k#</br>## ###</br>## ###            | Kate got out in 5 moves |
| 5</br>######</br>##  k#</br>## ###</br>######</br>## ### | Kate cannot get out     |


</details>

<details> <summary>Code</summary>

```Python
```

```Python
```

```Python
```

</details>

## 4.


<details><summary>Condition</summary>




Example

| Input | Output |
|-------|--------|
|       |        |
|       |        |


</details>

<details> <summary>Code</summary>

```Python
```

```Python
```

```Python
```

</details>

## 5.


<details><summary>Condition</summary>




Example

| Input | Output |
|-------|--------|
|       |        |
|       |        |


</details>

<details> <summary>Code</summary>

```Python
```

```Python
```

```Python
```

</details>
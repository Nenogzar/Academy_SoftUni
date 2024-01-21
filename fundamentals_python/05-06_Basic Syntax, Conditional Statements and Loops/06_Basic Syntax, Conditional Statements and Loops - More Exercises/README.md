# More Exercises: Basic Syntax, Conditional Statements, and Loops
1.	Find the Largest</br>
You will be given a number. Print the largest number that can be formed from the digits of the given number.

Examples

| Input | Output |
|-------|--------|
| 213   | 321    |
| 7389  | 9873   |

* Code


    `number_input = [n for n in input()]
    n = len(number_input)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if number_input[j] < number_input[j + 1]:
                number_input[j], number_input[j + 1] = number_input[j + 1], number_input[j]
    
    sorted_number = ''.join(number_input)
    
    print(sorted_number)`

or whit list


    `digits = list(input())
    digits.sort(reverse=True)
    largest_number = ''.join(digits)
    
    print(f"{largest_number}")`
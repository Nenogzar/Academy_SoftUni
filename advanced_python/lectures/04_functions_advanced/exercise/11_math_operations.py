# 11_math_operations

"""
11.	*Math Operations
Write a function named math_operations that receives a different number of integers as arguments and 4 keyword arguments.
The keys will be single letters: "a", "s", "d", "m", and the values will be numbers.
You need to take each integer argument from the sequence and do mathematical operations as follows:
•	The first element should be added to the value of the key "a"
•	The second element should be subtracted from the value of the key "s"
•	The third element should be divisor to the value of the key "d"
•	The fourth element should be multiplied by the value of the key "m"
•	Each result should replace the value of the corresponding key
•	You must repeat the same steps consecutively until you run out of numbers
Beware: You cannot divide by 0. If the operation could throw an error,
you should delete the element from the sequence and continue to the next operation.
For more clarifications, see the examples below.
Note: Submit only the function in the judge system
Input
•	There will be no input. Just parameters passed to your function.
•	All of the given numbers will be valid integers in the range [-100, 100]
Output
•	The function should return the final dictionary

Test Code

print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))

Output

{'a': 9, 's': 15, 'd': -3.0, 'm': -45}
{'a': 5, 's': 2, 'd': 0.0, 'm': 0}
{'a': 6, 's': 0, 'd': 0, 'm': 0}


Comment test 1:
We create 1 args list: [2, 12, 0, -3, 6, -20, -11] and 1 kwargs dict: {'a': 1, 's': 7, 'd': 33, 'm': 15}.
We start calculating from the first number and the first key-value:
1) 1 + 2 = 3 -> add 3 to the key 'a'
2) 7 – 12 = -5 -> add -5 to the key 's'
3) 33 / 0 throws ZeroDivisionError -> remove 0 and continue to the next operation
4) 15 * (-3) = (-45) -> add -45 to the key 'm'
5) 3 + 6 = 9 -> add 3 to the key 'a'
6) (-5) - (-20) = 15 -> add 3 to the key 's'
7) 33 / (-11) = (-3.0) -> add 3 to the key 'd'


"""




def math_operations(*args, **kwargs):
    counter = 1
    for digit in args:
        if counter == 2:
            kwargs['s'] -= digit
        elif counter == 3:
            if digit != 0:
                kwargs['d'] /= digit
        elif counter == 4:
            kwargs['m'] *= digit
        elif counter == 1:
            kwargs['a'] += digit
        counter += 1
        if counter == 5:
            counter = 1
    result = []
    for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], x[0])):
        result.append(f"{key}: {value:.1f}")
    return '\n'.join(result)
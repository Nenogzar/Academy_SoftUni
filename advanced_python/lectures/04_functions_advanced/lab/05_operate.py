#################################### TASK CONDITION ############################
'''
https://judge.softuni.org/Contests/Practice/Index/1838#4

                      5.	Operate
Write a function called operate that receives an operator 
("+", "-", "*" or "/") as first argument and multiple numbers (integers) 
as additional arguments (*args). The function should return the result of
the operator applied to all the numbers. For more clarification, see the examples below. 
Submit only your function in the Judge system.
Note: Be careful when you have multiplication and division

_______________________________________________
Example_01

Test Code	(no input data in this task)
print(operate("+", 1, 2, 3))	

Output
6	

Explanation
1 + 2 + 3 = 6

_______________________________________________
Example_02

Test Code	(no input data in this task)
print(operate("*", 3, 4))	

Output
12	

Explanation
3 * 4 = 12


'''
##########: variant 1 :##########


def operate(operator, *args):
    def add(*nums):
        return sum(nums)

    def subtract(x, *nums):
        return x + sum(-y for y in nums)

    def multiply(x, *nums):
        result = x
        for y in nums:
            result *= y
        return result

    def divide(x, *nums):
        result = x
        for y in nums:
            result /= y
        return result

    if operator == "+":
        return add(*args)
    elif operator == "-":
        return subtract(*args)
    elif operator == "*":
        return multiply(*args)
    elif operator == "/":
        return divide(*args)
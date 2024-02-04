# Изчисляване на фактуриел

# def factorial_recursive(x):
#     if x == 0:
#         return 1
#     else:
#         return x * factorial_recursive(x - 1)
#
# n = int(input())
#
#
# result = factorial_recursive(n)
# print(f"{result}")


""" 2 """

# def factorial_recursive(x):
#     return 1 if x == 0 else x * factorial_recursive(x - 1)
#
# n = int(input())
# result = factorial_recursive(n)
# print(result)

"""  решение на задачата: """

def factorial_recursive(x):
    return 1 if x == 0 else x * factorial_recursive(x - 1)

#
# n1 = int(input())  # "Въведете първото число: "
# n2 = int(input())  # "Въведете второто число: "
#
# factorial_n1 = factorial_recursive(n1)
# factorial_n2 = factorial_recursive(n2)
#
# result = factorial_n1 / factorial_n2
# print(f"{result:.2f}")  # f"{n1}! / {n2}! = {result:.2f}"

"""  решение на задачата 2 : """


# def factorial_recursive(x):
#     if x == 0:
#         return 1
#     else:
#         return x * factorial_recursive(x - 1)
#
#
# n1 = int(input())  # "Въведете първото число: "
# n2 = int(input())  # "Въведете второто число: "
#
# factorial_n1 = factorial_recursive(n1)
# factorial_n2 = factorial_recursive(n2)
#
# result = factorial_n1 / factorial_n2
# print(f"{result:.2f}")

""" TANER"""

#
# def get_factorial(number: int):
#     output = 1
#     for i in range(1, number + 1):
#         output *= i
#
#     return output
#
#
# first_number = int(input())
# second_number = int(input())
# result = get_factorial(first_number) / get_factorial(second_number)
# print(f"{result:.2f}")


""" 2 """
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

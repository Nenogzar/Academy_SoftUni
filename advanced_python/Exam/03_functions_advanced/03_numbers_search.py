# ******* Advanced Retake Exam - 19 August 2020 ******* #

# *******  03_numbers_search  ******* #
 
# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/2463#2


Write a function called numbers_searching which receives a different amount of parameters.
All parameters will be integer numbers forming a sequence of consecutive numbers.
Your task is to find an unknown amount of duplicates from the given sequence and a missing value,
such that all the duplicate values and the missing value are between the smallest and the biggest received number.

The function should return a list with the last missing number as a first argument and a sorted list, containing the duplicates found, in ascending order.
For example: if we have the following numbers: 1, 2, 4, 2, 5, 4 will return 3 as missing number and 2, 4 as duplicate numbers in the following format: [3, [2, 4]]
Input
•	There will be no input
•	Parameters will be passed to your function
Output
•	The function should return a list in the following format: [missing number, [duplicate_numbers separated with comma and space]]
Constraints
•	The missing number will always be between the smallest and the biggest received number
Examples

Test Code
Input
print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))



Output
[3, [2, 4]]
[6, [5, 7, 9]]
[46, [44, 45, 47, 48, 50]]


"""

##########: variant 1 :##########

def numbers_searching(*args):
    from collections import Counter

    counter = Counter(args)
    duplicates = sorted([num for num, count in counter.items() if count > 1])

    min_num = min(args)
    max_num = max(args)

    full_set = set(range(min_num, max_num + 1))
    present_set = set(args)
    missing_number = list(full_set - present_set)[0]

    return [missing_number, duplicates]

print(numbers_searching(1, 2, 4, 2, 5, 4))  # Output: [3, [2, 4]]
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))  # Output: [6, [5, 7, 9]]
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))  # Output: [46, [44, 45, 47, 48, 50]]



##########: variant 2 :##########



##########: variant 3 solution SoftUni :##########



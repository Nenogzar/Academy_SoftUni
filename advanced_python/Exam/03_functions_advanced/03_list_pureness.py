# ******* Advanced Exam - 24 October 2020 ******* #

# *******  03_list_pureness  ******* #
 
# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/2551#2


Write function called best_list_pureness which will receive a list of numbers and a number K.
You have to rotate the list K times (last becomes first) to find the variation of the list with the best pureness
(pureness is calculated by summing all the elements in the list multiplied by their indices).
For example, in the list [4, 3, 2, 6] with the best pureness is (3 * 0) + (2 * 1) + (6 * 2) + (4 * 3) = 26.
At the end the function should return a string containing the highest pureness and
    the amount of rotations that were made to find this pureness in the following format:
    "Best pureness {pureness_value} after {count_rotations} rotations".

If there is more than one highest pureness, take the first one.
Note: Submit only the function in the judge system

Input
•	There will be no input, just parameters passed to your function

Output
•	There is no expected output
•	The function should return a string in the following format:
    "Best pureness {pureness_value} after {count_rotations} rotations"

Examples

Test Code
test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

Output
Best pureness 26 after 3 rotations

Comment
Rotation 0 -> Pureness 25
Rotation 1 -> Pureness 16
Rotation 2 -> Pureness 23
Rotation 3 -> Pureness 26
Rotation 4 -> Pureness 25

Test Code
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

Output
Best pureness 78 after 2 rotations

Comment
Rotation 0 -> Pureness 60
Rotation 1 -> Pureness 66
Rotation 2 -> Pureness 78
Rotation 3 -> Pureness 78

Test Code
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)

Output
Best pureness 40 after 0 rotations


"""

##########: variant 1 :##########

def best_list_pureness(numbers, K):
    def calculate_pureness(nums):
        return sum(i * num for i, num in enumerate(nums))

    max_pureness = calculate_pureness(numbers)
    best_rotation = 0

    current_list = numbers[:]
    for rotation in range(1, K + 1):
        current_list = [current_list[-1]] + current_list[:-1]
        current_pureness = calculate_pureness(current_list)

        if current_pureness > max_pureness:
            max_pureness = current_pureness
            best_rotation = rotation

    return f"Best pureness {max_pureness} after {best_rotation} rotations"

# Test cases
test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)

##########: variant 2 :##########



##########: variant 3 solution SoftUni :##########



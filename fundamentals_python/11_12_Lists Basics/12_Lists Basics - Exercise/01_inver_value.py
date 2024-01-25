# Exercise - 1.	Invert Values
# Write a program that receives a single string containing positive and negative numbers separated by a single space.
# Print a list containing the opposite of each number.

# me_list = input()
# input_parts = input().split()
invert_list = [-int(x) for x in input().split()]
print(invert_list)


########################  From CEO #################################

# print([int(x) * - 1 for x in input().split()])


# numbers = input()
#
# lst = numbers.split(' ')
# new_list = list()
# for number in lst:
#
#     if number[0] == "-":
#         new_list.append(abs((int(number))))
#     else:
#         new_number = int(str("-" + number))
#         new_list.append(new_number)
#
# print(new_list)


# numbers = input()
#
# lst = numbers.split(' ')
# new_list = list()
#
# for number in lst:
#     result = int(number) * -1
#     new_list.append(result)
#
# print(new_list)

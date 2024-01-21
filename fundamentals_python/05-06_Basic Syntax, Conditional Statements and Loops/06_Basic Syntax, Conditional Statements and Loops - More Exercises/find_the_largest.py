""" 1 """
number = int(input())
number = str(number)
number = sorted(number)[::-1]
number = int("".join(number))
print(number)

""" from CEO """
# number_input = [n for n in input()]
# n = len(number_input)
#
# for i in range(n):
#     for j in range(0, n - i - 1):
#         if number_input[j] < number_input[j + 1]:
#             number_input[j], number_input[j + 1] = number_input[j + 1], number_input[j]
#
# sorted_number = ''.join(number_input)
#
# print(sorted_number)

""" from CEO """
# number_input = [n for n in input()]
# number_input.sort(reverse=True)
# for i in number_input:
#     print(i, end="")

""" from CEO """

# number_input = input()
#
# numbers = list(number_input)
# numbers.sort(reverse=True)
#
# for i in numbers:
#     print(i, end="")
# import math
#
# x, y, z = map(lambda r: math.floor(int(input())), range(3))
# sign = ''
# result = x * y * z
#
# if result < 0:
#     sign = 'negative'
# elif result > 0:
#     sign = 'positive'
# else:
#     sign = 'zero'
#
# print(sign)

""" 1 """
import math

# Въвеждане на три числа и закръгляне надолу до най-близкото цяло
x, y, z = map(lambda r: math.floor(int(input())), range(3))

def check_numbers(one, two, three):
    if (three > 0 and one < 0 and two < 0) or \
            (two > 0 and one < 0 and three < 0) or \
            (one > 0 and two < 0 and three < 0) or \
            (one > 0 and two > 0 and three > 0):
        return "positive"
    elif one == 0 or two == 0 or three == 0:
        return "zero"
    elif one < 0 or two < 0 or three < 0:
        return "negative"

print(check_numbers(x, y, z))


""" 2 """

def check_numbers(first, second, third):
    if any(x == 0 for x in (first, second, third)):
        return "zero"

    if all(x > 0 for x in (first, second, third)) or \
            sum(1 for x in (first, second, third) if x < 0) == 2:
        return "positive"

    return "negative"


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(check_numbers(first_number,
                    second_number,
                    third_number
                    )
      )
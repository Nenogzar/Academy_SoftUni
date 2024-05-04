# def is_balanced(expression):
#     stack = []
#     opening_brackets = "([{"
#     closing_brackets = ")]}"
#     brackets_map = {')': '(', ']': '[', '}': '{'}
#
#     for char in expression:
#         if char in opening_brackets:
#             stack.append(char)
#         elif char in closing_brackets:
#             if not stack:
#                 return "NO"
#             last_opening_bracket = stack.pop()
#             if brackets_map[char] != last_opening_bracket:
#                 return "NO"
#
#     if stack:
#         return "NO"
#     else:
#         return "YES"
#
# print(is_balanced(input()))

""" """
from collections import deque

parentheses = deque(input())
check = []
while parentheses:
    current = parentheses.popleft()
    if current in "{[(":
        check.append(current)
    elif current in "}])" and check:
        if check.pop() + current not in "()[]{}":
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")

""" """

# from collections import deque
#
# parentheses = deque(input())
# open_per = deque()
# balanced = True
# while parentheses:
#     check_par = parentheses.popleft()
#     if check_par in "{[(":
#         open_per.append(check_par)
#     elif not open_per:
#         balanced = False
#         break
#     else:
#         check_last_par = open_per.pop()
#         test_pair = f"{check_last_par + check_par}"
#         if test_pair not in "{}()[]":
#             balanced = False
#             break
#
# if balanced and not open_per:
#     print("YES")
# else:
#     print("NO")

""" """
# from collections import deque
#
# expression = deque(input())
# opening_brackets = "([{"
# closing_brackets = ")]}"
# counter = 0
#
# while expression and counter < len(expression) / 2:
#     if expression[0] not in opening_brackets:
#         break
#     index = opening_brackets.index(expression[0])
#     if expression[1] == closing_brackets[index]:
#         expression.popleft()
#         expression.popleft()
#         expression.rotate(counter)
#         counter = 0
#     else:
#         expression.rotate(-1)
#         counter += 1
# if expression:
#     print("NO")
# else:
#     print("Yes")

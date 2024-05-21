#################################### TASK CONDITION ############################
"""
                         6. Balanced Parentheses
You will be given a sequence consisting of parentheses. 
Your job is to determine whether the expression is balanced. 
A sequence of parentheses is balanced if every opening 
parenthesis has a corresponding closing parenthesis that occurs 
after the former. There will be no interval symbols between 
the parentheses. You will be given three types of parentheses: (), {}, and [].

{[()]} - Parentheses are balanced.
(){}[] - Parentheses are balanced.
{[(])} - Parentheses are NOT balanced.
Input
•	On a single line, you will receive a sequence of parentheses.
Output 
•	For each test case, print on a new line "YES" if the parentheses are balanced. 
•	Otherwise, print "NO"
Constraints
•	1 ≤ lens ≤ 1000, where the lens is the length of the sequence
•	Each character of the sequence will be one of {, }, (, ), [, ]

____________________________________________________________________________________________
Example_01

Input
{[()]}	

Output
YES

____________________________________________________________________________________________
Example_02

Input
{[(])}	

Output
NO

____________________________________________________________________________________________
Example_02

Input
{{[[(())]]}}

Output
YES

"""
""" 1 """
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

""" 2 """
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

""" 3 """

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

""" 4 """
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

""" 5 - Bi """
from collections import deque

parentheses = list(input())
open_parenthesis = {"[": "]", "{": "}", "(": ")"}
is_balanced = deque()

for el in parentheses:

    if el in open_parenthesis.keys():
        is_balanced.append(el)
    else:
        if is_balanced and open_parenthesis[is_balanced[-1]] == el:
            is_balanced.pop()
        else:
            print("NO")
            break
else:
    print("YES")


""" 6 """

input_string = input()
stack = []
balanced = True

for char in input_string:
    if char in "([{":
        stack.append(char)
    else:
        if not stack:
            balanced = False
            break
        last_opening = stack.pop()
        if (char == ")" and last_opening != "(") or \
           (char == "]" and last_opening != "[") or \
           (char == "}" and last_opening != "{"):
            balanced = False
            break

if stack:
    balanced = False

if balanced:
    print("YES")
else:
    print("NO")

""" 7 """

from collections import deque


class BalancedParentheses:

    def __init__(self):
        self.sequence = deque(input())
        self.is_balanced = True
        self.opening_brackets = []
        self.balancing = {"(": ")", "[": "]", "{": "}"}
        self.message = ''
        self.main()

    def check_brackets(self, some_bracket):
        opening_bracket = self.opening_brackets.pop()
        if self.balancing[opening_bracket] != some_bracket:
            self.is_balanced = False

    def check_for_balancing(self):
        while self.sequence and self.is_balanced:
            bracket = self.sequence.popleft()
            if bracket in "{[(":
                self.opening_brackets.append(bracket)
            elif self.opening_brackets:
                self.check_brackets(bracket)
            else:
                self.is_balanced = False


    def prepare_result(self):
        self.message = 'YES' if self.is_balanced else 'NO'

    def main(self):
        self.check_for_balancing()
        self.prepare_result()

    def __repr__(self):
        return self.message


if __name__ == "__main__":
    print(BalancedParentheses())

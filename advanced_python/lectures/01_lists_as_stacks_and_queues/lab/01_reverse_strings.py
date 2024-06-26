#################################### TASK CONDITION ############################
"""

1.	Reverse Strings
Write program that:
•	Reads an input string
•	Reverses it using a stack
•	Prints the result back on the console

____________________________________________________________________________________________
Example_01

Input
I Love Python

Output
nohtyP evoL I

____________________________________________________________________________________________
Example_02

Input
Stacks and Queues

Output
seueuQ dna skcatS

"""

from collections import deque

# input_str = input()
#
# stack = []
# new_str = ''
#
# for letter in input_str:
#     stack.append(letter)
#
# while stack:
#     new_str += stack.pop()
#
# print(new_str)        # time 1.14

"""test values"""

# Input:      I Love Python
# Output:     nohtyP evoL I
#
# Input:      Stacks and Queues
# Output:     seueuQ dna skcatS


""" OR """

# test = list(input())
# while test:
# 	print(test.pop(),end="")    

""" OR """

# test = list(input())
# stack = []
# for index in range(len(test)):
# 	stack.append(test.pop())
# print("".join(stack))       

""" Whit deque """

stack = deque(input())
# print(stack)
stack.reverse()
print(*stack, sep="")       

""" """
class ReverseString:

    def __init__(self, stack):
        self.stack = stack
        self.reversed_stack = []

    def reversing_string(self):
        for _ in range(len(self.stack)):
            self.reversed_stack.append(self.stack.pop())

    def __repr__(self):
        return ''.join(self.reversed_stack)

string = [char for char in input()]

output = ReverseString(string)
output.reversing_string()
print(output)

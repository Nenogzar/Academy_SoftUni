import time
from collections import deque

start_time = time.time()


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
# 	print(test.pop(),end="")    # time 1.13

""" OR """

# test = list(input())
# stack = []
# for index in range(len(test)):
# 	stack.append(test.pop())
# print("".join(stack))       # time 1.17

""" Whit deque """

stack = deque(input())
# print(stack)
stack.reverse()
print(*stack, sep="")       # time  1.08



end_time = time.time()
execution_time = end_time - start_time
print(f"Време за изпълнение:, {execution_time:.2f}, секунди")


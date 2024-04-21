""" reverse numbers """
input_list = list(map(int, input().split()))
new_list =[]
for _ in range(len(input_list)):
    new_list= list(reversed(input_list))    # reverse
print(' '.join(map(str, new_list)))

""" reverse numbers  whit stack """
input_list = list(map(int, input().split()))
new_list =[]
for _ in range(len(input_list)):
    new_list.append(input_list.pop())     # stacks
print(' '.join(map(str, new_list)))

""" reverse number whit queues """
from collections import deque           # queues
number = input().split()
reversed_list = deque(number)
new_list =[]
for _ in range(len(reversed_list)):
    new_list.append(reversed_list.pop())
print(" ".join(new_list))


# input:                output:
# 1 2 3 4 5             5 4 3 2 1

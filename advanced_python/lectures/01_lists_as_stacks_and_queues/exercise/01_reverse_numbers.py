#################################### TASK CONDITION ############################
"""

                       1.	Reverse Numbers
Write a program that reads a string with N integers from the console, 
separated by a single space, and reverses them using a stack. 
Print the reversed integers on one line, separated by a single space.

____________________________________________________________________________________________
Example_01

Input
1 2 3 4 5	

Output
5 4 3 2 1

____________________________________________________________________________________________
Example_02

Input
1

Output
1

"""
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

""" qceka88 """
class Reversing:

    def __init__(self):
        self.initial_string = input().split()
        self.reversed_string = []
        self.reversing_string()

    def reversing_string(self):
        while self.initial_string:
            self.reversed_string.append(self.initial_string.pop())

    def __repr__(self):
        return f'{" ".join(self.reversed_string)}'


if __name__ == "__main__":
    print(Reversing())

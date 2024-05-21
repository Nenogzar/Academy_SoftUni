#################################### TASK CONDITION ############################
"""
                        2. Stacked Queries
You have an empty stack. You will receive an integer – N. 
On the next N lines, you will receive queries. Each query is one of these four types:
•	'1 {number}' – push the number (integer) into the stack
•	'2' – delete the number at the top of the stack
•	'3' – print the maximum number in the stack
•	'4' – print the minimum number in the stack
It is guaranteed that each query is valid.
After you go through all the queries, print the stack from top to bottom in the following format:
"{n}, {n1}, {n2}, ... {nn}"

____________________________________________________________________________________________
Example_01

Input
9
1 97
2
1 20
2
1 26
1 20
3
1 91
4

Output
26
20
91, 20, 26

____________________________________________________________________________________________
Example_02

Input
10
2
1 47
1 66
1 32
4
3
1 25
1 16
1 8
4

Output
32
66
8
8, 16, 25, 32, 66, 47


"""

"""whit dictionary"""
stack = []

def delete():
    stack.pop()

def print_max():
    max_value = max(stack)
    print(*max_value)

def print_min():
    min_value = min(stack)
    print(*min_value)

commands = {
    '2': delete,
    '3': print_max,
    '4': print_min
}

# N = int(input())
# for _ in range(N):
#     query = input().split()
#     command = query[0]
#     if command == '1':
#         number = int(query[1])
#         commands[command](number)
#     else:
#         commands[command]()

N = int(input())
for _ in range(N):
    command, *numbers = input().split()
    if command == '1':
        number = [int(num) for num in numbers]
        stack.append(number)
    else:
        if stack:
            commands[command]()

reversed_stack = reversed(stack)
print(', '.join(str(*item) for item in reversed_stack))





""" """
# number_of_commands = int(input())
#
# stack_queries = []
#
# def check_stack_size():
#     if len(stack_queries) != 0:
#         return True
#
# for _ in range(number_of_commands):
#     command = input()
#     if command.startswith("1"):
#         __, number = command.split()
#         stack_queries.append(int(number))
#     elif check_stack_size():
#         if command.startswith("2"):
#             stack_queries.pop()
#         elif command.startswith("3"):
#             print(max(stack_queries))
#         elif command.startswith("4"):
#             print(min(stack_queries))
#
# print(", ".join(str(stack_queries.pop()) for n in range(len(stack_queries))))

""" qceka88 """
##################################### variant 01 #####################################
class StacketQueries:

    def __init__(self):
        self.number = int(input())
        self.stack = []
        self.actions = {1: self.push_number,
                        2: self.delete_number,
                        3: self.find_max_number,
                        4: self.find_min_number}
        self.log_file = []

    def push_number(self, some_data):
        self.stack.append(some_data[1])

    def delete_number(self, some_data):
        if self.stack:
            self.stack.pop()

    def find_max_number(self, some_data):
        if self.stack:
            self.log_file.append(max(self.stack))

    def find_min_number(self, some_data):
        if self.stack:
            self.log_file.append(min(self.stack))

    def actions_with_numbers(self):
        for iteration in range(self.number):
            input_line = list(map(int, input().split()))
            self.actions[input_line[0]](input_line)

    def __repr__(self):
        return '\n'.join(str(n) for n in self.log_file) + "\n" + ', '.join(map(str, self.stack[::-1]))


if __name__ == '__main__':
    output = StacketQueries()
    output.actions_with_numbers()
    print(output)
##################################### variant 02 #####################################
class StacketQueries:

    def __init__(self):
        self.number = int(input())
        self.stack = []
        self.actions = {1: lambda x: self.stack.append(x[1]),
                        2: lambda x: self.stack.pop() if self.stack else None,
                        3: lambda x: self.log_file.append(max(self.stack)) if self.stack else None,
                        4: lambda x: self.log_file.append(min(self.stack)) if self.stack else None}
        self.log_file = []

    def actions_with_numbers(self):
        for iteration in range(self.number):
            input_line = list(map(int, input().split()))
            self.actions[input_line[0]](input_line)

    def __repr__(self):
        return '\n'.join(str(n) for n in self.log_file) + "\n" + ', '.join(map(str, self.stack[::-1]))


if __name__ == '__main__':
    output = StacketQueries()
    output.actions_with_numbers()
    print(output)



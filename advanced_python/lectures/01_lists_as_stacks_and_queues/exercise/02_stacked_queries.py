import time
start_time = time.time()
"""whit dictionary"""
stack = []

def push(number):
    stack.append(number)

def delete():
    if stack:
        stack.pop()

def print_max():
    if stack:
        print(max(stack))

def print_min():
    if stack:
        print(min(stack))

commands = {
    '1': push,
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
        numbers = [int(num) for num in numbers]
        commands[command](*numbers)
    else:
        commands[command]()

print(", ".join(map(str, reversed(stack))))


""" time = 1.26"""


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

""" time = 1.33"""

end_time = time.time()
print("Execution time: {:.2f} seconds".format(end_time - start_time))
""" """

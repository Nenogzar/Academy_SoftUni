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


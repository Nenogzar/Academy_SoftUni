first_line = set(int(x) for x in input().split())
second_line = set(int(x) for x in input().split())

for _ in range(int(input())):
    command = input().split()
    action, arg = command[0] + " " + command[1], command[2:]

    if action == 'Add First':
        for num in arg:
            first_line.add(int(num))
    elif action == 'Add Second':
        for num in arg:
            second_line.add(int(num))
    elif action == 'Remove First':
        for num in arg:
            first_line.discard(int(num))
    elif action == 'Remove Second':
        for num in arg:
            second_line.discard(int(num))
    elif action == 'Check Subset':
        print(second_line.issubset(first_line))

print(*sorted(first_line), sep=", ")
print(*sorted(second_line), sep=", ")




"""  comprehention """
first_line = set(int(x) for x in input().split())
second_line = set(int(x) for x in input().split())

for _ in range(int(input())):
    command = input().split()
    action, arg = command[0] + " " + command[1], command[2:]

    if action == 'Add First':
        {first_line.add(int(num)) for num in arg}
    elif action == 'Add Second':
        {second_line.add(int(num)) for num in arg}
    elif action == 'Remove First':
        {first_line.discard(int(num)) for num in arg}
    elif action == 'Remove Second':
        {second_line.discard(int(num)) for num in arg}
    elif action == 'Check Subset':
        print(second_line.issubset(first_line))

print(*sorted(first_line), sep=", ")
print(*sorted(second_line), sep=", ")

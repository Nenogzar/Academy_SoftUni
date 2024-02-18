count_of_numbers = list(map(int, input().split()))
command = input().split()
while command[0] != "Finish":
    if len(command) <= 2:
        action = command[0]
        value = int(command[1])
        if action == "Add":
            count_of_numbers.append(value)
        elif action == "Remove":
            count_of_numbers.remove(value)
        elif action == "Collapse":
            for i in count_of_numbers:
                if i < value:
                    count_of_numbers.remove(i)
    elif len(command) > 2:
        value = int(command[1])
        replacement = int(command[2])

        index = count_of_numbers.index(value)
        count_of_numbers.pop(index)
        count_of_numbers.insert(index, replacement)

    command = input().split()

print(*count_of_numbers, sep=" ")
def add_num(list_num, num):
    list_num.append(num)
    return list_num


def rem_num(list_num, num):
    if num in list_num:
        list_num.remove(num)
    return list_num


def rep_num(list_num, num, r_num):
    if num in list_num:
        index = list_num.index(num)
        list_num[index] = r_num
    return list_num


def colaps_num(list_num, upper_limit):
    filtered_list = [num for num in list_num if num >= upper_limit]
    return filtered_list


input_numbers = list(map(int, input().split(" ")))
command = input()
while command != "Finish":

    command_list = list(map(str, command.split(" ")))
    if len(command_list) == 2:
        first = int(command_list[1])
    elif len(command_list) == 3:
        first, second = int(command_list[1]), int(command_list[2])

    if command_list[0] == "Add":
        input_numbers = add_num(input_numbers, first)
    elif command_list[0] == "Remove":
        input_numbers = rem_num(input_numbers, first)
    elif command_list[0] == "Replace":
        input_numbers = rep_num(input_numbers, first, second)
    elif command_list[0] == "Collapse":
        input_numbers = colaps_num(input_numbers, first)

    command = input()

result_string = ' '.join(map(str, input_numbers))
print(result_string)

#function#

def add_num(list_num, num):
    list_num.append(num)
    return list_num


def rem_num(list_num, num):
    if num in list_num:
        list_num.remove(num)
    return list_num


def rep_num(list_num, num, r_num):
    if num in list_num:
        index = list_num.index(num)
        list_num[index] = r_num
    return list_num


def collapse_num(list_num, upper_limit):
    list_num = [num for num in list_num if num >= upper_limit]
    return list_num


def execute_command(command_list, input_numbers):
    if len(command_list) == 2:
        first = int(command_list[1])
    elif len(command_list) == 3:
        first, second = int(command_list[1]), int(command_list[2])

    if command_list[0] == "Add":
        return add_num(input_numbers, first)
    elif command_list[0] == "Remove":
        return rem_num(input_numbers, first)
    elif command_list[0] == "Replace":
        return rep_num(input_numbers, first, second)
    elif command_list[0] == "Collapse":
        return collapse_num(input_numbers, first)


input_numbers = list(map(int, input().split(" ")))
command = input()

while command != "Finish":
    command_list = list(map(str, command.split(" ")))
    input_numbers = execute_command(command_list, input_numbers)
    command = input()

result_string = ' '.join(map(str, input_numbers))
print(result_string)


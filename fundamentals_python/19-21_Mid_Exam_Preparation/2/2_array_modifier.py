def swap_element(list_mod, index1, index2):
    list_copy = list(list_mod)
    temp = list_copy[index1]
    list_copy[index1] = list_copy[index2]
    list_copy[index2] = temp
    return list_copy


def multiply_element(list_mod, index1, index2):
    list_copy = list(list_mod)
    list_copy[index1] = list_copy[index1] * list_copy[index2]
    return list_copy


list_to_modifier = list(map(int, input().split()))
command = input()

while command != "end":

    comman_list = list(map(str, command.split(" ")))
    if len(comman_list) > 1:
        firs, second = int(comman_list[1]), int(comman_list[2])

    if comman_list[0] == "swap":
        list_to_modifier = swap_element(list_to_modifier, firs, second)
    elif comman_list[0] == "multiply":
        list_to_modifier = multiply_element(list_to_modifier, firs, second)
    elif comman_list[0] == "decrease":
        list_to_modifier = [x - 1 for x in list_to_modifier]

    command = input()

result_string = ', '.join(map(str, list_to_modifier))
print(result_string)

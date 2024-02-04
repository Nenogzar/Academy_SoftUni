# input_string = list(map(int, input().split(", ")))
#
# for num in input_string:
#     num_str = str(num)
#     if num_str == num_str[::-1]:
#         command = "True"
#     else:
#         command = "False"
#
#     print(command)


""" 2 """

# input_string = list(map(int, input().split(", ")))
# result = ["True" if str(num) == str(num)[::-1] else "False" for num in input_string]
# print("\n".join(result))

""" 3 """

def palindrom_func(input):
    results = []
    for num in input:
        num_str = str(num)
        if num_str == num_str[::-1]:
            results.append("True")
        else:
            results.append("False")
    return results

inp_string = list(map(int, input().split(", ")))
palindrom = palindrom_func(inp_string)
print("\n".join(palindrom))


input_str = input()
new_list = list(map(int, input_str.split()))
sorted_list = sorted(new_list)
print(sorted_list)

""" 2 """

print(sorted(list(map(int, input().split()))))

""" 3 """


def convert_to_int_list(input_string):
    return sorted(list(map(int, input_string.split())))


# Example usage:
input_numbers = input()
result_list = convert_to_int_list(input_numbers)
print(result_list)

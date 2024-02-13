# # That means the new list-of-lists should contain lists of the first item from each list, the second item from each and so on:
# matrix = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
# # list-of-lists
# transposed_matrix = list(map(list, zip(*matrix)))
#
# print(transposed_matrix)
# ##
# # list-of-tuple
# transposed_list = list(zip(*matrix))
#
# print(transposed_list)
#
# ###
#
# csv_data = [
#     ["Mary's Coffee", "3.50", "Dining"],
#     ["Spirit", "187.00", "Travel"],
#     ["Joe's Eats", "24.28", "Dining"],
#     ["Metro", "12.00", "Travel"],
#     ["Lyft", "23.45", "Travel"],
#     ["Lyft", "4.00", "Travel"],
#     ["Mary's Coffee", "6.75", "Dining"],
# ]
#
# transposed_csv = list(map(list, zip(*csv_data)))
# for i in range(0, len(transposed_csv)):
#     print(f"{i}: {transposed_csv[i]}]")
# print(transposed_csv)
#


####
import string

csv_data = [
    ["Mary's Coffee", "3.50", "Dining"],
    ["Spirit", "187.00", "Travel"],
    ["Joe's Eats", "24.28", "Dining"],
    ["Metro", "12.00", "Travel"],
    ["Lyft", "23.45", "Travel"],
    ["Lyft", "4.00", "Travel"],
    ["Mary's Coffee", "6.75", "Dining"],
]

transposed_csv = list(map(list, zip(*csv_data)))

variable_names = list(string.ascii_lowercase)  # ['a', 'b', 'c', ..., 'z']
result_dict = {}

for i, variable_name in enumerate(variable_names):
    if i < len(transposed_csv):
        result_dict[variable_name] = transposed_csv[i]

# Принтиране на резултата
for key, value in result_dict.items():
    print(f"{key}: {value}")



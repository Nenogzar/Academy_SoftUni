""" 1 """
# num_str = int(input())
#
# for string in range(num_str):
#     pure_str = input()
#     if "," in pure_str or \
#         "." in pure_str or \
#         "_" in pure_str:
#         print(f"{pure_str} is not pure!")
#     else:
#         print(f"{pure_str} is pure.")

""" 2 """
# how_many_strings = int(input())
#
# skip_parameters = [",", ".", "_"]
#
# for _ in range(how_many_strings):
#     string_ = input()
#     for element in skip_parameters:
#         if element in string_:
#             print(f"{string_} is not pure!")
#             break
#     else:
#         print(f"{string_} is pure.")

""" 3 """
# string_number = int(input())
# special_chars = [',', '.', '_']
# contains_comma = False
# contains_dot = False
# contains_underscore = False
#
# for _ in range(string_number):
#     my_string = input()
#
#
#     for char in special_chars:
#         if char in my_string:
#             if char == ',':
#                 contains_comma = True
#             elif char == '.':
#                 contains_dot = True
#             elif char == '_':
#                 contains_underscore = True
#
#     if contains_comma or contains_dot or contains_underscore:
#         print(f"{my_string} is not pure!")
#     else:
#         print(f"{my_string} is pure.")


""" 4 """
num_strings = int(input())

for _ in range(num_strings):
    my_string = input()

    contains_special_chars = any(char in my_string for char in [',', '.', '_'])

    if contains_special_chars:
        print(f"{my_string} is not pure.")
    else:
        print(f"{my_string} is pure.")


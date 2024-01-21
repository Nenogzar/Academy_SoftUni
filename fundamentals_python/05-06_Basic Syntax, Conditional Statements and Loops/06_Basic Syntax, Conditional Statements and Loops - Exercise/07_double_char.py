""" 1 """
# current_string = input()
# while current_string != "End":
#     if current_string != "SoftUni":
#         new_string = ""
#         for char in current_string:
#             new_string += char * 2
#         print(new_string)
#     current_string = input()

""" 2 """
#
# string_current = input()
#
# while string_current != "End":
#     if string_current != "SoftUni":
#         [print(i * 2, end="") for i in string_current]
#         print()
#     string_current = input()
#
#
""" 3 """
command = input()
while command != "End":
    if command != "SoftUni":
        for char in command:
            print(char * 2, end="")
        print()  # Добавяме нов ред след всяка итерация
    command = input()

""" 4 """
for string_input in iter(input,"End"):
    if string_input != "SoftUni":
        doubled_string = ''.join(char * 2 for char in string_input)
        print(doubled_string)

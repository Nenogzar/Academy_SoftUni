""" automatic file generation, according to the specified text """

import os

section_name = input("Section: ")
judge_link = input("Judge link: ")

matrix = []
input_string = input("File name: ")

while input_string:
    input_string = input_string.replace('*', '').replace('.', '').replace('-', '')
    input_string = ('_'.join(input_string.split())).lower()

    matrix.append(input_string)
    input_string = input()

for file_name in matrix:
    with open(f"{file_name}.py", "w") as file:
        symbol  = "# ******* "
        file.write(f'{symbol}{section_name}{symbol[::-1]}\n'
                   f'\n{symbol}{" " + file_name + " "}{symbol[::-1]}\n '
                   f'\n{symbol} TASK CONDITION {symbol[::-1]}\n'
                   f'"""\n '
                   f'{judge_link}\n'
                   f'\n"""\n'
                   f'\n##########: SOLUTION :##########\n\n\n'
                   f'\n##########: TEST CODE :##########\n\n\n'
                   f'\n"""\nOutput:\n\n """'
                   f'\n##########: UNITTEST :##########\n\n\n')

print("The files were created successfully.")


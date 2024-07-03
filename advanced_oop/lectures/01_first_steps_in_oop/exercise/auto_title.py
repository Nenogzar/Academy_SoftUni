""" automatic file generation, according to the specified text """

import os

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
        file.write(f'{(symbol ) + input("Section : ") + ( symbol[::-1])}\n'
                    f'\n{(symbol ) + (" "+ file_name + " ") + ( symbol[::-1])}\n '
                    f'\n{(symbol ) + " TASK CONDITION " + ( symbol[::-1])}\n'
                    f'"""\n '
                    f'{input("Judge link: ")}\n'
                    f'\n"""'
                    f'\n##########: variant 1 :##########\n\n\n'
                    f'\n##########: variant 2 :##########\n\n\n'
                    f'\n##########: variant 3 solution SoftUni :##########\n\n\n')

print("The files were created successfully.")



First Steps in OOP - Exercise
https://judge.softuni.org/Contests/Compete/Index/1935
""" automatic file generation, according to the specified text """

import os

matrix = []
input_string = input()


while input_string:
    input_string = input_string.replace('*', '').replace('.', '').replace('-', '')
    input_string = ('_'.join(input_string.split())).lower()

    matrix.append(input_string)
    input_string = input()

for file_name in matrix:
    with open(f"{file_name}.py", "w") as file:
        symbol  = "#"
        file.write(f'{(30*symbol) + (" "+ file_name+ " ") + (30*symbol)}\n '
                   f' {(30*symbol) + " TASK CONDITION " + (30*symbol)}'
                   f'\n"""\n '
                   f'{input("Judge link: ")}'
                   f'\n"""\n'
                   f'\n##########: variant 1 :##########\n\n\n'
                   f'\n##########: variant 2 whit Dictionary :##########\n\n\n'
                   f'\n##########: variant 3 solution SoftUni :##########\n\n\n')

print("Файловете бяха успешно създадени.")
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
                   f'\n"""\n https://judge.softuni.org/Contests/Practice/Index/3889#0'
                   f'\n\n"""')

print("Файловете бяха успешно създадени.")
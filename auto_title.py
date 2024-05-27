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

        file.write("# This file was created automatically\n")

print("The files were created successfully.")

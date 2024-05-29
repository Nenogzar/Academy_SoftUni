import os

matrix = []
input_string = input()
while input_string:
    input_string = input_string.replace('*', '').replace('.', '').replace('-', '')
    input_string = ('_'.join(input_string.split())).lower()

    matrix.append(input_string)
    input_string = input()

for dir_name in matrix:
    os.makedirs(dir_name, exist_ok=True)

print("Директориите бяха успешно създадени.")
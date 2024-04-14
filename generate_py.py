import os

while True:
    input_string = input("Input String: ")
    input_string = input_string.replace('*', '').replace('.', '').replace('-', '')
    input_string = '_'.join(input_string.split())
    formatted_string = input_string.lower()

    file_name = formatted_string + ".py"

    with open(file_name, "w"):
        pass

    repeat = input("Repeat? (Y/N)? ")
    if repeat.upper() == "N":
        print("Bye!")
        break
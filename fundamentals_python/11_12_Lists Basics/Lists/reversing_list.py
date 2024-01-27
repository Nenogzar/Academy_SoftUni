while True:
    input_string = input(
        "Въведете части на списък, разделени със запетайка: ")  # дефиниране на променлива която присвоява текст
    input_parts = input_string.split(',')  # преобразуване в string list

    try:
        parts = [int(part.strip()) for part in input_parts]  # преобразуване в string  в  int

        reversing_list = parts [::-1]

        print(f"Реверсията на стринга {parts} e {reversing_list}")
    except ValueError:
        print("Невалидни входни данни. Моля, въведете числови стойности разделени със запетайка.")

    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break
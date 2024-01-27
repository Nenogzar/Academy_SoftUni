while True:

    input_string = input("Въведете части на списък, разделени със запетайка: ") # дефиниране на променлива която присвоява текст
    input_parts = input_string.split(',')  # преобразуване в string list
    print(input_parts)
    try:
        parts = [int(part.strip()) for part in input_parts] # преобразуване в string  в  int
        print(parts)

        max_index = parts.index(max(parts))

        print("Максималният индекс на елемент от списъка е:", max_index )
    except ValueError:
        print("Невалидни входни данни. Моля, въведете числови стойности разделени със запетайка.")

    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break

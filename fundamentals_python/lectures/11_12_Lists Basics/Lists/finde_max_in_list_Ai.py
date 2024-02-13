while True:

    input_string = input("Въведете части на списък, разделени със запетайка: ")
    input_parts = input_string.split(',')

    try:
        parts = [int(part.strip()) for part in input_parts]
        print(parts)
        max_element = max(parts)  # Намиране на максималния елемент
        print("Максималният елемент от списъка е:", max_element)
    except ValueError:
        print("Невалидни входни данни. Моля, въведете числови стойности разделени със запетайка.")



    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break

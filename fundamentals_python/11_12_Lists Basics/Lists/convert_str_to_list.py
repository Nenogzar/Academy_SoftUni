while True:

    input_string = input("Въведете части на списък, разделени със запетайка: ") # дефиниране на променлива която присвоява текст
    input_parts = input_string.split(',')  # преобразуване в string list

    my_list = list(input_string)

    print(f"input_string - {input_string} - присвоява текста")
    print(f"input_parts - {input_parts} - присвоения текст го вкарва в списък")
    print(f"my_list - {my_list} - раздробява списъка ")
    try:
        parts = [int(part.strip()) for part in input_parts] # преобразуване в string  в  int
        print(f"parts - {parts} обединява само стойностите в списък")
        #code

        print("***", {"function"} )
    except ValueError:
        print("Невалидни входни данни. Моля, въведете числови стойности разделени със запетайка.")



    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break

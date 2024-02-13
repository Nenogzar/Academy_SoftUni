# колко пъти въведеното число се среща в списъка.
while True:

    input_string = input("Въведете части на списък, разделени със запетайка: ") # дефиниране на променлива която присвоява текст
    num = int(input("кое число броим?"))
    input_parts = input_string.split(',')  # Преобразуване в list по разделител ','

    try:
        # преобразуване от string  в  int
        parts = [int(part.strip()) for part in input_parts]

        #ще търси елемент (num), колко пъти се повтаря в листа
        count_num = parts.count(num)

        print(f"числото {num} се повтаря {count_num} пъти в листа: {parts}")
    except ValueError:
        print("Невалидни входни данни. Моля, въведете числови стойности разделени със запетайка.")

    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break

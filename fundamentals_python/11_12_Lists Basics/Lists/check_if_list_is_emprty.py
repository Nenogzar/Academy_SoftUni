while True:

    input_string = input("Въведете части на списък, разделени със запетайка: ") # дефиниране на променлива която присвоява текст
    input_parts = input_string.split(',')  # преобразуване в string list

    if not input_string: #Проверка дали списъка е празен, ако да печати
        print("list is empty")
        continue

    parts = [int(part.strip()) for part in input_parts]



        #print("***", {"function"} )
    #except ValueError:
        #print("Невалидни входни данни. Моля, въведете числови стойности разделени със запетайка.")

    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break

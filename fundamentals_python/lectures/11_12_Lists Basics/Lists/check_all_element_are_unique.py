# колко пъти въведеното число се среща в списъка.
while True:

    input_string = input("Въведете части на списък, разделени със запетайка: ") # дефиниране на променлива която присвоява текст

    input_parts = input_string.split(',')  # Преобразуване в list

    try:
        # преобразуване от string  в  int
        parts = [int(part.strip()) for part in input_parts]
        print(f"int списъка е: {input_parts}")
        if len(parts) == len(set(parts)):
            print("all elements are unique")
        else:
            non_unique_elements = []
            for num in parts:
                if parts.count(num) > 1 and num not in non_unique_elements:
                    non_unique_elements.append(num)
                    count_num = parts.count(num)
                    print(f"Елементът {num} не е уникален. Среща се {count_num} пъти.")


    except ValueError:
        print("Невалидни входни данни. Моля, въведете числови стойности разделени със запетайка.")

    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break

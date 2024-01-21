while True:
    screening_type = input("Каква е прожекцията: /Premiere, Normal, Discount/: ")
    rows = input("Колко преда има в залата: ")
    column = input("колко колони има в залата: ")
    income = float(0)
    capacity = int(rows) * int(column)

    if screening_type == "Premiere":
        income = capacity * 12.00
    elif screening_type == "Normal":
        income = capacity * 7.50
    elif screening_type == "Discount":
        income = capacity * 5.00
    else:
        input("Неправилна пржекция!")
        continue
    print(f"{income:.2f} leva")
    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break

while True:
    num = input("Въседете число от 1 - 7 за дните на седмицата:")
    if num != "" and (1 <= int(num) <= 7):
        num = int(num)
    else:
        print("Error")

    if num == 1:
        print("Monday")
    elif num == 2:
        print("Tuesday")
    elif num == 3:
        print("Wednesday")
    elif num == 4:
        print("Thursday")
    elif num == 5:
        print("Friday")
    elif num == 6:
        print("Saturday")
    else:
        print("Sunday")

    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break
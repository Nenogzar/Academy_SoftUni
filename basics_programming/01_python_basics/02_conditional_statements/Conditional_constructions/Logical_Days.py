while True:

    day = input("Изберете ден от седмицата: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday: ")

    a = "Working day"
    b = "Weekend"
    if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
        day = a
    elif day == "Saturday" or day == "Sunday":
        day = b
    else:
        print("Error")

    if day != "":
        print(day)
    else:
        print("Error")
        continue

    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break

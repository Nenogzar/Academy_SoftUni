while True:

    fruits = input("Въведете плод: banana / apple / orange / grapefruit / kiwi / pineapple / grapes: ")
    days = input("Въведете ден от седмицата: Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Sunday: ")
    quantity = float(input("Какво количество: "))
    price = 1
    total_price = 1
    if days == "Monday" or days == "Tuesday" or days == "Wednesday" or days == "Thursday" or days == "Friday":
        if fruits == "banana":
            price = 2.5
        elif fruits == "apple":
            price = 1.2
        elif fruits== "orange":
            price = 0.85
        elif fruits == "grapefruit":
            price = 1.45
        elif fruits == "kiwi":
            price = 2.7
        elif fruits == "pineapple":
            price = 5.5
        elif fruits == "grapes":
            price = 3.85
        else:
            print("error")
            continue
        total_price = price * quantity
    elif days == "Saturday" or days == "Sunday":
        if fruits == "banana":
            price = 2.7
        elif fruits == "apple":
            price = 1.25
        elif fruits == "orange":
            price = 0.90
        elif fruits == "grapefruit":
            price = 1.60
        elif fruits == "kiwi":
            price = 3.00
        elif fruits == "pineapple":
            price = 5.6
        elif fruits == "grapes":
            price = 4.2
        else:
            print("error")
            continue
        total_price = price * quantity
    else:
        print("Неправилен ден от седмицата")
        continue

    print(f"{total_price:.2f}")

    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break

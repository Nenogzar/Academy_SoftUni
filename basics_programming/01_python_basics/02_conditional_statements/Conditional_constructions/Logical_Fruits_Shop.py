while True:
    days = input("Изберете ден от седмицата: M, T, W, Th, F, S, Su: ")
    if days == "": #проверка дали e празен
        continue
    fruits = input("Изберете плод: banana, apple, orange, grapefruit, pineapple, grapes: ")
    if fruits == "": #проверка дали e празен
        continue
    quantity = input("Какво количество: ")
    if bool(quantity) and quantity.isnumeric(): #проверка дали e число и не е празен
        quantity = float(quantity)
    else:
        print("Въведете правилна стойност!")
        continue

    a = "през седмицата"
    b = " през почивните дни"
    if days == "M" or days == "T" or days == "W" or days == "Th" or days == "F":
        days = a
    elif days == "S" or days == "Su":
        days = b
    else:
        print("грепен ден от седмицата: ")
        continue

    valid_fruit = True  # По подразбиране считаме, че плода е валиден
    price = 0

    if fruits == "banana" and days == a:
        price = 2.5
    elif fruits == "banana":
        price = 2.7
    elif fruits == "apple" and days == a:
        price = 1.2
    elif fruits == "apple":
        price = 1.25
    elif fruits == "orange" and days == a:
        price = 0.85
    elif fruits == "orange":
        price = 0.90
    elif fruits == "grapefruit" and days == a:
        price = 1.45
    elif fruits == "grapefruit":
        price = 1.60
    elif fruits == "pineapple" and days == a:
        price = 5.50
    elif fruits == "pineapple":
        price = 6.00
    elif fruits == "grapes" and days == a:
        price = 3.85
    elif fruits == "grapes":
        price = 4.20
    else:
        print("Невалиден плод")
        valid_fruit = False  # Маркираме, че плода е невалиден
        continue

    if valid_fruit:  # Проверка дали плодът е валиден
        total_price = quantity * price
        print(f"Цената за {quantity} {fruits}  {days} ще бъде {total_price:.2f}лв.")

    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break

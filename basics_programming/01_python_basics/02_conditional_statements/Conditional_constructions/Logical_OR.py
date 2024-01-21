while True:
    food = input('Име на продукт: ')
    if food == "banana" or food == "apple" or food == "kiwi" or food == "cherry" or food == "lemon" or food == "grapes":
        print("fruit")
    elif food == "tomato" or food == "cucumber" or food == "pepper" or food == "carrot":
        print("vegetable")
    else:
        print("unknown")

    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break

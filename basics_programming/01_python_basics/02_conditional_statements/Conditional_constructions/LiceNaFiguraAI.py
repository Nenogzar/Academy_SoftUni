import math

while True:
    figura = input("Choose: square, rectangle, circle or triangle: ")
    lice = 0  # Инициализиране на променливата
    if figura == "square":
        a = float(input("Въведете страната на квадрата: "))
        lice = a * a
    elif figura == "rectangle":
        a = float(input("Въведете първа страна на правоъгълника: "))
        b = float(input("Въведете втора страна на правоъгълника: "))
        lice = a * b
    elif figura == "circle":
        r = float(input("Въведете радиуса на окръжността: "))
        lice = math.pi * r * r
    elif figura == "triangle":
        a = float(input("Въведете страната на триъгълника: "))
        h = float(input("Въведете височината на триъгълника: "))
        lice = (a * h) / 2
    else:
        print("Невалиден вид на фигура")
        repeat = input("Искате ли да повторите (Y/N)? ")
        if repeat.upper() == "N":
            print("Благодаря!")
            break
    if lice != 0:
        print(f"Лицето на фигурата {figura} равно на {lice:.3f}")

    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break

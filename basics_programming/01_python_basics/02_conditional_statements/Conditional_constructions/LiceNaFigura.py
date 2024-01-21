import math

while True:
    figura = input("Choose: square, rectangle, circle or triangle: ")

    if figura == "square":
        a = float(input("Въведете страната на квадрата: "))
        print(f"Лицето на квадрат със дължина на страната {a} е равно на {a*a:.2f}")
    elif figura == "rectangle":
        a = float(input("Въведете първа страната на правоъгълника: "))
        b = float(input("Въведете втора страната на правоъгълника: "))
        print(f"Лицето на правоъгълник със страни {a} и {b} e {a*b:.2f}")
    elif figura == "circle":
        a = float(input("Въведете радиуса на окръжността: "))
        print(f"Лицето на окръжност със радиус {a} е равно на {math.pi*a*а:.2f}")
    else:
        a = float(input("Въведете страната на триъгълника: "))
        b = float(input("Въведете височината на триъгълника: "))
        print(f"Лицето на триъгълник със страна {a} и височина {b} е {(a*b)/2 :.2f}")

    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break

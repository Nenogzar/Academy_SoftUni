while True:
    a = int(input('Въведете стойност на a: '))
    b = int(input('Въведете стойност на b: '))

    if a > b:
        print(f"{a} > {b}")
    elif a < b:
        print(f"{a} < {b}")
    else:
        print(f"{a} = {b}")

    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break
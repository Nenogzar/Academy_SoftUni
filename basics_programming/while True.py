while True:

    n = int(input("Въведете стъпка"))
    for i in range (2, 20, n):
        print(i, end=" ")

    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break

while True:

    a=int(input())
    if 100 >= a >= -100 and a != 0:
        print ("YES")
    else:
        print("No")

    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break

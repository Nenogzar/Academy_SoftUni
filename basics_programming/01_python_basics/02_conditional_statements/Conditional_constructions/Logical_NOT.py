while True:
    a = int(input())
    valid = 100 <= a <= 200 or a == 0
    if not valid:
      print("Invalid")

    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break

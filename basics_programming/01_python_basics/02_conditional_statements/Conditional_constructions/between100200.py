while True:
    number = int(input("Въведете цяло число: "))

    if number < 100:
        print("Числото е под 100.")
    elif 100 <= number <= 200:
        print("Числото е между 100 и 200.")
    else:
        print("Числото е над 200.")

    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break
while True:

    password = input("Въведете парола: ")
    test = "s3cr3t!P@ssw0rd"

    if password == test:
        print("Welcome")
    else:
        print("Wrong password!")

    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break

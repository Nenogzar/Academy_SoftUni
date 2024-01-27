while True:

    my_lsit = [1, 5, 3, 9, 2]
    max_value = max(my_lsit)
    print(my_lsit)
    print(max_value)


    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break

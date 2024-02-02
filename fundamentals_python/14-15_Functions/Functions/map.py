while True:


    # value = input('Enter space separated value: ').split()
    # a, b, c = map(int, value)

    a, b, c = map(int, input('Enter space separated value: ').split())

    print(f"{a= }, {b= }, {c= }")

    repeat = input("repeat? (Y/N)? ")
    if repeat.upper() == "N":
        print("Bay!")
        break

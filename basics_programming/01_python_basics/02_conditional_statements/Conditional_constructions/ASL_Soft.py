while True:
    age = int(input('На колко години сте: '))
    sex = input('Какъв пол сте? man / woman')

    if sex == 'man':
        if age < 16:
            print('Master')
        else:
            print('Mr.')
    else:
        if age < 16:
            print('Miss')
        else:
            print('Ms.')


    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break

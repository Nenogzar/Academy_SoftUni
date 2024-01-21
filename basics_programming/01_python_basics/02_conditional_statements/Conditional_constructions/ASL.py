while True:
    age = int(input('На колко години сте: '))
    sex = input('Какъв пол сте? man / woman')

    title=''
    if sex == 'man' and age < 16:
        title="Master"
    elif sex == 'woman' and age < 16:
        title="Miss"
    elif sex == 'woman' and age >= 16:
        title="Ms."
    elif sex == 'man' and age >= 16:
        title='Mr.'
    else:
        print(" Грешен пол!")

    if sex != 0 and (0 < int(age) <= 100):
        print(title)
    elif (0 >= int(age)):
        print("Вие не сте роден!")
    else:
        print("Вие сте СТОЛЕТНИК")
        continue

    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break

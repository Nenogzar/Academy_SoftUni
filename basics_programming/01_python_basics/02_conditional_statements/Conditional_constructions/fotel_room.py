while True:

    months = input("Изберете месец: May, June, July, August, September или October: ")
    nights = int(input("колко нощувки: "))
    studio = 0.00
    apartament = 0.00

    if months == "May" or months == "October":

        if 1<= nights <7:
            studio = nights * 50
            print(studio)
        elif 7<= nights < 14:
            studio=(nights*50)*0.95
        elif nights >= 14:
            studio = (nights * 50) * 0.70
            print(studio)
        else:
            print("Изберете положителен брой на нощувки")

        if 1<= nights <=14:
            apartament = nights * 65
        elif nights > 14:
            apartament=(nights * 65)*0.9
        else:
            print("Изберете положителен брой на нощувки")

    elif months == "June" or months == "September":
        if 1<= nights <=14:
            studio= nights * 75.20
        elif nights >14:
            studio= (nights * 75.20)*0.80
        else:
            print("Изберете положителен брой на нощувки")

        if 1<= nights <=14:
            apartament = nights * 68.70
        elif nights > 14:
            apartament =(nights * 68.70)*0.90
        else:
            print("Изберете положителен брой на нощувки")

    elif months == "July" or months == "August":
        studio = nights * 76
        if 1<= nights <=14:
            apartament = nights * 77
        elif nights > 14:
            apartament = (nights * 77)*0.90
        else:
            print("Изберете положителен брой на нощувки")

    print(f"Apartment: {apartament:.2f} lv.")
    print(f"Studio: {studio:.2f} lv.")

    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break

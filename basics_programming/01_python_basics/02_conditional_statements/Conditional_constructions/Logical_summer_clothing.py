while True:
    temperature = int(input("колко градуса е: "))
    period = input(" каква част от деня е: Morning, Afternoon или Evening: ")

    Outfit = ""
    Shoes = ""

    if period ==  "Morning":
        if 10 <= temperature <= 18:
            Outfit = "Sweatshirt"
            Shoes = "Sneakers"
        elif 18 < temperature <= 24:
            Outfit = "Shirt"
            Shoes = "Moccasins"
        elif temperature >=25:
            Outfit = "T-Shirt"
            Shoes = "Sandals"
    elif period ==  "Afternoon":
        if 10 <= temperature <= 18:
            Outfit = "Shirt"
            Shoes = "Moccasins"
        elif 18 < temperature <= 24:
            Outfit = "T-Shirt"
            Shoes = "Sandals"
        elif temperature >=25:
            Outfit = "Swim Suit"
            Shoes = "Barefoot"
    elif period ==  "Evening":
        if 10 <= temperature <= 18:
            Outfit = "Shirt"
            Shoes = "Moccasins"
        elif 18 < temperature <= 24:
            Outfit = "Shirt"
            Shoes = "Moccasins"
        elif temperature >=25:
            Outfit = "Shirt"
            Shoes = "Moccasins"
    else:
        print("Неправелен период от деня:")

    print(f"It's {temperature} degrees, get your {Outfit} and {Shoes}.")

    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break

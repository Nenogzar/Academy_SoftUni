while True:

    budget = float(input("С какъв бюджет разполагате? "))
    season = input("през кой сезон искате да наемет кора: Spring, Summer, Autumn или Winter")
    fishman = int(input("Колко рибари сте? "))
    Spring = 3000
    Summer = 4200
    Autumn = 4200
    Winter = 2600
    price = 0.00
    discount = 0.00

    #Условия за отстъпка
    if 0 < fishman <= 6:
        discount = 0.90
    elif 7 <= fishman <= 11:
        discount = 0.85
    elif fishman >= 12:
        discount = 0.75
    else:
        print("Въведете положителна стойнот на броя рибари: ")
        continue
    print(discount)
   # условия за сезона
    if season == "Spring":
        price = Spring * discount
    elif season == "Summer":
        price = Summer * discount
    elif season == "Autumn":
        price = Autumn * discount
    elif season == "Winter":
        price = Winter * discount
    else:
        print("ВЪведете правилен сезон:")
        continue
    print(price)

    if fishman % 2 == 0 and season != "Automn":
        price = price * 1.05
    else:
        price = price

    if budget >= price:
        print(f"Yes! You have {(budget-price):.2f} leva left.")
    else:
        print(f"Not enough money! You need {((budget-price)*-1):.2f} leva.")



    #повторение на програмата
    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break

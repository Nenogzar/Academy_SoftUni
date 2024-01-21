while True:

    product = input("Изберете от тези продукти:coffee, water, beer, sweeps, peanuts: ")
    city = input("Въведете град (Sofia, Plovdiv или Varna): ")
    quantity = float(input("Въведете количество: "))

    price = 0

    if city == "Sofia":
        if product == "coffee":
            price = 0.50
        elif product == "water":
            price = 0.80
        elif product == "beer":
            price = 1.20
        elif product == "sweeps":
            price = 1.45
        elif product == "peanuts":
            price = 1.60
    elif city == "Plovdiv":
        if product == "coffee":
            price = 0.40
        elif product == "water":
            price = 0.70
        elif product == "beer":
            price = 1.15
        elif product == "sweeps":
            price = 1.30
        elif product == "peanuts":
            price = 1.50
    elif city == "Varna":
        if product == "coffee":
            price = 0.45
        elif product == "water":
            price = 0.70
        elif product == "beer":
            price = 1.10
        elif product == "sweeps":
            price = 1.35
        elif product == "peanuts":
            price = 1.55

    total_price = quantity * price
    print(f"Общата цена за {quantity} броя {product} в град {city} е {total_price:.2f} лв.")

    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break

while True:
    product = input("Въведете продукт (coffee, water, beer, sweets или peanuts): ")
    town = input("Въведете град (Sofia, Plovdiv или Varna): ")
    quantity = float(input("Въведете количество: "))
    price = float()

    if town == "Sofia":
        if product == "coffee":
            price = 0.50 * quantity
        elif product == "water":
            price = 0.80 * quantity
        elif product == "beer":
            price = 1.2 * quantity
        elif product == "sweets":
            price = 1.45 * quantity
        elif product == "peanuts":
            price = 1.60 + quantity
    elif town == "Plovdiv":
        if product == "coffee":
            price = 0.40 * quantity
        elif product == "water":
            price = 0.70 * quantity
        elif product == "beer":
            price = 1.15 * quantity
        elif product == "sweets":
            price = 1.30 * quantity
        elif product == "peanuts":
            price = 1.50 + quantity
    elif town == "Varna":
        if product == "coffee":
            price = 0.45 * quantity
        elif product == "water":
            price = 0.70 * quantity
        elif product == "beer":
            price = 1.10 * quantity
        elif product == "sweets":
            price = 1.35 * quantity
        elif product == "peanuts":
            price = 1.55 + quantity

        print(f"Общата цена за {quantity} броя {product} в град {town} е {price:.2f} лв.")
    repeat = input("Y/N")
    if repeat.upper() == "N":
        print("10x")
        break
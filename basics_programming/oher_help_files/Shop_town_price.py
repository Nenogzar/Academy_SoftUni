towns = ('Sofia', 'Plovdiv', 'Varna')
prices ={
    'coffee': (0.50, 0.40, 0.45),
    'water': (0.80, 0.70, 0.70),
    'beer': (1.20, 1.15, 1.10),
    'wseets': (1.45, 1.30, 1.35),
    'peanuts': (1.60, 1.50, 1.55),
}
while True:
    town = input("Въведете град (Sofia, Plovdiv или Varna): ")
    product = input("Въведете продукт (coffee, water, beer, sweets или peanuts): ")
    quantity = float(input("Въведете количество: "))

    # Изчисляване на цената
    town_index = towns.index(town)
    product_price = prices[product][town_index]
    total_price = product_price * quantity

    # Изход
    print(f"Общата цена за {quantity} броя {product} в град {town} е {total_price:.2f} лв.")
    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break
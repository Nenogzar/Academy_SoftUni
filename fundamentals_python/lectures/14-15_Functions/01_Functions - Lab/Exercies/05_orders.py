def order(products, quantity_products):
    price = 0.00
    if products == "coffee":
        price = 1.50
    elif products == "coke":
        price = 1.40
    elif products == "water":
        price = 1.00
    elif products == "snacks":
        price = 2.00
    else:
        print("Wrong order product")

    total_order = price * quantity_products
    print(f"{total_order:.2f}")

products = input()
quantity_products = int(input())

order(products, quantity_products)

#  whit dictionary

product_prices = {
    "coffee": 1.50,
    "coke": 1.40,
    "water": 1.00,
    "snacks": 2.00
}


def order(products, quantity_products):
    price = product_prices.get(products)

    if price is None:
        print("Wrong order product")
        return

    total_order = price * quantity_products
    print(total_order)


products_input = input()
quantity_input = int(input())

order(products_input, quantity_input)

#



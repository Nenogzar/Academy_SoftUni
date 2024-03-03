dict_products = {}

input_info = input()

while input_info != "buy":
    input_info = input_info.split(" ")
    names, prices, quantities = input_info[0], float(input_info[1]), int(input_info[2])

    if names in dict_products:
        existing_prices, existing_quantities = dict_products[names]
        dict_products[names] = (prices, existing_quantities + quantities)
    else:
        dict_products[names] = (prices, quantities)

    input_info = input()

for names, (prices, quantities) in dict_products.items():
    total_price = prices * quantities
    print(f"{names} -> {total_price:.2f}")

####################
""" """

def orders_func(dict_products, input_info):
    names = input_info[0]
    price = float(input_info[1])
    quantity = int(input_info[2])

    if names in dict_products:
        dict_products[names] = [price, (quantity + dict_products[names][1])]
    else:
        dict_products[names] = [price, quantity]

    return dict_products

def orders():

    dict_products = {}
    input_info = input()
    while  input_info != 'buy':

        input_info = input_info.split(' ')
        dict_products = orders_func(dict_products, input_info)
        input_info = input()

    for k in dict_products:
        total_sum = dict_products[k][0] * dict_products[k][1]
        print(f'{k} -> {total_sum:.2f}')

orders()

####################
""" """

dict_products = {}

input_info = input()
while input_info != "buy":
    names, price, quantity = [float(item) if item[-1].isdigit() else item for item in input_info.split()]

    dict_products[names] = dict_products.get(names, {"price": 0, "quantity": 0})
    dict_products[names]['quantity'] += quantity
    dict_products[names]['price'] = price

    input_info = input()

for key, value in dict_products.items():
    print(f"{key} -> {value['price'] * value['quantity']:.2f}")

####################
""" """
dict_products = {}

input_info = input()
while input_info != "buy":
    names, price, quantity = [item for item in input_info.split()]

    dict_products[names] = dict_products.get(names, {"price": 0, "quantity": 0})
    dict_products[names]['price'] = float(price)
    dict_products[names]['quantity'] += int(quantity)

    input_info = input()

for key, value in dict_products.items():
    print(f"{key} -> {value['price'] * value['quantity']:.2f}")
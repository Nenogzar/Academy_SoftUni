def change_price(br, type):
    prices = {
        '90X130': {'count': [30, 60], 'discount': [0.95, 0.92], 'price_per_unit': 110},
        '100X150': {'count': [40, 80], 'discount': [0.94, 0.90], 'price_per_unit': 140},
        '130X180': {'count': [20, 50], 'discount': [0.93, 0.88], 'price_per_unit': 190},
        '200X300': {'count': [25, 50], 'discount': [0.91, 0.86], 'price_per_unit': 250}
    }

    if type in prices:
        price = prices[type]['price_per_unit'] * br
        count_range = prices[type]['count']
        discount_rates = prices[type]['discount']

        if count_range[0] < br < count_range[1]:
            price *= discount_rates[0]
        elif br > count_range[1]:
            price *= discount_rates[1]

        return price


br_joinery, type_joinery, type_delivery = int(input()), input(), input()
if br_joinery < 10:
    print("Invalid order")
else:
    price = change_price(br_joinery, type_joinery)

    if price is not None:
        if type_delivery == "With delivery":
            price += 60

        if br_joinery > 99:
            price *= 0.96
        print(f"{price:.2f} BGN")


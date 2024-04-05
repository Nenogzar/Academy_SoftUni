# def change_price(br, type):
#     if type == '90X130':
#         price = 110 * br
#         if 30 <= br < 60:
#             price *= 0.95
#         elif br >= 60:
#             price *= 0.92
#     elif type == '100X150':
#         price = 140 * br
#         if 40 <= br < 80:
#             price *= 0.94
#         elif br >= 80:
#             price *= 0.90
#     elif type == '130X180':
#         price = 190 * br
#         if 20 <= br < 50:
#             price *= 0.93
#         elif br >= 50:
#             price *= 0.88
#     elif type == '200X300':
#         price = 250 * br
#         if 25 <= br < 50:
#             price *= 0.91
#         elif br >= 50:
#             price *= 0.86
#     return price
#
#
# br_dograma, type_dograma, type_delivery = int(input()), input(), input()
# if br_dograma <= 10:
#     print("Invalid order")
# else:
#     price = change_price(br_dograma, type_dograma)
#
#     if type_delivery == "With delivery":
#         price += 60
#         if br_dograma >= 99:
#             price *= 0.96
#             print(f"{price:.2f} BGN")
#     else:
#         print(f"{price:.2f} BGN")

def change_price(br, type):
    prices = {
        '90X130': {'count': [30, 60], 'discount': [0.95, 0.92], 'price_per_unit': 110},
        '100X150': {'count': [40, 80], 'discount': [0.94, 0.90], 'price_per_unit': 140},
        '130X180': {'count': [20, 50], 'discount': [0.93, 0.88], 'price_per_unit': 190},
        '200X300': {'count': [20, 50], 'discount': [0.91, 0.86], 'price_per_unit': 250}
    }

    if type in prices:
        price = prices[type]['price_per_unit'] * br
        count_range = prices[type]['count']
        discount_rates = prices[type]['discount']

        if count_range[0] <= br < count_range[1]:
            price *= discount_rates[0]
        elif br >= count_range[1]:
            price *= discount_rates[1]

        return price


br_joinery, type_joinery, type_delivery = int(input()), input(), input()
if br_joinery <= 10:
    print("Invalid order")
else:
    price = change_price(br_joinery, type_joinery)

    if price is not None:
        if type_delivery == "With delivery":
            price += 60
            if br_joinery >= 99:
                price *= 0.96
        print(f"{price:.2f} BGN")
    else:
        print("Invalid type")

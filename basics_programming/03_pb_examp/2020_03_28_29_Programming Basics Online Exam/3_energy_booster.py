fruit = input()  # "Watermelon", "Mango", "Pineapple" or "Raspberry"
sets = input()   # "small" or "big"
sets_number = int(input())
set_type = 0
discount = 1
price = 0.00

if sets == "small":
    set_type = 2
elif sets == "big":
    set_type = 5

if fruit == "Watermelon":
    if sets == "small":
        price = 56
    elif sets == "big":
        price = 28.70
elif fruit == "Mango":
    if sets == "small":
        price = 36.66
    elif sets == "big":
        price = 19.60
elif fruit == "Pineapple":
    if sets == "small":
        price = 42.10
    elif sets == "big":
        price = 24.80
elif fruit == "Raspberry":
    if sets == "small":
        price = 20
    elif sets == "big":
        price = 15.20

set_price = set_type * price
total_set_price = set_price * sets_number

if 400 <= total_set_price <= 1000:
    total_set_price *= 0.85
elif total_set_price > 1000:
    total_set_price *= 0.5

print(f"{total_set_price:.2f} lv.")

# frud = input()
# set_available = input()
# order_set = int(input())
#
#
# watermalone_small = 56
# watermalone_big = 28.70
# mango_small = 36.66
# mango_big = 19.60
# pinapple_small = 42.10
# pinapple_big = 24.80
# malina_small = 20
# malina_big = 15.20
# fourhundred_off = 0.15
# onethousand = 0.50
#
# if "Watermelon" in frud:
#     if "big" in set_available:
#         total = 5 * watermalone_big
#         set_price = order_set * total
#         if 400 <= set_price <= 1000:
#             set_price = set_price - set_price * fourhundred_off
#         elif set_price > 1000:
#             set_price = set_price - set_price * onethousand
#     elif "small" in set_available:
#         total = 2 * watermalone_small
#         set_price = order_set * total
#         if 400 <= set_price <= 1000:
#             set_price = set_price - set_price * fourhundred_off
#         elif set_price > 1000:
#             set_price = set_price - set_price * onethousand
# elif "Mango" in frud:
#     if "big" in set_available:
#         total = 5 * mango_big
#         set_price = order_set * total
#         if 400 <= set_price <= 1000:
#             set_price = set_price - set_price * fourhundred_off
#         elif set_price > 1000:
#             set_price = set_price - set_price * onethousand
#     elif "small" in set_available:
#         total = 2 * mango_small
#         set_price = order_set * total
#         if 400 <= set_price <= 1000:
#             set_price = set_price - set_price * fourhundred_off
#         elif set_price > 1000:
#             set_price = set_price - set_price * onethousand
# elif "Pineapple" in frud:
#     if "big" in set_available:
#         total = 5 * pinapple_big
#         set_price = order_set * total
#         if 400 <= set_price <= 1000:
#             set_price = set_price - set_price * fourhundred_off
#         elif set_price > 1000:
#             set_price = set_price - set_price * onethousand
#     elif "small" in set_available:
#         total = 2 * pinapple_small
#         set_price = order_set * total
#         if 400 <= set_price <= 1000:
#             set_price = set_price - set_price * fourhundred_off
#         elif set_price > 1000:
#             set_price = set_price - set_price * onethousand
# elif "Raspberry" in frud:
#     if "big" in set_available:
#         total = 5 * malina_big
#         set_price = order_set * total
#         if 400 <= set_price <= 1000:
#             set_price = set_price - set_price * fourhundred_off
#         elif set_price > 1000:
#             set_price = set_price - set_price * onethousand
#     elif "small" in set_available:
#         total = 2 * malina_small
#         set_price = order_set * total
#         if 400 <= set_price <= 1000:
#             set_price = set_price - set_price * fourhundred_off
#         elif set_price > 1000:
#             set_price = set_price - set_price * onethousand
#
# print(f"{set_price:.2f} lv.")


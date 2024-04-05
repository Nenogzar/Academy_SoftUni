# fruit = input()  # "Watermelon", "Mango", "Pineapple" or "Raspberry"
# sets = input()   # "small" or "big"
# sets_number = int(input())
# set_type = 0
# discount = 1
# price = 0.00
#
# if sets == "small":
#     set_type = 2
# elif sets == "big":
#     set_type = 5
#
# if fruit == "Watermelon":
#     if sets == "small":
#         price = 56
#     elif sets == "big":
#         price = 28.70
# elif fruit == "Mango":
#     if sets == "small":
#         price = 36.66
#     elif sets == "big":
#         price = 19.60
# elif fruit == "Pineapple":
#     if sets == "small":
#         price = 42.10
#     elif sets == "big":
#         price = 24.80
# elif fruit == "Raspberry":
#     if sets == "small":
#         price = 20
#     elif sets == "big":
#         price = 15.20
#
# set_price = set_type * price
# total_set_price = set_price * sets_number
#
# if 400 <= total_set_price <= 1000:
#     total_set_price *= 0.85
# elif total_set_price > 1000:
#     total_set_price *= 0.5
#
# print(f"{total_set_price:.2f} lv.")



fruit = input()  # "Watermelon", "Mango", "Pineapple" or "Raspberry"
sets = input()  # "small" or "big"
sets_number = int(input())

prices = {
    "Watermelon": {"small": 56, "big": 28.70},
    "Mango": {"small": 36.66, "big": 19.60},
    "Pineapple": {"small": 42.10, "big": 24.80},
    "Raspberry": {"small": 20, "big": 15.20}
}

# Отстъпки
discounts = {
    "400": 0.15,
    "1000": 0.50
}

if fruit in prices and sets in prices[fruit]:
    price = prices[fruit][sets]
    set_type = 2 if sets == "small" else 5
    set_price = set_type * price
    total_set_price = set_price * sets_number

    if 400 <= total_set_price <= 1000:
        total_set_price *= (1 - discounts["400"])
    elif total_set_price > 1000:
        total_set_price *= (1 - discounts["1000"])

    print(f"{total_set_price:.2f} lv.")
else:
    print("Invalid fruit or set size.")


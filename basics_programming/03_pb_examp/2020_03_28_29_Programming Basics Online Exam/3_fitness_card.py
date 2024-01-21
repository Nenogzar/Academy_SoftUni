money_on_hand = float(input())
gender = input()    # 'm' or 'f'
age = int(input())
sport = input()     # "Gym"	"Boxing"	"Yoga"	"Zumba"	"Dances" "Pilates"
price = 0
if gender == 'm':
    if sport == "Gym":
        price = 42
    elif sport == "Boxing":
        price = 41
    elif sport == "Yoga":
        price = 45
    elif sport == "Zumba":
        price = 34
    elif sport == "Dances":
        price = 51
    elif sport == "Pilates":
        price = 39
elif gender == 'f':
    if sport == "Gym":
        price = 35
    elif sport == "Boxing" or sport == "Pilates":
        price = 37
    elif sport == "Yoga":
        price = 42
    elif sport == "Zumba":
        price = 31
    elif sport == "Dances":
        price = 53

if age < 19:
    price *= 0.8

difference = abs(money_on_hand - price)

if price <= money_on_hand:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${difference:.2f} more.")


# availabe_money = float(input())
# sex = input()
# age = int(input())
# sport = input()
#
# male = {
#     "Gym": 42,
#     "Boxing": 41,
#     "Yoga": 45,
#     "Zumba": 34,
#     "Dances": 51,
#     "Pilates": 39
# }
#
# female = {
#     "Gym": 35,
#     "Boxing": 37,
#     "Yoga": 42,
#     "Zumba": 31,
#     "Dances": 53,
#     "Pilates": 37
# }
#
# if age <= 19:
#     if "f" in sex:
#         card_off = female[sport] - female[sport] * 0.20
#
#         if availabe_money >= card_off:
#             card_result = f"You purchased a 1 month pass for {sport}."
#
#         else:
#             money_needed = card_off - availabe_money
#             card_result = f"You don't have enough money! You need ${money_needed:.2f} more."
#
#     if "m" in sex:
#         card_off = male[sport] - male[sport] * 0.20
#
#         if availabe_money >= card_off:
#             card_result = f"You purchased a 1 month pass for {sport}."
#
#         else:
#             money_needed = card_off - availabe_money
#             card_result = f"You don't have enough money! You need ${money_needed:.2f} more."
#
# elif "f" in sex:
#
#     if availabe_money >= female[sport]:
#         card_result = f"You purchased a 1 month pass for {sport}."
#
#     else:
#         money_needed = female[sport] - availabe_money
#         card_result = f"You don't have enough money! You need ${money_needed:.2f} more."
#
# elif "m" in sex:
#
#     if availabe_money >= male[sport]:
#
#         card_result = f"You purchased a 1 month pass for {sport}."
#
#     else:
#         money_needed = male[sport] - availabe_money
#         card_result = f"You don't have enough money! You need ${money_needed:.2f} more."
#
# print(card_result)

# picture_whit_trophy = 40 # L
# discounts:
# > 4000 L 25% and picture_whit_trophy = 0 => if picture_whit_trophy == "N"
# > 2500 L 10 %
championship_stage = input()
ticket_type = input()
ticket_numbner = int(input())
picture_whit_trophy = input().upper()  # Y or N
price = 0.00
picture_with_trophy_price = 40
discount = 1

if ticket_type == "Standard":
    if championship_stage == "Quarter final":
        price += 55.50
    elif championship_stage == "Semi final":
        price += 75.88
    elif championship_stage == "Final":
        price += 110.10

elif ticket_type == "Premium":
    if championship_stage == "Quarter final":
        price += 105.20
    elif championship_stage == "Semi final":
        price += 125.22
    elif championship_stage == "Final":
        price += 160.66
elif ticket_type == "VIP":
    if championship_stage == "Quarter final":
        price += 118.90
    elif championship_stage == "Semi final":
        price += 300.40
    elif championship_stage == "Final":
        price += 400

# total_price = ticket_numbner * price
# print("total_price =>", total_price)
total_sum = ticket_numbner * price

if total_sum > 4000:
    total_sum *= 0.75
    picture_with_trophy_price = 0
elif total_sum > 2500:
    total_sum *= 0.90

if picture_whit_trophy == "Y":
    total_sum += ticket_numbner * picture_with_trophy_price

print(f"{total_sum:.2f}")

############################################################


competitions_type = input()
ticket_type = input()
number_tickets = int(input())
picture_with_trophy = input()
picture_with_trophy_price = 40

tournament_info = {
    "Quarter final": {"Standard": 55.50, "Premium": 105.20, "VIP": 118.90},
    "Semi final": {"Standard": 75.88, "Premium": 125.22, "VIP": 300.40},
    "Final": {"Standard": 110.10, "Premium": 160.66, "VIP": 400},
}

ticket_price = tournament_info[competitions_type][ticket_type]
total_sum = ticket_price * number_tickets

if total_sum > 4000:
    total_sum *= 0.75
    picture_with_trophy_price = 0
elif total_sum > 2500 and picture_with_trophy == "Y":
    total_sum *= 0.90

if picture_with_trophy == "Y":
    total_sum += number_tickets * picture_with_trophy_price

print(f"{total_sum:.2f}")

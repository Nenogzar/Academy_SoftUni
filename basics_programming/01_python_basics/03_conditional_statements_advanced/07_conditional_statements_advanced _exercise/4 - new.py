budget = int(input())
season = input()
fishermen_count = int(input())

spring_price = 3000
summer_autumn_price = 4200
winter_price = 2600

# Discounts
discount_6_or_less = 0.10
discount_7_to_11 = 0.15
discount_12_or_more = 0.25
fishermen_discount = 0.05

# def boat_price
if season == "Spring":
    boat_price = spring_price
elif season == "Summer" or season == "Autumn":
    boat_price = summer_autumn_price
else:
    boat_price = winter_price

# def group_discount
if 0 < fishermen_count <= 6:
    group_discount = discount_6_or_less
elif 7 <= fishermen_count <= 11:
    group_discount = discount_7_to_11
else:
    group_discount = discount_12_or_more

# def total_discount
if fishermen_count % 2 == 0 and season != "Autumn":
    total_discount = group_discount + fishermen_discount
else:
    total_discount = group_discount

# final_price
final_price = boat_price * (1 - total_discount)

# chek
if budget >= final_price:
    left_money = budget - final_price
    print(f"Yes! You have {left_money:.2f} leva left.")
else:
    needed_money = final_price - budget
    print(f"Not enough money! You need {needed_money:.2f} leva.")

# Входни данни
budget = int(input())
season = input().lower()
fishermen_count = int(input())

# Цени за наем на кораба според сезона
spring_price = 3000
summer_autumn_price = 4200
winter_price = 2600
boat_price = 0
# Изчисление на цената на наем на кораба според сезона
if season == "spring":
    boat_price = spring_price
elif season == "summer" or season == "autumn":
    boat_price = summer_autumn_price
elif boat_price == "winter":
    boat_price = winter_price
else:
    boat_price = boat_price
print(boat_price)
# Изчисление на общата отстъпка според броя на групата и рибарите
total_discount = 0

if 0 < fishermen_count <= 6:
    total_discount += 0.10
elif 7 <= fishermen_count <= 11:
    total_discount += 0.15
else:
    total_discount += 0.25

if fishermen_count % 2 == 0 and season != "Autumn":
    total_discount += 0.05

# Изчисление на крайната цена
final_price = boat_price * (1 - total_discount)

# Проверка дали бюджетът е достатъчен
if budget >= final_price:
    left_money = budget - final_price
    print(f"Yes! You have {left_money:.2f} leva left.")
else:
    needed_money = final_price - budget
    print(f"Not enough money! You need {needed_money:.2f} leva.")

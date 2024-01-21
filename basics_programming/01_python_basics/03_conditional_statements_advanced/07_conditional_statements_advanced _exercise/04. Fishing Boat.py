# Входни данни
budget = float(input())
season = input().lower()
fishermen = int(input())

# Цени за наем на кораба
spring_price = 3000
summer_price = 4200
autumn_price = 4200
winter_price = 2600

# Изчисление на цената на кораба според сезона
if season == "spring":
    price = spring_price
elif season == "summer" or season == "autumn":
    price = summer_price
elif season == "winter":
    price = winter_price
else:
    print("Invalid season")
    exit(1)

# Изчисление на отстъпката според броя на рибарите
if fishermen >= 12:
    price *= 0.75  # 25% отстъпка
elif 7 <= fishermen <= 11:
    price *= 0.85  # 15% отстъпка
elif fishermen <= 6:
    price *= 0.90  # 10% отстъпка
#print("price", price )
# Допълнителна отстъпка за четен брой рибари
if fishermen % 2 == 0 and season != "autumn":
    price *= 0.95  # 5% отстъпка

# Изчисление на необходимите средства
done_money = abs(budget - price)


# Проверка дали бюджетът е достатъчен и отпечатване на резултата
if budget >= price:
    print(f"Yes! You have {done_money:.2f} leva left.")
else:
    print(f"Not enough money! You need {done_money:.2f} leva.")
# Въвеждане на вид цветя, брой цветя и бюджет от потребителя
flower_type = input()
flower_count = int(input())
budget = int(input())

# Инициализация на цените на цветята
flower_prices = {
    "Roses": 5.00,
    "Dahlias": 3.80,
    "Tulips": 2.80,
    "Narcissus": 3.00,
    "Gladiolus": 2.50
}

# Инициализация на отстъпките и наценките
discounts = {
    "Roses": 0.10,
    "Dahlias": 0.15,
    "Tulips": 0.15,
}

markup = {
    "Narcissus": 0.15,
    "Gladiolus": 0.20
}

# Изчисляване на крайната цена
price_per_flower = flower_prices[flower_type]

if flower_type in discounts and flower_count > 80:
    price_per_flower -= price_per_flower * discounts[flower_type]

if flower_type in markup and flower_count < 120:
    price_per_flower += price_per_flower * markup[flower_type]

total_price = flower_count * price_per_flower

# Проверка дали бюджетът е достатъчен
if budget >= total_price:
    remaining_budget = budget - total_price
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {remaining_budget:.2f} leva left.")
else:
    needed_budget = total_price - budget
    print(f"Not enough money, you need {needed_budget:.2f} leva more.")

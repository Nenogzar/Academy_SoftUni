flower_type = input()
flower_count = int(input())
budget = int(input())

# Изчисляване на крайната цена
if flower_type == "Roses":
    price_per_flower = 5.00
    if flower_count > 80:
        price_per_flower *= 0.90  # 10% отстъпка
elif flower_type == "Dahlias":
    price_per_flower = 3.80
    if flower_count > 90:
        price_per_flower *= 0.85  # 15% отстъпка
elif flower_type == "Tulips":
    price_per_flower = 2.80
    if flower_count > 80:
        price_per_flower *= 0.85  # 15% отстъпка
elif flower_type == "Narcissus":
    price_per_flower = 3.00
    if flower_count < 120:
        price_per_flower *= 1.15  # 15% наценка
elif flower_type == "Gladiolus":
    price_per_flower = 2.50
    if flower_count < 80:
        price_per_flower *= 1.20  # 20% наценка

total_price = flower_count * price_per_flower

# Проверка дали бюджетът е достатъчен
if budget >= total_price:
    remaining_budget = budget - total_price
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {remaining_budget:.2f} leva left.")
else:
    needed_budget = total_price - budget
    print(f"Not enough money, you need {needed_budget:.2f} leva more.")
fruit = input().lower()
day = input().capitalize()
quantity = float(input())

fruit_prices_weekday = {
    "banana": 2.5, "apple": 1.2, "orange": 0.85,
    "grapefruit": 1.45, "kiwi": 2.7, "pineapple": 5.5, "grapes": 3.85
}

fruit_prices_weekend = {
    "banana": 2.7, "apple": 1.25, "orange": 0.9,
    "grapefruit": 1.6, "kiwi": 3, "pineapple": 5.6, "grapes": 4.2
}

if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] and fruit in fruit_prices_weekday:
    # Изчисляване на цената според деня от седмицата и количеството
    if day in ["Saturday", "Sunday"]:
        price = fruit_prices_weekend[fruit] * quantity
    else:
        price = fruit_prices_weekday[fruit] * quantity

    # Отпечатване на цената с две цифри след десетичната точка
    print(f"{price:.2f}")
else:
    print("error")

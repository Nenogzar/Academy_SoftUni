while True:

    # Цени за нощувки
    room_prices = {
        "room for one person": 18.00,
        "apartment": 25.00,
        "president apartment": 35.00
    }

    # Намаления
    discounts = {
        "room for one person": [0, 0, 0],  # Няма намаление за този тип стая
        "apartment": [0.30, 0.35, 0.50],  # Намаление според дни на престой
        "president apartment": [0.10, 0.15, 0.20]  # Намаление според дни на престой
    }

    # Оценки
    rating_modifiers = {
        "positive": 1.25,  # 25% надценка
        "negative": 0.90  # 10% намаление
    }

    # Входни данни
    try:
        days = int(input())
        room_type = input()
        rating = input()

        if days <= 0:
            raise ValueError("Дни за престой трябва да бъде положително число.")
        if room_type not in room_prices:
            raise ValueError("Невалиден тип помещение.")
        if rating not in rating_modifiers:
            raise ValueError("Невалидна оценка.")
    except ValueError as error:
        print(f"Грешка: {error}")
    else:
        # Изчисления
        price_per_night = room_prices[room_type]
        total_nights = days - 1  # Нощувки са дните минус 1

        if total_nights < 10:
            discount = discounts[room_type][0]
        elif 10 <= total_nights <= 15:
            discount = discounts[room_type][1]
        else:
            discount = discounts[room_type][2]

        total_price = total_nights * price_per_night * (1 - discount)  # Намаление

        if rating == "positive":
            total_price *= rating_modifiers["positive"]  # 25% надценка при позитивна оценка
        elif rating == "negative":
            total_price *= rating_modifiers["negative"]  # 10% намаление при негативна оценка

        print(f"{total_price:.2f}")  # Отпечатване на цената до 2 знака след десетичната запетая

    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break

projection_type = input().capitalize()
rows = int(input())
columns = int(input())

ticket_prices = {
    "Premiere": 12.00,
    "Normal": 7.50,
    "Discount": 5.00
}

if projection_type in ticket_prices:
    # Изчисляване на общите приходи при пълна зала
    total_income = rows * columns * ticket_prices[projection_type]

    # Отпечатване на общите приходи, форматирани до 2 знака след десетичната точка
    print(f"{total_income:.2f} leva")
else:
    print("error")
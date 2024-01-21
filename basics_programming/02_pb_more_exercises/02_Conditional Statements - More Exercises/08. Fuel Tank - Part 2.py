# Създаване на речник с цени на горивата и отстъпки
fuel_prices = {
    "Gasoline": {"price": 2.22, "discount": 0.18},
    "Diesel": {"price": 2.33, "discount": 0.12},
    "Gas": {"price": 0.93, "discount": 0.08}
}

# Входни данни
type_fuel = input()  # "Gas", "Gasoline" или "Diesel"
quantity = float(input())  # Количество гориво – реално число в интервала [1.00 … 50.00]
club_card = input()  # клубна карта – текст с възможности: "Yes" или "No"

# Проверка за валидност на типа на горивото
if type_fuel not in fuel_prices:
    print("Invalid fuel!")
else:
    price = fuel_prices[type_fuel]["price"]
    discount = fuel_prices[type_fuel]["discount"]

    # Изчисление на цената
    if quantity <= 20:
        discount_percentage = 0
    elif 20 < quantity <= 25:
        discount_percentage = 0.08
    else:
        discount_percentage = 0.10

    if club_card == 'Yes':
        final_price = (price - discount) * quantity * (1 - discount_percentage)
    else:
        final_price = price * quantity * (1 - discount_percentage)

    if final_price >= 0:
        print(f"{final_price:.2f} lv.")
    else:
        print("error")

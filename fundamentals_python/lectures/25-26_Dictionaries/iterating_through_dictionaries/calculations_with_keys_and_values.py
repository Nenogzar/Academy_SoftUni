incomes = {"apple": 5600.00, "orange": 3500.00, "banana": 5000.00}
total_income = 0.00

for income in incomes.values():
    total_income += income

print(total_income)  # 14100.0

###################################################################

order = {"coffe": {
    "price": 1.50,
    "quantity": 2},
    "jus": {
        "price": 2.50,
        "quantity": 3}}

for key, value in order.items():
    price = float(value["price"])
    quantity = int(value["quantity"])
    total_sum = quantity * price

    print(f"{key}: {total_sum:.2f}")

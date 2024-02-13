total_sum = 0
data = input()
customers = list()
discount = 0.1

while data != "special" and data != "regular":
    price = float(data)
    if price < 0:
        print("Invalid price!")
        data = input()
        continue
    else:
        customers.append(data)
        data = input()

if not customers:
    print("Invalid order!")
else:
    total_sum = sum(float(n) for n in customers)
    taxes = total_sum * 0.2
    total_price = total_sum + taxes

    if data == "special":
        total_price = total_price - (total_price * discount)

    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_sum:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")
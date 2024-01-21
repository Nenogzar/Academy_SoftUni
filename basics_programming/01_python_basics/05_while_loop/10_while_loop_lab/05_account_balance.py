total_amount = 0.0

while True:
    command = input()

    if command == "NoMoreMoney":
        break

    amount = float(command)

    if amount < 0:
        print("Invalid operation!")
        break

    print(f"Increase: {amount:.2f}")
    total_amount += amount

print(f"Total: {total_amount:.2f}")

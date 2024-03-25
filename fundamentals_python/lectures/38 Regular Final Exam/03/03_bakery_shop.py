stock = {}
sold_count = 0

command_line = input()
while command_line != "Complete":
    info = command_line.split(" ")
    command, quantity, food = info[0], int(info[1]), info[2]

    if quantity <= 0:
        continue
    else:
        if command == "Receive":
            if food in stock:
                stock[food] += quantity
            else:
                stock[food] = quantity
        elif command == "Sell":
            if food not in stock:
                print(f"You do not have any {food}.")
            elif stock[food] < quantity:
                sold_quantity = stock[food]
                print(f"There aren't enough {food}. You sold the last {sold_quantity} of them.")
                sold_count += sold_quantity
                del stock[food]
            else:
                stock[food] -= quantity
                sold_count += quantity
                print(f"You sold {quantity} {food}.")
                if stock[food] == 0:
                    del stock[food]

    command_line = input()

for food, quantity in stock.items():
    print(f"{food}: {quantity}")
print(f"All sold: {sold_count} goods")

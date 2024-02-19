def profit(earned, expense):
    return earned - expense


def special_event(expense):
    return expense * 1.5


def loss(expense):
    return expense * 0.9


city_num = int(input())
report = {}
total_profit = 0

for position in range(1, city_num + 1):
    city = input()
    owner_earned = float(input())
    owner_expense = float(input())

    if position % 3 == 0:
        current_profit = profit(owner_earned, special_event(owner_expense))
    elif position % 5 == 0:
        current_profit = profit(owner_earned, loss(owner_expense))
    else:
        current_profit = profit(owner_earned, owner_expense)

    total_profit += current_profit
    report[city] = {'earned': owner_earned, 'expense': owner_expense, 'profit': current_profit}

    # Print individual city message
    print(f"In {city} Burger Bus earned {current_profit:.2f} leva.")

# Print total profit message at the end
print(f"Burger Bus total profit: {total_profit:.2f} leva.")

"""" """

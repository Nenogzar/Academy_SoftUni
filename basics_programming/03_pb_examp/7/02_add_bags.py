def calculate_baggage_price(base_price, weight, days_until_travel, num_bags):
    if weight < 10:
        baggage_fee = 0.2 * base_price
    elif weight <= 20:
        baggage_fee = 0.5 * base_price
    else:
        baggage_fee = base_price

    if days_until_travel > 30:
        baggage_fee *= 1.1
    elif 7 <= days_until_travel <= 30:
        baggage_fee *= 1.15
    else:
        baggage_fee *= 1.4

    total_price = baggage_fee * num_bags
    return total_price


base_price = float(input())
weight = float(input())
days_until_travel = int(input())
num_bags = int(input())

total_price = calculate_baggage_price(base_price, weight, days_until_travel, num_bags)

# Printing the result
print(f"The total price of bags is: {total_price:.2f} lv.")

"""
Write a program that calculates the total cost of bought furniture.
You will be given information about each purchase on separate lines until you receive the command "Purchase".
Valid information should be in the format: ">>{furniture_name}<<{price}!{quantity}".
The price could be a floating-point or integer number.
You should store the names of the furniture and the total price.
"""

import re

pattern = r">>([a-zA-Z]+)<<(\d+\.?\d*)!(\d+)"
furn_name_list = []
total_price = 0

info = input()
while info != 'Purchase':

    match = re.search(pattern, info)
    if match:
        furniture_name, price, quantity = match.groups()
        furn_name_list.append(furniture_name)
        price = float(price)
        quantity = int(quantity)
        price_item = price * quantity
        total_price += price_item
    info = input()

print("Bought furniture:")
for furniture_name in furn_name_list:
    print(furniture_name)
print(f"Total money spend: {total_price:.2f}")



budget = float(input())
costs = 0
counter_or_products = 0
needed_money = 0

while True:
    name_of_product = input()

    if name_of_product == 'Stop':
        break

    counter_or_products += 1
    product_price = float(input())
    if counter_or_products % 3 == 0:
        product_price /= 2

    if product_price > budget:
        needed_money = product_price - budget
        break

    costs += product_price
    budget -= product_price

if needed_money == 0:
    print(f"You bought {counter_or_products} products for {costs:.2f} leva.")
else:
    print(f"You don't have enough money!")
    print(f"You need {needed_money:.2f} leva!")

# budget = float(input())
#
# product = input()
# product_counter = 0
# starting_budget = budget
#
# while product != 'Stop':
#     price = float(input())
#     product_counter += 1
#
#     if product_counter % 3 == 0:
#         price *= 0.50
#
#     budget -= price
#     if  budget < 0:
#         print("You don't have enough money!")
#         print(f"You need {abs(budget):.2f} leva!")
#         break
#
#     product = input()
#
# else:
#     print(f'You bought {product_counter} products for {abs(budget - starting_budget):.2f} leva.')



# budget = float(input())
#
# is_budget_bigger = True
# left_budget = budget
# products_bought = 0
# total_bought_products = 0
# product_count = 0
#
# while is_budget_bigger:
#
#     product_name = input()
#     product_count += 1
#     if product_name == "Stop":
#         print(f"You bought {products_bought} products for {total_bought_products:.2f} leva.")
#         is_budget_bigger = False
#
#     else:
#         product_price = float(input())
#         if product_count % 3 == 0:
#             left_budget += - (product_price / 2)
#             product_price = product_price / 2
#
#         else:
#             left_budget += - product_price
#
#     if left_budget >= 0:
#         products_bought += 1
#         total_bought_products += product_price
#
#     else:
#         print(f"You don't have enough money!\nYou need {abs(left_budget):.2f} leva!")
#         is_budget_bigger = False

""" 1"""
budget = float(input())
price_flour = float(input())
price_egg_one_pack = 0.75 * price_flour
price_l_milk = 1.25 * price_flour
price_quarter_milk = price_l_milk * 0.25
price_loaf = price_egg_one_pack + price_flour + price_quarter_milk
colored_eggs = 0
current_bread_count = 0
money_left = budget

while money_left >= price_loaf:
    current_bread_count += 1
    money_left -= price_loaf
    colored_eggs += 3

    if current_bread_count % 3 == 0:
        colored_eggs -= (current_bread_count - 2)

print(f"You made {current_bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")


""" 2 """
# budget = float(input())
# price_of_kg_flour = float(input())
#
# eggs_pack = price_of_kg_flour * 0.75
# milk_one_l = (price_of_kg_flour * 1.25) / 4
# colored_eggs = 0
# for number_breads in range(1, int(budget) + 1):
#     if eggs_pack + milk_one_l + price_of_kg_flour <= budget:
#         budget -= (eggs_pack + milk_one_l + price_of_kg_flour)
#         colored_eggs += 3
#         if number_breads % 3 == 0:
#             colored_eggs -= (number_breads - 2)
#     else:
#         print(
#             f"You made {number_breads - 1} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
#         break

#
"""
100
5
You made 9 loaves of Easter bread! Now you have 15 eggs and 7.19BGN left.
"""


""" 3 """
# budget = float(input())
# flour_price = float(input())
# eggs_price = flour_price * 0.75
# milk_price = (flour_price * 1.25) / 4
# loaf_price = flour_price + eggs_price + milk_price
#
# colored_eggs = 0
# bread_loaves = 0
#
# while budget <= loaf_price:
#
#     if budget <= loaf_price:
#         print(f"You made {bread_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
#         break
#
#     budget -= loaf_price
#     bread_loaves += 1
#     colored_eggs += 3
#
#     if bread_loaves % 3 == 0:
#         colored_eggs -= bread_loaves - 2




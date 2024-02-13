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





"""

20.5
1.25


"""

""" You made 7 loaves of Easter bread! Now you have 16 eggs and 2.45BGN left. """
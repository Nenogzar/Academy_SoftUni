quantity = int(input())
days = int(input())
ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15
total_cost = 0
gained_spirit = 0
for day in range(1, days + 1):
    tree_set = False
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        total_cost += ornament_set * quantity
        gained_spirit += 5
    if day % 3 == 0:
        total_cost += (tree_skirt + tree_garlands) * quantity
        tree_set = True
        gained_spirit += 13
    if day % 5 == 0:
        total_cost += tree_lights * quantity
        gained_spirit += 17
        if tree_set:
            gained_spirit += 30
    if day % 10 == 0:
        total_cost += tree_skirt + tree_garlands + tree_lights
        gained_spirit -= 20
if days % 10 == 0:
    gained_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {gained_spirit}")

""" 2 """

# quantity_of_decoration = int(input())
# remaining_days = int(input())
# ornament_set_price = 2
# tree_skirt_price = 5
# tree_garland_price = 3
# tree_lights_price = 15
# total_spirit = 0
# total_cost = 0
#
#
# for current_day in range(1, remaining_days + 1):
#     if current_day % 11 == 0:
#         quantity_of_decoration += 2
#     if current_day % 2 == 0:
#         total_cost += quantity_of_decoration * ornament_set_price
#         total_spirit +=5
#     if current_day % 3 == 0:
#         total_cost += quantity_of_decoration * (tree_skirt_price + tree_garland_price)
#         total_spirit += 10 + 3
#     if current_day % 5 == 0:
#         total_cost += quantity_of_decoration * tree_lights_price
#         total_spirit += 17
#         if current_day % 3 == 0:
#             total_spirit += 30
#     if current_day % 10 == 0:
#         total_spirit -=20
#         total_cost += tree_skirt_price + tree_lights_price + tree_garland_price
# if remaining_days % 10 == 0:
#     total_spirit -= 30
# print(f"Total cost: {total_cost}")
# print(f"Total spirit: {total_spirit}")
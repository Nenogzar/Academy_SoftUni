# from collections import defaultdict
#
# def add_food(food, quantity, bekery):
#     bekery[food]['quantity'] = quantity
#
# def add_quantity(food, quantity, bekery):
#     bekery[food]['quantity'] += quantity
#
# def action_command(action, quantity, food, bekery, total_sold):
#     if action == 'Receive':
#         if food not in bekery:
#             add_food(food, quantity, bekery)
#         else:
#             if quantity <= 0:
#                 """If the quantity is invalid (<= 0), ignore the command."""
#             else:
#                 add_quantity(food, quantity, bekery)
#     elif action == 'Sell':
#         if food not in bekery:
#             print(f"You do not have any {food}.")
#         elif quantity > bekery[food]['quantity']:
#             total_sold += bekery[food]['quantity']
#             print(f"There aren't enough {food}. You sold the last {bekery[food]['quantity']} of them.")
#             del bekery[food]
#         else:
#             total_sold += quantity
#             bekery[food]['quantity'] -= quantity
#             print(f"You sold {quantity} {food}.")
#
# bekery = defaultdict(lambda: {'quantity': 0})
# commands = input()
# total_sold = 0
# while commands != "Complete":
#     action, quantity, food = commands.split(" ")[0], int(commands.split(" ")[1]), commands.split(" ")[2]
#     action_command(action, quantity, food, bekery, total_sold)
#     commands = input()
#
# for food, quantity in bekery.items():
#     print(f"{food}: {quantity['quantity']}")
# print(f"All sold: {total_sold} goods")


""" """




bekery = {}
commands = input()
total_sold = 0
while commands != "Complete":
    action, quantity, food = commands.split(" ")[0], int(commands.split(" ")[1]), commands.split(" ")[2]
    if action == 'Receive':
        if food not in bekery:
            bekery[food] = {}
        if 'quantity' not in bekery[food]:
            bekery[food]['quantity'] = 0
        bekery[food]['quantity'] += quantity
    elif action == 'Sell':
        if food not in bekery:
            print(f"You do not have any {food}.")
        elif quantity > bekery[food].get('quantity', 0):
            total_sold += bekery[food].get('quantity', 0)
            print(f"There aren't enough {food}. You sold the last {bekery[food].get('quantity', 0)} of them.")
            del bekery[food]
        else:
            total_sold += quantity
            bekery[food]['quantity'] -= quantity
            print(f"You sold {quantity} {food}.")
    commands = input()

for food, quantity in bekery.items():
    print(f"{food}: {quantity.get('quantity', 0)}")

print(f"All sold: {total_sold} goods")

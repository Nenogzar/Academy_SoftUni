#Искате да отидете до Франция с влак, а билетът за влака струва точно 150$.
# Нямате достатъчно пари, затова решавате да закупите някои артикули с бюджета си
# и след това да ги продадете на по-висока цена – с надценка от 40%.
# Ще получите колекция от елементи и бюджет в следния формат:
#""" {type->price|type->price|type->price……|type->price} """"
#""" {budget} """
# Цените за всеки от видовете не могат да надвишават конкретна цена, която е:
#       Type        #   Maximum Price   #
#########################################
#       Clothes     #   50.00           #
#       Shoes       #   35.00           #
#       Accessories #   20.50           #
#########################################
# Ако цената за определен артикул е по-висока от максималната цена, не го купувайте.
# Всеки път, когато купувате артикул, трябва да намалите бюджета с цената му.
# Ако нямаш достатъчно пари за него, не можеш да го купиш.
# Купете колкото можете повече артикули.
# След това трябва да увеличите цената на всеки артикул, който успешно сте купили,
# с 40% и след това да го продадете.
# Изчислете дали бюджетът след продажбата на всички артикули е достатъчен за закупуване на билет за влак.
#### Input / Constraints
# • На 1-ви ред ще получите артикулите с техните цени в описания по-горе формат –
#       реални числа в диапазона [0.00……1000.00]
# • На 2-ри ред ще ви бъде даден бюджетът – реално число в диапазона [0.0….1000.0]

#### Output
# • Първо отпечатайте списъка с новите цени на закупения артикул, форматирани до втория десетичен знак в следния формат:
#   "{price1} {price2} {price3} … {priceN}"
# • Второ, отпечатайте печалбата, форматирана до втория десетичен знак в следния формат:
#   "Profit: {profit}"
# • Накрая:
# o Ако бюджетът е достатъчен за закупуване на билет за влак, отпечатайте: "Hello, France!"
# o В противен случай отпечатайте: "Not enough money."

train_ticket_cost = 150
maximum_prices = {
    "Clothes": 50.00,
    "Shoes": 35.00,
    "Accessories": 20.50
}

collection_items, budget = input().split("|"), float(input())
old_budget = budget
new_list = []
sold_items = []

for item_data in collection_items:
    item_type, item_price = item_data.split("->")
    item_price = float(item_price)

    if item_type in maximum_prices and item_price <= maximum_prices[item_type] and budget >= item_price:
        budget -= item_price
        sold_items.append(item_type)
        new_list.append((item_type, item_price))

sold_item_prices = [item[1] * 1.4 for item in new_list if item[0] in sold_items]
profit = sum(sold_item_prices) - sum(item[1] for item in new_list if item[0] in sold_items)

new_dujet= old_budget + profit
#print("new_dujet", new_dujet)

print(" ".join([f"{price:.2f}" for price in sold_item_prices]))
print(f"Profit: {profit:.2f}")

if 150 <= new_dujet:
    print("Hello, France!")
else:
    print("Not enough money.")


############################### FROM CEO ####################################################


# items_accessories = input().split("|")
# budget = int(input())
#
# items_price, budget_left, train_ticket = 0, budget, 150
#
# for clean_text in items_accessories:
#     type_item, price = (float(x) if x[-1].isdigit() else x for x in clean_text.split('->'))
#     if budget_left < price:
#         continue
#     if any(("Clothes" in type_item and price <= 50,
#             "Shoes" in type_item and price <= 35,
#             "Accessories" in type_item and price <= 20.50)):
#             items_price += price
#             budget_left -= price
#             print(f'{price * 1.40:.2f}' , end=" ")
#
# difference =  items_price * 1.4 - items_price
# print(f"\nProfit: {difference:.2f}")
#
# if budget + difference > train_ticket:
#     print(f"Hello, France!")
# else:
#     print("Not enough money.")





# collection_of_items = input().split("|")
# budget = int(input())
# budget_left = budget
# train_ticket = 150
# total_money = 0
# items_bought = []
#
#
# def add_money(current_price):
#     global total_money, budget_left
#     total_money += current_price
#     budget_left -= current_price
#
#
# for index in collection_of_items:
#     current_item, current_price = [float(x) if x[-1].isdigit() else x for x in index.split('->')]
#     if budget_left >= current_price:
#         if current_item == 'Clothes' and current_price <= 50:
#             add_money(current_price)
#             items_bought.append(current_price + (current_price * 0.40))
#         elif current_item == 'Shoes' and current_price <= 35:
#             add_money(current_price)
#             items_bought.append(current_price + (current_price * 0.40))
#         elif current_item == 'Accessories' and current_price <= 20.50:
#             add_money(current_price)
#             items_bought.append(current_price + (current_price * 0.40))
#
# difference = sum(items_bought) - total_money
# print(' '.join(f"{n:.2f}" for n in items_bought))
# print(f'Profit: {difference:.2f}')
# if budget + difference > train_ticket:
#     print('Hello, France!')
# else:
#     print('Not enough money.')






# items_accessories = input().split("|")
# budget = int(input())
#
# items_price = list()
# budget_left = budget
# selling_items = list()
# train_ticket = 150
#
# for clean_text in items_accessories:
#     if "Clothes->" in clean_text:
#         text = float(clean_text.replace("Clothes->", ""))
#
#         if 0 < text <= 50 and budget_left >= text:
#             items_price.append(text)
#             budget_left -= text
#             selling_items.append(text + text * 0.40)
#
#     elif "Shoes->" in clean_text:
#         text = float(clean_text.replace("Shoes->", ""))
#
#         if 0 < text <= 35 and budget_left >= text:
#             items_price.append(text)
#             budget_left -= text
#             selling_items.append(text + text * 0.40)
#
#     elif "Accessories->" in clean_text:
#         text = float(clean_text.replace("Accessories->", ""))
#
#         if 0 < text < 20.50 and budget_left >= text:
#             items_price.append(text)
#             budget_left -= text
#             selling_items.append(text + text * 0.40)
#
# for n in selling_items:
#     print(f"{n:.2f}", end=" ")
#
# normal_price = sum(items_price)
# re_sale = sum(selling_items)
# difference = re_sale - normal_price
#
# print(f"\nProfit: {difference:.2f}")
#
# if budget + difference > train_ticket:
#     print(f"Hello, France!")
# else:
#     print("Not enough money.")
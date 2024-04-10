""" The .keys() Method """
likes = {"color": "blue", "fruit": "apple", "pet": "dog"}

dict_keys = likes.keys()
print(dict_keys) # dict_keys(['color', 'fruit', 'pet'])

###
for key in likes.keys():
    print(key)
    # color
    # fruit
    # pet

""" Walking Through Dictionary Values: The .values() Method"""

dict_value = likes.values()
print(dict_value) # dict_values(['blue', 'apple', 'dog'])

for value in likes.values():
    print(value)
    # blue
    # apple
    # dog

""" Changing Dictionary Values During Iteration"""
fruits = {"apple": 0.40, "orange": 0.35, "banana": 0.25}

for fruit, price in fruits.items():
    fruits[fruit] = round(price * 0.9, 2)


print(fruits) # {'apple': 0.36, 'orange': 0.32, 'banana': 0.23}

###

incomes = {"apple": 5600.00, "orange": 3500.00, "banana": 5000.00}
total_income = 0.00

for income in incomes.values():
    total_income += income

print(total_income)  # 14100.0

###################################################################

order = {"coffe": {
    "price": 1.50,
    "quantity": 2},
    "jus": {
        "price": 2.50,
        "quantity": 3}}

for key, value in order.items():
    price = float(value["price"])
    quantity = int(value["quantity"])
    total_sum = quantity * price

    print(f"{key}: {total_sum:.2f}")

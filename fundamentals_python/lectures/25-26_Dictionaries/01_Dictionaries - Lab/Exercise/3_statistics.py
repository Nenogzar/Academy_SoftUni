def product_func(dict_product, product_dict):
    key, value = dict_product[0], int(dict_product[1])

    if key not in product_dict:
        product_dict[key] = value
    else:
        product_dict[key] += value
    return product_dict


command = input()
product_dict = {}
while command != "statistics":
    product_info = command.split(": ")
    product_dict = product_func(product_info, product_dict)

    command = input()

# print("Products in stock:")
# for k, v in product_dict.items():
#     print(f"- {k}: {v}")
#
# print(f"Total Products: {len(product_dict)}")
# print(f"Total Quantity: {sum(product_dict.values())}")

print(f"Products in stock:")
[print(f"- {item}: {quantity}") for item, quantity in product_dict.items()]
print(f"Total Products: {len(product_dict)}\nTotal Quantity: {sum(product_dict.values())}")

"""  CEO """
#
# product_input = input()
#
# products_in_stock = {}
#
# while product_input != 'statistics':
#     product, quantity = product_input.split(': ')
#     products_in_stock[product] = products_in_stock.get(product, 0) + int(quantity)
#     product_input = input()
#
# print('Products in stock:')
# for product, quantity in products_in_stock.items():
#     print(f'- {product}: {quantity}')
# print(f'Total Products: {len(products_in_stock)}')
# print(f'Total Quantity: {sum(products_in_stock.values())}')


"""  CEO """

# product_input = input()
# food_info_dic = dict()
# while product_input != "statistics":
#     food_type = product_input.split(": ")
#     if food_type[0] not in food_info_dic:
#         food_info_dic[food_type[0]] = 0
#     food_info_dic[food_type[0]] = food_info_dic[food_type[0]] + int(food_type[-1])
#     product_input = input()
#
#
# def showing_products(dictionary):
#     print("Products in stock:")
#     total_products = 0
#     total_quantity = 0
#     for key, value in dictionary.items():
#         print(f"- {key}: {value}")
#         total_products += 1
#         total_quantity += value
#     print(f"Total Products: {total_products}")
#     print(f"Total Quantity: {total_quantity}")
#
#
# showing_products(food_info_dic)



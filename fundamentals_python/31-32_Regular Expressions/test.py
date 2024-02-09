# total_sum = 0
# data = input()
#
# special = 1
#
# while data != "special" and data != "regular":
#     price = float(data)
#
#     if price > 0:
#         total_sum += price
#     else:
#         print("Invalid price!")
#
#     data = input()
#
# taxes = total_sum * 0.2
#
# if data == "special":
#     special = 0.9
#
# if total_sum == 0:
#     print("Invalid order!")
#
# else:
#     print("Congratulations you've just bought a new computer!")
#     print(f"Price without taxes: {total_sum:.2f}$")
#     print(f"Taxes: {taxes:.2f}$")
#     print("-----------")
#     print(f"Total price: {(total_sum + taxes) * special:.2f}$")
#
#
# """  whit list """
#
# # Инициализация на празен списък и променлива за сумата
# numbers = []
# customers = ""
# positive_sum = 0.0
# discount = 0
# # Вход на числата от конзолата
# while True:
#     input_value = input()
#
#     if input_value.lower() == 'special' or input_value.lower() == 'regular':
#         customers = input_value.lower()
#         break
#     try:
#         num = float(input_value)
#         if num < 0:
#             print("Invalid price!")
#         else:
#             numbers.append(num)
#             positive_sum += num
#     except ValueError:
#         print("Invalid order!")
#
# taxes = positive_sum * 0.2
# total_price = positive_sum + taxes
#
# # Проверка за валидност на въведените данни
# if not numbers or total_price == 0:
#     print("Invalid order!")
#
# else:
#     # Изпълнение на кода в зависимост от въведената дума
#     if customers == 'special':
#         discount = 0.9
#     elif customers == 'regular':
#         discount = 1
#
#     total_price_with_discount = total_price * discount
#
#     print("Congratulations you've just bought a new computer!")
#     print(f"Price without taxes: {positive_sum:.2f}$")
#     print(f"Taxes: {taxes:.2f}$")
#     print("-----------")
#     print(f"Total price: {total_price_with_discount:.2f}$")

""" 3 """
total_sum = 0
data = input()
customers = list()
discount = 0.1

while data != "special" and data != "regular":
    price = float(data)
    if price < 0:
        print("Invalid price!")
        data = input()
        continue
    else:
        customers.append(data)
        data = input()

if not customers:
    print("Invalid order!")
else:
    total_sum = sum(float(n) for n in customers)
    taxes = total_sum * 0.2
    total_price = total_sum + taxes

    if data == "special":
        total_price = total_price - (total_price * discount)

    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_sum:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")

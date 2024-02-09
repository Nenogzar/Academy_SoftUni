# Инициализация на празен списък и променлива за сумата
numbers = []
positive_sum = 0.0
taxe = 20
# Вход на числата от конзолата
while True:
    input_value = input("Въведете число (за край въведете 'special' или 'regular'): ")

    if input_value.lower() == 'special' or input_value.lower() == 'regular':
        customers = input_value.lower()  # Присвояване на 'special' или 'regular' на променливата customers
        break
    try:
        num = float(input_value)
        if num < 0:
            print("Invalid price")
        else:
            numbers.append(num)
            positive_sum += num
    except ValueError:
        invalid_price = "ValueError"

# Печат на въведените числа
print("Въведени числа:", numbers)

# Изпълнение на кода в зависимост от въведената дума
if customers == 'special':
    taxe = 1
    print("Избран е special код.")
elif customers == 'regular':
    taxe = 1.1
    print("Избран е regular код.")
print(invalid_price)
# Печат на сумата на положителните числа
print("Сума на положителните числа:", positive_sum)
total_price = positive_sum * taxe
print("Крайна цена:", total_price)
# Въвеждане на възраст и пол от потребителя
age = float(input())
gender = input().lower()  # Преобразуване на пола в малки букви

# Проверка на възрастта и пола и отпечатване на съответното обръщение
if gender == 'm':
    if age >= 16:
        print("Mr.")
    else:
        print("Master")
elif gender == 'f':
    if age >= 16:
        print("Ms.")
    else:
        print("Miss")
else:
    print("Error")

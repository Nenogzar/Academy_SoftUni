day_number = int(input())

# Проверка за валидност на въведеното число
if 1 <= day_number <= 7:
    # Превръщане на числото в съответния ден от седмицата
    if day_number == 1:
        day = "Monday"
    elif day_number == 2:
        day = "Tuesday"
    elif day_number == 3:
        day = "Wednesday"
    elif day_number == 4:
        day = "Thursday"
    elif day_number == 5:
        day = "Friday"
    elif day_number == 6:
        day = "Saturday"
    else:
        day = "Sunday"

    # Извеждане на деня от седмицата
    print(day)
else:
    print("Error")
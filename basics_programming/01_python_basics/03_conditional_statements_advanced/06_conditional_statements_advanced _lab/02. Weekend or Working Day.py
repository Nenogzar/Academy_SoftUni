day = input().capitalize()

# Проверка дали въведеният текст е ден от седмицата и определя дали е работен или почивен ден
if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    print("Working day")
elif day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Error")
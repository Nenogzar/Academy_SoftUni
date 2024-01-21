# Въвеждане на час от денонощието и ден от седмицата от потребителя
hour = int(input())
day = input().capitalize().lower()  # Преобразуване на деня в малки букви след въвеждането

if day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday" or day == "saturday":
    if 10 <= hour <= 18:
        print("open")
    else:
        print("closed")
elif day == "sunday":
    print("closed")
else:
    print("error")
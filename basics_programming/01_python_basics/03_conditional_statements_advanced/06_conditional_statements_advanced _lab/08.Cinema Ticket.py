day = input("Въведете ден от седмицата: ").capitalize().lower()

if day == "monday" or day == "friday" or day == "tuesday":
    price = 12
elif day == "wednesday" or day == "thursday":
    price = 14
elif day == "saturday" or day == "sunday":
    price = 16
else:
    print("error")
    price = None

if price is not None:
    print(f"{price}")

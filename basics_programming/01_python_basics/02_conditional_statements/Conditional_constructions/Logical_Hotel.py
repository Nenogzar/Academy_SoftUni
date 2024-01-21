while True:
    days = input("Колко дни ще отседнете в хотела? ")
    if days == "":
        print("Въведете брой дни")
        continue
    days = int(days)

    room_type = input("В какъв вид стая искате да отседнете: room_for_one_person, apartment, president_apartment: ")
    if room_type not in ["room_for_one_person", "apartment", "president_apartment"]:
        print("Невалиден тип стая")
        continue

    rating = input("Каква оценка бихте дали на хотела: positive или negative: ")
    if rating not in ["positive", "negative"]:
        print("Невалидна оценка")
        continue

    room_for_one_person = 18.00 # Цени
    apartment = 25.00
    president_apartment = 35.00
    nights = days-1  # дефинирам нощувка
    positive = 0.25
    negative = 0.10
    total_price=0.00

    if room_type == "room_for_one_person":
        total_price = room_for_one_person * nights
    elif room_type == "apartment":
        total_price = apartment * nights
        if days < 10:
            total_price *= 0.7
        elif 10 <= days <= 15:
            total_price *= 0.65
        else:
            total_price *= 0.5
    elif room_type == "president_apartment":
        total_price = president_apartment * nights
        if days < 10:
            total_price *= 0.9
        elif 10 <= days <= 15:
            total_price *= 0.85
        else:
            total_price *= 0.8


    if rating == "positive":
        total_price *= (1 + positive)
    elif rating == "negative":
        total_price *= (1 - negative)
    else:
        print("Невалидна оценка")

    #print(f"Цената за {days - 1} нощувки в стая {room_type} ще Ви струва: {total_price:.2f}лв.")
    print(f"{total_price:.2f}")
    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break
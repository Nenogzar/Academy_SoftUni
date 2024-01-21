budget = float(input())   # Бюджет – реално число в интервала [10.00...10000.00]
season = input()        # Сезон – текст "Summer" или "Winter"

vehicle = ""
type_class = ""

if budget <= 100:
    type_class = "Economy class"
    if season == "Summer":
        vehicle = "Cabrio"
        budget *= 0.35
    elif season == "Winter":
        vehicle = "Jeep"
        budget *= 0.65
elif budget < 500:
    type_class = "Compact class"
    if season == "Summer":
        vehicle = "Cabrio"
        budget *= 0.45
    elif season == "Winter":
        vehicle = "Jeep"
        budget *= 0.80
elif budget > 500:
    type_class = "Luxury class"
    vehicle = "Jeep"
    budget *= 0.90


print(f"{type_class}")
print(f"{vehicle} - {budget:.2f}")


# car_budget = float(input())
# season = input()
#
# if season == "Summer" and car_budget <= 100:
#     total = car_budget * 0.35
#     print(f"Economy class\nCabrio - {total:.2f}")
# elif season == "Summer" and car_budget <= 500:
#     total = car_budget * 0.45
#     print(f"Compact class\nCabrio - {total:.2f}")
# elif season == "Winter" and car_budget <= 100:
#     total = car_budget * 0.65
#     print(f"Economy class\nJeep - {total:.2f}")
# elif season == "Winter" and car_budget <= 500:
#     total = car_budget * 0.80
#     print(f"Compact class\nJeep - {total:.2f}")
# elif car_budget > 500:
#     total = car_budget * 0.90
#     print(f"Luxury class\nJeep - {total:.2f}")

budget = float(input())     # Бюджет – реално число в интервала [10.00...10000.00]
season = input()            # Сезон - текст "Summer" или "Winter"
place = ""                  # "Hotel", "Hut" или "Camp".
summer_location = "Alaska"
winter_location = "Morocco"

if budget <= 1000:
    place = "Camp"
    if season == "Summer":
        budget *= 0.65
    elif season == "Winter":
        budget *= 0.45

elif budget <= 3000:
    place = "Hut"
    if season == "Summer":
        budget *= 0.8
    elif season == "Winter":
        budget *= 0.6

elif budget > 3000:
    place = "Hotel"
    budget *= 0.9

if season == "Summer":
    print(f"{summer_location} - {place} - {budget:.2f}")
elif season == "Winter":
    print(f"{winter_location} - {place} - {budget:.2f}")



# vacation_budget = float(input())
# season = input()
#
# if season == "Summer" and vacation_budget <= 1000:
#     total = vacation_budget * 0.65
#     print(f"Alaska - Camp - {total:.2f}")
# elif season == "Summer" and vacation_budget <= 3000:
#     total = vacation_budget * 0.80
#     print(f"Alaska - Hut - {total:.2f}")
# elif season == "Winter" and vacation_budget <= 1000:
#     total = vacation_budget * 0.45
#     print(f"Morocco - Camp - {total:.2f}")
# elif season == "Winter" and vacation_budget <= 3000:
#     total = vacation_budget * 0.60
#     print(f"Morocco - Hut - {total:.2f}")
# elif vacation_budget > 3000 and season == "Summer":
#     total = vacation_budget * 0.90
#     print(f"Alaska - Hotel - {total:.2f}")
# else:
#     total = vacation_budget * 0.90
#     print(f"Morocco - Hotel - {total:.2f}")

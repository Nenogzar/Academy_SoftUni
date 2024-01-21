budget = float(input())
season = input()
holiday = ""
destination = ""
camp = "Camp"
hotel = "Hotel"
need_money = 0.00

if 0 <= budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        holiday = camp
        need_money = budget * 0.7
    elif season == "winter":
        holiday = hotel
        need_money = budget * 0.3
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        holiday = camp
        need_money = budget * 0.6
    elif season == "winter":
        holiday = hotel
        need_money = budget * 0.2
else:
    destination = "Europe"
    holiday = hotel
    need_money = budget * 0.1

#print("destinacia", destination)
#print("holiday", holiday)
#print("need+money", need_money)

print(f"Somewhere in {destination}")
print(f"{holiday} - {(budget - need_money):.2f}")
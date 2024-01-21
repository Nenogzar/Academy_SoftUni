days = int(input())
type_room = input()
rating = input().lower()
nights = days -1
room = 18
apartment = 25
p_apartmant = 35
price_room = room * nights
price_apartment = apartment * nights
price_president = p_apartmant * nights
price = 0.00

if type_room == "room for one person":
    price = price_room

if  0 < days < 10:
    if type_room == "apartment" :
        price = ((price_apartment) * 0.70)
    elif type_room == "president apartment":
        price = (price_president) * 0.90
elif 10 < days < 15:
    if type_room == "apartment":
        price = (price_apartment) * 0.65
    elif type_room == "president apartment":
        price = (price_president) * 0.85
elif days >= 15:
    if type_room == "apartment":
        price = (price_apartment) * 0.50
    elif type_room == "president apartment":
        price = (price_president) * 0.80
else:
    print("error")
#print(price)
if rating == "positive":
    price=(price * 0.25) + price
elif rating == "negative":
    price = price - (price * 0.10)
else:
    print("error")
print(f"{price:.2f}")
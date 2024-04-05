discount = 1
rating_discount = 1
price = 1
days_to_stay = int(input())
night_stay = days_to_stay - 1
type_of_room = input()          # "room for one person" or  "apartment" or "president apartment"
rating = input()                # "positive"  or "negative"

if type_of_room == "room for one person":
    price = 18.00
elif type_of_room == "apartment":
    price = 25.00
    if night_stay < 10:
        discount = 0.3
    elif night_stay < 15:
        discount = 0.35
    elif night_stay >= 15:
        discount = 0.5
elif type_of_room == "president apartment":
    price = 35.00
    if night_stay < 10:
        discount = 0.1
    elif night_stay < 15:
        discount = 0.15
    elif night_stay >= 15:
        discount = 0.2

price_for_stay = (night_stay * price)
price_whit_discount = price_for_stay - (price_for_stay * discount)
if price_whit_discount == 0.00:
    price_whit_discount = price_for_stay
if rating == "positive":
    rating_discount = 1.25
elif rating == "negative":
    rating_discount = 0.9

total_price = price_whit_discount * rating_discount
print(f"{total_price:.2f}")

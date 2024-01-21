price_nylon = 1.50
price_paint = 14.50
price_thinner = 5

quantity_nylon = int(input())
quantity_paint = int(input())
quantity_thinner = int(input())
working_hours = int(input())

price_materials = ((price_nylon * (quantity_nylon + 2))
                   +(price_paint * (quantity_paint*1.10))
                   +(price_thinner*quantity_thinner) + 0.40)
workint_price = (price_materials * 0.3) * working_hours
total = price_materials + workint_price
print(total)


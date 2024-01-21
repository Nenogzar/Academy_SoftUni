budjet = float(input())
decor = budjet*0.10
walk = int(input())
cloting_discount = 0
cloting_cost = float(input())

clots = cloting_cost * walk
if walk > 150:
    cloting_discount = clots * 0.10

cloting = clots - cloting_discount
expense = decor + cloting
deficit = budjet - expense

if expense <= budjet:
    print("Action!")
    print(f"Wingard starts filming with {deficit:.2f} leva left.")
elif expense > budjet:
    print("Not enough money!")
    print(f"Wingard needs {(budjet-expense) *-1:.2f} leva more.")
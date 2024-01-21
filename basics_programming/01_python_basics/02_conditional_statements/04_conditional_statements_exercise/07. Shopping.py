budget = float(input())
vcard = int(input())
cpu = int(input())
ram = int(input())

vcard_price = 250
basis = vcard * vcard_price
cpu_price = cpu * (basis*0.35)
ram_price = ram *(basis*0.10)

total_price = basis + cpu_price + ram_price
discount = total_price * 0.15

if vcard > cpu:
    total_price -=discount

if budget >= total_price:
    print(f"You have {budget - total_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva more!")
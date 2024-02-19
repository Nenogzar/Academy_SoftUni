import math

budget = float(input())
students = int(input())
price_flour = float(input())
price_one_egg = float(input()) * 10
price_apron = float(input())

po_malko = 0
for n in range(1, students + 1):
    if n % 5 == 0:
        po_malko += 1


total_price_flour = price_flour * (students - po_malko)
total_price_egg = price_one_egg * students
total_price_apron = price_apron * (math.ceil(students*1.2))

razhod = (total_price_flour + total_price_egg + total_price_apron)

if razhod <= budget:
    print(f"Items purchased for {razhod:.2f}$.")
else:
    print(f"{abs(budget - razhod):.2f}$ more needed.")

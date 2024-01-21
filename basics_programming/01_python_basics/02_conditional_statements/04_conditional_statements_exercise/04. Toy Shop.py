puzzle = 2.60
talking_doll= 3
teddy_bear = 4.10
mignon = 8.20
truck = 2

excursion_price = float(input())
puzzle_num = int(input())
talking_doll_num  = int(input())
teddy_bear_num = int(input())
mignon_num = int(input())
truck_num = int(input())

count_toys = puzzle_num+ talking_doll_num+teddy_bear_num+mignon_num+truck_num
price = puzzle*puzzle_num + talking_doll*talking_doll_num + teddy_bear*teddy_bear_num + mignon*mignon_num + truck*truck_num


discount = 0
if count_toys >= 50:
    discount =price * 0.25

rent = (price - discount) * 0.1
profit = price - discount - rent

if excursion_price <= profit:
    print(f"Yes! {profit-excursion_price:.2f} lv left.")
else:
    print(f"Not enough money! {excursion_price - profit:.2f} lv needed.")
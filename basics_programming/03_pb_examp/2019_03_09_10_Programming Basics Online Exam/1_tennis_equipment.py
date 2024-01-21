import math

tennis_racket = float(input())
sneakers = tennis_racket / 6
numbers_racket = int(input())
numbers_sneakers = int(input())

price_rackets = tennis_racket * numbers_racket
price_sneakers = sneakers * numbers_sneakers
price_other_equip = (price_rackets + price_sneakers) * 0.2
total_price = price_rackets + price_sneakers + price_other_equip
nole_price = total_price / 8
sponsors_price = total_price - nole_price

print(f"Price to be paid by Djokovic {math.floor(nole_price)}")
print(f"Price to be paid by sponsors {math.ceil(sponsors_price)}")

# import math
#
# price_tennis_racket = float(input())
# total_tennis_racket = int(input())
# number_tennis_sneakers = int(input())
#
# rackets_total_price = price_tennis_racket * total_tennis_racket
# one_sneakers_price = price_tennis_racket / 6
# all_sneakers_price = one_sneakers_price * number_tennis_sneakers
# total_price_equipment = (rackets_total_price + all_sneakers_price) * 1.2
#
# djokovic_price = total_price_equipment / 8
# sponsors_price = total_price_equipment * (7 / 8)
#
# print(f"Price to be paid by Djokovic {math.floor(djokovic_price)}")
# print(f"Price to be paid by sponsors {math.ceil(sponsors_price)}")

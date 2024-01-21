chicken_menu = 10.35
fish_menu = 12.40
vegan_menu = 8.15
delivery = 2.50

quantity_chicken = int(input())
quantity_fish = int(input())
quantity_vegan = int(input())

price = ((chicken_menu * quantity_chicken)
               +(fish_menu * quantity_fish)
               +(vegan_menu * quantity_vegan))
dessert = price * 0.20
total_price = price + dessert + delivery
print(f"{total_price:.2f}")

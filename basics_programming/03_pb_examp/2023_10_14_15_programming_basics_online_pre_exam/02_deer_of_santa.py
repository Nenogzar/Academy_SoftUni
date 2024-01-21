import math

absence_in_days = int(input()) # days
food_supply = int(input()) # kg
deer_one = float(input())
deer_two = float(input())
deer_three = float(input())

needed_food = (deer_one+deer_two+deer_three) * absence_in_days
difference_food = abs(food_supply - needed_food)
if needed_food < food_supply:
    print(f"{math.floor(difference_food)} kilos of food left.")
else:
    print(f"{math.ceil(difference_food)} more kilos of food are needed.")


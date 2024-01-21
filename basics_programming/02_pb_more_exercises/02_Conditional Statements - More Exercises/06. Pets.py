import math
days = int(input())             # брой дни – цяло число в интервал [1…5000]
food_kilos= int(input())        # оставена храна в килограми – цяло число в интервал [0…100000]
food_dog = float(input())         # храна на ден за кучето в килограми – реално число в интервал [0.00…100.00]
food_cat = float(input())       # храна на ден за котката в килограми– реално число в интервал [0.00…100.00]
food_turtles = float(input())   # храна на ден за костенурката в грамове – реално число в интервал [0.00…10000.00]

need_food = days * food_cat + days * (food_turtles/1000) + days * food_dog
difference = abs(need_food - food_kilos)

if need_food <= food_kilos:
    print(f"{math.floor(difference)} kilos of food left.")
else:
    print(f"{math.ceil(difference)} more kilos of food are needed.")

# import math
#
# number_days = int(input())
# left_foot_inkg = int(input())
# food_for_dog_per_kg = float(input())
# food_for_cat_per_kg = float(input())
# food_for_turtle_per_grams = float(input())
#
# dog_food_needed = number_days * food_for_dog_per_kg
# cat_food_needed = number_days * food_for_cat_per_kg
# turtle_food_needed = (number_days * food_for_turtle_per_grams) / 1000
#
# total_food = left_foot_inkg - (dog_food_needed + cat_food_needed + turtle_food_needed)
#
# if total_food >= 0:
#     print(f"{math.floor(total_food)} kilos of food left.")
# else:
#     print(f"{math.ceil(abs(total_food))} more kilos of food are needed.")

dog_food = int(input())
dog_food_grams = dog_food * 1000
total_food = 0
while True:
    any_part = input()
    if any_part == "Adopted":
        break
    else:
        total_food += int(any_part)
difference = abs(total_food - dog_food_grams)
if total_food < dog_food_grams:
    print(f"Food is enough! Leftovers: {difference} grams." )
else:
    print(f"Food is not enough. You need {difference} grams more." )



# food_kg = int(input())
#
# food = 0
# while True:
#     eated_food = (input())
#     if eated_food == "Adopted":
#         break
#     food += int(eated_food)
#
# total_buy_food = food_kg * 1000
#
# if total_buy_food >= food:
#     total = total_buy_food - food
#     print(f"Food is enough! Leftovers: {total} grams.")
#
# else:
#     total = food - total_buy_food
#     print(f"Food is not enough. You need {total} grams more.")

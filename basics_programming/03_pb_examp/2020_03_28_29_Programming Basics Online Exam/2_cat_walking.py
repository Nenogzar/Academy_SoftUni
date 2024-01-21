min_daily_walk = int(input())
walks_daily = int(input())
calories_daily = float(input())

total_time_walks = min_daily_walk * walks_daily
calories_burned = total_time_walks * 5
good_calories = calories_daily / 2

if calories_burned >= good_calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_burned}.")

else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_burned}.")




# min_walk = int(input())
# count_walks = int(input())
# cat_calories = int(input())
#
# calories_per_minute = 5
# total_walks_minutes = count_walks * min_walk
# calories_burn = total_walks_minutes * calories_per_minute
# target_calories = cat_calories / 2
#
# if calories_burn >= target_calories:
#     print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_burn}.")
#
# else:
#     print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_burn}.")

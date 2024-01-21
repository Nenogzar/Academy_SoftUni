heritage = float(input())  # Наследените пари – реално число в интервала [1.00 ... 1 000 000.00]
year_live = int(input())  # Годината, до която трябва да живее (включително) – цяло число в интервала [1801 ... 1900]
money = 0

ivan_year = 17
need_year = 0

# за всяка четна година ще харчи 12 000 лева
# променете year_live на rent в условието
for rent in range(1800, year_live + 1):
    need_year += 1
    #print("need_year", need_year)

    if rent % 2 == 0:
        money += 12000
        #print(rent, "четна", money)
    else:
        money += 12000 + (ivan_year + need_year) * 50
        #print(rent, "нечетна", money)

total_sum = heritage - money
if total_sum >= 0:
    print(f"Yes! He will live a carefree life and will have {abs(total_sum):.2f} dollars left.")
else:
    print(f"He will need {abs(total_sum):.2f} dollars to survive.")


# money = float(input())
# year = int(input())
# total_summ = money
# age = 18
# for year in range(1800, year + 1):
#
#     if year % 2 == 0:
#         total_summ -= 12000
#
#     else:
#         total_summ -= (12000 + (age * 50))
#     age += 1
#
#
# if total_summ >= 0:
#     print(f'Yes! He will live a carefree life and will have {total_summ:.2f} dollars left.')
# else:
#     print(f'He will need {abs(total_summ):.2f} dollars to survive.')





# heritage_money = float(input())
# year_till_he_will_live = int(input())
#
# total_heritage_left = heritage_money
# starting_year = 18
# expense_per_year = 12_000
#
# for year in range(1800, year_till_he_will_live + 1):
#
#     if year % 2 == 0:
#         total_heritage_left = total_heritage_left - expense_per_year
#         starting_year += 1
#
#     else:
#         total_heritage_left = total_heritage_left - (expense_per_year + (starting_year * 50))
#         starting_year += 1
#
# if total_heritage_left >= 0:
#     print(f"Yes! He will live a carefree life and will have {total_heritage_left:.2f} dollars left.")
# else:
#     print(f"He will need {abs(total_heritage_left):.2f} dollars to survive.")

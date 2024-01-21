#1

for number in range(1, 1000 + 1):
    if number % 10 == 7:
        print(number)



#2

import math

count_of_numbers = int(input())
sum_of_all_elements = 0
max_element = -math.inf
for number in range(count_of_numbers):  # range(1, count_of_numbers +1)
    current_number = int(input())
    sum_of_all_elements += current_number
    if current_number > max_element:
        max_element = current_number
if max_element == sum_of_all_elements - max_element:
    print("Yes")
    print(f"Sum = {max_element}")
else:
    difference = abs(max_element - (sum_of_all_elements - max_element))
    print("No")
    print(f"Diff = {difference}")



#3

count_of_numbers = int(input())
p1_counter = 0
p2_counter = 0
p3_counter = 0
p4_counter = 0
p5_counter = 0
for number in range(count_of_numbers):
    current_number = int(input())
    if current_number < 200:
        p1_counter += 1
    elif current_number < 400:
        p2_counter += 1
    elif current_number < 600:
        p3_counter += 1
    elif current_number < 800:
        p4_counter += 1
    elif current_number >= 800:   #else:
        p5_counter += 1
p1_percent = p1_counter / count_of_numbers * 100
p2_percent = p2_counter / count_of_numbers * 100
p3_percent = p3_counter / count_of_numbers * 100
p4_percent = p4_counter / count_of_numbers * 100
p5_percent = p5_counter / count_of_numbers * 100
print(f"{p1_percent:.2f}%")
print(f"{p2_percent:.2f}%")
print(f"{p3_percent:.2f}%")
print(f"{p4_percent:.2f}%")
print(f"{p5_percent:.2f}%")


#4

ages = int(input())
laundry_price = float(input())
price_per_toy = int(input())
total_money = 0
total_toys = 0
current_birthday_money = 0
for birthday in range(1, ages + 1):
    if birthday % 2 == 0:
        current_birthday_money += 10
        total_money += current_birthday_money - 1
    else:
        total_toys += 1
total_money += total_toys * price_per_toy
difference = abs(total_money - laundry_price)
if total_money >= laundry_price:
    print(f"Yes! {difference:.2f}" )
else:
    print(f"No! {difference:.2f}" )



#5

opened_tabs = int(input())
salary = int(input())
for current_tab in range(opened_tabs):
    website_name = input()
    if website_name == "Facebook":
        salary -= 150
    elif website_name == "Instagram":
        salary -= 100
    elif website_name == "Reddit":
        salary -= 50
    if salary <= 0:
        break
if salary > 0:
    print(salary)
else:
    print("You have lost your salary.")


#6




#7

number_of_groups = int(input())
mousalla_climbers = 0
monblan_climbers = 0
kilimandjaro_climbers = 0
k2_climbers = 0
everest_climbers = 0
total_climbers = 0
for current_group in range(number_of_groups):
    current_group_climbers = int(input())
    if current_group_climbers <= 5:
        mousalla_climbers += current_group_climbers
    elif current_group_climbers <= 12:
        monblan_climbers += current_group_climbers
    elif current_group_climbers <= 25:
        kilimandjaro_climbers += current_group_climbers
    elif current_group_climbers <= 40:
        k2_climbers += current_group_climbers
    elif current_group_climbers >= 41:  # else:
        everest_climbers += current_group_climbers
    total_climbers += current_group_climbers
percentage_mousalla_climbers = mousalla_climbers / total_climbers * 100
percentage_monblan_climbers = monblan_climbers / total_climbers * 100
percentage_kilimandjaro_climbers = kilimandjaro_climbers / total_climbers * 100
percentage_k2_climbers = k2_climbers / total_climbers * 100
percentage_everest_climbers = everest_climbers / total_climbers * 100
print(f"{percentage_mousalla_climbers:.2f}%")
print(f"{percentage_monblan_climbers:.2f}%")
print(f"{percentage_kilimandjaro_climbers:.2f}%")
print(f"{percentage_k2_climbers:.2f}%")
print(f"{percentage_everest_climbers:.2f}%")



#8

number_of_tournaments = int(input())
start_points = int(input())
total_points = 0
tournaments_won = 0
for tournament in range(number_of_tournaments):
    position = input()
    if position == "W":
        total_points += 2000
        tournaments_won += 1
    elif position == "F":
        total_points += 1200
    elif position == "SF":  # else
        total_points += 720
average_points = total_points // number_of_tournaments
total_points += start_points
won_tournaments_percent = tournaments_won / number_of_tournaments * 100
print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{won_tournaments_percent:.2f}%")




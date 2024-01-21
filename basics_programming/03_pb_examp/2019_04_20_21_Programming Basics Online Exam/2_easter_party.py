guests_number = int(input())
one_person_price = float(input())
budget = float(input())
cake_price = budget * 0.1

if 10 <= guests_number <= 15:
    one_person_price *= 0.85
elif 15 < guests_number <= 20:
    one_person_price *= 0.80
elif guests_number > 20:
    one_person_price *= 0.75

costing = guests_number * one_person_price + cake_price
difference = budget - costing

# print("cake_price", cake_price)
# print("one_person_price", one_person_price)
# print("guests_number", guests_number, "+ one_person_price",one_person_price, "+ cake_price", cake_price, "= costing ",  costing)

if costing <= budget:
    print(f"It is party time! {abs(difference):.2f} leva left.")
else:
    print(f"No party! {abs(difference):.2f} leva needed.")

# number_guests = int(input())
# reservation_one_person = float(input())
# budget = float(input())
#
# cake_price = budget * 0.10
# discount = 0
#
# if number_guests < 10:
#     discount = 1
#
# elif 10 <= number_guests <= 15:
#     discount = 0.85
#
# elif number_guests <= 20:
#     discount = 0.80
#
# elif number_guests > 20:
#     discount = 0.75
#
# expenses = ((number_guests * reservation_one_person) * discount) + cake_price
# total_sum = budget - expenses
#
# if total_sum >= 0:
#     print(f'It is party time! {total_sum:.2f} leva left.')
# else:
#     print(f'No party! {abs(total_sum):.2f} leva needed.')







# guest_numbers = int(input())
# price_reservation = float(input())
# budget = float(input())
#
# off_reservation = 0
#
# if guest_numbers < 10:
#     off_reservation = price_reservation
#
# elif guest_numbers <= 15:
#     off_reservation = price_reservation - (price_reservation * 0.15)
#
# elif guest_numbers <= 20:
#     off_reservation = price_reservation - (price_reservation * 0.20)
#
# elif guest_numbers > 20:
#     off_reservation = price_reservation - (price_reservation * 0.25)
#
# cake = budget - (budget * 0.90)
# total = (off_reservation * guest_numbers) + cake
# money_left = abs(budget - total)
#
# if total <= budget:
#     print(f"It is party time! {money_left:.2f} leva left.")
#
# else:
#     print(f"No party! {money_left:.2f} leva needed.")

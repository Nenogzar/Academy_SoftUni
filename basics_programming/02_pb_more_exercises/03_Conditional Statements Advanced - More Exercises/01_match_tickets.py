budget = float(input())
ticket_type = input()
people = int(input())

money_for_tickets = 0.00

transport_charges = 0.00

if 0 < people <= 4:
    transport_charges = budget * 0.75
elif people <= 9:
    transport_charges = budget * 0.60
elif people <= 24:
    transport_charges = budget * 0.50
elif people <= 49:
    transport_charges = budget * 0.40
elif people > 49:
    transport_charges = budget * 0.25


if ticket_type == "VIP":
    money_for_tickets = people * 499.99
elif ticket_type == "Normal":
    money_for_tickets = people * 249.99

money_difference = budget - transport_charges - money_for_tickets

if money_difference > 0:
    print(f"Yes! You have {abs(money_difference):.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(money_difference):.2f} leva.")

# budget = float(input())
# category = input()
# people_count = float(input())
#
# trip_info = {
#     1: 0.75,
#     5: 0.60,
#     10: 0.50,
#     25: 0.40,
#     50: 0.25,
#     "VIP": 499.99,
#     "Normal": 249.99
# }
#
# if 1 <= people_count <= 4:
#     transport_cost = budget - (trip_info[1] * budget)
#     total_tickets_cost = (trip_info[category]) * people_count
# elif people_count <= 9:
#     transport_cost = budget - (trip_info[5] * budget)
#     total_tickets_cost = (trip_info[category]) * people_count
# elif people_count <= 24:
#     transport_cost = budget - (trip_info[10] * budget)
#     total_tickets_cost = (trip_info[category]) * people_count
# elif people_count <= 49:
#     transport_cost = budget - (trip_info[25] * budget)
#     total_tickets_cost = (trip_info[category]) * people_count
# elif people_count > 50:
#     transport_cost = budget - (trip_info[50] * budget)
#     total_tickets_cost = (trip_info[category]) * people_count
#
# total = abs(total_tickets_cost - transport_cost)
# if transport_cost >= total_tickets_cost:
#     print(f"Yes! You have {total:.2f} leva left.")
# else:
#     print(f"Not enough money! You need {total:.2f} leva.")
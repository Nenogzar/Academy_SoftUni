# destination = input()
# dates = input()
# night_numbers = int(input())
#
# price = 0
#
# if destination == 'France':
#
#     if dates == '21-23':
#         price = 30
#
#     elif dates == '24-27':
#         price = 35
#
#     elif dates == '28-31':
#         price = 40
#
# elif destination == 'Italy':
#
#     if dates == '21-23':
#         price = 28
#
#     elif dates == '24-27':
#         price = 32
#
#     elif dates == '28-31':
#         price = 39
#
# elif destination == 'Germany':
#
#     if dates == '21-23':
#         price = 32
#
#     elif dates == '24-27':
#         price = 37
#
#     elif dates == '28-31':
#         price = 43
#
# total_price = price * night_numbers
#
# print(f'Easter trip to {destination} : {total_price:.2f} leva.')


""" Dictionaries """


# holiday_destination = input()
# dates_for_reservation = input()
# number_sleep_over = int(input())
#
# holiday_info = {
#     "21-23": {
#         "France": 30,
#         "Italy": 28,
#         "Germany": 32},
#     "24-27": {
#         "France": 35,
#         "Italy": 32,
#         "Germany": 37},
#     "28-31": {
#         "France": 40,
#         "Italy": 39,
#         "Germany": 43},
#
# }
#
# total = holiday_info[dates_for_reservation][holiday_destination] * number_sleep_over
#
# print(f"Easter trip to {holiday_destination} : {total:.2f} leva.")


""" OR """
holiday_destination = input()
dates_for_reservation = input()
number_sleep_over = int(input())

holiday_info = {
    "France":{"21-23":30,
              "24-27": 35,
              "28-31": 40},
    "Italy": {"21-23":28,
              "24-27": 32,
              "28-31": 39},
    "Germany": {"21-23":32,
              "24-27": 37,
              "28-31": 43}
    }
if holiday_destination in holiday_info and dates_for_reservation in holiday_info[holiday_destination]:
    price = holiday_info[holiday_destination][dates_for_reservation]
    total = price * number_sleep_over


print(f"Easter trip to {holiday_destination} : {total:.2f} leva.")
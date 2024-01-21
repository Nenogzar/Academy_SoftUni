n = int(input())            # брой километри
period_of_time = input()    # “day” или “night”

taxi_start = 0.7            # day = 0.79  night = 0.90
taxi_day = 0.79
taxi_night = 0.90

bus_start = 0.09            # >= 20 km
train = 0.06                # >= 100 km
bill = 0

if n >= 100:
    bill = n * train
    print(f"{bill:.2f}")

elif n >= 20:
    bill = n * bus_start
    print(f"{bill:.2f}")

elif n > 0:
    if period_of_time == "day":
        bill = n * taxi_day + taxi_start
        print(f"{bill:.2f}")
    elif period_of_time == "night":
        bill = n * taxi_night + taxi_start
        print(f"{bill:.2f}")
    else:
        print("error")
else:
    print("error")



# distance_km = int(input())
# day_or_night = input().lower()
#
# if distance_km < 20:
#     if day_or_night == "day":
#         taxi_price = 0.79
#         price = 0.7 + distance_km * taxi_price
#         print(f"{price:.2f}")
#
#     elif day_or_night == "night":
#         taxi_price = 0.9
#         price = 0.7 + distance_km * taxi_price
#         print(f"{price:.2f}")
#
# elif 20 <= distance_km < 100:
#     price = distance_km * 0.09
#     print(f"{price:.2f}")
# else:
#     price = distance_km * 0.06
#     print(f"{price:.2f}")





# n = int(input())  # брой километри
# day_or_night = input()  # day or night
# total = 0
#
# if n < 20:
#     if day_or_night == "day":
#         total = 0.70 + n * 0.79
#     else:
#         total = 0.70 + n * 0.90
#
# elif n < 100:
#     total = n * 0.09
#
# elif n >= 100:
#     total = n * 0.06
#
# print(f"{total:.2f}")







#
# numbers_of_kilometers = int(input())
# day_type = input()
#
# taxi_inicial = 0.70
# taxi_day_tariff = 0.79
# taxi_night_tariff = 0.90
# bus_tax = 0.09
# train = 0.06
# total = 0
#
# if numbers_of_kilometers < 20:
#     if day_type == "day":
#         total = taxi_inicial + numbers_of_kilometers * taxi_day_tariff
#     else:
#         total = taxi_inicial + numbers_of_kilometers * taxi_night_tariff
# elif numbers_of_kilometers < 100:
#     total = numbers_of_kilometers * bus_tax
# elif numbers_of_kilometers >= 100:
#     total = numbers_of_kilometers * train
#
# print(f"{total:.2f}")

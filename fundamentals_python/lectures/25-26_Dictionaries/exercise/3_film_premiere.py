# movie_name = input()
# movie_extra = input()
# movie_tickets = int(input())
#
# extras = 0
# off = 0
# total = 0
#
# if movie_name == "John Wick":
#
#     if movie_extra == "Drink":
#         extras += 12
#
#     elif movie_extra == "Popcorn":
#         extras += 15
#
#     elif movie_extra == "Menu":
#         extras += 19
#
# elif movie_name == "Star Wars":
#
#     if movie_extra == "Drink":
#         extras += 18
#
#     elif movie_extra == "Popcorn":
#         extras += 25
#
#     elif movie_extra == "Menu":
#         extras += 30
#
# elif movie_name == "Jumanji":
#
#     if movie_extra == "Drink":
#         extras += 9
#
#     elif movie_extra == "Popcorn":
#         extras += 11
#
#     elif movie_extra == "Menu":
#         extras += 14
#
# total = extras * movie_tickets
# if movie_tickets >= 4 and movie_name == "Star Wars":
#     total = total - (total * 0.30)
#
# elif movie_tickets == 2 and movie_name == "Jumanji":
#     total = total - (total * 0.15)
#
# print(f"Your bill is {total:.2f} leva.")


""" Dictionary """

movie_name = input()
movie_extra = input()
movie_tickets = int(input())

movie_info = {
    "John Wick":
        {"Drink": 12,
         "Popcorn": 15,
         "Menu": 19},
    "Star Wars":
        {"Drink": 18,
         "Popcorn": 25,
         "Menu": 30},
    "Jumanji":
        {"Drink": 9,
         "Popcorn": 11,
         "Menu": 14}
}



# for movie, extras in movie_info.items():
#     for extra, price in extras.items():
#         if movie_name == movie and extra == movie_extra:
#             total += price * movie_tickets

if movie_name in movie_info and movie_extra in movie_info[movie_name]:
    price = movie_info[movie_name][movie_extra]
    total = price * movie_tickets
else:
    total = 0.00

if movie_tickets >= 4 and movie_name == "Star Wars":
    total *= 0.70

elif movie_tickets == 2 and movie_name == "Jumanji":
    total *= 0.85

print(f"Your bill is {total:.2f} leva.")

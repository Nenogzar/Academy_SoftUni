movie_name = input()
movie_extra = input()
movie_tickets = int(input())

movie_info = {
    "John Wick": {"Drink": 12, "Popcorn": 15, "Menu": 19},
    "Star Wars": {"Drink": 18, "Popcorn": 25, "Menu": 30},
    "Jumanji": {"Drink": 9, "Popcorn": 11, "Menu": 14}
}

if movie_extra not in movie_info.get(movie_name, {}):
    print(f"Extra not found for {movie_name = } in list. Please provide prices for Drink, Popcorn, and Menu.")
    movie_info[movie_name] = {
        "Drink": float(input("Price for Drink: ")),
        "Popcorn": float(input("Price for Popcorn: ")),
        "Menu": float(input("Price for Menu: "))
    }

if movie_name in movie_info and movie_extra in movie_info[movie_name]:
    price = movie_info[movie_name][movie_extra]
    total = price * movie_tickets

if movie_tickets >= 4 and movie_name == "Star Wars":
    total *= 0.70

elif movie_tickets == 2 and movie_name == "Jumanji":
    total *= 0.85

print(f"Your bill is {total:.2f} leva.")

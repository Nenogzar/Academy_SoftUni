movie_budget = float(input())
movie_destination = input()
season = input()
number_days = int(input())

price = 0
money_left = 0

if "Dubai" == movie_destination and season == "Winter":
    price += 45_000

elif "Dubai" == movie_destination and season == "Summer":
    price += 40_000

elif "Sofia" == movie_destination and season == "Summer":
    price += 12_500

elif "Sofia" == movie_destination and season == "Winter":
    price += 17_000

elif "London" == movie_destination and season == "Winter":
    price += 24_000

elif "London" == movie_destination and season == "Summer":
    price += 20_250

if "Dubai" == movie_destination:
    price = price - (price * 0.30)

elif "Sofia" == movie_destination:
    price = price + (price * 0.25)

total = price * number_days
money_left = movie_budget - total
if movie_budget >= total:
    print(f"The budget for the movie is enough! We have {money_left:.2f} leva left!")

else:
    print(f"The director needs {abs(money_left):.2f} leva more!")


#################################################################

movie_budget = float(input())
movie_destination = input()
season = input()
number_days = int(input())

destination_season = {
    "Dubai": {
        "season": {"Winter": 45000, "Summer": 40000},
        "discount": 0.30
    },
    "Sofia": {
        "season": {"Winter": 17000, "Summer": 12500},
        "discount": 0.25
    },
    "London": {
        "season": {"Winter": 24000, "Summer": 20250},
        "discount": 0  # No discount
    }
}


if movie_destination in destination_season and season in destination_season[movie_destination]["season"]:
    price = destination_season[movie_destination]["season"][season]
    discount = destination_season[movie_destination]["discount"]

    if discount< 1:
        price *= (1 - discount)

    total_cost = price * number_days
    money_left = movie_budget - total_cost

    if money_left >= 0:
        print(f"The budget for the movie is enough! We have {money_left:.2f} leva left!")
    else:
        print(f"The director needs {abs(money_left):.2f} leva more!")
else:
    print("Invalid destination or season input.")


#########################################################################

movie_budget = float(input())
movie_destination = input()
season = input()
number_days = int(input())

destination_season = {
    "Dubai": {
        "season": {"Winter": 45000,
                   "Summer": 40000},
        "discount": 0.30
    },
    "Sofia": {
        "season": {"Winter": 17000,
                   "Summer": 12500},
        "discount": 0.25
    },
    "London": {
        "season": {"Winter": 24000,
                   "Summer": 20250},
        "discount": 0
    }
}

price = destination_season[movie_destination]['season'][season]
discount = destination_season[movie_destination]['discount']

if discount < 1:
    price *= (1 - discount)

total_cost = price * number_days
money_left = movie_budget - total_cost

if money_left >= 0:
    print(f"The budget for the movie is enough! We have {money_left:.2f} leva left!")
else:
    print(f"The director needs {abs(money_left):.2f} leva more!")

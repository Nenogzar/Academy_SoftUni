country = input()
apparatus = input()

difficulty = 0
turn = 0

if apparatus == "ribbon":
    if country == "Russia":
        difficulty = 9.100
        turn = 9.400
    elif country == "Bulgaria":
        difficulty = 9.600
        turn = 9.400
    elif country == "Italy":
        difficulty = 9.200
        turn = 9.500

elif apparatus == "hoop":
    if country == "Russia":
        difficulty = 9.300
        turn = 9.800
    elif country == "Bulgaria":
        difficulty = 9.550
        turn = 9.750
    elif country == "Italy":
        difficulty = 9.450
        turn = 9.350

elif apparatus == "rope":
    if country == "Russia":
        difficulty = 9.600
        turn = 9.000
    elif country == "Bulgaria":
        difficulty = 9.500
        turn = 9.400
    elif country == "Italy":
        difficulty = 9.700
        turn = 9.150

total_score = difficulty + turn
difference_to_max_score = 20 - total_score

print(f"The team of {country} get {total_score:.3f} on {apparatus}.")
print(f"{(difference_to_max_score / 20) * 100:.2f}%")

""" dictionary """

country = input()
apparatus = input()

difficulty = 0
turn = 0

appliance_dict = {
    "Russia": {
        "ribbon": {"difficulty": 9.100, "turn": 9.400},
        "hoop": {"difficulty": 9.300, "turn": 9.800},
        "rope": {"difficulty": 9.600, "turn": 9.000}
    },
    "Bulgaria": {
        "ribbon": {"difficulty": 9.600, "turn": 9.400},
        "hoop": {"difficulty": 9.550, "turn": 9.750},
        "rope": {"difficulty": 9.500, "turn": 9.400}
    },
    "Italy": {
        "ribbon": {"difficulty": 9.200, "turn": 9.500},
        "hoop": {"difficulty": 9.450, "turn": 9.350},
        "rope": {"difficulty": 9.700, "turn": 9.150}
    }
}

if country not in appliance_dict:
    appliance_dict[country] = {}
    appliance_dict[country][apparatus] = {}
    appliance_dict[country][apparatus]["difficulty"] = float(input("Please enter the difficulty: "))
    appliance_dict[country][apparatus]["turn"] = float(input("Please enter the turn: "))

if country in appliance_dict and apparatus in appliance_dict[country]:
    difficulty = appliance_dict[country][apparatus]["difficulty"]
    turn = appliance_dict[country][apparatus]["turn"]

total_score = difficulty + turn
difference_to_max_score = 20 - total_score

print(f"The team of {country} get {total_score:.3f} on {apparatus}.")
print(f"{(difference_to_max_score / 20) * 100:.2f}%")

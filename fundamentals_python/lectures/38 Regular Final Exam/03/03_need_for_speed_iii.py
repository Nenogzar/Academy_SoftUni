number_of_cars = int(input())
cars = {}

for car in range(number_of_cars):
    info_car = input().split("|")
    brand, mileage, fuel = info_car[0], info_car[1], info_car[2]
    if brand in cars:
        cars[brand]['mileage'] = int(mileage)
        cars[brand]['fuel'] = int(fuel)
    else:
        cars[brand] = {
            'mileage': int(mileage),
            'fuel': int(fuel)
        }
commands = input()

while commands !='Stop':
    commands_split = commands.split(" : ")
    action, brand = commands_split[0], commands_split[1]
    if action == "Drive":
        distance, fuel = int(commands_split[2]), int(commands_split[3])
        if cars[brand]['fuel'] - fuel <= 0:
            print("Not enough fuel to make that ride")
        else:
            cars[brand]['mileage'] += distance
            cars[brand]['fuel'] -= fuel
            print(f"{brand} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars[brand]['mileage'] >= 100000:
            del cars[brand]
            print(f"Time to sell the {brand}!")

    elif action == "Refuel":
        fuel = int(commands_split[2])
        max_fuel_tank = 75
        if fuel + cars[brand]['fuel'] >= max_fuel_tank:
            needet_fuel = 75 - cars[brand]['fuel']
            cars[brand]['fuel'] = 75
            print(f"{brand} refueled with {needet_fuel} liters")
        else:
            cars[brand]['fuel'] += fuel
            print(f"{brand} refueled with {fuel} liters")

    elif action == "Revert":
        kilometers = int(commands_split[2])
        min_mileage = 10000
        if cars[brand]['mileage'] - kilometers >= min_mileage:
            cars[brand]['mileage'] -= kilometers
            print(f"{brand} mileage decreased by {kilometers} kilometers")
        else :
            cars[brand]['mileage'] = min_mileage

    commands = input()

for car, details in cars.items():
    print(f"{car} -> Mileage: {details['mileage']} kms, Fuel in the tank: {details['fuel']} lt.")

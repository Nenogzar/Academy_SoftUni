# def drive_action(car, distance, fuel, racing_car):
#     if racing_car[car]['fuel'] < fuel:
#         print("Not enough fuel to make that ride")
#     else:
#         consumed_fuel = min(fuel, racing_car[car]['fuel'])
#         racing_car[car]['mileage'] += distance
#         racing_car[car]['fuel'] -= consumed_fuel
#         print(f"{car} driven for {distance} kilometers. {consumed_fuel} liters of fuel consumed.")
#         if racing_car[car]['mileage'] >= 100000:
#             print(f"Time to sell the {car}!")
#             del racing_car[car]
#
#
# def refuel_car(car, fuel, racing_car):
#     max_fuel_tank = 75
#     if racing_car[car]['fuel'] + fuel >= max_fuel_tank:
#         needet_fuel = max_fuel_tank - racing_car[car]['fuel']
#         racing_car[car]['fuel'] = max_fuel_tank
#         print(f"{car} refueled with {needet_fuel} liters")
#     else:
#         racing_car[car]['fuel'] += fuel
#         print(f"{car} refueled with {fuel} liters")
#
#
# def revert_car(car, kilometers, racing_car):
#     min_mileage = 10000
#     if racing_car[car]['mileage'] - kilometers >= min_mileage:
#         racing_car[car]['mileage'] -= kilometers
#         print(f"{car} mileage decreased by {kilometers} kilometers")
#     else:
#         racing_car[car]['mileage'] = min_mileage
#
#
#
# racing_car = {}
# number_of_cars = int(input())
# for cars in range(number_of_cars):
#     info_cars = input().split("|")
#     car, mileage, fuel = info_cars[0], int(info_cars[1]), int(info_cars[2])
#     racing_car[car] = {
#         'mileage': mileage,
#         'fuel': fuel
#     }
#
# manipulations = input()
# while manipulations != "Stop":
#     action, car = manipulations.split(" : ")[0], manipulations.split(" : ")[1]
#     if action == "Drive":
#         distance, fuel = map(int, manipulations.split(" : ")[2:])
#         drive_action(car, distance, fuel, racing_car)
#     elif action == "Refuel":
#         fuel = int(manipulations.split(" : ")[2])
#         refuel_car(car, fuel, racing_car)
#     elif action == "Revert":
#         kilometers = int(manipulations.split(" : ")[2])
#         revert_car(car, kilometers, racing_car)
#
#     manipulations = input()
#
# for car, details in racing_car.items():
#         print(f"{car} -> Mileage: {details['mileage']} kms, Fuel in the tank: {details['fuel']} lt.")


""" defaultdict """
from collections import defaultdict

def drive_action(car, distance, fuel, racing_car):
    if racing_car[car]['fuel'] < fuel:
        print("Not enough fuel to make that ride")
    else:
        consumed_fuel = min(fuel, racing_car[car]['fuel'])
        racing_car[car]['mileage'] += distance
        racing_car[car]['fuel'] -= consumed_fuel
        print(f"{car} driven for {distance} kilometers. {consumed_fuel} liters of fuel consumed.")
        if racing_car[car]['mileage'] >= 100000:
            print(f"Time to sell the {car}!")
            del racing_car[car]

def refuel_car(car, fuel, racing_car):
    max_fuel_tank = 75
    if racing_car[car]['fuel'] + fuel >= max_fuel_tank:
        needet_fuel = max_fuel_tank - racing_car[car]['fuel']
        racing_car[car]['fuel'] = max_fuel_tank
        print(f"{car} refueled with {needet_fuel} liters")
    else:
        racing_car[car]['fuel'] += fuel
        print(f"{car} refueled with {fuel} liters")

def revert_car(car, kilometers, racing_car):
    min_mileage = 10000
    if racing_car[car]['mileage'] - kilometers >= min_mileage:
        racing_car[car]['mileage'] -= kilometers
        print(f"{car} mileage decreased by {kilometers} kilometers")
    else:
        racing_car[car]['mileage'] = min_mileage

racing_car = defaultdict(lambda: {'mileage': 0, 'fuel': 0})
number_of_cars = int(input())
for _ in range(number_of_cars):
    info_cars = input().split("|")
    car, mileage, fuel = info_cars[0], int(info_cars[1]), int(info_cars[2])
    racing_car[car] = {'mileage': mileage, 'fuel': fuel}

manipulations = input()
while manipulations != "Stop":
    action, car = manipulations.split(" : ")[0], manipulations.split(" : ")[1]
    if action == "Drive":
        distance, fuel = map(int, manipulations.split(" : ")[2:])
        drive_action(car, distance, fuel, racing_car)
    elif action == "Refuel":
        fuel = int(manipulations.split(" : ")[2])
        refuel_car(car, fuel, racing_car)
    elif action == "Revert":
        kilometers = int(manipulations.split(" : ")[2])
        revert_car(car, kilometers, racing_car)

    manipulations = input()

for car, details in racing_car.items():
    print(f"{car} -> Mileage: {details['mileage']} kms, Fuel in the tank: {details['fuel']} lt.")

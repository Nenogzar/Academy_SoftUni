from project import controller
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race
from project.controller import Controller

# print("SportsCar")
# try:
#     carSport = SportsCar("Opel", 500)
#     print(carSport.model, "model")
#     print(carSport.min_speed_limit(), "min")
#     print(carSport.max_speed_limit(), "max")
#     print(carSport.speed_limit, "speed_limit")
# except ValueError as e:
#     print(e)
# print("----------------")
# print("MuscleCar")
# try:
#     carMuscle = MuscleCar("Mustang", 350)
#     print(carMuscle.model, "model")
#     print(carMuscle.min_speed_limit(), "min")
#     print(carMuscle.max_speed_limit(), "max")
#     print(carMuscle.speed_limit, "speed_limit")
#
# except ValueError as e:
#     print(e)
# print("----------------")
# print("Driver")
# try:
#     driver = Driver("Ivan")
#     print(driver.name, "name")
#     print(driver.car, "car")
#     print(driver.number_of_wins, "number_of_wins")
#
# except ValueError as e:
#     print(e)
# print("----------------")
# print("Race")
# try:
#     raceName = Race("Ivan")
#     print(raceName.name, "name")
#     print(raceName.drivers, "drivers")
#
# except ValueError as e:
#     print(e)
# print("----------------")
#
# print("create_car")
#
#
# def test_create_car():
#     controller = Controller()
#
#     # Test case 1: Creating a MuscleCar
#     try:
#         result = controller.create_car("MuscleCar", "Mustang", 300)
#         print(result)  # Expected: "MuscleCar Mustang is created."
#     except Exception as e:
#         print(e)
#
#     # Test case 2: Creating another MuscleCar with different model
#     try:
#         result = controller.create_car("MuscleCar", "Challenger", 320)
#         print(result)  # Expected: "MuscleCar Challenger is created."
#     except Exception as e:
#         print(e)
#
#     # Test case 3: Attempting to create a MuscleCar with an existing model
#     try:
#         result = controller.create_car("MuscleCar", "Mustang", 350)
#         print(result)
#     except Exception as e:
#         print(e)  # Expected: "Car Mustang is already created!"
#
#     # Test case 4: Creating a SportsCar
#     try:
#         result = controller.create_car("SportsCar", "Ferrari", 500)
#         print(result)  # Expected: "SportsCar Ferrari is created."
#     except Exception as e:
#         print(e)
#
#     # Test case 5: Invalid car type
#     try:
#         result = controller.create_car("Truck", "BigTruck", 200)
#         print(result)  # Expected: No output, as "Truck" is not a valid car type
#     except Exception as e:
#         print(e)
#
#     # Print all created cars
#     for car in controller.cars:
#         print(f"Car model: {car.model}, Car speed limit: {car.speed_limit}")
#
#
# # Run the test function
# test_create_car()
#
# print("----------------")
#
#
# # Validation class
# class Validation:
#     @staticmethod
#     def valid_model(model: str, message: str):
#         if len(model) < 4:
#             raise ValueError(message)
#
#     @staticmethod
#     def valid_speed(valid_speed: int, min_speed: int, max_speed: int, message: str):
#         if valid_speed not in range(min_speed, max_speed + 1):
#             raise ValueError(message)
#
#     @staticmethod
#     def valid_driver_name(name: str, message: str):
#         if not name or name.isspace():
#             raise ValueError(message)
#
# print("----------------")
#
# print("create_driver")
#
# # Test function
# def test_create_driver():
#     controller = Controller()
#
#     # Test case 1: Creating a new driver
#     try:
#         result = controller.create_driver("John")
#         print(result)  # Expected: "Driver John is created."
#     except Exception as e:
#         print(e)
#
#     # Test case 2: Creating another new driver
#     try:
#         result = controller.create_driver("Alice")
#         print(result)  # Expected: "Driver Alice is created."
#     except Exception as e:
#         print(e)
#
#     # Test case 3: Attempting to create a driver with an existing name
#     try:
#         result = controller.create_driver("John")
#         print(result)
#     except Exception as e:
#         print(e)  # Expected: "Driver John is already created!"
#
#     # Test case 4: Creating a driver with an empty name (invalid)
#     try:
#         result = controller.create_driver("")
#         print(result)
#     except Exception as e:
#         print(e)  # Expected: "Name should contain at least one character!"
#
#     # Print all created drivers
#     for driver in controller.drivers:
#         print(f"Driver name: {driver.name}, Number of wins: {driver.number_of_wins}")
#
# # Run the test function
# test_create_driver()
#
#
# print("----------------")
#
# print("create_race")
#
# def test_create_race():
#     controller = Controller()
#
#     # Test case 1: Creating a new race
#     try:
#         result = controller.create_race("Desert Rally")
#         print(result)  # Expected: "Race Desert Rally is created."
#     except Exception as e:
#         print(e)
#
#     # Test case 2: Creating another new race
#     try:
#         result = controller.create_race("Mountain Challenge")
#         print(result)  # Expected: "Race Mountain Challenge is created."
#     except Exception as e:
#         print(e)
#
#     # Test case 3: Attempting to create a race with an existing name
#     try:
#         result = controller.create_race("Desert Rally")
#         print(result)
#     except Exception as e:
#         print(e)  # Expected: "Race Desert Rally is already created!"
#
#     try:
#         result = controller.create_race("")
#         print(result)
#     except Exception as e:
#         print(e)  # Expected: "empty string"
#
#
#     # Print all created races
#     for race in controller.races:
#         print(f"Race name: {race.name}, Drivers: {race.drivers}")
#
# # Run the test function
# test_create_race()
#
#
# ###################################################
# print("----------------")
# print("add_car_to_driver")
# def test_add_car_to_driver():
#     controller = Controller()
#
#     # Създаване на тестови данни
#     controller.create_car("MuscleCar", "Mustang", 300)
#     controller.create_car("MuscleCar", "Camaro", 320)
#     controller.create_driver("John")
#     controller.create_driver("Alice")
#
#     # Присвояване на автомобил на шофьор
#     try:
#         result = controller.add_car_to_driver("John", "MuscleCar")
#         print(result)  # Очаквано: "Driver John chose the car Camaro."
#     except Exception as e:
#         print(e)
#
#     # Опит за присвояване на автомобил на шофьор, който вече има автомобил
#     try:
#         result = controller.add_car_to_driver("John", "MuscleCar")
#         print(result)  # Очаквано: "Driver John changed his car from Camaro to Mustang."
#     except Exception as e:
#         print(e)
#
#     # Опит за присвояване на автомобил на не съществуващ шофьор
#     try:
#         result = controller.add_car_to_driver("NonExistentDriver", "MuscleCar")
#         print(result)
#     except Exception as e:
#         print(e)  # Очаквано: "Driver NonExistentDriver could not be found!"
#
#     # Опит за присвояване на не съществуващ автомобил
#     try:
#         result = controller.add_car_to_driver("Alice", "SportsCar")
#         print(result)
#     except Exception as e:
#         print(e)  # Очаквано: "Car SportsCar could not be found!"
#
# # Run the test function
# test_add_car_to_driver()
#
# ###################################################
# print("----------------")
# print("add_driver_to_race")
#
# def test_add_driver_to_race():
#     controller = Controller()
#
#     # Създаване на тестови данни
#     controller.create_car("MuscleCar", "Mustang", 300)
#     controller.create_driver("John")
#     controller.create_race("Race1")
#
#     # Присвояване на автомобил на шофьор
#     controller.add_car_to_driver("John", "MuscleCar")
#
#     # Добавяне на шофьор към състезание
#     try:
#         result = controller.add_driver_to_race("Race1", "John")
#         print(result)  # Очаквано: "Driver John added in Race1 race."
#     except Exception as e:
#         print(e)
#
#     # Опит за добавяне на шофьор, който вече е добавен
#     try:
#         result = controller.add_driver_to_race("Race1", "John")
#         print(result)  # Очаквано: "Driver John is already added in Race1 race."
#     except Exception as e:
#         print(e)
#
#     # Опит за добавяне на шофьор без автомобил
#     controller.create_driver("Alice")
#     try:
#         result = controller.add_driver_to_race("Race1", "Alice")
#         print(result)
#     except Exception as e:
#         print(e)  # Очаквано: "Driver Alice could not participate in the race!"
#
#     # Опит за добавяне на шофьор в несъществуващо състезание
#     try:
#         result = controller.add_driver_to_race("NonExistentRace", "John")
#         print(result)
#     except Exception as e:
#         print(e)  # Очаквано: "Race NonExistentRace could not be found!"
#
#     # Опит за добавяне на несъществуващ шофьор в състезание
#     try:
#         result = controller.add_driver_to_race("Race1", "NonExistentDriver")
#         print(result)
#     except Exception as e:
#         print(e)  # Очаквано: "Driver NonExistentDriver could not be found!"
#
# # Run the test function
# test_add_driver_to_race()

control = Controller()
print(control.create_driver("Peter"))
print(control.create_car("SportsCar", "Porsche 718 Boxster", 470))
print(control.add_car_to_driver("Peter", "SportsCar"))
print(control.create_car("SportsCar", "Porsche 911", 580))
print(control.add_car_to_driver("Peter", "SportsCar"))
print(control.create_car("MuscleCar", "BMW ALPINA B7", 290))
print(control.create_car("MuscleCar", "Mercedes-Benz AMG GLA 45", 420))
print(control.create_driver("John"))
print(control.create_driver("Jack"))
print(control.create_driver("Kelly"))
print(control.add_car_to_driver("Kelly", "MuscleCar"))
print(control.add_car_to_driver("Jack", "MuscleCar"))
print(control.add_car_to_driver("John", "SportsCar"))
print(control.create_race("Christmas Top Racers"))
print(control.add_driver_to_race("Christmas Top Racers", "John"))
print(control.add_driver_to_race("Christmas Top Racers", "Jack"))
print(control.add_driver_to_race("Christmas Top Racers", "Kelly"))
print(control.add_driver_to_race("Christmas Top Racers", "Peter"))
print(control.start_race("Christmas Top Racers"))
[print(d.name, d.number_of_wins) for d in control.drivers]

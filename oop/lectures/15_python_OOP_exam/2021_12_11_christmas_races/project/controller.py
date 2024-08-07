from typing import List

from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars: List[Car] = []
        self.drivers: List[Driver] = []
        self.races: List[Race] = []

    @property
    def car_type(self):
        return {
            "MuscleCar": MuscleCar,
            "SportsCar": SportsCar
        }

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type in self.car_type:
            for c in self.cars:
                if c.model == model:
                    raise Exception(f"Car {model} is already created!")

            car_class = self.car_type[car_type]
            car = car_class(model, speed_limit)
            self.cars.append(car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        for d in self.drivers:
            if d.name == driver_name:
                raise Exception(f"Driver {driver_name} is already created!")

        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        for r in self.races:
            if r.name == race_name:
                raise Exception(f"Race {race_name} is already created!")

        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        # Проверка дали шофьорът съществува
        driver = next((d for d in self.drivers if d.name == driver_name), None)
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        # Намиране на последния добавен автомобил от желания тип, който не е зает
        available_car = None
        for car in reversed(self.cars):
            if type(car).__name__ == car_type and not car.is_taken:
                available_car = car
                break

        if available_car is None:
            raise Exception(f"Car {car_type} could not be found!")

        # Ако шофьорът вече има автомобил, сменяме го с новия
        if driver.car:
            old_car = driver.car
            old_car.is_taken = False  # Освобождаваме стария автомобил
            driver.car = available_car
            available_car.is_taken = True
            return f"Driver {driver_name} changed his car from {old_car.model} to {available_car.model}."

        # Ако шофьорът няма автомобил, присвояваме новия автомобил
        driver.car = available_car
        available_car.is_taken = True
        return f"Driver {driver_name} chose the car {available_car.model}."


    def add_driver_to_race(self, race_name: str, driver_name: str):
        # Проверка дали състезанието съществува
        race = next((r for r in self.races if r.name == race_name), None)
        if race is None:
            raise Exception(f"Race {race_name} could not be found!")

        # Проверка дали шофьорът съществува
        driver = next((d for d in self.drivers if d.name == driver_name), None)
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        # Проверка дали шофьорът има автомобил
        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        # Проверка дали шофьорът вече е добавен към състезанието
        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        # Добавяне на шофьора към състезанието
        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."


    def start_race(self, race_name: str):
        race = next((r for r in self.races if r.name == race_name), None)
        if race is None:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        # Сортиране на участниците по скорост в низходящ ред и избор на първите трима
        sorted_drivers = sorted(race.drivers, key=lambda d: d.car.speed_limit, reverse=True)[:3]

        result = []
        for driver in sorted_drivers:
            driver.number_of_wins += 1
            result.append(f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.")

        return "\n".join(result)

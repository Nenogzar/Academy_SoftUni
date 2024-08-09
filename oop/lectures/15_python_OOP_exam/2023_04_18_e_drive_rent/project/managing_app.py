from typing import List

from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    def __init__(self):
        self.users: List[User] = []  # contain all users (objects) that are created.
        self.vehicles: List[BaseVehicle] = []  # contain all vehicles (objects) that are created.
        self.routes: List[Route] = []  # contain all routes (objects) that are created.

    @property
    def valid_vehicle_type(self):
        return {"PassengerCar": PassengerCar,
                "CargoVan": CargoVan}

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        existing_driving_license_number = next(
            (f for f in self.users if f.driving_license_number == driving_license_number), None)
        if existing_driving_license_number:
            return f"{driving_license_number} has already been registered to our platform."

        new_user = User(first_name, last_name, driving_license_number)
        self.users.append(new_user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):

        if vehicle_type not in self.valid_vehicle_type:
            return f"Vehicle type {vehicle_type} is inaccessible."

        exist_license = next((l for l in self.vehicles if l.license_plate_number == license_plate_number), None)
        if exist_license:
            return f"{license_plate_number} belongs to another vehicle."

        new_vehicle = self.valid_vehicle_type[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(new_vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        route = next((r for r in self.routes if r.start_point == start_point and r.end_point == end_point), None)
        if route:
            if route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            elif route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            else:
                route.is_locked = True
        new_route = Route(start_point, end_point, length, len(self.routes) + 1)
        self.routes.append(new_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,
                  is_accident_happened: bool):
        user = next(
            (u for u in self.users if
             u.driving_license_number == driving_license_number and
             u.is_blocked == False), None)

        if user == None:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        vehicle = next(
            (v for v in self.vehicles if
             v.license_plate_number == license_plate_number and
             v.is_damaged == False), None)

        if vehicle == None:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        route = next((r for r in self.routes if r.route_id == route_id and r.is_locked == False), None)

        if route == None:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)
        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count: int):
        damaged_vehicles = [v for v in self.vehicles if v.is_damaged]

        damaged_vehicles.sort(key=lambda v: (v.brand, v.model))

        # vehicles_to_repair = damaged_vehicles[:count] if count > 0 else damaged_vehicles # TODO ако ти подадът 0
        vehicles_to_repair = damaged_vehicles[:count] if count >= 0 else damaged_vehicles  # >= един вариант
        # vehicles_to_repair = damaged_vehicles[:count] # TODO може и така за по-кратко

        for vehicle in vehicles_to_repair:
            vehicle.is_damaged = False
            vehicle.recharge()


        count_of_repaired_vehicles = len(vehicles_to_repair)

        return f"{count_of_repaired_vehicles} vehicles were successfully repaired!"

    def users_report(self):
        sorted_users = sorted(self.users, key=lambda u: u.rating, reverse=True)

        report = "*** E-Drive-Rent ***\n"
        report += "\n".join(str(user) for user in sorted_users)

        return report


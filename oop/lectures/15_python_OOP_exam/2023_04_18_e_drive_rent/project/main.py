from project.managing_app import ManagingApp
from project.route import Route
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar

print("**************")
print("class - User")
try:
    u = User("Stoyan", "Naidenov", "qwer123")
    print(u.rating)
    u.increase_rating()
    print(u.rating)     # 0.00
    u.increase_rating()
    print(u.rating)     # 0.05
    u.increase_rating()
    print(u.rating)     # 1.00
    u.decrease_rating()
    print(u.rating)     # 1.5
    u.decrease_rating()
    print(u.rating)     #
    u.decrease_rating()
    print(u.rating)
except ValueError as e:
    print(e)

print("**************")
print("class - PassengerCar")

try:
    p = PassengerCar("Renaut", "Megan", "asd45682ad")
    print(p.max_mileage)
    print(p.battery_level)
    p.drive(445)
    print(p.battery_level)
    p.recharge()
    print(p.battery_level)
    print(p.is_damaged)
    p.change_status()
    print(p.is_damaged)
    p.change_status()
    print(p.is_damaged)
    print(p)

except ValueError as a:
    print(a)

print("**************")
print("class - CargoVan")

try:
    p = CargoVan("BMV", "5000", "asd45682ad")
    print(p.max_mileage)
    print(p.battery_level)
    p.drive(170)
    print(p.battery_level)
    p.recharge()
    print(p.battery_level)
    print(p.is_damaged)
    p.change_status()
    print(p.is_damaged)
    print(p)

except ValueError as e:
    print(e)



print("**************")
print("class - Route")

try:
    r = Route("Varna", "Burgas", 1, 51)


except ValueError as e:
    print(e)

print("**************")
print("class - ManagingApp ")

try:
    app = ManagingApp()
    print(app.register_user( 'Tisha', 'Reenie', '7246506' ))
    print(app.register_user( 'Bernard', 'Remy', 'CDYHVSR68661'))
    print(app.register_user( 'Mack', 'Cindi', '7246506'))
    print(app.upload_vehicle('PassengerCar', 'Chevrolet', 'Volt', 'CWP8032'))
    print(app.upload_vehicle( 'PassengerCar', 'Volkswagen', 'e-Up!', 'COUN199728'))
    print(app.upload_vehicle('PassengerCar', 'Mercedes-Benz', 'EQS', '5UNM315'))
    print(app.upload_vehicle('CargoVan', 'Ford', 'e-Transit', '726QOA'))
    print(app.upload_vehicle('CargoVan', 'BrightDrop', 'Zevo400', 'SC39690'))
    print(app.upload_vehicle('EcoTruck', 'Mercedes-Benz', 'eActros', 'SC39690'))
    print(app.upload_vehicle('PassengerCar', 'Tesla', 'CyberTruck', '726QOA'))
    print(app.allow_route('SOF', 'PLD', 144))
    print(app.allow_route('BUR', 'VAR', 87))
    print(app.allow_route('BUR', 'VAR', 87))
    print(app.allow_route('SOF', 'PLD', 184))
    print(app.allow_route('BUR', 'VAR', 86.999))
    print(app.make_trip('CDYHVSR68661', '5UNM315', 3, False))
    print(app.make_trip('7246506', 'CWP8032', 1, True))
    print(app.make_trip('7246506', 'COUN199728', 1, False))
    print(app.make_trip('CDYHVSR68661', 'CWP8032', 3, False))
    print(app.make_trip('CDYHVSR68661', '5UNM315', 2, False))
    print(app.repair_vehicles(2))
    print(app.repair_vehicles(20))
    print(app.users_report())







except ValueError as e:
    print(e)
except Exception as s:
    print(s)




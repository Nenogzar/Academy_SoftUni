from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.christmas_pastry_shop_app import ChristmasPastryShopApp
from project.delicacies.stolen import Stolen
from project.delicacies.gingerbread import Gingerbread
print("Stolen")
print("-----------------------")
try:
    d = Stolen("Red velved", 6)
    print(d.details())
except ValueError as e:
    print(e)

print("-----------------------")
print("Gingerbread")


try:
    d = Gingerbread("Medenka", 3.8)
    print(d.details())
except ValueError as e:
    print(e)

print("-----------------------")
print("OpenBooth")


try:
    b = OpenBooth(1, 6)
    print("price for person", b.price_per_person)
    b.reserve(5)
    print("reservation for 5 person", b.price_for_reservation)

except ValueError as e:
    print(e)

print("-----------------------")
print("PrivateBooth")


try:
    b = PrivateBooth(1, 5)
    print("price for person", b.price_per_person)
    b.reserve(5)
    print("reservation for 5 person", b.price_for_reservation)

except ValueError as e:
    print(e)


print("-----------------------")
print("ChristmasPastryShopApp")

shop = ChristmasPastryShopApp()
print(shop.add_delicacy("Gingerbread", "Gingy", 5.20))


print("-----------------------")

print("-----------------------")
shop = ChristmasPastryShopApp()
print(shop.add_delicacy("Gingerbread", "Gingy", 5.20))
print(shop.delicacies[0].details())
print(shop.add_booth("Open Booth", 1, 30))
print(shop.add_booth("Private Booth", 10, 5))
print(shop.reserve_booth(30))
print(shop.order_delicacy(1, "Gingy"))
print(shop.leave_booth(1))
print(shop.reserve_booth(5))
print(shop.order_delicacy(1, "Gingy"))
print(shop.order_delicacy(1, "Gingy"))
print(shop.order_delicacy(1, "Gingy"))
print(shop.leave_booth(1))
print(shop.get_income())

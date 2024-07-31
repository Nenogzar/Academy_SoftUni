from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.drink import Drink
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.bakery import Bakery
"""Cake"""
print("Cake")
try:
    pasta = Cake("Garash", 1.5)
    print(repr(pasta))
except ValueError as e:
    print(e)

print("________________________")
"""Bread"""
print("Bread")
try:
    leb = Bread("Mek leb", 5.8)
    print(repr(leb))
except ValueError as e:
    print(e)

print("________________________")
"""Tea"""
print("Tea")
try:
    tea = Tea("Black tea", 150, "Ahmad")
    print(repr(tea))
except ValueError as e:
    print(e)
print("________________________")
"""Water"""
print("Water")
try:
    water = Water("Mineral water", 220, "Bankya")
    print(repr(water))
except ValueError as e:
    print(e)

print("________________________")

"""table OutsideTable"""
print("OutsideTable")
try:
    tab = OutsideTable(51,10)
    print(repr(tab))
    print(tab.free_table_info())
except ValueError as e:
    print(e)
print("________________________")
"""InsideTable"""
print("InsideTable")
try:
    tab1 = InsideTable(3,5)
    print(repr(tab1))
    print(tab1.free_table_info())
except ValueError as e:
    print(e)
print("________________________")

tab2 = InsideTable(3,5)
tab2.reserve(4)

print(tab2.is_reserved)
print(tab2.number_of_people)
print(tab2.free_table_info())
print("_____")

tab2.clear()
print(tab2.is_reserved)
print(tab2.number_of_people)


print("________________________")
"""Bakery"""
print("Bakery")

try:
    app = Bakery("Koza")
    print(app)
    print(app.get_free_tables_info())
except ValueError as e:
    print(e)

print("________________________")

"""add_food"""
print("add_food")
try:
    mandja = Bakery("Yare")
    print(mandja.add_food("Bread", "Tipov", 2.2))
    print(mandja.add_food("Bread", "Tipov", 2.2))

except ValueError as e:
    print(e)

print("________________________")

"""add_drink"""
print("add_drink")
try:
    ahmad = Bakery("Chay")
    print(ahmad.add_drink("Water", "Rose", 200, "Mechka"))
    print(ahmad.add_drink("Tea", "Black", 200, "Ahmad"))
    print(ahmad.add_drink("Tea", "Black", 200, "Ahmad"))

except ValueError as e:
    print(e)

print("________________________")

"""add_table"""
print("add_table")
try:
    masa = Bakery("Chay")
    print(masa.add_table("InsideTable", 10, 6))
    print(masa.add_table("InsideTable", 55, 6))
    print(masa.add_table("InsideTable", 0, 6))

except ValueError as e:
    print(e)

print("________________________")

"""reserve_table"""
print("reserve_table")
try:
    app = Bakery("Dom")
    print(app.add_food("Bread", "White", 2.50))
    print(app.add_food("Bread", "Black", 2.00))
    print(app.add_drink("Water", "Mineral", 220, "Bankya"))
    print(app.add_table("InsideTable", 10, 3))
    print(app.add_table("InsideTable", 1, 4))
    print(app.add_table("InsideTable", 7, 6))
    print(app.add_drink("Water", "Rose", 200, "Mechka"))
    print(app.add_drink("Tea", "Black", 200, "Ahmad"))

    print(app.reserve_table(7))

    print(app.order_food(7,"White", "Black", "Salat"))

    print(app.order_drink(7,"Rose", "Black", "Konyak"))

    print(app.leave_table(7))
    print(app.reserve_table(5))
    print("------------")

    print(app.get_free_tables_info())

    print("*****************************")
    print(app.get_total_income())
except ValueError as e:
    print(e)



from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.drink import Drink
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.bakery import Bakery

try:
    #
    # """Cake"""
    # print("Cake")
    #
    # pasta = Cake("Garash", 1.5)
    # print(repr(pasta))
    # print("________________________")
    #
    # """Bread"""
    # print("Bread")
    #
    # leb = Bread("Mek leb", 5.8)
    # print(repr(leb))
    # print("________________________")
    #
    # """Tea"""
    # print("Tea")
    #
    # tea = Tea("Black tea", 150, "Ahmad")
    # print(repr(tea))
    # print("________________________")
    #
    # """Water"""
    # print("Water")
    #
    # water = Water("Mineral water", 220, "Bankya")
    # print(repr(water))
    # print("________________________")
    #
    # """table OutsideTable"""
    # print("OutsideTable")
    #
    # tab = OutsideTable(49, 10)
    # print(repr(tab))
    # print(tab.free_table_info())
    # print("________________________")

    # """InsideTable"""
    # print("InsideTable")
    #
    # tab1 = InsideTable(51, 5)
    # print(repr(tab1))
    # print(tab1.free_table_info())
    # print("________________________")
    #
    # tab2 = InsideTable(3, 5)
    # tab2.reserve(4)
    #
    # print(tab2.is_reserved)
    # print(tab2.number_of_people)
    # print(tab2.free_table_info())
    # print("_____")
    #
    # tab2.clear()
    # print(tab2.is_reserved)
    # print(tab2.number_of_people)
    # print("________________________")

    # """Bakery"""
    # print("Bakery")
    #
    # app1 = Bakery("Koza")
    # print(app1)
    # print(app1.get_free_tables_info())
    # print("________________________")
    #
    # """add_food"""
    # print("add_food")
    #
    # mandja = Bakery("Yare")
    # print(mandja.add_food("Bread", "Tipov", 2.2))
    # print(mandja.add_food("Bread", "Tipov", 2.2))
    # print("________________________")
    #
    # """add_drink"""
    # print("add_drink")
    #
    # ahmad = Bakery("Chay")
    # print(ahmad.add_drink("Water", "Rose", 200, "Mechka"))
    # print(ahmad.add_drink("Tea", "Black", 200, "Ahmad"))
    # print(ahmad.add_drink("Tea", "Black", 200, "Ahmad"))

    # """add_table"""
    # print("________________________")
    # print("add_table")
    # masa = Bakery("Chay")
    # print(masa.add_table("InsideTable", 10, 6))
    # print(masa.add_table("InsideTable", 55, 6))
    # print(masa.add_table("InsideTable", 0, 6))

    """Bakery"""
    print("Bakery")
    print("________________________")
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

    print(app.order_food(7,"White", "Black"))

    print(app.order_drink(7,"Rose", "Black"))

    print(app.leave_table(7))
    print(app.reserve_table(5))
    print("------------")

    print(app.get_free_tables_info())

    print("*****************************")
    print(app.get_total_income())

except ValueError as e:
    print(e)



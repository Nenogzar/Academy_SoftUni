from project.client import Client
from project.food_orders_app import FoodOrdersApp
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.starter import Starter

try:
    n = Client("0899999999")
except ValueError as e:
    print(e)

print("----------------")
print("Starter")
try:
    s = Starter("Tarator", 2.50, 25)
    print(s.details())
    print("quantity", s.quantity)
except ValueError as e:
    print(e)

print("----------------")
print("MainDish")
try:
    s = MainDish("Torlu Guvech", 9.70)
    print(s.details())
    print("quantity", s.quantity)
except ValueError as e:
    print(e)

print("----------------")
print("Dessert")
try:
    s = Dessert("Gаrash", 3.5)
    print(s.details())
    print("quantity", s.quantity)
except ValueError as e:
    print(e)

print("----------------")
print("register_client")
try:
    a = FoodOrdersApp()
    print(a.register_client("0899999999"))
    print(a.register_client("0899999999"))
except Exception as i:
    print(i)


print("----------------")
print("add_meals_to_menu")
try:
    a = FoodOrdersApp()
    print(a.register_client("0899999999"))
    hummus_and_avocado_sandwich = Starter("Hummus and Avocado Sandwich", 7.90)
    tortilla_with_beef_and_pork = MainDish("Tortilla with Beef and Pork", 12.50, 12)
    risotto_with_wild_mushrooms = MainDish("Risotto with Wild Mushrooms", 15)
    chocolate_cake_with_mascarpone = Dessert("Chocolate Cake with Mascarpone", 4.60, 17)
    chocolate_and_violets = Dessert("Chocolate and Violets", 5.20)
    a.add_meals_to_menu(hummus_and_avocado_sandwich,tortilla_with_beef_and_pork,risotto_with_wild_mushrooms,chocolate_cake_with_mascarpone,chocolate_and_violets)
    print(a.menu)
except Exception as i:
    print(i)

print("----------------")
print("show_menu")
try:
    a = FoodOrdersApp()
    print(a.register_client("0899999999"))
    hummus_and_avocado_sandwich = Starter("Hummus and Avocado Sandwich", 7.90)
    tortilla_with_beef_and_pork = MainDish("Tortilla with Beef and Pork", 12.50, 12)
    risotto_with_wild_mushrooms = MainDish("Risotto with Wild Mushrooms", 15)
    chocolate_cake_with_mascarpone = Dessert("Chocolate Cake with Mascarpone", 4.60, 17)
    chocolate_and_violets = Dessert("Chocolate and Violets", 5.20)
    no_in_menu = Dessert("No Name", 4.60, 17)
    a.add_meals_to_menu(hummus_and_avocado_sandwich,tortilla_with_beef_and_pork,risotto_with_wild_mushrooms,chocolate_cake_with_mascarpone,chocolate_and_violets)
    print(a.menu)
    print("- Menu -")
    print(a.show_menu())
    print("----------------")
    food = {"Hummus and Avocado Sandwich": 60,
        "Risotto with Wild Mushrooms": 50,
        "Chocolate and Violets": 30}
    print(a.add_meals_to_shopping_cart("0987654321", **food))


except Exception as i:
    print(i)

print("----------------")
print("test from problem")
print("----------------")

food_orders_app = FoodOrdersApp()
print(food_orders_app.register_client("0899999999"))
french_toast = Starter("French toast", 6.50, 5)
hummus_and_avocado_sandwich = Starter("Hummus and Avocado Sandwich", 7.90)
tortilla_with_beef_and_pork = MainDish("Tortilla with Beef and Pork", 12.50, 12)
risotto_with_wild_mushrooms = MainDish("Risotto with Wild Mushrooms", 15)
chocolate_cake_with_mascarpone = Dessert("Chocolate Cake with Mascarpone", 4.60, 17)
chocolate_and_violets = Dessert("Chocolate and Violets", 5.20)
print(food_orders_app.add_meals_to_menu(
    french_toast, hummus_and_avocado_sandwich,
    tortilla_with_beef_and_pork,
    risotto_with_wild_mushrooms,
    chocolate_cake_with_mascarpone,
    chocolate_and_violets))
print(food_orders_app.show_menu())
food = {"Hummus and Avocado Sandwich": 5,
        "Risotto with Wild Mushrooms": 1,
        "Chocolate and Violets": 4}
print(food_orders_app.add_meals_to_shopping_cart('0899999999', **food))
additional_food = {"Risotto with Wild Mushrooms": 2,
                   "Tortilla with Beef and Pork": 2}
print(food_orders_app.add_meals_to_shopping_cart('0899999999', **additional_food))
# print("----------------")
# print("cancel_order")
# print(food_orders_app.cancel_order("0899999999"))
# print("----------------")
print(food_orders_app.finish_order("0899999999"))
print(food_orders_app)

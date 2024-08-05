from project.player import Player
from project.supply.drink import Drink
from project.supply.food import Food

# print("-----------")
# print("Food")
# try:
#     n = Food("koko")
#     print(n.details())
# except ValueError as e:
#     print(e)
#
# print("-----------")
# print("Drink")
# try:
#     d = Drink("Water")
#     print(d.details())
# except ValueError as e:
#     print(e)
#
#
# print("-----------")
# print("Player")
# try:
#     player1 = Player("John", 15, 90)
#     print(player1)
#     player2 = Player("Jane", 14, 50)
#     print(player2)
#     player4 = Player("Jan", 13, -15)  # Stamina not valid!
#     print(player4)
#     player3 = Player("Jane", 13, -1)    # Name Jane is already used!n
#     print(player3)
#
# except Exception as e:
#     print(e)

from project.controller import Controller
from project.player import Player
from project.supply.drink import Drink
from project.supply.food import Food

controller = Controller()
apple = Food("apple", 22)
cheese = Food("cheese")
juice = Drink("orange juice")
water = Drink("water")
first_player = Player('Peter', 15)
second_player = Player('Lilly', 12, 94)
print(controller.add_supply(cheese, apple, cheese, apple, juice, water, water))
print(controller.add_player(first_player, second_player))
print(controller.duel("Peter", "Lilly"))
print(controller.add_player(first_player))
print(controller.sustain("Lilly", "Drink"))
first_player.stamina = 0
print(controller.duel("Peter", "Lilly"))
print(first_player)
print(second_player)
controller.next_day()
print(controller)

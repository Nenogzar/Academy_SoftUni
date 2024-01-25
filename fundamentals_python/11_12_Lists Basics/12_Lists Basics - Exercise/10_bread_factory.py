# Като млад пекар, вие печете хляба от пекарната.
# Имате начална енергия 100 и начални монети 100.
# Ще ви бъде даден низ, представляващ събитията от работния ден.
# Всяко събитие е разделено с '|' (вертикална лента): "event1|event2| … eventN"
# Всяко събитие съдържа име на събитие или съставка и номер, разделени с тире ("{event/ingredient}-{number}"))

#•	If the event is "rest":
    #o Получавате енергия (числото във втората част).
        #   Забележка: вашата енергия не може да надвишава първоначалната ви енергия (100).
        #   Отпечатайте: "You gained {gained_energy} energy."

    #o След това отпечатайте текущата си енергия: "Current energy:
#               {current_energy}."

# •	If the event is "order":
        # o Спечелихте монети (числото във втората част).
        # o Всеки път, когато получите поръчка, енергията ви намалява с 30 точки.
            #  Ако имате енергията да завършите поръчката, отпечатайте:
#               "You earned {earned} coins."

            #  В противен случай пропуснете поръчката и спечелете 50 енергийни точки.
#               Отпечатайте: "You had to rest!".

# • Във всеки друг случай имате съставка, която трябва да купите.
# Втората част на събитието съдържа монетите, които трябва да похарчите.
        #  o Ако имате достатъчно пари, трябва да купите съставката и да отпечатате:
        #       "You bought {ingredient}."

        # o В противен случай отпечатайте "Closed! Cannot afford {ingredient}."  и вашата пекарна свърши.

# Ако сте успели да се справите с всички събития през деня, отпечатайте на следните 3 реда:
# "Day completed!"
# "Coins: {coins}"
# "Energy: {energy}"

#### Input / Constraints #####
# You will receive a string representing the working day events, separated with '|' (vertical bar) in the format:
# "event1|event2| … eventN".
# Each event contains an event name or an ingredient and a number, separated by a dash in the format:
# "{event/ingredient}-{number}"

#### Output ####

# Отпечатайте съответните съобщения, описани по-горе.


energy, money = 100, 100
gained_energy = 0

earned_coins = 0
event_list = input().split("|")
#print("event_list", event_list)
for item_data in event_list:
    event_type, event_value = item_data.split("-")
    #print("item_data", item_data)
    if event_type == "rest":

        if energy + int(event_value) > 100:
            print(f"You gained {100 - energy} energy.")
            energy = 100

        else:
            energy += int(event_value)
            print(f"You gained {int(event_value)} energy.")
        print(f"Current energy: {energy}.")

    elif event_type == "order":

        if energy >= 30:
            energy -= 30
            money += int(event_value)
            print(f"You earned {int(event_value)} coins.")
        else:
            energy += 50
            print("You had to rest!")

    else:
        something = event_type
        if int(event_value) <= money:
            money -= int(event_value)
            print(f"You bought {something}.")
        else:
            print(f"Closed! Cannot afford {something}.")
            break
else:
    print("Day completed!")
    print(f"Coins: {money}")
    print(f"Energy: {energy}")



########################  FROM CEO #####################################
# main_events = input().split("|")
#
# energy = 100
# coins = 100
#
#
# def rest_event(energy_number, energy):
#     if energy + energy_number > 100:
#         energy_number = abs(100 - energy)
#
#     energy += energy_number
#     print(f"You gained {energy_number} energy.")
#     print(f"Current energy: {energy}.")
#     return energy
#
#
# def order_event(coins_number, coins, energy):
#     if energy - 30 >= 0:
#         coins += coins_number
#         energy -= 30
#         print(f"You earned {coins_number} coins.")
#     else:
#         print("You had to rest!")
#         energy += 50
#     return energy, coins
#
#
# def ingredient_event(name, price_item, coins):
#     if price_item <= coins:
#         print(f"You bought {name}.")
#         coins -= price_item
#         return coins
#
#     print(f"Closed! Cannot afford {name}.")
#     exit()
#
#
# for event_type in main_events:
#     event_type = event_type.split("-")
#     event_command = event_type[0]
#     event_energy_coins = int(event_type[-1])
#
#     if event_command == "rest":
#         energy = rest_event(event_energy_coins, energy)
#     elif event_command == "order":
#         energy, coins = order_event(event_energy_coins, coins, energy)
#     else:
#         coins = ingredient_event(event_command, event_energy_coins, coins)
#
# print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")

#####################################################################################

# commands_list = input().split("|")
# gained_energy, current_energy, coins = 0, 100, 100
#
# for command in commands_list:
#     current_event = []
#     event_value = 0
#     for element in command.split("-"):
#         current_event.append(element)
#     event_value = int(current_event[-1])
#     if "rest" in current_event:
#         if current_energy + event_value > 100:
#             print(f"You gained {abs(100 - current_energy)} energy.")
#             current_energy = 100
#         else:
#             current_energy += event_value
#             print(f"You gained {event_value} energy.")
#         print(f"Current energy: {current_energy}.")
#
#     elif "order" in current_event:
#         if current_energy >= 30:
#             current_energy -= 30
#             coins += event_value
#             print(f"You earned {event_value} coins.")
#         else:
#             current_energy += 50
#             print("You had to rest!")
#     else:
#         ingredient = current_event[0]
#         if coins >= event_value:
#             coins -= event_value
#             print(f"You bought {ingredient}.")
#         else:
#             cannot_afford_ingredient = True
#             print(f"Closed! Cannot afford {ingredient}.")
#             break
#
# else:
#     print("Day completed!")
#     print(f"Coins: {coins}")
#     print(f"Energy: {current_energy}")

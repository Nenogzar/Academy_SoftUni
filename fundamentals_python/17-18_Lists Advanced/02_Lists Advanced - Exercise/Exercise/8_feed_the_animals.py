# command_names_food_area = input().split(":")
# animals = []
# daily_feed = []
# area = []
# while command_names_food_area[0] != "Last Info":
#     if command_names_food_area[0] == "Add":
#         if command_names_food_area[1] in animals:
#             index = animals.index(command_names_food_area[1])
#             daily_feed[index] += int(command_names_food_area[2])
#         else:
#             animals.append(command_names_food_area[1])
#             daily_feed.append(int(command_names_food_area[2]))
#             area.append(command_names_food_area[3])
#     elif command_names_food_area[0] == "Feed":
#         animal_index = animals.index(command_names_food_area[1])
#         feed = int(command_names_food_area[2])
#         daily_feed[animal_index] -= feed
#         if daily_feed[animal_index] <= 0:
#             print(f'{animals[animal_index]} was successfully fed')
#             animals.pop(animal_index)
#             daily_feed.pop(animal_index)
#             area.pop(animal_index)
#     command_names_food_area = input().split(":")
# print("Animals:")
# food_need_sorted = {}
# for index, value in enumerate(daily_feed):
#     if value in food_need_sorted:
#         food_need_sorted[value] += [animals[index]]
#     else:
#         food_need_sorted[value] = [animals[index]]
# if len(food_need_sorted) != 0:
#     for index in sorted(food_need_sorted.keys(), reverse=True):
#         for i in sorted(food_need_sorted[index]):
#             print(f'{i} -> {index}g')
# still_hungry_area = {}
# for value in area:
#     if value in still_hungry_area:
#         still_hungry_area[value] += 1
#     else:
#         still_hungry_area[value] = 1
# still_hungry_area = sorted(still_hungry_area.items(), key=lambda x: x[1], reverse=True)
# print('Areas with hungry animals:')
# if len(still_hungry_area) != 0:
#     for value in still_hungry_area:
#         print(f'{value[0]} : {value[1]}')


""" 2 """


def add_animal(command, animals, daily_feed, area):
    if command[1] in animals:
        index = animals.index(command[1])
        daily_feed[index] += int(command[2])
    else:
        animals.append(command[1])
        daily_feed.append(int(command[2]))
        area.append(command[3])


def feed_animal(command, animals, daily_feed, area):
    animal_index = animals.index(command[1])
    feed = int(command[2])
    daily_feed[animal_index] -= feed
    if daily_feed[animal_index] <= 0:
        print(f'{animals[animal_index]} was successfully fed')
        animals.pop(animal_index)
        daily_feed.pop(animal_index)
        area.pop(animal_index)


def print_animals(animals, daily_feed):
    print("Animals:")
    food_need_sorted = {}
    for index, value in enumerate(daily_feed):
        if value in food_need_sorted:
            food_need_sorted[value] += [animals[index]]
        else:
            food_need_sorted[value] = [animals[index]]
    if len(food_need_sorted) != 0:
        for index in sorted(food_need_sorted.keys(), reverse=True):
            for i in sorted(food_need_sorted[index]):
                print(f'{i} -> {index}g')


def print_hungry_areas(area):
    still_hungry_area = {}
    for value in area:
        if value in still_hungry_area:
            still_hungry_area[value] += 1
        else:
            still_hungry_area[value] = 1
    still_hungry_area = sorted(still_hungry_area.items(), key=lambda x: x[1], reverse=True)
    print('Areas with hungry animals:')
    if len(still_hungry_area) != 0:
        for value in still_hungry_area:
            print(f'{value[0]} : {value[1]}')


def main():
    animals = []
    daily_feed = []
    area = []

    command_names_food_area = input().split(":")
    while command_names_food_area[0] != "Last Info":
        if command_names_food_area[0] == "Add":
            add_animal(command_names_food_area, animals, daily_feed, area)
        elif command_names_food_area[0] == "Feed":
            feed_animal(command_names_food_area, animals, daily_feed, area)
        command_names_food_area = input().split(":")

    print_animals(animals, daily_feed)
    print_hungry_areas(area)


if __name__ == "__main__":
    main()

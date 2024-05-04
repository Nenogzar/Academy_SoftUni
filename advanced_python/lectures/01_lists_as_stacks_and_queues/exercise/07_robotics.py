# from collections import deque
# from datetime import datetime, timedelta
#
# robots = {}
#
# for r in input().split(";"):
#     name, time_needed = r.split("-")
#     robots[name] = [int(time_needed), 0]
#
# factory_time = datetime.strptime(input(), "%H:%M:%S")
# products = deque()
#
#
# product = input()
# while product != "End":
#     products.append(product)
#     product = input()
#
# while products:
#     factory_time += timedelta(0, 1)
#     product = products.popleft()
#     free_robots = []
#
#     for name, value in robots.items():
#         if value[1] != 0:
#             robots[name][1] -= 1
#
#     for name, value in robots.items():
#         if value[1] == 0:
#             free_robots.append([name, value])
#
#     if not free_robots:
#         products.append(product)
#         continue
#
#     robot_name, data = free_robots[0]
#     robots[robot_name][1] = data[0]
#
#     print(f"{free_robots[0][0]} - {product} [{factory_time.strftime('%H:%M:%S')}]")

""" """
import datetime
from collections import deque

robots = []
starting_time = None
products_on_line = deque()

robot_data_list = input().split(";")
hours, minutes, seconds = [int(x) for x in input().split(":")]
starting_time = datetime.datetime(100, 1, 1, hours, minutes, seconds)
product = input()

while product != "End":
    products_on_line.append(product)
    product = input()


for robot_data in robot_data_list:
    name, process = [int(x) if x.isdigit() else x for x in robot_data.split("-")]
    robots.append({"name": name, "process_time": process, "busy_until": starting_time})

while products_on_line:

    starting_time += datetime.timedelta(0, 1) # Увеличаване на времето за стартиране с 1 секунда
    item = products_on_line.popleft()  # Взимане на първия продукт от опашката

    free_robot = None  # Инициализация на променлива за свободен робот. None  за да съхранява само един обект.

    # Проверка за свободен робот
    for robot in robots:
        if starting_time >= robot["busy_until"]:
            free_robot = robot
            break

    if free_robot: # Ако има свободен робот, обработи продукта с него
        free_robot["busy_until"] = starting_time + datetime.timedelta(0, free_robot["process_time"])
        print(f'{free_robot["name"]} - {item} [{starting_time.time()}]')

    else:
        products_on_line.append(item) # Ако няма свободен робот, продуктът остава в опашката


#################################### TASK CONDITION ############################
"""
                             7.	*Robotics
There is a robotics factory. The current project is assembly-line robots.
Each robot has a processing time – it is the time in seconds the robot needs 
to process a product. When a robot is free, it should take a product for 
processing and log its name, product, and processing start time.
Each robot processes a product coming from the assembly line. A product is 
coming from the line each second (so the first product should appear 
at [start time + 1 second]). If a product passes the line and there is not 
a free robot to take it, it should be queued at the end of the line again.
The robots are standing in the line in the order of their appearance.
Input
•	On the first line, you will receive the robots' names and their processing 
times in the format "robotName-processTime;robotName-processTime;robotName-processTime..."
•	On the second line, you will get the starting time in the format "hh:mm:ss"
•	Next, until the "End" command, you will get a product on each line.
Output 
•	Every time a robot takes a product, you should print: "{robotName} - {product} [hh:mm:ss]"

____________________________________________________________________________________________
Example_01

Input
ROB-15;SS2-10;NX8000-3
8:00:00
detail
glass
wood
apple
End	

Output
ROB - detail [08:00:01]
SS2 - glass [08:00:02]
NX8000 - wood [08:00:03]
NX8000 - apple [08:00:06]


____________________________________________________________________________________________
Example_02

Input
ROB-8
7:59:59
detail
glass
wood
sock
End	

Output
ROB - detail [08:00:00]
ROB - wood [08:00:08]
ROB - glass [08:00:16]
ROB - sock [08:00:24]

"""
""" 1 """
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

""" 2 """
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

""" 3 """

import time
from collections import deque


class Robotics:

    def __init__(self):
        self.robots = {}
        self.time = 0
        self.products = deque()
        self.log = []
        self.main_meth()

    def process_robots_data(self):
        for robot in input().split(';'):
            robot_name, robot_time = robot.split('-')
            if robot_name not in self.robots:
                self.robots[robot_name] = [int(robot_time), 0]

    def process_starting_time(self):
        h, m, s = input().split(':')
        self.time = int(h) * 3600 + int(m) * 60 + int(s)

    def take_product_to_production_line(self):
        while True:
            data = input()
            if data == 'End':
                break
            self.products.append(data)

    def convert_seconds_to_HH_MM_SS(self):
        value = time.strftime('%H:%M:%S', time.gmtime(self.time))
        return value

    def robot_process_the_product(self, free_robots, product):
        robot_name = list(free_robots)[0]
        self.robots[robot_name][1] = self.time + self.robots[robot_name][0]
        converted_time = self.convert_seconds_to_HH_MM_SS()
        self.log.append(f'{robot_name} - {product} [{converted_time}]')

    def check_for_free_robots(self):
        return {name: data for name, data in self.robots.items() if data[1] <= self.time}

    def robots_start_to_work(self):
        while self.products:
            product = self.products.popleft()
            self.time += 1
            free_robots = self.check_for_free_robots()
            if free_robots:
                self.robot_process_the_product(free_robots, product)
            else:
                self.products.append(product)

    def main_meth(self):
        self.process_robots_data()
        self.process_starting_time()
        self.take_product_to_production_line()
        self.robots_start_to_work()

    def __repr__(self):
        return '\n'.join(self.log)


if __name__ == '__main__':
    print(Robotics())

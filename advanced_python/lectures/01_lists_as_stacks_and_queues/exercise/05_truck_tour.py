""" Truck Tour"""
from collections import deque

liters, kilometers = deque(), deque()

for _ in range(int(input())):
    liter, kilometer = map(int, input().split())  # or lite
    # liter, kilometer = deque([int(x) for x in input().split()] for _ in range(int(input())))
    liters.append(liter)
    kilometers.append(kilometer)

liters_copy = liters.copy()
kilometers_copy = kilometers.copy()

tank_capacity = 0
count_run = 0

while liters_copy:
    liter = liters_copy.popleft()
    kilometer = kilometers_copy.popleft()
    tank_capacity += liter

    if tank_capacity >= kilometer:
        tank_capacity -= kilometer
    else:
        liters.append(liters.popleft())  # liters.rotate(-1)
        kilometers.append(kilometers.popleft())  # kilometers.rotate(-1)
        liters_copy = liters.copy()
        kilometers_copy = kilometers.copy()
        count_run += 1
        tank_capacity = 0

print(count_run)

""" """

from collections import deque

gas_station = int(input())
petrol_pumps = deque()

total_petrol = 0
distance_to_next = 0
start_index = 0

for i in range(gas_station):
    petrol, distance = map(int, input().split())
    petrol_pumps.append((petrol, distance))

    total_petrol += petrol
    total_petrol -= distance
    distance_to_next += distance

    if total_petrol < 0:
        start_index = i + 1
        total_petrol = 0
        distance_to_next = 0

print(start_index)

#################################### TASK CONDITION ############################
"""
                     5. Truck Tour
There is a circle road with N petrol pumps. The petrol pumps are numbered 
0 to (N−1) (both inclusive). For each petrol pump, you will receive two 
pieces of information (separated by a single space): 
-	The amount of petrol the petrol pump will give you
-	The distance from that petrol pump to the next petrol pump (kilometers)
You are a truck driver, and you want to go all around the circle. You know 
that the truck consumes 1 liter of petrol per 1 kilometer, and its tank has 
infinite petrol capacity. In the beginning, the tank is empty, but you start
your journey at a petrol pump so you can fill it with the given amount of petrol.
Your task is to calculate the first petrol pump from where the truck will be 
able to complete the circle. You never miss filling its tank at a petrol pump.
Input
•	On the first line, you will receive the number of petrol pumps - N
•	On the next N lines, you will receive the amount of petrol that each 
petrol pump will give and the distance between that petrol pump and the 
next petrol pump, separated by a single space
Output
•	An integer which will be the smallest index of a petrol pump from 
which you can start the tour
Constraints
•	1 ≤ N ≤ 1000001
•	1 ≤ amount of petrol, distance ≤ 1000000000
•	You will always have at least one point from where the truck will 
be able to complete the circle

____________________________________________________________________________________________
Example_01

Input
3
1 5
10 3
3 4	

Output
1


____________________________________________________________________________________________
Example_02

Input
5
22 5
14 10
52 7
21 12
36 9	

Output
0

"""
""" 1 """
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

"""2 """

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


"""3"""

from collections import deque


class TruckTour:

    def __init__(self):
        self.number_of_stations = int(input())
        self.data_deque = deque()
        self.searched_index = 0
        self.main_meth()

    def create_deque_with_data(self):
        for _ in range(self.number_of_stations):
            data = [int(n) for n in input().split()]
            self.data_deque.append(data)

    def start_journey(self):
        fuel_tank = 0
        found_index = True
        for data in self.data_deque:
            fuel, distance = data
            fuel_tank += fuel - distance
            if fuel_tank < 0:
                found_index = False
                break

        return found_index

    def find_station_index(self):
        for index in range(len(self.data_deque)):
            self.searched_index = index

            if self.start_journey():
                break
            self.data_deque.rotate(-1)

    def main_meth(self):
        self.create_deque_with_data()
        self.find_station_index()

    def __repr__(self):
        return f'{self.searched_index}'


if __name__ == '__main__':
    print(TruckTour())

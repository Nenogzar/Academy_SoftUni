""" Truck Tour"""

from collections import deque

liters, kilometers = deque(), deque()

for _ in range(int(input())):
    liter, kilometer = map(int, input().split())
    liters.append(liter)
    kilometers.append(kilometer)

liters_copy = liters.copy()
kilometers_copy = kilometers.copy()

gas_in_tank = 0
index = 0

while liters_copy:
    liter = liters_copy.popleft()
    kilometer = kilometers_copy.popleft()
    gas_in_tank += liter

    if gas_in_tank >= kilometer:
        gas_in_tank -= kilometer
    else:
        liters.append(liters.popleft()) # liters.rotate(-1)
        kilometers.append(kilometers.popleft()) # kilometers.rotate(-1)
        liters_copy = liters.copy()
        kilometers_copy = kilometers.copy()
        index += 1
        gas_in_tank = 0

print(index)


"""  """
#
def can_complete_circle(petrol_pumps):
    total_petrol = 0
    distance_to_next = 0
    start_index = 0

    for i, (petrol, distance) in enumerate(petrol_pumps):
        total_petrol += petrol
        total_petrol -= distance
        distance_to_next += distance

        if total_petrol < 0:
            start_index = i + 1
            total_petrol = 0
            distance_to_next = 0

    return start_index

def main():
    gas_station = int(input())
    petrol_pumps = []

    for _ in range(gas_station):
        petrol, distance = map(int, input().split())
        petrol_pumps.append((petrol, distance))

    start_index = can_complete_circle(petrol_pumps)
    print(start_index)

if __name__ == "__main__":
    main()
#

""" dean"""
# from collections import deque
#
# pump_data = deque([[int(x) for x in input().split()] for _ in range(int(input()))])
#
# # OR
# # pump_data = [deque(map(int, input().split())) for _ in range(int(input()))]
#
# pump_data_copy = pump_data.copy()
# gas_in_tank = 0
# index = 0
#
# while pump_data_copy:
#     petrol, distance = pump_data_copy.popleft()
#     gas_in_tank += petrol
#     if gas_in_tank >= distance:
#         gas_in_tank -= distance
#     else:
#         pump_data.rotate(-1)
#         pump_data_copy = pump_data.copy()
#
#         index += 1
#         gas_in_tank = 0
# print(index)


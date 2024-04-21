""" Truck Tour"""

from collections import deque

gas_station = int(input())
liters, kilometers = deque(), deque()
current_gas_station = 0

for i in range(gas_station):
    liter, kilometer = map(int, input().split())
    liters.append(liter)
    kilometers.append(kilometer)
if sum(kilometers) <= sum(liters):
    while kilometers:
        current_liter = liters.popleft()
        current_kilometer = kilometers.popleft()

        if current_liter < current_kilometer:
            current_gas_station += 1
            liters.append(current_liter)
            kilometers.append(current_kilometer)
        else:
            break
            remaining_liters = current_liter - current_kilometer
            if liters:
                liters[0] += remaining_liters



print(current_gas_station)

""" """
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

import math

record_in_seconds = float(input())
distance_in_meters = float(input())
distance_in_s_for_1m = float(input())

all_distance_in_seconds = distance_in_meters * distance_in_s_for_1m

delay_times = math.floor(distance_in_meters // 15)
delay_seconds = delay_times * 12.5

total_time = all_distance_in_seconds + delay_seconds

difference = abs(total_time - record_in_seconds)

if total_time < record_in_seconds:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {math.floor(difference):.2f} seconds slower.')

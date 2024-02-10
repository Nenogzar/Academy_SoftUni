rooms_number = int(input())
free_chairs = 0

for room in range(1, rooms_number + 1):
    chairs, visitors = input().split()
    chairs = len(chairs)  # брой на столовете
    visitors = int(visitors)  # брой на посетителите
    if chairs >= visitors:
        free_chairs += (chairs - visitors)
    else:
        need_chairs = visitors - chairs
        print(f"{need_chairs} more chairs needed in room {room}")
        free_chairs += (chairs - visitors)

if free_chairs >= 0:
    print(f"Game On, {free_chairs} free chairs left")

""" Ivan Shopov"""
# 5

def check_the_rooms(number_of_rooms):
    free_chairs = 0
    for number_of_room in range(1, number_of_rooms + 1):
        free_chairs_in_current_room, visitors = input().split()
        difference = len(free_chairs_in_current_room) - int(visitors)
        if difference < 0:
            print(f"{abs(difference)} more chairs needed in room {number_of_room}")
        free_chairs += difference
    return free_chairs


count_of_rooms = int(input())
total_free_chairs = check_the_rooms(count_of_rooms)
if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")

# 5.1

count_of_rooms = int(input())
total_free_chairs = 0
for number_of_room in range(1, count_of_rooms + 1):
    free_chairs_in_current_room, visitors = input().split()
    difference = len(free_chairs_in_current_room) - int(visitors)
    if difference < 0:
        print(f"{abs(difference)} more chairs needed in room {number_of_room}")
    total_free_chairs += difference
if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")
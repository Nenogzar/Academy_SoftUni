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


"""  kumchovalcho"""

number_of_rooms = int(input())
free_chairs = 0
enough_chairs = False


def free_chair(chair, visitor):
    result = abs(chair - visitor)
    print(f"{result} more chairs needed in room {room}")


def not_enough_chairs(chair, visitor):
    result = chair - visitor
    return result


for room in range(1, number_of_rooms + 1):
    current_room = input().split()
    chairs = len(current_room[0])
    visitors = int(current_room[1])
    if chairs - visitors < 0:
        free_chair(chairs, visitors)
        enough_chairs = True
    elif chairs - visitors > 0:
        free_chairs += not_enough_chairs(chairs, visitors)

if not enough_chairs:
    print(f"Game On, {free_chairs} free chairs left")


""" CEO  """

number_rooms = int(input())

enough_chairs = True
chairs_left = 0


def check_chairs(chairs, people, room_floor):
    if chairs < people:
        result = people - chairs
        global enough_chairs
        enough_chairs = False
        return print(f"{result} more chairs needed in room {room_floor}")
    else:
        global chairs_left
        chairs_left += chairs - people


for room in range(1, number_rooms + 1):
    room_input, chairs = input().split()
    check_chairs(len(room_input), int(chairs), room)

if enough_chairs:
    print(f"Game On, {chairs_left} free chairs left")
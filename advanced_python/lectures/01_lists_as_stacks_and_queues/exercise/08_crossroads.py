# from collections import deque
#
# green_light = int(input())
# free_window = int(input())
#
# cars = deque()
# passed_cars = []
#
# command = input()
# while command != "END":
#     if command == "green":
#         current_green_light = green_light
#         while cars:
#             car = cars.popleft()
#             car_length = len(car)
#             if current_green_light >= car_length:
#                 current_green_light -= car_length
#                 passed_cars.append(car)
#             else:
#                 if free_window + 1 < len(car):
#                     character_hit = car[free_window + 1]
#                 if current_green_light + free_window < car_length:
#                     print("A crash happened!")
#                     print(f"{car} was hit at {character_hit}.")
#                     quit()
#                 else:
#                     passed_cars.append(car[:current_green_light + free_window])
#                     break
#     else:
#         cars.append(command)
#
#     command = input()
#
# print("Everyone is safe.")
# print(f"{len(passed_cars)} total cars passed the crossroads.")



from collections import deque

green_lift_duration = int(input())
free_window_in_sec = int(input())
car_or_command = input()

car_q = deque()
passed_cars = 0

while car_or_command != "END":
    if car_or_command != "green":
        car_q.append(car_or_command)
    else:
        if car_q:
            green_lift_start = green_lift_duration
            free_window_on_gree = free_window_in_sec
            for _ in range(len(car_q)):
                car_enter = False
                car = car_q.popleft()
                coming_tru_car = len(car)
                if green_lift_start != 0:
                    green_lift_start -= coming_tru_car
                    car_enter = True
                if green_lift_start < 0:
                    coming_tru_car = abs(green_lift_start)
                    green_lift_start = 0
                else:
                    passed_cars += 1
                    continue
                if coming_tru_car and car_enter:
                    coming_tru_car -= free_window_on_gree
                    if coming_tru_car > 0:
                        print(f"A crash happened!\n{car} was hit at {list(car)[-coming_tru_car]}.")
                        exit()
                    passed_cars += 1
                    break

    car_or_command = input()

print(f"Everyone is safe.\n{passed_cars} total cars passed the crossroads.")


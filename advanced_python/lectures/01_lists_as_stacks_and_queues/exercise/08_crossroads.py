#################################### TASK CONDITION ############################
"""
                              8.	*Crossroads
The super-spy action hero Sam has finally found some time to go on a holiday. 
He is taking his wife somewhere nice, and they're going to have a really 
good time, but first, they have to get there. Even on his holiday trip, 
Sam is still going to run into some problems, and the first one is 
getting to the airport. Right now, he is stuck in a traffic jam at a 
crossroads where a lot of accidents happen.
Your job is to keep track of the traffic at the crossroads and report 
whether a crash happened or everyone passed the crossroads safely.
Sam is on a single lane of cars that queue until the light goes green. 
When it does, they start passing one by one on a flashing green light 
and during the free window before the intersecting road's light goes 
green. For each second, only one part of a car (a single character) 
passes the crossroad. If a car is still in the middle of the crossroads 
when the free window ends, it will get hit at the first character that 
is still in the crossroads.
Input
•	On the first line, you will receive the duration of the green light 
in seconds – an integer [1 … 100]
•	On the second line, you will receive the duration of the free window 
in seconds – an integer [0 … 100]
•	On the following lines, until you receive the "END" command, you will
 receive one of two things:
	A car - a string containing the model of the car, or
	The command "green" that indicates the start of a green light cycle
A green light cycle goes as follows:
•	During the green light, cars will enter and exit the crossroads one by one
•	During the free window, cars will only exit the crossroads
Output
•	If a crash happens, end the program and print:
"A crash happened!"
"{car} was hit at {character_hit}."
•	If everything goes smoothly and you receive an "END" command, print:
"Everyone is safe."
"{total_cars_passed} total cars passed the crossroads."
Constraints
•	The input will be within the constraints specified above and will always be valid. 
There is no need to check it explicitly.

____________________________________________________________________________________________
Example_01

Input
10
5
Mercedes
green
Mercedes
BMW
Skoda
green
END	

Output
Everyone is safe.
3 total cars passed the crossroads.	

Explanation
During the first green light (10 seconds), the Mercedes (8) passes safely.
During the second green light, the Mercedes (8) passes safely, 
and there are 2 seconds left. The BMW enters the crossroads, and when 
the green light ends, it still has 1 part inside ('W') but has 5 seconds 
to leave and passes successfully.The Skoda never entered the crossroads, 
so 3 cars passed successfully.

____________________________________________________________________________________________
Example_02

Input
9
3
Mercedes
Hummer
green
Hummer
Mercedes
green
END

Output
A crash happened!
Hummer was hit at e.

Explanation
Mercedes (8) passes successfully, and Hummer (6) enters the crossroads,
but only the 'H' passes during the green light. There are 3 seconds of 
a free window, so "umm" passes, and the Hummer gets hit at 'e', and the 
program ends with a crash.


"""
""" 1 """
from collections import deque

green_light = int(input())
free_window = int(input())

cars = deque()
passed_cars = []

command = input()
while command != "END":
    if command == "green":
        current_green_light = green_light
        while cars:
            car = cars.popleft()
            car_length = len(car)
            if current_green_light >= car_length:
                current_green_light -= car_length
                passed_cars.append(car)
            else:
                if free_window + 1 < len(car):
                    character_hit = car[free_window + 1]
                if current_green_light + free_window < car_length:
                    print("A crash happened!")
                    print(f"{car} was hit at {character_hit}.")
                    quit()
                else:
                    passed_cars.append(car[:current_green_light + free_window])
                    break
    else:
        cars.append(command)

    command = input()

print("Everyone is safe.")
print(f"{len(passed_cars)} total cars passed the crossroads.")

""" 2 """

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

""" 3 """

from collections import deque


class Crossroads:

    def __init__(self):
        self.green_light = int(input())
        self.window_time = int(input())
        self.cars = deque()
        self.passed_cars = 0
        self.crash = False
        self.message = ''
        self.main_meth()

    def main_meth(self):
        self.control_traffic_lights()

    def control_traffic_lights(self):
        data = input()
        while data != 'END' and not self.crash:
            if data == 'green':
                self.start_passing_cars()
            else:
                self.cars.append(data)
            data = input()

    def start_passing_cars(self):
        green_time = self.green_light
        while self.cars and green_time > 0:
            car = self.cars.popleft()
            car_time = len(car)
            if car_time < green_time:
                green_time -= car_time
                self.passed_cars += 1
            else:
                car_time -= green_time
                if car_time > self.window_time:
                    hit_index = self.window_time + green_time
                    self.crash = True
                    self.message = f'A crash happened!\n{car} was hit at {car[hit_index]}.'
                    break
                self.passed_cars += 1
                green_time = 0

    def __repr__(self):
        if not self.crash:
            self.message = f'Everyone is safe.\n{self.passed_cars} total cars passed the crossroads.'
        return self.message


if __name__ == "__main__":
    print(Crossroads())

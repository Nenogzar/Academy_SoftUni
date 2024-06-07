# ******* Advanced Exam - 22 October 2023 ******* #

# *******  01_offroad_challenge  ******* #

# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/4193#0

John is quite an avid off-road fan. He bought a new jeep and made the necessary improvements to it.
John is ready for new off-road adventures and can't wait to get started.
In this challenge, he must save his fuel very carefully…

There will be two sequences of integers.
    The first sequence will represent the initial fuel and
    the second - additional consumption index due to thin air at high altitudes,
    hence higher fuel consumption.
    There will also be a third sequence of integers,
    representing values equal to the necessary amount of fuel needed to reach the corresponding altitude in the challenge.

Your task is to take the last fuel quantity from the fuel sequence and
the first index from the additional consumption index sequence.
Subtract the values and check the result.

•	The corresponding altitude is reached
    if the calculated result is bigger or equal to the first element from the needed amount of fuel sequence.
        You need to remove both the fuel and the consumption index from their sequences
            as well as the needed amount of fuel index from their sequence.
•	If the calculated result is smaller or not equal to the first element from the needed amount of fuel sequence,
        the corresponding altitude is not reached, movement cannot continue, and the program should end.

Input
•	The first line will represent the initial fuel – integers, separated by a single space.
•	The second line will represent the consumption indexes that decrease initial fuel – integers, separated by a single space.
•	The third line will represent the quantities needed to reach the corresponding altitude – integers, separated by a single space.

Output
•	On the first or the next n lines, output the corresponding message on the console from the following options:
    	If John reaches the altitude, print the message:
        "John has reached: Altitude 1"
        …
        "John has reached: Altitude {n}"

	If John fails to reach the altitude, print the message:
        "John did not reach: Altitude {n}"

•	On the next lines, based on whether he reached the top or not,
        print the following on the console in the specified format:

	If John doesn't have enough fuel to reach the top but has reached some altitude, display the following messages:
        "John failed to reach the top."
        "Reached altitudes: Altitude 1, … Altitude {n}"

	If John does not have enough fuel to reach the top and has not reached any altitude, print:
        "John failed to reach the top."
        "John didn't reach any altitude."

	If John manages to reach all the altitudes, he will reach the top.

    End the program and print on the console the following message:
        "John has reached all the altitudes and managed to reach the top!"

Constraints
•	All the given numbers will be valid integers in the range [1, 200].
•	All sequences always consist of four elements.
•	There will be no negative input.

Examples

Input
200 90 40 100
20 40 30 50
50 60 80 90

Output
John has reached: Altitude 1
John did not reach: Altitude 2
John failed to reach the top.
Reached altitudes: Altitude 1

Comment
We start by taking the last fuel quantity from the fuel sequence (100) and the first additional consumption index
    from the consumption index fuel sequence (20).
    The result from subtraction is 100 - 20 = 80.
    After that, we check if the sum equals or exceeds the first amount of needed fuel.
        The result (80) is more than the needed fuel (50) for this altitude, so the altitude is reached.
    As the altitude is reached, we remove an element from every sequence.
    We continue with the next altitude to do the same and as a result,
        we have 40 – 40 = 0.
    The needed fuel is 60, we do not have enough fuel to reach the current altitude,
    so the challenge for John ends here.


Input
40 66 123 100
10 30 70 33
40 55 77 100

Output
John has reached: Altitude 1
John has reached: Altitude 2
John did not reach: Altitude 3
John failed to reach the top.
Reached altitudes: Altitude 1, Altitude 2

Comment
Here we take the last fuel quantity and like in the previous case subtract the consumption index from the fuel and continue forward until the result is equal to or greater than the required fuel otherwise the program stops.

Input
199 190 100 100
20 40 30 50
50 60 70 80

Output
John has reached: Altitude 1
John has reached: Altitude 2
John has reached: Altitude 3
John has reached: Altitude 4
John has reached all the altitudes and managed to reach the top!

Comment
Here all altitudes are conquered, and John successfully reaches the top.


"""

##########: variant 1 :##########

from collections import deque

initial_fuel = list(map(int, input().split()))
additional_index = deque(map(int, input().split()))
needed_fuel = deque(map(int, input().split()))
altitudes_reached = []
first_len = len(initial_fuel)
initial_length = len(initial_fuel)

for run in range(1, initial_length + 1):
    fuel = initial_fuel.pop()
    additional_expense = additional_index.popleft()
    need_fuel = needed_fuel.popleft()
    cost = fuel - additional_expense

    if cost >= need_fuel:
        altitudes_reached.append(run)
        print(f"John has reached: Altitude {run}")
    else:
        print(f"John did not reach: Altitude {run}")

        if len(altitudes_reached) == 0:
            print("John failed to reach the top.\n John didn't reach any altitude.")
        else:
            print("John failed to reach the top.")

            formatted_altitudes = [f"Altitude {alt}" for alt in altitudes_reached]
            print(f"Reached altitudes: {', '.join(formatted_altitudes)}")

        break
else:

    if len(altitudes_reached) == first_len:
        print("John has reached all the altitudes and managed to reach the top!")

##########: variant 2  CEO:##########
from collections import deque

get_list_of_integers = lambda input_value: [int(x) for x in input_value.split()]

initial_fuel = get_list_of_integers(input())
consumption_index = deque(get_list_of_integers(input()))
fuel_needed = deque(get_list_of_integers(input()))

while initial_fuel and consumption_index and fuel_needed:
    fuel_quantity = initial_fuel.pop()
    consumption = consumption_index.popleft()
    current_fuel = fuel_needed.popleft()

    is_altitude_reached = (fuel_quantity - consumption) >= current_fuel
    if not is_altitude_reached:
        print(f"John did not reach: Altitude {4 - len(fuel_needed)}")
        fuel_needed.appendleft(current_fuel)
        break

    print(f"John has reached: Altitude {4 - len(fuel_needed)}")

if 0 <= len(initial_fuel) < 4 and 0 < len(fuel_needed) < 4:
    altitudes = []
    for i in range(1, 4 - len(fuel_needed) + 1):
        altitudes.append(f"Altitude {i}")

    print("John failed to reach the top.")
    print(f"Reached altitudes:", ", ".join(altitudes))

if len(fuel_needed) == 4:
    print("John failed to reach the top.")
    print("John didn't reach any altitude.")

if all(not x for x in (initial_fuel, consumption_index, fuel_needed)):
    print("John has reached all the altitudes and managed to reach the top!")

##########: variant 2  TANER:##########



##########: variant 3 solution SoftUni :##########

from collections import deque

altitude_names = deque(["Altitude 1", "Altitude 2", "Altitude 3", "Altitude 4"])

fuel = list(map(int, input().split()))
consumption_index = deque(map(int, input().split()))
needed_fuel_amount = deque(map(int, input().split()))

altitudes_with_values = {}
for key in altitude_names:
    if needed_fuel_amount:
        value = needed_fuel_amount.popleft()
        altitudes_with_values[key] = value

reached_altitudes = []

while fuel and consumption_index and altitudes_with_values:
    current_level = altitude_names[0]
    current_fuel = fuel[-1]
    additional_consumption = consumption_index[0]
    difference = current_fuel - additional_consumption

    if difference >= altitudes_with_values[current_level]:
        fuel.pop()
        consumption_index.popleft()
        reached_altitudes.append(current_level)
        del altitudes_with_values[current_level]
        altitude_names.popleft()
        print(f"John has reached: {current_level}")
    else:
        fuel.pop()
        consumption_index.popleft()
        altitude_names.popleft()
        print(f"John did not reach: {current_level}")
        break

if not altitudes_with_values:
    print("John has reached all the altitudes and managed to reach the top!")
else:
    print("John failed to reach the top.")
    if reached_altitudes:
        print("Reached altitudes: ", end="")
        print(", ".join(reached_altitudes))
    else:
        print("John didn't reach any altitude.")

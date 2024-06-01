############################## 01_rubber_duck_debuggers ##############################
  ############################## TASK CONDITION ##############################
"""
https://judge.softuni.org/Contests/Practice/Index/3893#0

 Rubber Duck Debugging is a type of debugging where you place
 a rubber duck on your desk and explain to it your code line by line.
 You gathered a few programmers and gave them a task and judging by the time it took them to write the code,
 you reward them with a type of rubber ducky.

Learn more about Rubber Duck Debugging after your exam from here.

You will be given two sequences of integers.
The first one represents the time it takes a programmer to complete a single task.
The second one represents the number of tasks you’ve given to your programmers.
Your task is to count how many rubber ducks of each type you’ve given to your programmers.

While you have values in the sequences,
    you need to start from the first value of the programmers time's sequence
    and multiply them by the last value of the tasks' sequence:
        •	If the calculated time is between any of the time ranges below,
                you give the corresponding ducky and remove the programmer time's value and the tasks' value.
        •	If the calculated time goes above the highest range, decrease the number of the tasks' value by 2.
            Then, move the programmer time's value to the end of its sequence, and continue with the next operation.

Rubber Ducky type	                    Time needed to earn it

Darth Vader Ducky	                            0 - 60
Thor Ducky	                                   61 – 120
Big Blue Rubber Ducky	                      121 - 180
Small Yellow Rubber Ducky	                  181 - 240

Your task is considered done when the sequences are empty.


Input
•	The first line will represent each programmer’s time to complete a single task – integers, separated by a single space.
•	The second line will represent the number of tasks that should be completed – integers, separated by a single space.

Output.

•	On the first line, you output:

    "Congratulations, all tasks have been completed! Rubber ducks rewarded:"

•	On the next 4 lines, you output the type and number of ducks given, ordered like in the table:

    "Darth Vader Ducky: {count}
    Thor Ducky: {count}
    Big Blue Rubber Ducky: {count}
    Small Yellow Rubber Ducky: {count}"




Constraints
•	All the given numbers will be valid integers in the range [1, 1000].
•	There will be no negative inputs.
•	The number of values in both sequences will always be equal.
Examples

Input

10 15 12 18 22 6
12 16 5 6 9 1

Output

Congratulations, all tasks have been completed! Rubber ducks rewarded:
Darth Vader Ducky: 1
Thor Ducky: 3
Big Blue Rubber Ducky: 1
Small Yellow Rubber Ducky: 1


Input

2 55 17 31 23
7 5 17 4 27


Output

Congratulations, all tasks have been completed! Rubber ducks rewarded:
Darth Vader Ducky: 1
Thor Ducky: 0
Big Blue Rubber Ducky: 2
Small Yellow Rubber Ducky: 2

"""

##########: variant 1 :##########
from collections import deque


time_diapazon = {
    "Darth Vader Ducky": [0, 60],
    "Thor Ducky": [61, 120],
    "Big Blue Rubber Ducky": [121, 180],
    "Small Yellow Rubber Ducky": [181, 240],
}


needed_time = deque(map(int, input().split()))
exam_number = deque(map(int, input().split()))


duckies_awarded = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0,
}


while needed_time and exam_number:
    programmer_time = needed_time.popleft()
    task_number = exam_number.pop()

    calculated_time = programmer_time * task_number

    awarded = False
    for ducky, (low, high) in time_diapazon.items():
        if calculated_time in range(low, high + 1):
            duckies_awarded[ducky] += 1
            awarded = True
            break

    if not awarded:
        exam_number.append(task_number - 2)
        needed_time.append(programmer_time)


print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for ducky in ["Darth Vader Ducky", "Thor Ducky", "Big Blue Rubber Ducky", "Small Yellow Rubber Ducky"]:
    print(f"{ducky}: {duckies_awarded[ducky]}")


##########: variant 2 - whit Dictionary :##########

from collections import deque

time_diapazon = {
    "Darth Vader Ducky": [0, 60],
    "Thor Ducky": [61, 120],
    "Big Blue Rubber Ducky": [121, 180],
    "Small Yellow Rubber Ducky": [181, 240],
}


def check_diapazon(calculated_time, time_diapazon):
    """Check which diapazon the calculated_time falls into."""
    for ducky, (low, high) in time_diapazon.items():
        if calculated_time in range(low, high + 1):
            return ducky
    return None


def update_awards(duckies_awarded, ducky):
    """Update the duckies_awarded dictionary."""
    if ducky:
        duckies_awarded[ducky] += 1


needed_time = deque(map(int, input().split()))
exam_number = deque(map(int, input().split()))

duckies_awarded = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0,
}


while needed_time and exam_number:
    programmer_time = needed_time.popleft()
    task_number = exam_number.pop()

    calculated_time = programmer_time * task_number

    ducky = check_diapazon(calculated_time, time_diapazon)
    update_awards(duckies_awarded, ducky)

    if not ducky:
        exam_number.append(task_number - 2)
        needed_time.append(programmer_time)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for ducky in ["Darth Vader Ducky", "Thor Ducky", "Big Blue Rubber Ducky", "Small Yellow Rubber Ducky"]:
    print(f"{ducky}: {duckies_awarded[ducky]}")


##########: variant 3 solution SoftUni :##########


from collections import deque

programmers = deque(map(int, input().split()))
tasks = list(map(int, input().split()))
givenDucks = {"Darth Vader Ducky": 0, "Thor Ducky": 0, "Big Blue Rubber Ducky": 0, "Small Yellow Rubber Ducky": 0}

while programmers and tasks:
    current_programmer = programmers.popleft()
    current_task = tasks.pop()
    time_taken = current_programmer * current_task

    if 0 < time_taken <= 60:
        givenDucks["Darth Vader Ducky"] += 1
    elif 60 < time_taken <= 120:
        givenDucks["Thor Ducky"] += 1
    elif 120 < time_taken <= 180:
        givenDucks["Big Blue Rubber Ducky"] += 1
    elif 180 < time_taken <= 240:
        givenDucks["Small Yellow Rubber Ducky"] += 1
    else:
        programmers.append(current_programmer)
        tasks.append(current_task - 2)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded: ")
for key, value in givenDucks.items():
    print(key + ": " + str(value))
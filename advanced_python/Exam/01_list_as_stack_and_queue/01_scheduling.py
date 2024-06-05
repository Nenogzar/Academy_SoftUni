# ******* Advanced Exam - 24 October 2020 ******* #

# *******  01_scheduling  ******* #

# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/2551#0

 You are hired to create a program that implements SJF (Shortest Job First).
 It works by letting the shortest jobs to take the CPU, so jobs won't get frozen.

On the first line you will be given the jobs as integers
    (clock-cycles needed to finish the job) separated by comma and space ", ".
On the second line you will be given the index of the job
    that we are interested in and want to know how many cycles will pass until the job is done.

The tasks that need the least amount of clock-cycles will be completed first.
For the jobs that need the same amount of clock-cycles, the order is FIFO (First In First Out).
You have to print how many clock-cycles will pass until the task you are interested in is completed.
    For more clarifications, see the examples below.

Input
•	On the first line you will receive numbers separated by ", "
•	On the second line you will receive the index of the task you are interested in
Output
•	Single line: the clock-cycles that will pass until the task you are interested in is finished

Examples

Input
3, 1, 10, 1, 2
0

Output
7


Comment
The first task will be 1 at index 1 (1 clock-cycle)
Next is 1 at index 3 (total 2 clock-cycles)
Next is 2 at index 4 (total 4 clock-cycles)
Next, we arrive at 3 on index 0 (total 7 clock-cycles) which is the one we need, and we end the program


Input
4, 10, 10, 6, 2, 99
2

Output
32

Comment
2 at index 4 -> total 2 clock-cycles
4 at index 0 -> total 6 clock-cycles
6 at index 3 -> total 12 clock-cycles
10 at index 1 -> total 22 clock-cycles
10 at index 2 -> total 32 clock-cycles


"""


##########: variant 1 :##########
def sjf_scheduler(jobs, interested_index):
    job_times = list(map(int, jobs.split(", ")))
    interested_index = int(interested_index)

    indexed_jobs = [(time, idx) for idx, time in enumerate(job_times)]
    sorted_jobs = sorted(indexed_jobs, key=lambda x: (x[0], x[1]))
    total_cycles = 0
    for time, idx in sorted_jobs:
        total_cycles += time
        if idx == interested_index:
            break

    return total_cycles


input_jobs = input()
input_index = input()

result = sjf_scheduler(input_jobs, input_index)
print(result)

##########: variant 2 :##########

jobs = [int(x) for x in input().split(", ")]
idx = int(input())

computed_element = jobs[idx]
total_cycles = 0
for job in sorted(jobs):
    if job > computed_element:
        break
    total_cycles += job

print(total_cycles)

##########: variant 3 solution CEO :##########
jobs = [int(x) for x in input().split(", ")]
index_to_find = int(input())
clock_cycles = 0


def change_number(index):
    jobs[index] = "x"


for num in sorted(jobs[:]):
    found_index = jobs.index(num)
    clock_cycles += jobs[found_index]
    change_number(found_index)
    if found_index == index_to_find:
        break

print(clock_cycles)

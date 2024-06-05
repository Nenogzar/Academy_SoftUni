# ******* Advanced Retake Exam - 16 December 2020 ******* #

# *******  01_matching  ******* #

# *******  TASK CONDITION  ******* #
"""
 https://judge.softuni.org/Contests/Practice/Index/2720#0

First you will be given a sequence of integers representing males.
    Afterwards you will be given another sequence of integers representing females.

You have to start from the first female and try to match it with the last male.

•	If their values are equal,
        you have to match them and remove both of them.
        Otherwise you should remove only the female and decrease the value of the male by 2.

•	If someone’s value is equal to or below 0,
        you should remove him/her from the records before trying to match him/her with anybody.

•	Special case
    - if someone’s value divisible by 25 without remainder,
        you should remove him/her and the next person of the same gender before trying to match them with anybody.

You need to stop matching people when you have no more females or males.

Input
•	On the first line of input you will receive the integers, representing the males, separated by a single space.
•	On the second line of input you will receive the integers, representing the females, separated by a single space.


Output
•	On the first line of output - print the number of successful matches:
    "Matches: {matchesCount}"

•	On the second line - print all males left:
    o	If there are no males:
        "Males left: none"
    o	If there are males:
        "Males left: {maleN}, … , {male3}, {male2}, {male1}"

•	On the third line - print all females left:
    o	If there are no females:
        "Females left: none"
    o	If there are females:
        "Females left: {female1}, {female2}, {female3},…, {femaleN}"

Constraints
•	All of the given numbers will be valid integers in the range [-100, 100].

Input
4 5 7 3 6 9 12
12 9 6 1

Output
Matches: 3
Males left: 1, 7, 5, 4
Females left: none

***** Comment *****

The first pair is the first female with value of 12 and the last male of value 12, their values are equal,
so we match them, therefore - remove them from the records. Then we have two more matches (9 == 9 and 6 == 6).
But the value of the next male is 3 and the value of the next female is 1,
it's not a match and we remove the female and reduce the male’s value by 2.Then, we print the desired output.

Input
3 0 3 6 9 0 12
12 9 6 1 2 3 15 13 4

Output
Matches: 4
Males left: none
Females left: 15, 13, 4


"""

##########: variant 1 :##########
from collections import deque

males_list = list(int(x) for x in input().split() if int(x) > 0)
females_list = deque(int(x) for x in input().split() if int(x) > 0)

matches = 0

while males_list and females_list:
    male = males_list[-1]
    female = females_list[0]

    if male % 25 == 0:
        males_list.pop()
        if males_list:
            males_list.pop()
        continue

    if female % 25 == 0:
        females_list.popleft()
        if females_list:
            females_list.popleft()
        continue

    if male == female:
        matches += 1
        males_list.pop()
        females_list.popleft()
    else:
        females_list.popleft()
        males_list[-1] -= 2
        if males_list[-1] <= 0:
            males_list.pop()

print(f"Matches: {matches}")

if males_list:
    print(f"Males left: {', '.join(map(str, reversed(males_list)))}")
else:
    print("Males left: none")

if females_list:
    print(f"Females left: {', '.join(map(str, females_list))}")
else:
    print("Females left: none")

##########: variant 2 :##########

from collections import deque

def remove_if_multiple_of_25(stack_or_queue):
    if stack_or_queue and stack_or_queue[0] % 25 == 0:
        stack_or_queue.popleft()
        if stack_or_queue:
            stack_or_queue.popleft()

def remove_if_multiple_of_25_reverse(stack_or_queue):
    if stack_or_queue and stack_or_queue[-1] % 25 == 0:
        stack_or_queue.pop()
        if stack_or_queue:
            stack_or_queue.pop()


males_list = list(int(x) for x in input().split() if int(x) > 0)
females_list = deque(int(x) for x in input().split() if int(x) > 0)

matches = 0

while males_list and females_list:

    if males_list[-1] % 25 == 0:
        remove_if_multiple_of_25_reverse(males_list)
        continue

    if females_list[0] % 25 == 0:
        remove_if_multiple_of_25(females_list)
        continue

    male = males_list[-1]
    female = females_list[0]

    if male == female:
        matches += 1
        males_list.pop()
        females_list.popleft()
    else:
        females_list.popleft()
        males_list[-1] -= 2
        if males_list[-1] <= 0:
            males_list.pop()

print(f"Matches: {matches}")

if males_list:
    print(f"Males left: {', '.join(map(str, reversed(males_list)))}")
else:
    print("Males left: none")

if females_list:
    print(f"Females left: {', '.join(map(str, females_list))}")
else:
    print("Females left: none")


##########: variant 3  :##########

from collections import deque

males = [int(x) for x in input().split()]
females = deque(int(x) for x in input().split())
matches = 0


while males and females:
    if females[0] <= 0:
        del females[0]
        continue
    if females[0] % 25 == 0:
        del females[0]
        del females[0]
        continue
    if males[-1] <= 0:
        del males[-1]
        continue
    if males[-1] % 25 == 0:
        del males[-1]
        del males[-1]
        continue
    female = females.popleft()
    male = males.pop()
    if female == male:
        matches += 1
        continue
    males.append(male - 2)

print(f"Matches: {matches}")

if males:
    print(f"Males left: {', '.join(str(x) for x in males[::-1])}")
else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join(str(x) for x in females)}")
else:
    print("Females left: none")

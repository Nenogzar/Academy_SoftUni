############################## 01_climb_the_peaks ##############################
  ############################## TASK CONDITION ##############################
"""
 https://judge.softuni.org/Contests/Practice/Index/3744#0

Alex is a vlogger and he wants to make videos of climbing the five highest peaks in Pirin mountain in just one week.
He will take his video set, a tent, and his backpack to the mountain. The backpack fits food portions for one week, exactly.
His daily stamina is also limited.
Your task is to trace his adventure and create a post for his profile @alaroundtheworld, at the end of the journey.
You will have to keep information for all the conquered peaks if any.

Every day, Alex will use one portion of his daily food supplies and will exhaust one of his daily stamina.

First,
    you will be given a sequence of numbers,
    representing the quantities of the daily portions of food supplies in his backpack.
Afterward,
    you will be given another sequence of numbers,
    epresenting the quantities of the daily stamina he will have at his disposal for the next seven days.

You have to sum the quantity of the last daily food portion with the quantity of the first daily stamina.
He will start climbing from the first peak in the table below to the last one.

•	If the sum is equal to or greater than the corresponding Mountain Peak’s Difficulty level from the table below,
    it means that the peak is conquered.
    In this case, you should remove both quantities from the sequences and continue with the next ones towards the next peak.

•	If the sum is less than the corresponding Mountain Peak’s Difficulty level from the table below,
    the peak remains unconquered.
    You should remove both quantities from the sequences.
    Alex will have to sleep in his tent. On the next day, he will try the same peak once again.


Mountain Peaks	    Difficulty level
Vihren	                80
Kutelo	                90
Banski Suhodol	        100
Polezhan	            60
Kamenitza	            70


Alex will try to conquer as many peaks as he can in seven days.
If he manages to climb all the peaks, the journey ends and the output is printed on the Console.

Finally, print on the Console all the conquered peaks(in the order of climbing).

Input

•	On the first line, you will receive the food portions, separated by a comma and a single space (', ').
•	On the second line, you will receive the stamina, separated by a comma and a single space (', ').

Output

•	On the first line – print whether Alex managed to reach his goal and climb all the peaks in his list:
    o	If he managed to conquer all:
        "Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK"
    o	If he didn't manage to climb all of the peaks:
        "Alex failed! He has to organize his journey better next time -> @PIRINWINS"

•	Then, in either case, you need to print all the conquered peaks (in the order of climbing) if any:
"Conquered peaks:
{peak1}
{peak2}
…
{peakn}"

    o	If there are no concurred peaks, do NOT print this message.

Constraints
•	All of the given numbers will be valid integers in the range [0…100].
Examples

Input

40, 40, 40, 40, 40, 40, 40
40, 50, 60, 20, 30, 5, 2

Output

Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK
Conquered peaks:
Vihren
Kutelo
Banski Suhodol
Polezhan
Kamenitza


Input
10, 20, 34, 26, 12, 10, 45
30, 28, 17, 17, 13, 10, 10

Output
Alex failed! He has to organize his journey better next time -> @PIRINWINS


"""

##########: variant 1 :##########

from collections import deque

climbing_peak = {
    'Vihren': 80,
    'Kutelo': 90,
    'Banski Suhodol': 100,
    'Polezhan': 60,
    'Kamenitza': 70,
}

conquered_peaks = []

food_supplies = deque(map(int, input().split(", ")))
daily_stamina = deque(map(int, input().split(", ")))

days = 1
current_peak = iter(climbing_peak.items())  # Създавам итератор за върховете

# Взимам първия връх
try:
    peak_name, peak_difficulty = next(current_peak)
except StopIteration:
    peak_name, peak_difficulty = None, None

while days <= 7 and food_supplies and daily_stamina:
    day_food = food_supplies.pop()
    day_stamina = daily_stamina.popleft()
    dayly_peak = day_food + day_stamina

    if dayly_peak >= peak_difficulty:
        conquered_peaks.append(peak_name)
        # Придвижвам се към следващия връх
        try:
            peak_name, peak_difficulty = next(current_peak)
        except StopIteration:
            break  # Ако няма повече върхове, прекратявам цикъла

    days += 1


if len(conquered_peaks) == 5:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
    print("Conquered peaks:")
    print("\n".join(conquered_peaks))
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
    if conquered_peaks:
        print("Conquered peaks:")
        print("\n".join(conquered_peaks))



##########: variant 2 whit Dictionary :##########



##########: variant 3 solution SoftUni :##########

# from collections import deque
#
# daily_food = list(map(int, input().split(", ")))
# daily_stamina = deque(map(int, input().split(", ")))
#
# day = 1
# conquered_peaks = []
# all_peaks = deque([
#     ("Vihren", 80),
#     ("Kutelo", 90),
#     ("Banski Suhodol", 100),
#     ("Polezhan", 60),
#     ("Kamenitza", 70)
# ])
#
# while True:
#     if len(conquered_peaks) == 5:
#         print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
#         break
#     if day > 7 or not daily_food or not daily_stamina:
#         print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
#         break
#     food = daily_food.pop()
#     stamina = daily_stamina.popleft()
#     result = food + stamina
#     index = 0
#     next_peak = all_peaks.popleft()
#     if result >= next_peak[1]:
#         conquered_peaks.append(next_peak[0])
#         day += 1
#     else:
#         all_peaks.appendleft(next_peak)
#         day += 1
#
#
# if conquered_peaks:
#     print("Conquered peaks:")
#     for peak in conquered_peaks:
#         print(peak)

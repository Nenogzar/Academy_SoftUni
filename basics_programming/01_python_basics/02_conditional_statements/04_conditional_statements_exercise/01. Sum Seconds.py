import math

time_first = int(input())
time_second = int(input())
time_therd = int(input())

total_time = time_first + time_second + time_therd

mm = total_time // 60
ss = total_time % 60

minutes = math.floor(mm)

if ss < 10:
    print(f"{mm}:0{ss}")
else:
    print(f"{mm}:{ss}")




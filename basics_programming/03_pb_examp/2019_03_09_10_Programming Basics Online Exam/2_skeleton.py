# печели и квота
# време в секунди за 100 метра
# за всеки 120 метра времето му намалява с 2,5 секунди

minute_control = float(input())
seconds_control = float(input())
minutes_control_sec = minute_control * 60 + seconds_control
chute_length_m = float(input())
target_time_sec = float(input())
reduced_sec = 2.5
#print("minutes_control_sec", minutes_control_sec)
reduced_time = (chute_length_m / 120) * reduced_sec
#print("reduced_time", reduced_time)
time_player = (chute_length_m / 100) * target_time_sec - reduced_time
#print("time_player", time_player)

if time_player <= minutes_control_sec:
    print(f"Marin Bangiev won an Olympic quota!")
    print(f"His time is {time_player:.3f}.")
else:
    print(f"No, Marin failed! He was {abs(time_player - minutes_control_sec):.3f} second slower.")



# minutes_control = int(input())
# seconds_control = int(input())
# length_chute = float(input())
# seconds_per_100_meters = int(input())
#
# control_time = minutes_control * 60 + seconds_control
# slowing_time = length_chute / 120
# total_slowing_time = slowing_time * 2.5
# marin_time = (length_chute / 100) * seconds_per_100_meters - total_slowing_time
#
# if marin_time <= control_time:
#     print("Marin Bangiev won an Olympic quota!")
#     print(f"His time is {marin_time:.3f}.")
# else:
#     print(f"No, Marin failed! He was {marin_time - control_time:.3f} second slower.")

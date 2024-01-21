import math

wr_sec = float(input())
distans_m = float(input())
time_m_sem = float(input())
resistance = 12.5

distans_res = math.floor(distans_m /15) * resistance
swiming_start=distans_m * time_m_sem
swiming_end = swiming_start + distans_res

if swiming_end < wr_sec:
    print(f" Yes, he succeeded! The new world record is {swiming_end:.2f} seconds.")
else:
    print(f"No, he failed! He was {swiming_end-wr_sec:.2f} seconds slower.")